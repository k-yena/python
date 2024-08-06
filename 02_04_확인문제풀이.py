''' 
3,4

'''

'''
split() - d
upper() - b
lower() - a
strip() - c
'''

'''
100,200,300

'''

'''
string = "hello"

# print(id(string))

# string=string.upper()

# print(id(string))

string.upper()
print("A지점 :", string) #A지점:hello

print("B지점:", string.upper()) #B지점:HELLO

'''

'''
# 구의 부피와 겉넓이를 구하는 프로그램을 만들어 보세요.
# import math           math함수에서 import
r=float(input("구의 반지름을 입력해주세요:"))
pi = 3.141592
v= 4/3*pi*r**3
w=4*pi*r**2
# v= 4/3*math.pi*r**3       (math함수 이용한 방법)
# w=4*math.pi*r**2          (math함수 이용한 방법)
print("구의 부피는:",v,"입니다")
print("구의 겉넓이는:",w,"입니다")
'''



# 피타고라스의 정리
import math
print(math.sqrt(4)) #루트를 벗은 형태

a=float(input("밑변의 길이를 입력해주세요:"))
b=float(input("높이의 길이를 입력해주세요:"))
c= (a**2+b**2)**0.5
print("=빗변의 길이는",c,"입니다.")
print("=빗변의 길이는 {}".format(math.sqrt(a**2+b**2)),"입니다.")
