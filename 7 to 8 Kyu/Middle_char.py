#Returns the middle character of a string, if the string length is an even number, returns the two middle characters
def get_middle(s):
    i = len(s)
    j = int(i/2)
    if i % 2 == 0:
        return s[j-1]+s[j]
    else:  
        return s[j]