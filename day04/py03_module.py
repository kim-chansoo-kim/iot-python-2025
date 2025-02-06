# 모듈 - 레고
# 모듈을 사용하려면
# import 모듈명
# from 모듈명 import 상세...
import py02_car
hisCar = py02_car.Car('기아', '쏘렌토', '26차2623')
print(hisCar)


import py02_car as c
herCar = c.Car('포르쉐', 'GT911', '251우1513')
print(herCar)

from py02_car import Car

thatCar = Car('람보르기니', '아벤타도르', '164하5125')