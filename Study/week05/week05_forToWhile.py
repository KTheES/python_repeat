# i, dan  = 0,0
# dan = int(input("단을 입력하세요: "))

# for i in range(1,10,1):
#     for j in range(2,dan+1,1) :
#         print("%d x %2d = %2d" %(i, j , i*j), end=" ")
#     print("")
### for를 while로 치환
    
# i = 1
# while(i < 10):
#     j=2     # local으로 선언해야 합니다.
#     while(j < 10):
#         print("%d x %d = %2d "%(i,j,i*j), end="")
#         j += 1
#     print()
#     i += 1


# hap, i = 0,1

# while(i<101):
#     hap +=i
#     if(hap>=1000):
#         break
#     i= i+1
# print("1~100의 합계를 최초로 넘게 하는 숫자: %d" % i )


hap, i = 0,0

for i in range(1,101):
    hap+=i
    if(i%3 ==0):
        continue
    print("i: %d, hap: %d  " %(i, hap) )
    
# while
hap, i = 0,1
while(i<101):
    hap +=i
    i= i+1
    if(i%3 == 0):
        continue


print("1~100의 합계(3의 배수 제외): %d" % hap )


# u2065 = 별, 2665= 하트