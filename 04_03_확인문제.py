# [4,5]


# [7,6,5,4,3,2,1]


# range(3,9+1,3)


'''

# 빈칸을 채워 키와 값으로 이루어진 각 리스트를 조합해
# 하나의 딕셔너리를 만들어 보세요.
key_list = ["name","hp","mp","level"]
value_list = ["기사", 200,30,5]
character = {}

for i in range(4):     # for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]


print(character)

'''



'''

# 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다.
# 몇을 더할 때 10000을 넘는지 구해 보세요.
# 그리고 그 때의 값도 출력해 보세요. 다음은 10000이 넘는 경우를 구한 예입니다.


limit = 10000
i = 1

sum_value = 0
while sum_value <= limit :    # 몇 번까지 돌리는지 모르는 경우 while
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i,limit,sum_value))


'''








# 1부터 100까지의 숫자가 있다고 합시다. 이를 다음과 같이 계산한다고 했을 때,
# 최대가 되는 경우는 어떤 숫자를 곱했을 때인지를 찾아 주세요.
max_value = 0
a = 0
b = 0

for i in range(1,99+1):     # for i in range(1, 100//2+1):
    j=100-i
    if max_value < i * j:    # i*j의 값이 max_value 보다 크면 참이 되어 
        max_value = i * j       # i*j 의 값을 max_value 에 받음
        a, b = i, j  # 튜플 

print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))    

