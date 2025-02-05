class Person:
    # 명사(속성)인 멤버변수
    name = '퐁당'
    age = 26
    weight = 93
    gender = 'male'

    # 초기화(생성자) 메서드(파이썬 기본으로 포함)
    def __init__(self, name, age, wegiht, gender):
        self.name = name
        self.age = age
        self.weight = wegiht
        self.gender = gender

    def __str__(self): # 객체 출력을 문자열 포맷팅!
        retStr = f'{self.name}\n{self.age}세\n{self.weight}kg\n{self.gender}'
        return retStr

    # 동사(기상)인 멤버함수(메서드)
    def getup(self): # myself
        print(f'{self.name}이(가) 일어납니다.')

    # 몸무게 변경
    def setWdight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')
    
    def getGender(self):
        return self.gender

man = Person('당근', 25, 82.7, 'man') # __init__()특수 함수를 실행.
man.getup()
man.setWdight(83.5)
print(f'{man.name}의 성별은 {man.getGender()}입니다.')
print('--------------------------')
print('객체 정보')
print(man)