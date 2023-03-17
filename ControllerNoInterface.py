from model import CalculatorModel
from ViewNoInterface import View


class Controller:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = View()

    def run(self):
        operator, operand1, operand2 = self.view.get_input()
        self.model.pending_value = operand1
        self.model.value = operand2
        self.model.operator = operator
        result = self.model.calculate()
        self.view.display_result(result)