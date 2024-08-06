'''

dict_a={"name":"구름"}
print(dict_a)

'''

'''

dict_a={"name":"구름"}
del dict_a["name"]      # dict_a.clear()
print(dict_a)

'''


'''

# # 빈칸을 채워서 numbers 내부에 들어있는 숫자가
# # 몇 번 등장하는지를 출력하는 코드를 작성해보세요

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for i in numbers:
    if i in counter:
        counter[i] = counter[i]+1
    else:
        counter[i]=1

print(counter)

'''
    

'''
# 아래 예시를 참조해 다음 빈칸을 채워 실행결과와 같이 출력되게 만들어 보세요.
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "swprd": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key, value in character.items():
    if type(value) == dict: #딕셔너리 일때 
        for s_key, s_value in value.items():
            print(f"{s_key}:{s_value}")
    elif type(value) == list: #리스트 일때 
        for item in value:
            print(f"{key}:{item}")
    else:
        print(f"{key}:{value}")

print("--"*40)

'''


'''
for i in range(3):
    for j in [1,2,3]:
        print("*",end=' ')
    print()


# 구구단 만들기 
for i in range(2,9+1):
    for j in range(1,9+1):
        print("%d*%d=%2d" %(i,j,i*j), end=' ')
    print()

'''    
'''

# 아래의 별모양 출력
# *
# **
# ***
# ****
# *****

# for을 한번만 사용하는 방법
# for i in range(1,5+1):
#     print("*"*i)  


# for문을 여러번 사용    
# for i in range(1,5+1):
#     for j in range(i):
#         print("*",end=' ')
#     print() 

'''




'''

# 트리모양 만들기
str1=''
for i in range(0,7):
    for j in range(6,i,-1):
        str1 +=' '
    for k in range(0,2*i-1):
        str1 +='*'        
    str1 +='\n'

for i in range(2):
    for i in range(4):
        str1 +=' '
    for k in range(3):
          str1 +='*'        
    str1 +='\n'  

print(str1)     

'''  


'''

#홀짝프로그램 만들기
n=1
while n<=10 :
    n = n+1
    if n%2 == 0:
        print("짝수")
    else: 
        print("홀수")


'''



'''

# 예약어 break
for i in range(1,10):
    if i == 5:
        break # 중단해라
    print(i)
    
'''    



# 예약어 continue
for i in range(1,10):
    if i == 5:
        continue # 건너뛰어라(5인 부분 실행x) 
    print(i)

       
