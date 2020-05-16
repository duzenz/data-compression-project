from algorithms.Utils import Utils

utils = Utils()

raw_file_name = "output/mtf_encoded.txt"
arithmetic_encoded_file_name = "output/arithmetic_encoded.txt"
arithmetic_decoded_file_name = "output/arithmetic_decoded.txt"

utils.replace_file_endings(raw_file_name)

frequencies = utils.get_frequencies(raw_file_name)
frequencies.increment(256)  # EOF symbol

utils.arithmetic_code(raw_file_name, arithmetic_encoded_file_name, frequencies)

utils.arithmetic_decode(arithmetic_encoded_file_name, arithmetic_decoded_file_name)
