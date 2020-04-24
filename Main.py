from MoveToFront import MoveToFront
from ArithmeticCoding import ArithmeticCoding
from BurrowsWheelerTransform import BurrowsWheelerTransform

moveToFront = MoveToFront()
arithmeticCoding = ArithmeticCoding()
burrowsWheelerTransform = BurrowsWheelerTransform()

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
