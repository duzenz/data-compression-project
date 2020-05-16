from algorithms.BurrowsWheelerTransform import BurrowsWheelerTransform
from algorithms.MoveToFront import MoveToFront
from algorithms.Utils import Utils

burrowsWheelerTransform = BurrowsWheelerTransform()
moveToFront = MoveToFront()
utils = Utils()

block_size = 8192
raw_file_name = "samples/big.txt"
bwt_encoded_file_name = "output/bwt_encoded.txt"
mtf_encoded_file_name = "output/mtf_encoded.txt"
arithmetic_encoded_file_name = "output/arithmetic_encoded.txt"

utils.replace_file_endings(raw_file_name)

# encode bwt
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

utils.replace_file_endings(bwt_encoded_file_name)

# encode mtf
bwt_encoded_file = open(bwt_encoded_file_name, "r")
encode = moveToFront.code(bwt_encoded_file.read())

mtf_encoded_file = open(mtf_encoded_file_name, "w+")
mtf_encoded_file.write(' '.join(map(str, encode)))
mtf_encoded_file.close()

# encode arithmetic
utils.replace_file_endings(mtf_encoded_file_name)

frequencies = utils.get_frequencies(mtf_encoded_file_name)
frequencies.increment(256)

utils.arithmetic_code(mtf_encoded_file_name, arithmetic_encoded_file_name, frequencies)
