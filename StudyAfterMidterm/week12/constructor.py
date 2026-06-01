class  Car :
    color = ""
    speed = 0
    
    def __init__(self):   # noargsConstructor - java와 약간 달라보입니다 (기본 생성자가 아니나 this를 사용하듯.)
        self.color = "빨강"
        self.speed = 0
        
    def __init__(self,value1): # ReqArgsConstructor
        self.color = value1
    
    def __init__(self,value1,value2): # AllArgsConstructor
        self.color = value1
        self.speed = value2

    def  upSpeed(self, value) :
        self.speed += value
        if self.speed >= 150 : self.speed = 150

    
    def  downSpeed(self, value) :
        self.speed -= value
        
    def printMessage(self) :  # arg가 없을 시 self 붙여야 합니다.
        print("시험 출력!")


yourCar1 = Car("빨강",50)
yourCar2 = Car("파랑",1000)

yourCar1.printMessage()



print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(yourCar1.color, yourCar1.speed))
print("자동차 2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(yourCar2.color, yourCar2.speed))
print()

yourCar1.upSpeed(100)
print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(yourCar1.color, yourCar1.speed))


# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0

# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 100

# myCar3 = Car()
# myCar3.color = "초록"
# myCar3.speed = 20

# myCar1.upSpeed(30)
# myCar2.upSpeed(30)
# myCar3.upSpeed(30)
# print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar1.color, myCar1.speed))
# print("자동차 2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar2.color, myCar2.speed))
# print("자동차 3의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar3.color, myCar3.speed))


