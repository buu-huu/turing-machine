class Instruction:
    def __init__(self, condition_state, condition_read, result_state, result_write, result_move):
        self.condition_state = condition_state
        self.condition_read = condition_read
        self.result_state = result_state
        self.result_write = result_write
        self.result_move = result_move

    def __str__(self):
        return self.condition_state + ', ' + self.condition_read + ' -> ' + self.result_state \
            + ', ' + self.result_write + ', ' + self.result_move
