# 경우의 수  1,2,3,~,10

'''
< 기본적으로 다른 언어에서 사용하는 방법 >
num = 10


if num >= 1 and num < 4 :
    print("A")
elif num >= 4 and num < 7:
    print("B")   
else:
    print("C")     

'''

'''
# < 파이썬에서 편리하게 사용하는 방법 >
num = 7


if 1 <= num < 4 :
    print("A")
elif 4 <= num < 7:
    print("B")   
else:
    print("C")  
    
'''

'''
# datetime의 라이브러리에 접근하여 
# 봄,여름,가을,겨울 중 현재 달의 계절을 찍어내세요.
import datetime
now=datetime.datetime.now()

if 3 <= now.month < 6 :
    print("봄")
elif 6 <= now.month < 9 :
    print("여름")
elif 9 <= now.month < 12 :
    print("가을")
else:
    print("겨울")            

'''


mon = int(input("현재 몇 월:"))

if mon >= 3 and mon < 6 :
    print("봄")
elif  6 <= mon and mon < 9:
    print("여름")
elif  9 <= mon and mon < 12:
    print("가을")
else:
    print("겨울")         

