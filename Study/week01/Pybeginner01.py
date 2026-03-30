import os

print("Hello World")

a = 50
b = 100
# print(b**a)
# print("%d %d %f" %(100,200,300))
# print("%s%s" %(100,200))
print("%d / %d = %5.1f" %(100,200,0.5))


# format()
print("{0:d} {1:5d} {2:05d}".format(123,123,123))
            # 앞에 있는건 index num, 뒤에 있는게 자릿수 지정
print("{2:d} {1:d} {0:d}".format(100,200,300))  # index num을 계수로 해서 출력.

# 이스케이프 문자
print("\"하이\"")


# 변수선언
    # 어떤 값을 저장하는 메모리 공간.
boolVar = True;
intVar = 300
floatVar = 150.000
strVar = "니똥꼬제련"

a, b, c = "아","자","스"
# 참고로 파이썬에는 char건 str건 걍 다 str취급함...


# print("*********")
# print(" *******")
# print("  *****")
# print("   ***")
# print("    *")
# print("   ***")
# print("  *****")
# print(" *******")
# print("*********")

print(type(boolVar), type(intVar), type(a))


# input()

n = input()

if(n == "O") :
    print("그러세요그럼")
elif(n == "X"):
    print("그러를 그러지마세요")
else:
    print("뭐야?!")

os.system("pause") # import문 필요, os에 직접 pause명령. idle shell에서 쓰는게 나음.
    # 나는 ... vscode상에서 하니까.




# 과제는 self03-01.py형태로.