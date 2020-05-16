from algorithms.BurrowsWheelerTransform import BurrowsWheelerTransform
from algorithms.Utils import Utils

burrowsWheelerTransform = BurrowsWheelerTransform()
utils = Utils()

block_size = 8192
raw_file_name = "samples/small.txt"
bwt_encoded_file_name = "output/bwt_encoded.txt"
bwt_decoded_file_name = "output/bwt_decoded.txt"

utils.replace_file_endings(raw_file_name)

# encode
bwt_encoded_file = open(bwt_encoded_file_name, "w+")
with open(raw_file_name, "rb") as f:
    while True:
        byte = f.read(block_size)
        if len(byte.decode()) > 0:
            index, encoded = burrowsWheelerTransform.code(byte.decode())
            bwt_encoded_file.write(str(index))
            bwt_encoded_file.write('[')
            bwt_encoded_file.write(encoded)
            bwt_encoded_file.write("]")
        if not byte:
            break
bwt_encoded_file.close()

# decode
bwt_encoded_file = open(bwt_encoded_file_name, "r")
bwt_decoded_file = open(bwt_decoded_file_name, "w+")
for byte_string in bwt_encoded_file.read().split("]"):
    text = byte_string.split('[')
    if len(text) > 1:
        bwt_decoded_file.write(burrowsWheelerTransform.decode(int(text[0]), text[1]))

bwt_encoded_file.close()
bwt_decoded_file.close()
