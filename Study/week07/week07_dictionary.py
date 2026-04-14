# 키-값으로 이루어진 자료구조.

#- dict[key] 에서 없는 k를 호출하면 error,
# - 그러니 dict.get(key) 사용을 권장


#.keys() -> k들 출력
#.values() -> v들 출력 

# singer ={}

# singer['이름']= '트와이스'
# singer['구성원 수']= 9
# singer['데뷔']= '서바이벌 식스틴'
# singer['대표곡']= 'signal'

# for k in singer.keys():
#     print("%s --> %s"%(k,singer[k]))
# print()

# for v in singer.values():
#     print(singer)
# print()

# for i in singer.items():
#     print(singer)

# 이거 val / item다른점은  시험에 안나옵니다

# 딕셔너리도 정렬 가능합니다 ->operator 모듈 import 필요함 ()
# import operator

# tL = sorted(trainDic.items(),key = operator.itemgetter(0))



# 리스트 컴프리헨션

numList = [num for num in range(1,21) if(num%3==0)]
print(numList)

