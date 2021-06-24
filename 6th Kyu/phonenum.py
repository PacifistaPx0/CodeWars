"""phone number format"""

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])


phone = (0, 1, 2, 3, 5, 6, 7, 8, 9, 6)

print(create_phone_number(phone))