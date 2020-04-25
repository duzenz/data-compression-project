from MoveToFront import MoveToFront
from ArithmeticCoding import ArithmeticCoding
from BurrowsWheelerTransform import BurrowsWheelerTransform

moveToFront = MoveToFront()
arithmeticCoding = ArithmeticCoding()
burrowsWheelerTransform = BurrowsWheelerTransform()

f1 = open("raw_text.txt", "r")
f2 = open("encoded.txt", "w+")

# print(f.read())

with open("raw_text.txt", "rb") as f:
    while True:
        byte = f.read(1024)
        encrypted, power, frequency = arithmeticCoding.arithmetic_coding(byte)
        f2.write(str(encrypted))
        if not byte:
            break

f2.close()
'''
for byte_string in f1.read().split():
    print(byte_string.encode())
    encrypted, power, frequency = arithmeticCoding.arithmetic_coding(byte_string.encode())
    print(encrypted)
    f2.write(str(encrypted))

for byte_string in b'DABDDB DABDDBBDDBA ABRACADABRA TOBEORNOTTOBEORTOBEORNOT'.split():
    print(byte_string)
    encrypted, power, frequency = arithmeticCoding.arithmetic_coding(byte_string)
    print(encrypted)

f1.close()
f2.close()
'''

'''
encode = moveToFront.move_to_front_code('aaafhhimst')
print(encode)
decode = moveToFront.move_to_front_decode(encode)
print(decode)

for byte_string in b'DABDDB DABDDBBDDBA ABRACADABRA TOBEORNOTTOBEORTOBEORNOT'.split():
    print(byte_string)
    encrypted, power, frequency = arithmeticCoding.arithmetic_coding(byte_string)
    decrypted = arithmeticCoding.arithmetic_decoding(encrypted, power, frequency)

    print("%-25s=> %19s * %s" % (byte_string, encrypted, power))

    if byte_string != decrypted:
        raise Exception("\tHowever that is incorrect!")

a = burrowsWheelerTransform.burrows_wheeler_transform("SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES")
print(a)
print(burrowsWheelerTransform.inverse_burrows_wheeler_transform(a))
'''
