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


def read_initial_state(path):
    with open(path) as f:
        state = f.readlines()
        state_arr = state[0].replace(' ', '').split(',')

        result = []
        for element in state_arr:
            result.append(str(element))

        return result


def main():
    program = read_program('turing_programs/double_ones.txt')
    initial_state = read_initial_state('initial_state.txt')

    tape = Tape(10, 0, initial_state, program)
    tape.calc()

    # GUI
    app = QApplication(sys.argv)
    window = Window(program, tape.execution_storage, tape.head_storage, tape.state_storage)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
