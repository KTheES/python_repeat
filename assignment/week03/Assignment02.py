
# 중첩 if문
score= int(input("점수를 입력하세요 : "))

if (score >= 95):
    print("A+")
else:
    if (score >= 90):
        print("A")
    else:
        if(score >= 80):
            print("B")
        else:
            if(score >= 70):
                print("C")
            else:
                if(score >= 60):
                    print("D")
                else:
                    print("F")
    
print("학점입니다.")




# result 변수를 적용한 케이스 - 자세한 중첩 if문.

score= int(input("점수를 입력하세요 : "))
result = ''
if (score >= 95):
    result = "A+"
else:
    if (score >= 90):
        result = "A0"
    else:
        if(score >= 85):
            result = "B+"
        else:
            if(score >= 80):
                result = "B"
            else:
                if(score >= 75):
                    result = "C+"
                else:
                    if(score>=70) :
                        result = "C"
                    else:
                        if(score>=65) :
                            result = "D+"
                        else:
                            if(score>60) :
                                result = "D"
                            else:
                                result = "F"
    
print(result,"학점입니다.")


# elif
score= int(input("점수를 입력하세요 : "))

result = ''
if (score >= 95):
    result = "A+"
elif (score >= 90):
    result = "A0"
elif(score >= 85):
    result = "B+"
elif(score >= 80):
    result = "B"
elif(score >= 75):
    result = "C+"
elif(score >= 70) :
    result = "C"
elif(score >= 65) :
    result = "D+"
elif(score > 60) :
    result = "D"
else:
    result = "F"
    
print(result,"학점입니다.")

