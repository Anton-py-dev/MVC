class View:
    def display_result(self, result):
        print("Result: ", result)

    def get_input(self):
        operator = input("Enter an operator (+, -, *, /): ")
        operand1 = float(input("Enter the first operand: "))
        operand2 = float(input("Enter the second operand: "))
        return operator, operand1, operand2