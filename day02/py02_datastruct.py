# 복합자료형
# 자료구조 및 알고리즘

# 리스트 사용 이전
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)
# 리스트 사용시 []
# 리스트(배열) 사용 후 - 다른언어에서는 리스트와 배열은 다른 것
f = [1, 2, 3, 4, 5]
print(f)
print(type(f))

f = ['life', 'is', True, 0 , None, [1, 2, 3]]
print(f)
print(f[0]) # 리스트의 첫번째 값을 출력 (숫자는 언제나 0부터 시작)
# 리스트의 한 요소에도 값을 집어 넣을 수 있음
f[3] = 100
print(f)

## 튜플 
# 듀플 사용시()
# 리스트와 거의 흡사하나, 값을 변경할 수 없음
t = (1, 2, 3, 4)
print(t)
print(t[3])
# t[0] = 5 주석 토글 (Ctrl + /) 사용
print(type(t))

## 딕셔너리(사전형) {key : value} 의 집합
spiderman = {'name': 'Peter Parker', 'age': 20, 'weapon': 'Web Shooter'}
print(spiderman)
print(type(spiderman))

print(spiderman['name'])
spiderman['age'] = 21
print(spiderman)

## 집합 (), {}, [] 전부사용, 수학의 집합과 동일, 중복 제거, 리스트처럼 인덱스 가 없음
s = set([1, 3, 5, 7, 9, 5])
print(s)
print(type(s))

s = set('Hello World')
print(s)

## 변수명 지정 방식
## 의미있느 단어들의 조합으로 만들것
PhoneNumber = '010-4***-****'
salaryBankAccount = '939***-00-******'


samsung = ''
samsung1 = ''
_samsung = ''
samsung_ = ''
# 1samsung = '' # 변수는 숫자로 시작할 수 없음
# samsung! = '' # _이외의 특수문자 사용불가
# samsung* = ''
# samgsung-apple = '' # 파이썬 연산자는 사용불가
# samgsung+apple = '' 
# samgsung=apple = '' 