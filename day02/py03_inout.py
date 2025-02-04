# 화면입출력

print('출력입니다.')

# 기본입력
number = input('만 나이를 입력하세요 ->') # 입력 방법
# # 입력값, 출력값 모두 문자열이다
number = int(number) # str -> int 문자를 숫자로
print(type(number))
print("현재나이는", number + 1) # 여러값을 같이 출력하려면 , 로 구분

# 다중입력
x, y = input('합산할 두 수를 입력하세요.').split() # 기본으로 공백으로 잘라줘
x = int(x)
y = int(y)
print(x + y)