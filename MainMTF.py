from algorithms.MoveToFront import MoveToFront

moveToFront = MoveToFront()

block_size = 8192
raw_file_name = "bwt_encoded.txt"
mtf_encoded_file_name = "mft_encoded.txt"
mtf_decoded_file_name = "mft_decoded.txt"
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

with open(raw_file_name, 'rb') as open_file:
    content = open_file.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

with open(raw_file_name, 'wb') as open_file:
    open_file.write(content)

f1 = open(raw_file_name, "r")
encode = moveToFront.move_to_front_code(f1.read())

mtf_encoded_file = open(mtf_encoded_file_name, "w+")
mtf_encoded_file.write(' '.join(map(str, encode)))
mtf_encoded_file.close()

mtf_encoded_file = open(mtf_encoded_file_name, "r")
lst_int = [int(x) for x in mtf_encoded_file.read().split(" ")]

mtf_decoded_file = open(mtf_decoded_file_name, "w+")
decode = moveToFront.move_to_front_decode(lst_int)
mtf_decoded_file.write(decode)
mtf_decoded_file.close()



