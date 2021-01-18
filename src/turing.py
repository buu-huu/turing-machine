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
    # Initializing the tape with begin values
    tape = Tape(10, 0, ['1', '1', '1', '1'])

    # Reading program from file
    instructions = read_program('turing_programs/double_ones.txt')

    execution_storage = [tape.get_values()]

    # Running program
    while tape.current_state != 'zE':
        run = 0
        for instruction in instructions:
            if instruction.condition_state == tape.current_state:
                if instruction.condition_read == tape.read_current_value():
                    print('Executing instruction: ', instruction)
                    tape.execute_instruction(instruction)
                    execution_storage.append(tape.get_values())
                    break
            run += 1
            if run == len(instructions):
                print('No applicable instruction in program found. Avoiding endless loop. Exiting.')
                tape.current_state = 'zE'

    print('Program completed. Result:')
    print(tape)

    print(execution_storage)

    app = QApplication(sys.argv)
    window = Window(instructions)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
