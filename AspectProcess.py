import re

def aspectF(aspect):
    # Clean the aspect to contain only alphabetic characters and spaces
    cleaned_aspect = re.sub('[^A-Za-z ]+', '', aspect).strip()
    if cleaned_aspect:
        words = cleaned_aspect.split()
        # Return the last word of the aspect, in lowercase
        return words[-1].lower()
    return aspect.lower()
