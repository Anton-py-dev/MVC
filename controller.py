from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from model import CalculatorModel


class CalculatorController(QWidget):
    def __init__(self):
        super().__init__()
        self.model = CalculatorModel()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')
        self.setFixedSize(250, 250)

        self.result_display = QLineEdit('0')
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        self.result_display.setMaxLength(20)

        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        button_layout = QVBoxLayout()
        for row in button_grid:
            row_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.clicked.connect(self.handle_button_click)
                row_layout.addWidget(button)
            button_layout.addLayout(row_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_display)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def handle_button_click(self):
        button = self.sender()
        label = button.text()

        if label.isdigit() or label == '.':
            current_text = self.result_display.text()
            if label == '.' and '.' in current_text:
                return
            if current_text == '0' and label == '0':
                return
            if current_text == '0':
                current_text = ''
            self.result_display.setText(current_text + label)
        elif label in ['+', '-', '*', '/']:
            self.model.set_value(self.result_display.text())
            self.model.set_operator(label)
            self.result_display.setText('0')
        elif label == '=':
            self.model.set_value(self.result_display.text())
            self.model.calculate()
            self.result_display.setText(str(self.model.value))
        elif label == 'C':
            self.model.clear()
            self.result_display.setText('0')
