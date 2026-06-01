# def plus(v1,v2):
#     result = 0
#     result = v1+v2
#     return result

# def min(v1,v2):
#     result = 0
#     result = v1-v2
#     return result

# def mul(v1,v2):
#     result = 0
#     result = v1*v2
#     return result

# def avg(v1,v2):
#     result = 0
#     result = v1/v2
#     return result

# hap = 0

# hap = plus(100,200)
# print("100과 200의 plus() 함수 결과는 %d"%hap)
# hap = min(100,200)
# print("100과 200의 min() 함수 결과는 %d"%hap)
# hap = mul(100,200)
# print("100과 200의 mul() 함수 결과는 %d"%hap)
# hap = avg(100,200)
# print("100과 200의 avg() 함수 결과는 %d"%hap)







def calc(op,v1,v2):
    result = 0
    if op == "+": result = v1+v2
    elif op =="-": result = v1-v2
    elif op =="*": result = v1*v2
    else: result = v1/v2
    return result


num1  = int(input("숫자 1 입력: "))
num2  = int(input("숫자 2 입력: "))
operator = input("연산자 입력: ")

res = 0
res = calc(operator,num1,num2)
print("%d %s %d 의 결과는 %d 입니다."%(num1,operator,num2,res))







