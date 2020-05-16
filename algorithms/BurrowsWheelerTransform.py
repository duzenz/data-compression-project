from operator import itemgetter


class BurrowsWheelerTransform:

    def code(self, text):
        text_length = len(text)
        sorted_table = sorted([text[i:text_length] + text[0:i] for i in range(text_length)])
        index = sorted_table.index(text)
        transformed_text = ''.join([element[-1] for element in sorted_table])
        return index, transformed_text

    def decode(self, index, transformed_text):
        transformed_length = len(transformed_text)
        x = sorted([(i, x) for i, x in enumerate(transformed_text)], key=itemgetter(1))

        table = [None for i in range(transformed_length)]
        for i, y in enumerate(x):
            j, _ = y
            table[j] = i

        table_row = [index]
        for i in range(1, transformed_length):
            table_row.append(table[table_row[i - 1]])

        text = [transformed_text[i] for i in table_row]
        text.reverse()
        return ''.join(text)
