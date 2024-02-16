import re

def siplate1(text, aspect):
    text = text.lower()
    aspect = re.sub('[^A-Za-z]+', ' ', aspect.lower())
    text = re.sub('[^A-Za-z]+', ' ', text)
    
    but_index = text.find("but")
    if but_index != -1:
        text_left, _, text_right = text.partition(" but ")
        if text_left.find(aspect) != -1:
            return text_left
        else:
            return text_right
    return text
