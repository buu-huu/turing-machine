from tape import *
from instruction import *


def read_program(path):
    with open(path) as f:
        instructions = f.readlines()
    instructions = [x.strip() for x in instructions]

    instruction_list = []
    for instruction in instructions:
        conditions = instruction.split('>')[0].split(',')
        result = instruction.split('>')[1].split(',')

        new_instruction = Instruction(conditions[0],
                                      conditions[1],
                                      result[0],
                                      result[1],
                                      result[2])

        instruction_list.append(new_instruction)

    return instruction_list


def main():
    tape = Tape(10, 0)
    tape.set_initial_values([1, 1, 1])

    instructions = read_program('turing_programs/double_ones.txt')


if __name__ == '__main__':
    main()
