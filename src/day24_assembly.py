import math
import sys
from enum import Enum
from typing import List, Dict
from datetime import datetime


class InstructionType(str, Enum):
    inp = "inp",  # a - Read an input value and write it to variable a.
    add = "add",  # a b - Add the value of a to the value of b, then store the result in variable a.
    mul = "mul",  # a b - Multiply the value of a by the value of b, then store the result in variable a.
    div = "div",  # a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result.
    mod = "mod",  # a b - Divide the value of a by the value of b, then store the remainder.
    eql = "eql"   # a b - If the value of a and b are equal, then store the value 1. Otherwise, store the value 0.


class Instruction:
    instruction_type: InstructionType
    register_a: str
    register_b: str
    number_b: int

    def __init__(self, instruction_type, register_a, register_b, number_b):
        self.instruction_type = instruction_type
        self.register_a = register_a
        self.register_b = register_b
        self.number_b = number_b

    def get_a(self, local_variables: Dict[str, int]):
        return local_variables[self.register_a]

    def set_a(self, local_variables: Dict[str, int], new_value: int):
        local_variables[self.register_a] = new_value

    def get_b(self, local_variables: Dict[str, int]):
        return self.number_b if self.number_b is not None else local_variables[self.register_b]


def day24_parser(s: List[str]) -> Instruction:
    instruction_type = InstructionType(s[0])
    register_a = s[1]
    register_b = s[2] if len(s) >= 3 else None
    number_b = int(register_b)\
        if register_b is not None and (register_b.isdigit() or register_b[0] == "-")\
        else None

    return Instruction(instruction_type, register_a, register_b, number_b)


def find_highest_model_number(instructions: List[Instruction]) -> int:
    # To enable as many submarine features as possible, find the largest valid fourteen-digit model number
    # that contains no 0 digits.
    memory = {}
    count = 0
    for number in range(100000000000000, 10000000000000, -1):
        if "0" in str(number):
            continue

        count += 1
        if count % 1000000 == 0:
            print(f"{datetime.now()}: Checking the number {number}")

        if validate_model_number_short(instructions, str(number), memory):
            return number
    return -1


def validate_model_number(instructions: List[Instruction], number: str) -> bool:
    local_variables = {
        "x": 0,
        "y": 0,
        "z": 0,
        "w": 0,
    }

    number_spot = -1

    for instruction in instructions:
        if instruction.instruction_type == InstructionType.inp:
            number_spot += 1
            local_variables["w"] = int(number[number_spot])
        elif instruction.instruction_type == InstructionType.add:
            result = instruction.get_a(local_variables) + instruction.get_b(local_variables)
            instruction.set_a(local_variables, result)
        elif instruction.instruction_type == InstructionType.mul:
            result = instruction.get_a(local_variables) * instruction.get_b(local_variables)
            instruction.set_a(local_variables, result)
        elif instruction.instruction_type == InstructionType.div:
            result = int(math.floor(instruction.get_a(local_variables) / instruction.get_b(local_variables)))
            instruction.set_a(local_variables, result)
        elif instruction.instruction_type == InstructionType.mod:
            result = instruction.get_a(local_variables) % instruction.get_b(local_variables)
            instruction.set_a(local_variables, result)
        elif instruction.instruction_type == InstructionType.eql:
            result = 1 if instruction.get_a(local_variables) == instruction.get_b(local_variables) else 0
            instruction.set_a(local_variables, result)

    # Then, after MONAD has finished running all of its instructions, it will indicate that the model number was valid
    # by leaving a 0 in variable z.
    # However, if the model number was invalid, it will leave some other non-zero value in z.
    return local_variables["z"] == 0


def validate_model_number_short(instructions: List[Instruction], number: str, memory) -> bool:
    extra_3 = [1, 1, 1, 26, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26]
    extra_1 = [12, 10, 13, -11, 13, -1, 10, 11, 0, 10, -5, -16, -7, -11]
    extra_2 = [6, 6, 3, 11, 9, 3, 13, 6, 14, 10, 12, 10, 11, 15]

    # z = 0
    # for i, digit in enumerate(number):
    #     # inp w
    #     w = int(digit)
    #     key = (z, w, extra_1[i], extra_2[i], extra_3[i])
    #     if key in memory:
    #         z = memory[key]
    #     else:
    #         z = run_single_loop(*key)
    #         memory[key] = z

    z = []
    for i, digit in enumerate(number):
        if len(z) > 14 - i:  # No way we can get rid of it.
            return False
        w = int(digit)
        run_single_loop_stack(z, w, extra_1[i], extra_2[i], extra_3[i])

    return len(z) == 0 or z[0] == 0


# def run_single_loop(z: int, w: int, extra_1: int, extra_2: int, extra_3: int) -> int:
#     # x = 0 if (z % 26 + extra_1) == w else 1  # w between 1 and 9 means - extra_1 vs 0..25
#     # z = x * (w + extra_2) + (25 * x + 1) * (z if extra_3 == 1 else int(math.floor(z / extra_3)))  # extra_3 = {1, 26}
#     if z % 26 == w - extra_1:  # x == 0
#         z = (z if extra_3 == 1 else int(math.floor(z / extra_3)))
#     else:   # x == 1
#         if extra_3 == 1:
#             z = w + extra_2 + 26 * z
#         else:
#             z += w + extra_2 - z % 26
#
#     return z

