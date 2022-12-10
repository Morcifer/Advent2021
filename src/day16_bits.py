from typing import List


def day16_parser(s: List[str]) -> str:
    hex_as_strings = ["{0:04b}".format(int(c, 16)) for c in s[0]]
    return "".join(hex_as_strings)


def parse_literal_value(data: str) -> int:
    this_index = 0
    while int(data[this_index]) == 1:
        this_index += 5
    this_index += 5
    return this_index


def parse(data: str, return_after_done: bool, all_version_numbers: List[int]) -> int:
    this_index = 0

    while this_index < len(data):
        version = int(data[this_index:this_index + 3], 2)
        type_id = int(data[this_index + 3:this_index + 6], 2)
        this_index += 6

        print(f"version: {version}, type_id: {type_id}")

        # if version == 0 and type_id == 0:
            # print("gah")

        all_version_numbers.append(version)

        if type_id == 4:
            this_index += parse_literal_value(data[this_index:])
        else:
            length_type_id = int(data[this_index], 2)
            this_index += 1
            print(f"length_type_id: {length_type_id}")

            if length_type_id == 0:
                # The next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
                length_of_length_in_bits = 15
                length_in_bits = int(data[this_index:this_index + length_of_length_in_bits], 2)
                this_index += length_of_length_in_bits

                sub_data = data[this_index:this_index + length_in_bits]

                parse(sub_data, False, all_version_numbers)

                this_index += length_in_bits
            else:
                # The next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
                length_of_length_in_sub_packets = 11
                length_in_sub_packets = int(data[this_index:this_index + length_of_length_in_sub_packets], 2)
                this_index += length_of_length_in_sub_packets
                for _ in range(length_in_sub_packets):
                    this_index += parse(data[this_index:], True, all_version_numbers)

        # print(f"index before 0 packing is {this_index}")
        # while this_index + 4 < len(data) and int(data[this_index:this_index + 4], 2) == 0:
        #     this_index += 4
        # print(f"index after 0 packing is {this_index}")
        if return_after_done:
            return this_index

    return this_index