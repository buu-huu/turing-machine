#!/usr/bin/env python3

import os
import sys

from PyQt5.QtWidgets import QApplication

from instruction import *
from tape import *
from window import *


def read_program(path):
    with open(path) as f:
        instructions = f.readlines()
    instructions = [x.strip() for x in instructions]

    # Cleaning up spaces in program file
    instructions_cleaned = []
    for line in instructions:
        if not line.startswith('#'):
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
        lines = (line.rstrip() for line in f)

        state_string = ''
        for line in lines:
            if not line.startswith('#'):
                state_string += line
                break

        state_arr = state_string.replace(' ', '').split(',')

        result = []
        for element in state_arr:
            result.append(str(element))

        return result


def print_help():
    print('Turing machine\n')
    print('First, declare your initial state in the file initial_state.txt.')
    print('Usage: python turing.py <PROGRAM FILE PATH>')
    print('Example: python turing.py turing_programs/double_ones.txt')


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    programfile_path = sys.argv[1]

    if not os.path.isfile(programfile_path):
        print('The program file you specified does not exist!')
        sys.exit(0)

    program = read_program(programfile_path)
    initial_state = read_initial_state('initial_state.txt')

    tape = Tape(10, 0, initial_state, program)
    tape.calc()

    app = QApplication(sys.argv)
    window = Window(program, tape.execution_storage, tape.head_storage, tape.state_storage)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
