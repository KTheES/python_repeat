#for 문.


# 단순 구구단
# i, dan  = 0,0

# dan = int(input("단을 입력하세요: "))

# for i in range (1, 10, 1) :
#     print("%d x %d = %2d" %(dan, i , dan*i))
    
    
    
# 중첩 for 문 구구단 (가로)
# for i in range(2,10,1):
#     for j in range(1,10,1) :
#         print("%d x %d = %2d" %(i, j , i*j))
#     print("")


# 중첩 for 문 구구단 (세로)

i, dan  = 0,0
dan = int(input("단을 입력하세요: "))

for i in range(1,10,1):
    for j in range(2,dan+1,1) :
        print("%d x %2d = %2d" %(i, j , i*j), end=" ")
    print("")












