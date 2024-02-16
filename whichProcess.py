import nltk

def which1(sentence, aspect):
    sentence = sentence.lower()
    words = sentence.split()
    for i, word in enumerate(words):
        if word == 'which':
            # Replace "which" with "this which" for clarity
            words[i] = 'this which'
            break
        else:
            # Check if the current word is a noun
            tags = nltk.pos_tag([word])
            if tags[0][1].startswith('N'):
                continue
    return ' '.join(words)
