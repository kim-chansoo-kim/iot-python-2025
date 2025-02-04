# 문자열 포맷팅

loginTemp = '안녕하세요, %s님!' # %s = 문자열 string
# Name = '퐁당'

# # print(loginTemp % (Name))
# name = input('로그인할 이름 입력 -> ')
# print(loginTemp % (Name))

## 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살입니다. 몸무게는 %fkg이고, 키는 %fcm입니다.'
print(intro % ('퐁당', 26, 93, 170))

intro = '나는 %4s(이)고, %03d살입니다. 몸무게는 %3.1fkg이고, 키는 %3.1fcm입니다.' ## %뒤에 숫자를 넣을시 문자를 포함한 칸수지정 
print(intro % ('퐁당퐁당', 26, 93, 170))

## 중간세대 문자열 포맷팅
intro = '나는 {0}(이)고, {1}살입니다. 몸무게는 {2}kg이고, 키는 {3}cm입니다.'
print(intro.format('퐁당', 25, 75, 180))

intro = '나는 {0}(이)고, {1}살입니다. 몸무게는 {2}kg이고, 키는 {3}cm입니다.' ## {0:10s} 작성시 뒤에 칸이생김 > 포함시 오른쪽 정렬
print(intro.format('퐁당', 25, 75, 180))

## 신세대 문자열 포맷팅
name = '당퐁'
age = 27
weight = 89
length = 171
print(f'나는 {name}이고, 나이는 {age}살입니다. 몸무게는 {weight}Kg이고, 키는 {length}입니다.')

