"""For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text."""

#This fucntion does the exact opposite of the encrypt function
def decrypt(encrypted_text, n):
    if n<=0:
        return encrypted_text
    if encrypted_text == "":
        return ""
    while n>0:
        new = []
        mid =len(encrypted_text)//2 #splitting the text into two parts for reverse purpose
        even = list(encrypted_text[:mid])
        odd = list(encrypted_text[mid:])
        for x, y in zip(even, odd):
            new.append(y)
            new.append(x)
        if len(encrypted_text)%2 !=0: #zip would ignore the last item of the odd list if the len of the lists are different hence this code adds that item
            new.append(odd[len(odd)-1])
        encrypted_text = "".join(new)

        n-=1
    return encrypted_text


def encrypt(text, n):
    if n<=0:
        return text
    if not text:
        return ""
    text = list(text)

    while n>0:
        even = text[1::2]
        odd = text[::2]
        n-=1
        even, odd = "".join(map(str, even)), "".join(map(str, odd))
        encrypt_txt = even + odd 
        text = encrypt_txt

    return encrypt_txt

print(encrypt("This is a test!", 1))
print(decrypt(encrypt("This is a test!",2),2))

