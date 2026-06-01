# class  Car :
#     color = ""
#     speed = 0

#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed

#     def  getName(self) :
#         return self.name
    
#     def  getSpeed(self) :
#         return self.speed




class  Car :
    color = ""
    speed = 0
    count = 0
    year = 0
    company = ""

    def __init__(self):
        self.speed = 0
        Car.count += 1
        Car.company= "현대"
        
myCar1, myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30
print("자동차 1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대입니다."%(myCar1.speed, myCar1.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차 2의 현재 속도는 %dkm, 생산된 자동차는 총 %d대입니다."%(myCar2.speed, myCar2.count))

myCar3 = Car()
myCar3.speed= 10
myCar3.year= 2024
print("자동차 3의 생산연도는 %d년이며, 회사명은 %s입니다."%(myCar3.year,myCar3.company))




