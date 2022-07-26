def generate_hashtag(s):
    if not s:
        return False
    if len(s) > 140:
        return False 
    s = s.lower()
    s = list(s)
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            s[i] = s[i].upper()
    s = ''.join(map(str,s))
    new_s = s.replace(" ","")
    new_s = list(new_s)
    for i in new_s:
        new_s[0] = new_s[0].upper()
    new_s = ''.join(map(str,new_s))

    return "#" + new_s
s ="hello there hope you enjoy this kata"
print(generate_hashtag(s))