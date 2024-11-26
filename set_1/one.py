import base64
def tobase64(dec):
    return base64.b64encode(bytes.fromhex(dec))


dec = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(tobase64(dec))
