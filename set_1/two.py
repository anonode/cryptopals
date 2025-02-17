import binascii

def fixed_xor(one, two):
    one_bytes = binascii.a2b_hex(one)
    two_bytes = binascii.a2b_hex(two)
    if len(one_bytes) != len(two_bytes):
        return -1
    
    xored = bytes(a ^ b for (a,b) in zip(one_bytes,two_bytes))
    return xored

one = "1c0111001f010100061a024b53535009181c"
two = "686974207468652062756c6c277320657965"

ret = fixed_xor(one,two)
print(f'hex: {binascii.hexlify(ret)}\nascii:{ret.decode("ascii")}')