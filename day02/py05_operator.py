# 연산자

# 사칙연산 기호[ +, -, * ]
a, b = 15, 14
# shift + Del 는 한줄 삭제(매우 효율!)
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자 기호[ /, //, % ]
a = 14
b = 4
print(a / b) # 나눈 결과는 소수점이 있는 실수(float)
print(a // b) # 나눈 몫, int
print(a % b) # 나머지, int

# 거듭제곱 (Power) 기호[ ** ]
print(2 ** 5)

# 연산자 우선순위
## 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 ()사용
print((3 + 4) * 7)
print(3 + (4 * 7))

## 리스트 연산
## index = len(list) - 1
listSample = [1, 3, 5, 7, 9]
print(listSample[0])
print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])

listSample[4] = 11

print(listSample[len(listSample) - 1])
print(len(listSample), '-> 리스트의 길이입니다.') # len = 리스트의 길이

## 문자열 연산 : +, * 만 존재
greeting = 'Hello'
target = 'World'
print(greeting, target) # 문자열 연산이 아님 (기본문자열 작성)
print(greeting + target) # 문자열 연산 + string concatenate (두개를 '붙여서' 출력해줘)
# 한줄 띄운 문자열의 여러가지 방식
print(greeting + ' ' + target)
print(f'{greeting} {target}')
print('{0} {1}'.format(greeting, target))

print(greeting * 5) # 해당 문자열을 * 수로 반복

## 문자열(Charactor Array) : List와 유사하지만 값 수정 불가
print(greeting[1]) # 리스트 연산
# greeting[0] = 'C'
print(greeting)

## 리스트 연산, 슬라이싱
listSample = ['2','0','2','5','-','0','2','-','0','4']
current = '2025-02-04' # 위와 동일

for i in listSample:
    print(i, end='')
print()

print(current)
# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-7])
print(current[-7])

# 슬라이싱, 리스트 자르기
## [start:end] == end - 1까지만 추출
print(listSample[0:3 + 1]) # 원하는 곳까지 출력을 원할시 +1
print(current[0:3 + 1])

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:] # end 끝까지는 숫자를 생략
print(year, month, day)
print(current[-2:])

## 문자열 연산 중 함수를 사용

# 자르기 - .split
full_name = "Pongdang CS. Kim"
print(full_name.split())
print(full_name.split(' ')) # 위와 동일

names = full_name.split(' ')
print(type(names))
print(names)

names = full_name.split('.')
print(type(names))
print(names)

# 바꾸기 - .replace
print(full_name.replace('Pongdang CS.', 'Dangpong'))

# 공백제거 - .strip
origin = '     Hello  ~     '
print(f'//{origin}//')
print(f'//{origin.lstrip()}//')
print(f'//{origin.rstrip()}//')
print(f'//{origin.strip()}//')

# 단어 찾기
full_name = "Pongdang CS. Kim"
print(full_name.find('C'))
print(full_name.find('c')) # -1 == 소문자c를 찾을 수 없음!
print(full_name.count('g')) # g가 문장에 몇번 존재
# print(full_name.index('c')) # 오류발생! 

print(full_name.upper()) # 모든 단어 대문자
print(full_name.lower()) # 모든 단어 소문자

## T로 자를때
# '', "" == Empty(비어있다)
# ' ', " " == Space(공백존재)
origin = 'ITESTSTRING'
print(origin.split('T'))