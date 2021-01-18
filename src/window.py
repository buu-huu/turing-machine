from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self, program, execution_storage, head_storage, state_storage):
        super().__init__()

        self.program_length = len(program)
        self.column_count = len(max(execution_storage, key=len))
        self.row_count = len(execution_storage)
        self.values = execution_storage
        self.head_positions = head_storage
        self.state_storage = state_storage

        self.initUI()
        self.load_program_to_list(program)

    def initUI(self):
        self.setGeometry(300, 300, 950, 450)
        self.setWindowTitle('Turing Machine')

        self.program_list = QListWidget()
        self.program_list.setMaximumWidth(200)

        self.list_label = QLabel()
        self.list_label.setText('Program')
        self.list_label.setAlignment(Qt.AlignLeft)

        self.table_execution = QTableWidget()
        self.table_execution.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_execution.setRowCount(self.row_count)
        self.table_execution.setColumnCount(self.column_count)
        self.table_execution.resizeColumnsToContents()
        self.init_table_execution_blank()
        self.add_table_execution_rows()

        self.table_execution_label = QLabel()
        self.table_execution_label.setText('Execution (highlighted cell = head position)')
        self.table_execution_label.setAlignment(Qt.AlignLeft)

        self.table_state = QTableWidget()
        self.table_state.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_state.verticalScrollBar().hide()
        #self.table_state.verticalHeader().hide()
        self.table_state.setFixedWidth(120)
        self.table_state.setRowCount(self.row_count)
        self.table_state.setColumnCount(1)
        self.add_table_state_rows()
        self.table_state.setHorizontalHeaderLabels(['State'])
        self.table_state.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

        self.table_state_label = QLabel()
        self.table_state_label.setText('State')
        self.table_state_label.setAlignment(Qt.AlignLeft)

        self.table_execution.verticalScrollBar().valueChanged.connect(
            self.table_state.verticalScrollBar().setValue
        )
        self.table_state.verticalScrollBar().valueChanged.connect(
            self.table_execution.verticalScrollBar().setValue
        )

        # Layout
        self.master_layout = QHBoxLayout(self)
        self.master_layout.setAlignment(Qt.AlignLeft)

        self.prog_box = QVBoxLayout(self)
        self.prog_box.addWidget(self.list_label)
        self.prog_box.addWidget(self.program_list)

        self.table_state_box = QVBoxLayout(self)
        self.table_state_box.addWidget(self.table_state_label)
        self.table_state_box.addWidget(self.table_state)

        self.table_execution_box = QVBoxLayout(self)
        self.table_execution_box.addWidget(self.table_execution_label)
        self.table_execution_box.addWidget(self.table_execution)

        self.table_box = QHBoxLayout(self)
        self.table_box.addLayout(self.table_state_box)
        self.table_box.addLayout(self.table_execution_box)

        self.master_layout.addLayout(self.prog_box)
        self.master_layout.addLayout(self.table_box)
        self.setLayout(self.master_layout)

        self.show()

    def add_table_execution_rows(self):
        i = 0
        for value_set in self.values:
            j = 0
            for value in value_set:
                self.table_execution.setItem(i, j, QTableWidgetItem(value))
                j += 1
            i += 1

        for k in range(len(self.head_positions)):
            self.table_execution.item(k, self.head_positions[k]).setBackground(QColor(220, 140, 230))

    def add_table_state_rows(self):
        for i in range(len(self.state_storage)):
            self.table_state.setItem(i, 0, QTableWidgetItem(self.state_storage[i]))

    def init_table_execution_blank(self):
        for i in range(self.row_count):
            for j in range(self.column_count):
                self.table_execution.setItem(i, j, QTableWidgetItem())

    def load_program_to_list(self, program):
        for instruction in program:
            item_string = instruction.condition_state + ', ' + instruction.condition_read \
                        + ' -> ' + instruction.result_state + ', ' + instruction.result_write \
                        + ', ' + instruction.result_move
            self.program_list.addItem(item_string)