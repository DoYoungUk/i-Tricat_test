import math
import numpy as np
import matplotlib.pyplot as plt

# 기본 상수
pi = math.pi
e = math.e

class Calcular:
'''
기본 계산기 클래스
'''
    def __init__(self): # 생성자
        self.stack = [] # 스택

    def push(self, value):
        self.stack.append(value)
         #value를 받으면 스택에 추가하는 메소드

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        # 스택에 value가 있으면 value를 가져오고 제거하는 메소드
        else:
            raise ValueError("Stack is empty")
        # 스택이 비어있으면 "stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
        # 스택이 비어있는지 확인하는 메소드

    def calculate(self, expression):
        # expression에서 받은 value를 스택에 분류하는 메소드
        operand_stack = [] # 피연산자 스택
        operator_stack = [] # 연산자 스택
        #parenthesis_stack = [] 
        # 괄호 스택 (괄호 스택을 만들긴 했는데 괄호를 연산자랑 따로 처리하는 방법을 모르겠습니다ㅠ)
        for char in expression:
            if char.isdigit():
                operand_stack.append(float(char)) # 숫자일 경우 피연산자 스택에 추가
            elif char in "+-*/":
                operator_stack.append(char) # 연산자일 경우 연산자 스택에 추가
            elif char == '(':
                operator_stack.append(char) # 여는 괄호 연산자 스택에 추가
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.perform_operation(operand_stack, operator_stack)
                operator_stack.pop()
            # 닫는 괄호일 경우 연산자 스택에서 여는 괄호가 나올 때 까지 연산 수행
        while operator_stack:
            self.perform_operation(operand_stack, operator_stack) # 남은 연산 수행

        return operand_stack[0] # 피연산자 스택에 남아있는 마지막 값 반환

    def perform_operation(self, operand_stack, operator_stack):
        # 연산 수행 메소드
        if len(operand_stack) >= 2 and operator_stack: # 피연산자에 value가 2개 이상일때 돌아감
            operator = operator_stack.pop()
            b = operand_stack.pop()
            a = operand_stack.pop()
            result = self.do_math(a, b, operator)
            operand_stack.append(result)
        else:
            raise ValueError("수식이 올바르지 않습니다.") # 조건을 만족하지 못하면 오류

    def do_math(self, a, b, operator):
        # 연산자에 따른 value를 반환하는 메소드
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b != 0:
                return a / b
            else:
                raise ValueError("0으로 나눌 수 없습니다.") # 분모가 0인 예외경우 오류

     def __del__(self): # 소멸자
         pass


class EngineerCalculator(Calculator): # Calculator 클래스 상속받음
'''     
공학용 계산기 클래스
Calculator에서 상속받아 Calculator기능을 포함
'''
    def __init__(self):
        super().__init__() # 부모클래스인 Calculator 생성자 호출하여 초기화

    def calculate_trigonometric(self, function, angle):
        # 삼각함수 계산 메소드
        if function in ["sin", "cos", "tan"]:
            angle_rad = math.radians(angle) # 입력받은 각도를 라디안 단위로 변환
            if function == "sin":
                return math.sin(angle_rad)
            elif function == "cos":
                return math.cos(angle_rad)
            elif function == "tan":
                return math.tan(angle_rad)
        else:
            raise ValueError("Invalid trigonometric function")

    def calculate_factorial(self, n):
        # 팩토리얼 구하는 메소드
        if not isinstance(n,int) or n < 0:
            return "값을 구할 수 없습니다."
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)
        # n을 받으면 n-1이 1이 될때까지 곱한다

    def calculate_matrix(self, matrix_a, matrix_b):
        # 행렬곱 구하는 메소드
        return np.dot(matrix_a, matrix_b) # numpy 내장함수

    def plot_graph(self, x_values, y_values, title="Graph"):
        # 그래프 그리는 메소드
        plt.plot(x_values, y_values)
        plt.title(title)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()

calc = EngineerCalculator()

"""         계산기         """

# 사칙연산 #
expression = "1 + 2 - 3 * 4 / 5" # 큰따옴표 안에 수식
result = calc.calculate(expression)
print("사칙연산:", result)

# 삼각함수 #
tri = "cos" # sin or cos or tan
degree = pi # 각도
result_trigonometric = calc.calculate_trigonometric(tri, degree)
print("삼각함수:", result_trigonometric)

# 팩토리얼 #
fac = 10 # ?! 하고싶은 값
result_factorial = calc.calculate_factorial(fac)
print("팩토리얼:", result_factorial)

# 행렬식 #
matrix_a = np.array([[1, 2], [3, 4]]) # 행렬1
matrix_b = np.array([[5, 6], [7, 8]]) # 행렬2
result_matrix = calc.calculate_matrix(matrix_a, matrix_b)
print("행렬곱:", result_matrix)

# 그래프 #
x_values = np.linspace(0, 2 * np.pi, 100) # x값
y_values = np.sin(x_values) # y값
calc.plot_graph(x_values, y_values, title="Graph")
