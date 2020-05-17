import click
import yaml
import sys
import pathlib
from jinja2 import Template, Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
import re
from template_code.original_resume import original_resume

@click.command()
@click.option("--in", "-i", "content", required=True, help="Path to your resume.yaml file.")
@click.option("--out", "-o", "out_file", default="./resume.pdf", help="The path to store your generated resume!")
def process(content:str, out_file:str):
    """
    Process a content yaml file and converts it into its proper PDF form stored at out_file
    """
    resume_content = load_yaml_dictionary(content)
    template_context = load_template_context() # This is here for expandability later on

    print(template_context.render(resume_content))

def load_yaml_dictionary(content: str) -> dict:
    """
    Loads a yaml file into a python dictionary that can be formatted for Jinja2
    """
    resume_content = {}
    try:
        with open(content) as content_file:
            resume_content = yaml.safe_load(content_file)
    except FileNotFoundError:
        sys.exit("Your content file could not be found!")
    
    return resume_content

def load_template_context(template="{}/templates/original_resume.tex".format(pathlib.Path(__file__).parent.parent.absolute())):
    """
    Builds a Jinja2 Template context from a template .tex file
    """
    #TODO: Expand this functionality to include templates of other types of files
    latex_env = Environment(
        block_start_string= "\BLOCK{",
        block_end_string="}",
        variable_start_string="\VAR{",
        variable_end_string="}",
        comment_start_string="\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader = FileSystemLoader(pathlib.Path(".")) 
    )
    latex_env.globals['tex_escape'] = tex_escape
    instantiate_template_code(latex_env)

    temp_env = None
    try:
        temp_env = latex_env.get_template("templates/original_resume.tex") #TODO: Change this from hardcoded to something that makes sense
    except TemplateNotFound:
        sys.exit("Could not find the template for this resume!")
    return temp_env

def tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)

def instantiate_template_code(environ: Environment):
    """
    Passes the custom code model for the template into 
    the context for the template
    """
    # hard coded for now - just for simplicy
    environ.globals["template_code"] = original_resume()

if __name__ == "__main__":
    process()