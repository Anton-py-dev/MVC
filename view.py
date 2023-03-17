from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()

        # Create the widgets
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)

        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')

        self.button_add = QPushButton('+')
        self.button_subtract = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_divide = QPushButton('/')
        self.button_clear = QPushButton('C')
        self.button_equals = QPushButton('=')

        # Create the layout
        layout = QVBoxLayout()

        display_layout = QHBoxLayout()
        display_layout.addWidget(self.display)

        button_layout_1 = QHBoxLayout()
        button_layout_1.addWidget(self.button_7)
        button_layout_1.addWidget(self.button_8)
        button_layout_1.addWidget(self.button_9)
        button_layout_1.addWidget(self.button_add)

        button_layout_2 = QHBoxLayout()
        button_layout_2.addWidget(self.button_4)
        button_layout_2.addWidget(self.button_5)
        button_layout_2.addWidget(self.button_6)
        button_layout_2.addWidget(self.button_subtract)

        button_layout_3 = QHBoxLayout()
        button_layout_3.addWidget(self.button_1)
        button_layout_3.addWidget(self.button_2)
        button_layout_3.addWidget(self.button_3)
        button_layout_3.addWidget(self.button_multiply)

        button_layout_4 = QHBoxLayout()
        button_layout_4.addWidget(self.button_0)
        button_layout_4.addWidget(self.button_clear)
        button_layout_4.addWidget(self.button_equals)
        button_layout_4.addWidget(self.button_divide)

        layout.addLayout(display_layout)
        layout.addLayout(button_layout_1)
        layout.addLayout(button_layout_2)
        layout.addLayout(button_layout_3)

