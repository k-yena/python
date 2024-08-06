'''
# 1~100 사이에 있는 숫자 중 2진수로 변환했을 때 
# 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드를 만들어보세요.
output = [i for i in range(1,100+1) if "{:b}".format(i).count('0')==1]

for i in range(1,100+1) :
        print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))    

'''


'''
# 다음리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는 프로그램을 만들어보세요.
# 1,2,3,4가 사용되었으므로 4개가 사용되었다고 출력하면 됩니다.
# [1,2,3,4,1,2,3,1,4,1,2,3]

li = [1,2,3,4,1,2,3,1,4,1,2,3]
result = {}
for i in li :
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1    
print(result.keys())
print(result)

'''

'''

# 염기 서열을 입력했을 때 
# 각각의 염기가 몇 개 포함되어 있는지 세는 프로그램을 구현해 보세요

li= input()
result = {}
for i in li:
    if i in result.keys():
        result[i] += 1
print(f"a의 개수: {li.count('a')}")
print(f"t의 개수: {li.count('t')}")
print(f"g의 개수: {li.count('g')}")
print(f"c의 개수: {li.count('c')}")

'''        

# 염기 코돈 개수




# 리스트 평탄화
li = [1,2,[3,4],5,[6,7],[8,9]]
li_new=[]

for i in li:
    if type(i) is list:
        for j in i:
            li_new.append(j)
    else:
        li_new.append(i)         
print(li_new)