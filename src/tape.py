class Tape:
    def __init__(self, length, head_position):
        self.length = length
        self.values = []
        self.head_position = head_position

    def set_initial_values(self, values):
        self.values = values
