from ArithmeticCoding import ArithmeticCoding

arithmeticCoding = ArithmeticCoding()

block_size = 8192
raw_file_name = "mft_encoded.txt"
arithmetic_encoded_file_name = "arithmetic_encoded.txt"
arithmetic_decoded_file_name = "arithmetic_decoded.txt"
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

with open(raw_file_name, 'rb') as open_file:
    content = open_file.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

with open(raw_file_name, 'wb') as open_file:
    open_file.write(content)

arithmetic_encoded_file = open(arithmetic_encoded_file_name, "w+")

with open(raw_file_name, "rb") as f:
    while True:
        byte = f.read(block_size)
        if len(byte.decode()) > 0:
            print(byte)
            encrypted, power, frequency = arithmeticCoding.arithmetic_coding(byte)
            print(encrypted)
            arithmetic_encoded_file.write(str(encrypted))
            print(arithmeticCoding.arithmetic_decoding(encrypted, power, frequency))
        if not byte:
            break

arithmetic_encoded_file.close()
