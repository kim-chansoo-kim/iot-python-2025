# for문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for (변수) in 반복할값:
#     구문안으로...

# 아래와 같이 출력되는 프로그램을 작성하시오.
'''
최대별수 : 4
*
**
***
****
'''

# range() 범위를 생성하는 클래스
# 마지막수 : max - 1
# range(8) -> reange(0, 8)
# range(init, max, add)
# print(range(0, 8, 2))

# for i in [0, 1, 2, 3, 4, 5, 6, 7]: # 이 조건이 참인도안만 반복...
# for i in range(0, 8, 2):
#     print(i)

# num = int(input('최대별수 : '))

# for i in range(1, num + 1):
#     print('*' * i)

# for문 구구단
# 2단부터 2x9 ~ 9x9
# 요구사항1 - 한줄에 각 단씩 나오도록
# 요구사항2 - x * y값이 항상 두 줄 간격이 되도록
# 요구사항3 - 단시작을 표시
for x in range(2, 9 + 1):
    if x == 5: break
    # if x == 5: continue
    print(f'\n{x}단 시작 ')
    for y in range(1, 9 + 1):

        # if y == 8: break
        print(f'{x} x {y} = {x * y:2d}', end ='   ') # :2d - 두줄 간격맞추기

    print() # 그냥 한줄 내리기
    
print('\n구구단 종료')


## 반복문을 빠져나올때 : break
## 반복문에서 특정 조건을 지나칠때 : continue