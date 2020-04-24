"""
for byte_string in b'DABDDB DABDDBBDDBA ABRACADABRA TOBEORNOTTOBEORTOBEORNOT'.split():
    print(byte_string)
    encrypted, power, frequency = arithmetic_coding(byte_string)
    decrypted = arithmetic_decoding(encrypted, power, frequency)

    print("%-25s=> %19s * %d^%s" % (byte_string, encrypted, radix, power))

    if byte_string != decrypted:
        raise Exception("\tHowever that is incorrect!")
"""

'''
encode = move_to_front_code('aaafhhimst')

print(encode)

decode = move_to_front_decode(encode)

print(decode)

'''

'''
a = burrows_wheeler_transform("SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES")
print(a)
print(inverse_burrows_wheeler_transform(a))
'''