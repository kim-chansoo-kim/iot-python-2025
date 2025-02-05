# if문 : 흐름제어 가장 기본
# 흐름제어문 마지막엔 항상 콜론(:)을 사용해야 한다
# if (참이되는 조건):
#   if문 안으로 들어간다!

age = int(input('나이를 입력하세요.'))

# 만약에 나이가 19세가 아니면 담배를 살 수없음
# 조건이 여러개 일때 and, or로 계속 작성
# if age > 19 or age == 19: # 아래와 같은 참인 조건 (19살이상이거나 19살이거나)
if age >= 19: # 참인 조건, if는 무조건 참으로
    print('4500원 입니다.')
else: # 거짓(false)일때는 else
    print('죽을래? 집에가!')


grade = input('학접을 입력하십시오(A | B | C | D | F).').upper() # .upper -> 소문자를 입력해도 대문자로 변경
if grade == 'A' or grade == 'B': # 학점이 A이거나 B면, 이 구문(if grade == 'A'or'B')걸리면 
    # if문 안으로 들어간다
    print('공부를 열심히 하셨네요.')
    print('축하합니다!')
    if grade == 'A':
        print('장학금 받아가세요~')
    else:
        print('장학금까지 바랬냐?')
elif grade == 'C': # 학점이 C이면
    print('그럭저럭 하셨네요.')
else:
    print('공부좀 해라!')