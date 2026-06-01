# 함수와 모듈
# 함수의 집합 - 모듈
# 모듈 관리 - 패키지

# 함수(Function) : ‘무엇’을 넣으면, ‘어떤 것’을 돌려주는 요술 상자
# 메서드(Method)와 차이점 : 함수는 외부에 별도로 존재, 메서드는 클래스 안에 존재

# 매개변수가 있는 함수(ReqArgFunction) / 매개변수 없는 함수(void처럼..) 있습니다.

# Code
# coffee = 0

# def coffee_machine(button) :
#     print()
#     print("#1. (자동으로) 뜨거운 물을 준비한다.")
#     print("#2. (자동으로) 종이컵을 준비한다.")

#     if button == 1 :
#         print("#3. (자동으로) 보통커피를 탄다.")
#     elif button == 2 :
#         print("#3. (자동으로) 설탕커피를 탄다.")
#     elif button == 3 :
#         print("#3. (자동으로) 블랙커피를 탄다.")
#     else :
#         print("#3. (자동으로) 아무거나 탄다.\n")

#     print("#4. (자동으로) 물을 붓는다.")
#     print("#5. (자동으로) 스푼으로 젓는다.")
#     print()

# ## 메인 코드 부분 ##
# coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙) "))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.")

# coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙) "))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.");




# Plus Func

def plus(v1,v2):
    result = 0
    result = v1+v2
    print(result)
    return result #반환값 없으면 None뜹니다(당연...)
hap = 0

hap = plus(100,200)
print("100과 200의 plus() 함수 결과는 %d"%hap)
plus(10,20)


# 지역 변수 : 한정된 지역에서만 사용  - 함수 내부 등...
# 전역 변수 : 프로그램 전체에서 사용 - global (main 내-외부)















