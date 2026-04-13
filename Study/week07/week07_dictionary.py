# 키-값으로 이루어진 자료구조.

#- dict[key] 에서 없는 k를 호출하면 error,
# - 그러니 dict.get(key) 사용을 권장


#.keys() -> k들 출력
#.values() -> v들 출력 

singer ={}

singer['이름']= '트와이스'
singer['구성원 수']= 9
singer['데뷔']= '서바이벌 식스틴'
singer['대표곡']= 'signal'

for k in singer.keys():
    print("%s --> %s"%(k,singer[k]))