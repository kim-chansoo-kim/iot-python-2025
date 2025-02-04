# 변수와 자료형
# 변수는 => 변하는 수(Variable) <-> 상수(Constant)
# 상수의 예 Pi = 3.141592.....

# 변수
a = None    # 특수형 ( =의 뜻: None 을 a에 집어넣는다)
print(a) # a라는 변수에 무슨 값이 들어있는지 콘솔에 출력해줘! (print = 출력하는 함수)
print(type(a)) # a의 타입을 출력해줘

a = 10      # 정수(소수점없는 수), Integer
print(a) # 함수는 늘 괄호를 같이 사용
print(type(a))

a = 12345.34   # 실수(소수점있는 수), Float
print(a)
print(type(a))

a = 0b11111110  # 2진수(0과 1로 수를 표현방식), Binary
print(a)
print(type(a))

a = 0xFE    # 16진수(0~9, A, B, C, D, E, F[15] 로 수를 표현 방식), Hex
print(a)
print(type(a))

a = 1_900_000_000   # 천단위마다 쉼표와 같이 표현(Tip)
print(a)
print(type(a))

a = "Life is short, You need Python" # "문자열", String
print(a)
print(type(a))

a = 'Life is short, You need Python!' # '문자열', String
print(a)
print(type(a))

a = (3 > 1) # 불형 True | False, Boolean
print(a)
print(type(a))