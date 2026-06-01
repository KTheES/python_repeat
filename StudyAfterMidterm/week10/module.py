# 모듈 : 함수의 집합

# 그냥 다른 파일에 있는 함수 가져와 쓸 수 있게 하는 용도
# import myModule

# hap, sub = 0,0
# hap, sub = myModule.multi(100,200)

# print("합:",hap,"차:",sub)

from myModule import multi

hap, sub = 0,0
hap, sub = multi(100,200)

print("합:",hap,"차:",sub)
# multi()




from myModule import *





# 모듈의 종류
# ▪ 표준 모듈, 사용자 정의 모듈, 서드 파티 모듈로 구분
# ▪ 표준 모듈 : 파이썬에서 제공하는 모듈
# ▪ 사용자 정의 모듈 : 직접 만들어서 사용하는 모듈
# ▪ 서드 파티(3rd Party) 모듈 : 파이썬이 아닌 외부 회사나 단체에서 제공하는 모듈
    # - 이 경우 pip install으로.


# 패키지 ( 모듈 (함수))
# 패키지 안에 모듈, 모듈 안에 함수.
# 큰 그룹부터 import해주면 됩니다


# 내부 함수
    # 함수 안에 함수
    # 내부함수는 포함하는 함수 안에서만 호출 가능
    
    
#람다식...

# 기존 함수
def hap(num1,num2):
    res = num1+num2
    return res
print(hap(10,20))

# 람다 - 간단한 일에만 사용 가능합니다.
hap2 =lambda num1,num2 :num1+num2
print(hap2(10,20))


