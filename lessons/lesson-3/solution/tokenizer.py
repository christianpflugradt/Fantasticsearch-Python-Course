from re import findall, sub

textmatch = r'<h2 id=.+?>.+?</h2>(.+?)<h2>'
finaltextmatch = r'<h2 id=.+?>.+?</h2>(.+?)</div>'
tagsub = r'<.+?>'
specialsub = r'[^a-zA-Z0-9 \n\.]'

def find_texts(content):
    return findall(textmatch, content) + findall(finaltextmatch, content)

def remove_tags(text):
    return sub(tagsub, ' ', text)

def remove_symbols(text):
    return sub(specialsub, ' ', text)

def split_tokens(text):
    return text.split(' ')

def tokenize(content):
    tokens = set()
    for text in find_texts(content):
        tokens |= set(split_tokens(remove_symbols(remove_tags(text)).lower()))
    return tokens
