from collections import Counter

RADIX = 10  # can be any integer greater or equal with 2


class ArithmeticCoding:

    def arithmetic_coding(self, byte_of_str):
        # Karakterleri frekans dizisine dönüştür
        frequency = Counter(byte_of_str)

        frequency_table = self.get_cumulative_frequency_table(frequency)

        base_length = len(byte_of_str)

        # Lower bound
        lower_limit = 0

        # Product of all frequencies
        multiply_frequency = 1

        # Each term is multiplied by the product of the
        # frequencies of all previously occurring symbols
        for b in byte_of_str:
            lower_limit = lower_limit * base_length + frequency_table[b] * multiply_frequency
            multiply_frequency *= frequency[b]

        upper_limit = lower_limit + multiply_frequency

        power = 0
        while True:
            # floor division
            multiply_frequency //= RADIX
            if multiply_frequency == 0:
                break
            power += 1

        encrypted = (upper_limit - 1) // RADIX ** power
        return encrypted, power, frequency

    def arithmetic_decoding(self, encrypted, power, frequency):
        encrypted *= RADIX ** power
        base_length = sum(frequency.values())

        # Create the cumulative frequency table
        frequency_table = self.get_cumulative_frequency_table(frequency)

        # Create the dictionary
        dictionary = {}
        for key, value in frequency_table.items():
            dictionary[value] = key

        # Fill the gaps in the dictionary
        gap_char = None
        for i in range(base_length):
            if i in dictionary:
                gap_char = dictionary[i]
            elif gap_char is not None:
                dictionary[i] = gap_char

        # Decode the input number
        decoded = bytearray()
        for i in range(base_length - 1, -1, -1):
            power = base_length ** i
            division = encrypted // power

            char = dictionary[division]
            frequency_value = frequency[char]
            char_value = frequency_table[char]

            rem = (encrypted - power * char_value) // frequency_value

            encrypted = rem
            decoded.append(char)

        # Return the decoded string
        return bytes(decoded)

    def get_cumulative_frequency_table(self, frequency):
        cumulative_frequency_table = {}
        total = 0
        for char_byte in range(256):
            if char_byte in frequency:
                cumulative_frequency_table[char_byte] = total
                total += frequency[char_byte]
        return cumulative_frequency_table
