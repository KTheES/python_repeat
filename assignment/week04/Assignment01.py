# list와 같이 사용하는 condition - index 개념


# fruit = []
# .append() 를 이용합니다. ( add 시)

import random


numbers = []

for num in range(0,10) :
    numbers.append(random.randrange(0,10))
    
print("생성된 리스트",numbers)

# for num in range(0, 10):