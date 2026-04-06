# i , dan = 0,0


# dan  = int(input("단을 입력하세요: "))
# for i in range(9,0,-1):
#     print("%d x %d = %d"%(i,dan,dan*i))



# 중첩 for문


# for i in range(1,3):
#     for k  in range(1,3):
#         print("python (i: %d, k: %d)"%(i,k))



# for i in range(2,10,1):
#     print("## %d단 ##"%(i))
#     for k  in range(1,10,1):
#         print("%d x %d = %d"%(i,k,i*k))
#     print()


i, k, guguLine = 0,0,""

for i in range(2,10):
    guguLine = guguLine + ("# %d단 #" % i)
    
    
    
for i in range(1,10):
    guguLine=""
    for k in range(2,10):
        guguLine= guguLine +str("%2d X%2d = %d"%(k,i,k*i))
        guguLine = guguLine + " |"
    print(guguLine)










