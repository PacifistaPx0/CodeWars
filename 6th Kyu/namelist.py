def namelist(names):
    new = []
    for item in names:
        new.append(item['name'])
    if len(new)>2:
        j = ", ".join(new[:len(new)-2])
        return j + ", %s & %s"%(new[len(new)-2], new[len(new)-1])
    if len(new) ==2:
        return "%s & %s"%(new[0], new[1])
    if len(new) ==1:
        return "%s"%(new[0])
    else:
        return ""







print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
# returns 'Bart, Lisa & Maggie'
