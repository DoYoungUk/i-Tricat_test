기본 계산기 클래스를 만들고 이를 상속하여 공학용 계산 클래스를 생성하여 파이썬을 이용한 계산기를 구현해냈다.

-계산기의 기능은 다음과 같다-
1. 스택을 이용하여 사칙연산 가능
2. 괄호 처리 지원하며 사칙연산 식의 구성이 잘못됐을 경우 오류 발생
3. 삼각함수 계산이 가능함
4. 행렬 계산이 가능함
5. 팩토리얼 계산이 가능함
6. 그래프 그리기가 가능

첨부된 'test.py'의 line120 이후 값들을 변화시켜 원하는 계산식을 얻을 수 있다.
사용방법은 다음과 같다.

"""         계산기         """

# 사칙연산 #  --큰따옴표 안에 구하고자하는 사칙연산 식을 넣어 결과갚을 구할 수 있다.--
expression = "1 + 2 - 3 * 4 / 5" # 큰따옴표 안에 수식
result = calc.calculate(expression)
print("사칙연산:", result)

# 삼각함수 #  --tri에 원하는 삼각함수, degree에 각도를 넣어 삼각함수 값을 구할 수 있다--
tri = "cos" # sin or cos or tan
degree = pi # 각도
result_trigonometric = calc.calculate_trigonometric(tri, degree)
print("삼각함수:", result_trigonometric)

# 팩토리얼 #  --fac에 팩토리얼을 구하고싶은 정수를 넣어 값을 구할 수 있다--
fac = 10 # ?! 하고싶은 값
result_factorial = calc.calculate_factorial(fac)
print("팩토리얼:", result_factorial)

# 행렬식 #  --행렬1,2에 행렬곱을 구하고자하는 행렬을 넣는다--
matrix_a = np.array([[1, 2], [3, 4]]) # 행렬1
matrix_b = np.array([[5, 6], [7, 8]]) # 행렬2
result_matrix = calc.calculate_matrix(matrix_a, matrix_b)
print("행렬곱:", result_matrix)

# 그래프 # --그래프의 (x,y)좌표를 list를 이용해 지정하거나 numpy의 내장함수를 이용해 원하는 그래프를 그릴 수 있다.
x_values = np.linspace(0, 2 * np.pi, 100) # x값
y_values = np.sin(x_values) # y값
calc.plot_graph(x_values, y_values, title="Graph")
