class Tape:
    EMPTY_STRING = 'EMP'

    def __init__(self, length, head_position, initial_values, instructions):
        self.length = length
        self.values = initial_values
        self.head_position = head_position
        self.instructions = instructions
        self.execution_storage = [self.get_values()]
        self.head_storage = [self.head_position]
        self.state_storage = []

        self.current_state = 'z0'

    def __str__(self):
        result_string = '========= TAPE DUMP =========\n'
        for value in self.values:
            result_string += value
            result_string += ' '
        result_string += '\n============================='
        return result_string

    def set_initial_values(self, values):
        self.values = values

    def read_current_value(self):
        if self.head_position >= len(self.values):
            self.values.append(self.EMPTY_STRING)

        return self.values[self.head_position]

    def write_current_value(self, value):
        if self.head_position >= len(self.values):
            self.values.append(self.EMPTY_STRING)

        self.values[self.head_position] = value

    def move_head(self, instr_char):
        if instr_char == 'R':
            self.head_position += 1
        elif instr_char == 'L':
            if self.head_position > 0:
                self.head_position -= 1
            else:
                print('ERROR: Cant move head left. Already at ')
        elif instr_char == 'H':
            print('INFO: Hold signal sent to head.')
        else:
            print('ERROR: Cant move head. Unknown instruction: ', instr_char)

    def get_values(self):
        return [x for x in self.values]

    def execute_instruction(self, instruction):
        self.write_current_value(instruction.result_write)
        self.move_head(instruction.result_move)
        self.current_state = instruction.result_state

        self.execution_storage.append(self.get_values())
        self.head_storage.append(self.head_position)
        self.state_storage.append(instruction.condition_state + '->' + instruction.result_state)

    def calc(self):
        while self.current_state != 'zE':
            run = 0
            for instruction in self.instructions:
                if instruction.condition_state == self.current_state:
                    if instruction.condition_read == self.read_current_value():
                        print('Executing instruction: ', instruction)
                        self.execute_instruction(instruction)
                        break
                run += 1
                if run == len(self.instructions):
                    print('No applicable instruction in program found. Avoiding endless loop. Exiting.')
                    self.current_state = 'zE'

        print('Program completed. Result:')
        print(self.__str__())
