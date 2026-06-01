class  Car :
    color = ""
    speed = 0

    def  upSpeed(self, value) :
        self.speed += value
        if self.speed >= 150 : self.speed = 150

    
    def  downSpeed(self, value) :
        self.speed -= value
