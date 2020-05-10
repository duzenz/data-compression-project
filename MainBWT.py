from algorithms.BurrowsWheelerTransform import BurrowsWheelerTransform

burrowsWheelerTransform = BurrowsWheelerTransform()

block_size = 8192
raw_file_name = "samples/medium.txt"
bwt_encoded_file_name = "bwt_encoded.txt"
bwt_decoded_file_name = "bwt_decoded.txt"
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

with open(raw_file_name, 'rb') as open_file:
    content = open_file.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

with open(raw_file_name, 'wb') as open_file:
    open_file.write(content)

bwt_encoded_file = open(bwt_encoded_file_name, "w+")

with open(raw_file_name, "rb") as f:
    while True:
        byte = f.read(block_size)
        if len(byte.decode()) > 0:
            print(byte)
            index, encoded = burrowsWheelerTransform.bw_transform(byte.decode())
            bwt_encoded_file.write(str(index))
            bwt_encoded_file.write('[')
            bwt_encoded_file.write(encoded)
            bwt_encoded_file.write("]")
        if not byte:
            break

bwt_encoded_file.close()

bwt_encoded_file = open(bwt_encoded_file_name, "r")
bwt_decoded_file = open(bwt_decoded_file_name, "w+")
for byte_string in bwt_encoded_file.read().split("]"):
    text = byte_string.split('[')
    if len(text) > 1:
        bwt_decoded_file.write(burrowsWheelerTransform.bw_restore(int(text[0]), text[1]))

bwt_encoded_file.close()
bwt_decoded_file.close()
