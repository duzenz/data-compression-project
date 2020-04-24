'''
for byte_string in b'DABDDB DABDDBBDDBA ABRACADABRA TOBEORNOTTOBEORTOBEORNOT'.split():
    print(byte_string)
    encrypted, power, frequency = arithmetic_coding(byte_string)
    decrypted = arithmetic_decoding(encrypted, power, frequency)

    print("%-25s=> %19s * %d^%s" % (byte_string, encrypted, radix, power))

    if byte_string != decrypted:
        raise Exception("\tHowever that is incorrect!")
'''
