# return masked string
def maskify(cc):
    if len(cc)<=4:
        return cc
    else:
        cc = list(cc)
        i = 0
        while i<= len(cc) - 5:
            cc[i]="#"
            i+=1
    q = "".join(cc)
    return q
