i , hap =0,0

i = 1
while i <11:
    hap += i
    i = i+1
    
print("1에서 10까지의 합계 : %d" % hap)


while True:   # 무한반복.
    print("ㅋ", end = " ")

hap = 0
a,b = 0,0

while True:
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
    if a == 0:
        break
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a+b
    print("%d + %d = %d"%(a,b,hap))
    
print("0을 입력해 반복문을 탈출했습니다")