from algorithms.BurrowsWheelerTransform import BurrowsWheelerTransform
from algorithms.MoveToFront import MoveToFront
from algorithms.Utils import Utils

burrowsWheelerTransform = BurrowsWheelerTransform()
moveToFront = MoveToFront()
utils = Utils()

arithmetic_encoded_file_name = "output/arithmetic_encoded.txt"
bwt_decoded_file_name = "output/bwt_decoded.txt"
mtf_decoded_file_name = "output/mtf_decoded.txt"
arithmetic_decoded_file_name = "output/arithmetic_decoded.txt"

utils.arithmetic_decode(arithmetic_encoded_file_name, arithmetic_decoded_file_name)

utils.replace_file_endings(arithmetic_decoded_file_name)

mtf_encoded_file = open(arithmetic_decoded_file_name, "r")
code_list = [int(i) for i in mtf_encoded_file.read().split(" ")]
mtf_decoded_file = open(mtf_decoded_file_name, "w+")
decode = moveToFront.decode(code_list)
mtf_decoded_file.write(decode)
mtf_decoded_file.close()

# decode
bwt_encoded_file = open(mtf_decoded_file_name, "r")
bwt_decoded_file = open(bwt_decoded_file_name, "w+")
for byte_string in bwt_encoded_file.read().split("]"):
    text = byte_string.split('[')
    if len(text) > 1:
        bwt_decoded_file.write(burrowsWheelerTransform.decode(int(text[0]), text[1]))

bwt_encoded_file.close()
bwt_decoded_file.close()

