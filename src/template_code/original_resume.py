import sys

class original_resume:

    @staticmethod
    def parse_one_line_section(section_content: dict):
        """
        This function takes the root section element
        of a one line section and parses it into a 
        displayable format for the original_resume
        template.
        """
        # We are going to format the half lines
        # such that they are paired with each other
        # by nesting the second in the first 
        half_sections = list(filter(lambda x: section_content[x].get("type") == "half", section_content))
        paired = [(half_sections[i], half_sections[i+1]) for i in range(0,len(half_sections), 2)]
        for entry in paired:
            section_content[entry[0]]["title2"] = entry[1]
            section_content[entry[0]]["content2"] = section_content[entry[1]]["content"]
            del section_content[entry[1]]
        
        return section_content