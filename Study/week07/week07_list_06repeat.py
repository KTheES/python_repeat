myList = [30,10,20]
print("현재 리스트: %s" %myList)

# 1) mylist에 값 3개 40,41,42 추가하시오(반복문 사용)
add = 40
for i in range(2,5):
    myList.append(add)
    add +=1

print("append 후의 리스트: %s "%myList)

# 2) 리스트에서 마지막 값을 제거하시오
myList.pop()
print("pop()후의 리스트: %s" %myList)


# 3) 리스트의 전체 크기 출력하시오
print("리스트의 전체 크기: %s" %len(myList))
# 4) 리스트의 인덱스 2를 1000으로 변경하시오

myList[2] = 1000
print("인덱스 2를 1000으로 바꾼 후의 리스트: %s" %myList)

# 5) 리스트 내용 모두 삭제하세요

myList.clear()
print("clear() 후의 리스트: %s" %myList)

# myList.sort()
# print("sort() 후의 리스트: %s" %myList)

# myList.reverse()
# print("reverse() 후의 리스트: %s "%myList)

# # print("20값의 위치: %d"% myList.index(20))

# myList.insert(2,222)
# print("insert(2,222) 후의 리스트: %s" %myList)

# myList.remove(222)
# print("remove(222) 후의 리스트: %s" %myList)

# myList.extend([77,88,99])
# print("extend([77,88,99] 후의 리스트: %s" %myList)

# print("77값의 개수: %d" %myList.count(77))





