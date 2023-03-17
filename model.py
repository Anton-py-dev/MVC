from decimal import Decimal


class CalculatorModel:
    def __init__(self):
        self.value = Decimal('0')
        self.operator = None
        self.pending_value = None

    def clear(self):
        self.value = Decimal('0')
        self.operator = None
        self.pending_value = None

    def set_value(self, value):
        self.value = Decimal(value)

    def set_operator(self, operator):
        self.operator = operator
        self.pending_value = self.value
        self.value = Decimal('0')

    def calculate(self):
        if self.operator == '+':
            self.value = self.pending_value + self.value
        elif self.operator == '-':
            self.value = self.pending_value - self.value
        elif self.operator == '*':
            self.value = self.pending_value * self.value
        elif self.operator == '/':
            if self.value == 0:
                self.value = Decimal('0')
            else:
                self.value = self.pending_value / self.value

        self.operator = None
        self.pending_value = None
        return self.value
