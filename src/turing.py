from PyQt5.QtWidgets import QApplication

from window import *
from tape import *
from instruction import *

import sys


def read_program(path):
    with open(path) as f:
        instructions = f.readlines()
    instructions = [x.strip() for x in instructions]

    # Cleaning up spaces in program file
    instructions_cleaned = []
    for line in instructions:
        instructions_cleaned.append(line.replace(' ', ''))

    instructions_cleaned = list(filter(None, instructions_cleaned))

    instruction_list = []
    for instruction in instructions_cleaned:
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
    # Reading program from file
    instructions = read_program('turing_programs/double_ones.txt')

    # Initializing the tape with begin values
    tape = Tape(10, 0, ['1', '1', '1'], instructions)

    # Running program
    tape.calc()

    print('Program completed. Result:')
    print(tape)

    print(tape.get_execution_storage())

    app = QApplication(sys.argv)
    window = Window(instructions)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
