class BurrowsWheelerTransform:

    def burrows_wheeler_transform(self, string_to_transform):
        assert "\002" not in string_to_transform and "\003" not in string_to_transform, "Input string cannot contain STX and ETX characters"
        string_to_transform = "\002" + string_to_transform + "\003"  # Add start and end of text marker
        # Table of rotations of string
        table = sorted(string_to_transform[i:] + string_to_transform[:i] for i in range(len(string_to_transform)))
        last_column = [row[-1:] for row in table]  # Last characters of each row
        return "".join(last_column)  # Convert list of characters into string

    def inverse_burrows_wheeler_transform(self, string_to_inverse_transform):
        table = [""] * len(string_to_inverse_transform)  # Make empty table
        for i in range(len(string_to_inverse_transform)):
            # Add a column of r
            table = sorted(string_to_inverse_transform[i] + table[i] for i in range(len(string_to_inverse_transform)))
        s = [row for row in table if row.endswith("\003")][0]  # Find the correct row (ending in ETX)
        return s.rstrip("\003").strip("\002")  # Get rid of start and end markers
