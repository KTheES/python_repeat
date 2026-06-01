# 파일입출력 - 인코딩주의...
# inFp = None        # 입력 파일
# inStr = ""         # 읽어 온 문자열

# # inFp = open("StudyAfterMidterm\week11\data1.txt", "r")
# inFp = open("StudyAfterMidterm\week11\data2.txt", "w")

# inStr = inFp.writelines("hello\n")
# print(inStr, end = "")

# inStr = inFp.writelines("world\n")
# print(inStr, end = "")

# inStr = inFp.writelines("everyone\n")
# print(inStr, end = "")

# inFp.close()


# ##
# inFp =None
# inStr= ""

# infp = open("StudyAfterMidterm\week11\data1.txt", "r")

# while True:
#     inStr = inFp.readline()
#     if inStr =="":
#         break
#     print(inStr,end="")
    
# inFp.close() 


## code 11-6

# import os

# inFp = None
# fName, inList, inStr = "",[],""

# fName = input("파일명을 입력하세요: ")

# if os.path.exists(fName):
#     inFp = open(fName,"r")
    
#     inList= inFp.readlines()
#     for inStr in inList:
#         print(inStr,end="")
        
#     inFp.close()
    
# else:
#     print("%s파일이 없습니다"% fName)




## 

outFp = None
outStr = ""

outFp = open("C:/Temp/data2.txt",'w')

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr+"\n")
    else:
        break
    
outFp.close()
print("----정상적으로 파일에 씀----")


###
inFp, outFp = None,None
inStr = ""

inFp = open("C:/Windows/win.ini",'r')
outFp = open("C:/Temp/data3.txt","w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)
    

inFp.close() 
outFp.close() 
print("----정상적으로 파일에 복사됨----")






