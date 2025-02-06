# 객체지향 다시

class Car:
    ## 생성자(__new__ 사용빈도가 낮음, __init__대부분 사용)
    ## Car() 호출하면 아래의 메서드가 실행
    # company, name, palateNumber 모를때는 None(뭔지 몰라)
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company # 멤버변수 이름앞에 __두번쓰면 외부 접근불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

    # 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제차는 {self.__name}이고, 차번호는 {self.__plateNumber}입니다.'
    # 외부에서 잘못된 차번호를 넣으면 안들어감
    def setPlateNmber(self, newPlateNmber):
        if type(newPlateNmber) is str:
            self.__plateNumber = newPlateNmber

    def setname(self, newName='글쎄요'): # 이름을 모를때 글쎄요로 대체.
            self.__name = newName
    def getName(self):
         return self.__name

# 모듈화 하려면 예제 소스는 없어야 한다
# myCar = Car('현대자동차', '싼타페', '24누2451')
# 파라미터명 = 값 으로 매개변수 순서를 변경가능
# myCar = Car(name ='싼타페',  plateNumber = '24누2451', company = '현대자동차')
# print(myCar) # 차의 번호를 출력하고 싶음
# myCar.__plateNumber = '12누1295' # 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생하지 않음
# print(myCar)
# myCar.setPlateNmber('24누2456')
# print(myCar)

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNmber('23오1512')
# print(yourCar)
# yourCar.setname('소나타')
# print(yourCar)