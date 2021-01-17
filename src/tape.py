class Tape:
    def __init__(self, length, head_position):
        self.length = length
        self.values = []
        self.head_position = head_position

        self.current_state = 'z0'

    def set_initial_values(self, values):
        self.values = values

    def read_current_value(self):
        return self.values[self.head_position]
