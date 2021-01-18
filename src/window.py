from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self, program, execution_storage):
        super().__init__()

        self.program_length = len(program)
        self.column_count_max = len(max(execution_storage, key=len))

        self.initUI()
        self.load_program_to_list(program)

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Turing Machine')

        self.program_list = QListWidget()
        self.program_list.setMaximumWidth(200)

        self.list_label = QLabel()
        self.list_label.setText('Program')
        self.list_label.setAlignment(Qt.AlignLeft)

        self.table = QTableWidget()
        self.table.setRowCount(1)
        self.table.setColumnCount(self.column_count_max)
        self.table.resizeColumnsToContents()
        self.table.setItem(0, 0, QTableWidgetItem('1'))
        self.table.setItem(0, 1, QTableWidgetItem('2'))

        # Layout
        self.master_layout = QHBoxLayout(self)
        self.master_layout.setAlignment(Qt.AlignLeft)

        self.prog_box = QVBoxLayout(self)
        self.prog_box.addWidget(self.list_label)
        self.prog_box.addWidget(self.program_list)

        self.master_layout.addLayout(self.prog_box)
        self.master_layout.addWidget(self.table)
        self.setLayout(self.master_layout)

        self.show()

    def load_program_to_list(self, program):
        for instruction in program:
            item_string = instruction.condition_state + ', ' + instruction.condition_read \
                        + ' -> ' + instruction.result_state + ', ' + instruction.result_write \
                        + ', ' + instruction.result_move
            self.program_list.addItem(item_string)