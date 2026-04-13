## 오늘은 튜플, 리스트에 관해 배웁니다. 
    # list : 서로 자료형이 다른 원소들을 하나의 집합에 넣을 수 있음


# 이번 시험에는 for - while을 서로 바꾸는 것이 나옵니다.


# aa = []
# i = 0
# while(i<10):
#     aa.append(0)
#     i+=1

# i = 0
# hap = 0

# while(i<10):
#     aa[i] = int(input(str(i+1)+"번째 숫자 : "))
#     i+=1

# i = 0
# 축약시 while문 하나 생략 가능
# while(i<10):
#     hap = hap + aa[i]
#     i+=1

# print("합계 ===> %d"%hap)


# aa = []
# hap, i = 0,0
# while(i<10):
#     aa.append(0)
#     i+=1

# for i in range(0,4,2):
#     aa[i] = int(input(str(i+1)+"번째 숫자 : "))
#     hap += aa[i]

# for i in range(3,-1,-1):
#     aa[i] = int(input(str(i+1)+"번째 숫자 : "))
#     hap += aa[i]

# print("합계 ===> %d"%hap)


## list index slicing


aa =[1,2,3,4,5,6,7,8,9]

print(aa[2::])
print(aa[2:])

print(aa[0:])
print(aa[:-1])
print(aa[::-1])

aa[4:5] = [100,200]
print(aa[1:])
print(aa[:-1])
















