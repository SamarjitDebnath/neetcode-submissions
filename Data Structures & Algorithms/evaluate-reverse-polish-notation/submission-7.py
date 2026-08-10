class Solution:
    @staticmethod
    def __operate(a: int, b: int, operator: str):
        if operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        elif operator == '*':
            return a*b
        elif operator == "/":
            return int(a/b)
        else:
            raise ValueError('Invalid operator value')

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = "+-*/"
        for elem in tokens:
            if elem not in operators:
                nums.append(int(elem))
            else:
                num1 = nums.pop() # second operand
                num2 = nums.pop() # first operand
                nums.append(self.__operate(num2, num1, elem))
        return nums[0] if nums else 0

