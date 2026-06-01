# 지역 변수 : 한정된 지역에서만 사용  - 함수 내부 등...
# 전역 변수 : 프로그램 전체에서 사용 - global (main 내-외부)



## 함수 선언 부분 ##
# def func1() :
#     a = 10     # 지역 변수
#     print("func1()에서 a값 %d" % a)
# def func1() :
#     global a     # 전역 변수
#     a = 10
#     print("func1()에서 a값 %d" % a)

# def func2() :
#     print("func2()에서 a값 %d" % a)

# ## 전역 변수 선언 
# a = 20

# ## 메인 코드
# func1()
# func2()


def multi(v1, v2):

    hap = v1+v2
    sub = v1-v2
    return hap,sub

hap,sub = 0,0

hap,sub =multi(100,200)


print("합:",hap,"차:",sub)

















