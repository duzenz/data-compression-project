import contextlib
from algorithms.arithmeticcoding import SimpleFrequencyTable
from algorithms.arithmeticcoding import ArithmeticEncoder
from algorithms.arithmeticcoding import ArithmeticDecoder
from algorithms.arithmeticcoding import BitOutputStream
from algorithms.arithmeticcoding import BitInputStream

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


class Utils:

    def replace_file_endings(self, file_name):
        with open(file_name, 'rb') as open_file:
            content = open_file.read()

        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

        with open(file_name, 'wb') as open_file:
            open_file.write(content)

    def get_frequencies(self, filepath):
        freqs = SimpleFrequencyTable([0] * 257)
        with open(filepath, "rb") as input_file:
            while True:
                b = input_file.read(1)
                if len(b) == 0:
                    break
                freqs.increment(b[0])
        return freqs

    def read_frequencies(self, bit_in):
        def read_int(n):
            result = 0
            for _ in range(n):
                result = (result << 1) | bit_in.read_no_eof()  # Big endian
            return result

        frequencies = [read_int(32) for _ in range(256)]
        frequencies.append(1)  # EOF symbol
        return SimpleFrequencyTable(frequencies)

    def write_frequencies(self, bit_out, frequencies):
        for i in range(256):
            self.write_int(bit_out, 32, frequencies.get(i))

    # Writes an unsigned integer of the given bit width to the given stream.
    def write_int(self, bit_out, number_of_bits, value):
        for i in reversed(range(number_of_bits)):
            bit_out.write((value >> i) & 1)  # Big endian

    def compress(self, frequencies, input_file, bit_out):
        compressed = ArithmeticEncoder(32, bit_out)
        while True:
            symbol = input_file.read(1)
            if len(symbol) == 0:
                break
            compressed.write(frequencies, symbol[0])
        compressed.write(frequencies, 256)  # EOF
        compressed.finish()  # Flush remaining code bits

    def decompress(self, frequencies, bit_in, out):
        dec = ArithmeticDecoder(32, bit_in)
        while True:
            symbol = dec.read(frequencies)
            if symbol == 256:  # EOF symbol
                break
            out.write(bytes((symbol,)))

    def arithmetic_code(self, input_file, output_file, frequencies):
        # Read input file again, compress with arithmetic coding, and write output file
        with open(input_file, "rb") as inp, contextlib.closing(BitOutputStream(open(output_file, "wb"))) as bit_out:
            self.write_frequencies(bit_out, frequencies)
            self.compress(frequencies, inp, bit_out)

    # Perform file decompression
    def arithmetic_decode(self, input_file, output_file):
        with open(output_file, "wb") as out, open(input_file, "rb") as input_file:
            bit_in = BitInputStream(input_file)
            frequencies = self.read_frequencies(bit_in)
            self.decompress(frequencies, bit_in, out)
