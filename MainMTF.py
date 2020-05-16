from algorithms.MoveToFront import MoveToFront
from algorithms.Utils import Utils

moveToFront = MoveToFront()
utils = Utils()

bwt_encoded_file_name = "output/bwt_encoded.txt"
mtf_encoded_file_name = "output/mtf_encoded.txt"
mtf_decoded_file_name = "output/mtf_decoded.txt"

utils.replace_file_endings(bwt_encoded_file_name)

# encode
bwt_encoded_file = open(bwt_encoded_file_name, "r")
encode = moveToFront.code(bwt_encoded_file.read())

mtf_encoded_file = open(mtf_encoded_file_name, "w+")
mtf_encoded_file.write(' '.join(map(str, encode)))
mtf_encoded_file.close()

# decode
mtf_encoded_file = open(mtf_encoded_file_name, "r")
code_list = [int(i) for i in mtf_encoded_file.read().split(" ")]

mtf_decoded_file = open(mtf_decoded_file_name, "w+")
decode = moveToFront.decode(code_list)
mtf_decoded_file.write(decode)
mtf_decoded_file.close()