def run_single_loop(z: int, w: int, extra_1: int, extra_2: int, extra_3: int) -> int:
    # x = 0 if (z % 26 + extra_1) == w else 1  # w between 1 and 9 means - extra_1 vs 0..25
    # z = x * (w + extra_2) + (25 * x + 1) * (z if extra_3 == 1 else int(math.floor(z / extra_3)))  # extra_3 = {1, 26}
    modulu = z % 26

    # z behaves a bit like a stack/base-26 number
    if modulu == w - extra_1:  # x == 0.
        if extra_3 == 1:
            z = z
        else:   # 26
            z = int(math.floor(z / 26))  # Either 0, or the previous z?
    else:   # x == 1
        # in both of these cases we get (a multiple of 26) + w + extra_2
        if extra_3 == 1:
            z = w + extra_2 + 26 * z
        else:  # 26
            z += w + extra_2 - modulu

    return z


def run_single_loop_stack(z: List[int], w: int, extra_1: int, extra_2: int, extra_3: int):
    # x = 0 if (z % 26 + extra_1) == w else 1  # w between 1 and 9 means - extra_1 vs 0..25
    # z = x * (w + extra_2) + (25 * x + 1) * (z if extra_3 == 1 else int(math.floor(z / extra_3)))  # extra_3 = {1, 26}
    if len(z) == 0:
        return z.append(w + extra_2)

    modulu = z[-1]

    # z behaves a bit like a stack/base-26 number
    if modulu == w - extra_1:  # x == 0.
        if extra_3 == 1:
            # z = z
            pass
        else:   # 26
            # z = int(math.floor(z / 26))  # Either 0, or the previous z?
            z.pop(-1)
    else:   # x == 1
        # in both of these cases we get (a multiple of 26) + w + extra_2
        if extra_3 == 1:
            z.append(w + extra_2)
        else:  # 26
            z[-1] = w + extra_2


if __name__ == "__main__":
    extra_3 = [1, 1, 1, 26, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26]
    extra_1 = [12, 10, 13, -11, 13, -1, 10, 11, 0, 10, -5, -16, -7, -11]
    extra_2 = [6, 6, 3, 11, 9, 3, 13, 6, 14, 10, 12, 10, 11, 15]

    z = []

    # Answer is for sure higher than 59999667000000

    for w1 in range(9, 0, -1):
        z1 = z[:]
        run_single_loop_stack(z1, w1, extra_1[0], extra_2[0], extra_3[0])

        for w2 in range(9, 0, -1):
            z2 = z1[:]
            run_single_loop_stack(z2, w2, extra_1[1], extra_2[1], extra_3[1])

            for w3 in range(9, 0, -1):
                z3 = z2[:]
                run_single_loop_stack(z3, w3, extra_1[2], extra_2[2], extra_3[2])

                for w4 in range(9, 0, -1):
                    z4 = z3[:]
                    run_single_loop_stack(z4, w4, extra_1[3], extra_2[3], extra_3[3])

                    for w5 in range(9, 0, -1):
                        z5 = z4[:]
                        run_single_loop_stack(z5, w5, extra_1[4], extra_2[4], extra_3[4])

                        for w6 in range(9, 0, -1):
                            z6 = z5[:]
                            run_single_loop_stack(z6, w6, extra_1[5], extra_2[5], extra_3[5])

                            for w7 in range(9, 0, -1):
                                z7 = z6[:]
                                run_single_loop_stack(z7, w7, extra_1[6], extra_2[6], extra_3[6])

                                for w8 in range(9, 0, -1):
                                    print(f"{datetime.now()}: Checking the around the {w1}{w2}{w3}{w4}{w5}{w6}{w7}{w8}000000")

                                    z8 = z7[:]
                                    run_single_loop_stack(z8, w8, extra_1[7], extra_2[7], extra_3[7])

                                    for w9 in range(9, 0, -1):
                                        z9 = z8[:]
                                        run_single_loop_stack(z9, w9, extra_1[8], extra_2[8], extra_3[8])

                                        for w10 in range(9, 0, -1):
                                            z10 = z9[:]
                                            run_single_loop_stack(z10, w10, extra_1[9], extra_2[9], extra_3[9])

                                            for w11 in range(9, 0, -1):
                                                z11 = z10[:]
                                                run_single_loop_stack(z11, w11, extra_1[10], extra_2[10], extra_3[10])

                                                for w12 in range(9, 0, -1):
                                                    z12 = z11[:]
                                                    run_single_loop_stack(z12, w12, extra_1[11], extra_2[11], extra_3[11])

                                                    for w13 in range(9, 0, -1):
                                                        z13 = z12[:]
                                                        run_single_loop_stack(z13, w13, extra_1[12], extra_2[12], extra_3[12])

                                                        for w14 in range(9, 0, -1):
                                                            z14 = z13[:]
                                                            run_single_loop_stack(z14, w14, extra_1[13], extra_2[13], extra_3[13])

                                                            if len(z14) == 0 or z14[0] == 0:
                                                                print("NUMBER FOUND!!!")
                                                                print(f"{w1}{w2}{w3}{w4}{w5}{w6}{w7}{w8}{w9}{w10}{w11}{w12}{w13}{w14}")
                                                                sys.exit()
