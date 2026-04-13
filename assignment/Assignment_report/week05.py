# 조건문 응용 (1)
# userInput = int(input("정수를 받아 0보다 작으면 음수, 크면 음수가 아님을 출력하는 프로그램입니다. 입력: "))
# if(userInput < 0):
#     print("음수입니다")
# else:
#     print("음수가 아닙니다")

# 조건문 응용 (2)
# game_score = int(input("점수 입력: "))
# if(game_score >=10000) :
#     print("고수입니다")
# else:
#     print("입문자입니다")

# 조건문 응용 (3)
# print("값이 같은지 다른지를 판별하는 프로그램입니다")
# userInput1 = int(input("정수 1번 입력: "))
# userInput2 = int(input("정수 2번 입력: "))
# if(userInput1 == userInput2) :
#     print("두 값이 일치합니다")
# else:
#     print("두 값이 일치하지 않습니다")


# 조건문 응용 (4)
# userInput = int(input("연도를 입력하시오: "))
# if(userInput % 400 == 0):
#     print("%d 년은 윤년입니다"%userInput)
# elif(userInput % 4 == 0):
#     if(userInput % 100 == 0):
#         print("%d 년은 윤년이 아닙니다."%userInput)
#     else:
#         print("%d 년은 윤년입니다"%userInput)

# import random

# # 조건문 응용 (5)

# player1 = input("player1의 이름: ")
# player2 = input("player2의 이름: ")
# print("......주사위를 굴립니다......")
# resultP1 = random.randint(1,6)
# resultP2 = random.randint(1,6)
# print("%s의 주사위 번호는 %d"%(player1,resultP1))
# print("%s의 주사위 번호는 %d"%(player2,resultP2))
# if(resultP1>resultP2):
#     print("%s이 이겼습니다."%player1)
# elif(resultP2>resultP1):
#     print("%s이 이겼습니다."%player2)
# else:
#     print("비겼습니다.")


# 반복문 응용 (6)
# for i in range(0,5) :
#     print("####################")


# 반복문 응용 (7)
# i = 1
# dan = int(input("원하는 단은: "))
# while( i < dan ):
#     i += 1
#     print("%d*%d=%d" % (dan,i,dan*i))


# 반복문 응용 (8)
# import random

# correct = random.randint(1,100)
# attempt = 0
# print("1부터 100 사이의 숫자를 맞추시오")
# while(True):
#     num = int(input("숫자를 입력하시오: "))
#     attempt += 1
#     if(num == correct):
#         break
#     elif(num < correct):
#         print("높음!")
#     else:
#         print("낮음!")
# print("축하합니다. 총 시도횟수:%d"%attempt)


# # 반복문 응용 (9)
# import random

# while(True):
#     num1, num2 = random.randint(1,100), random.randint(1,100)
#     answer = int(input("%d + %d = "%(num1,num2)))
#     if(answer == ( num1+num2 )):
#         print("잘했어요!")
#     else:
#         print("정답은 %d 입니다. 다음 번에는 잘 할수 있죠?"%(num1+num2))

# 반복문 응용 (10)

inp = input("단어를 입력하세요: ")

for i in range(0,len(inp)):
    if(inp[i] == 'a' or inp[i] == 'i' or inp[i] =='e' or inp[i] =='o' or inp[i] =='u'):
        print(inp[0:i])
        break
    