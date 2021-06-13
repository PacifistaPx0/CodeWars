#Returns string without vowel characters

def disemvowel(string_):
    char_replace = {
        'A':'',
        'a':'',
        'E':'',
        'e':'',
        'I':'',
        'i':'',
        'O':'',
        'o':'',
        'U':'',
        'u':''
        }
    for key, value in char_replace.items():
        string_ = string_.replace(key,value)
    
    return string_
