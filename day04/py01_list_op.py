# 리스트 연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 구조
# iterable -> 반복할 수 있는 요소가 for, while문에 사용 된다 (반복이되는 range나 리스트셈플을 사용)

listsample = [1,2,3,4,5,6,7,8,9,10] # <- 반복되는것

sum = 0
for i  in listsample:
    sum = sum + i # sum += i
print(f'합산결과 = {sum}')

# 리스트 연산
arr = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
print(arr)
print(arr[4])
print(arr[0] + arr[2])
print(arr[-2])
print(arr[2:3])

# # 문자열 연산이랑 같은
print(arr + arr2) # 리스트 두개 합치기
print(arr * 2) # 리스트 두번출력

# # 리스트 길이
print(len(arr))

# # 데이터 할당
arr[2] = 9
print(arr)

## 리스트 요소 삭제
arr[2] = None
print(arr)

del(arr[2])
print(len(arr), arr)

## 리스트 요소 추가
arr.append(7)
print(arr)

arr.insert(2, 100)
print(arr)

## 리스트를 합칠때
print(arr.extend(arr2))

## 리스트 정렬(쇼핑몰 낮은가격순, 높은가격순, 최신등록일자, ...)
arr = [6, 7, 1, 3, 9, 0, 2, 8]
print(arr)
arr.sort() # 오름차순 정렬
print(arr)
arr.sort(reverse=True) # 내림차순 정렬
print(arr)
## arr.reverse() # 정렬아님
# print(arr)

## 요소의 위치
print(arr.index(6)) # 없는 데이터를 인덱스하면 오류 발생

## 요소꺼내기 - 마지막 인덱스를 꺼내버림 출력이 안됨 (append와 반대개념)
print(arr.pop())
print(arr)

## 리스트컴프리핸션(반복문), 대량의 리스트를 쉽게 생성 할 수 있는 방법!!!
arr = [i for i in range(1, 100 + 1)]
print(arr)

sum = 0
for i in arr:
    sum = sum + i
print(f'{len(arr)}까지의 합산은, {sum}입니다.')