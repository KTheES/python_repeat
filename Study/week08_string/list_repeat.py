singer= {'이름' : '트와이스','구성원 수': '9', '데뷔':'서바이벌 식스틴', '대표곡':"signal"}

print(singer)
print()
print(list(singer.keys()))   # key
print()
print(list(singer.values()))# value
print()


for i in singer.keys():   #모든 요소 K-V 출력함.
    print("%s --> %s, " %(i,singer[i]))
print()

for k,v in singer.items():   #모든 요소 K-V 출력함.
    print("%s --> %s, " %(k,v)) # items -> k-v 둘 다 처리합니다. 
    # k-v 변수로 받아서 사용 가능함.index 번호 쓸 필요 없음. 