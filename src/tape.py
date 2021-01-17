class Tape:
    def __init__(self, length, head_position, values):
        self.length = length
        self.values = values
        self.head_position = head_position

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
        try:
            value = self.values[self.head_position]
        except IndexError:
            self.values.append('EMP')
            value = self.values[self.head_position]
        return value

    def write_current_value(self, value):
        try:
            self.values[self.head_position] = value
        except IndexError:
            self.values.append('EMP')
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

    def execute_instruction(self, instruction):
        self.write_current_value(instruction.result_write)
        self.move_head(instruction.result_move)
        self.current_state = instruction.result_state
