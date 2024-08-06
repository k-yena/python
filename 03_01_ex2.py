'''
# 학점을 나타내는 프로그램

score = int(input("(0점에서 100점 사이로만)점수 입력하세요."))

if 90 <= score and score <= 100 :
    print("A학점")
elif 80 <= score and score < 90 :
    print("B학점")
elif 70 <= score and score < 80 :
    print("C학점") 
elif 0 <= score and score < 70 :
    print("F학점") 
else:
    print("0점에서 100점 사이 점수로만 넣으세요")    
'''    
    
'''
# 중첩문
# if x>10:
#     if x<20:
if x>10 and if x<20 :
    print("조건에 맞습니다")

'''
'''
import datetime
now=datetime.datetime.now()

a = input("입력:")
a = a.strip()

if '안녕' in a :
    print("> 안녕하세요")
elif '몇 시' in a :  
    print("> 지금은 {}시입니다.".format(now.hour))

'''

# num = int(input("정수를 입력해주세요:"))

# if num%2 == 0 :
#     print("짝수입니다.")    
# elif num%3 == 0 :
#     print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(num))
#     print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(num))
# elif num%4 == 0:
#     print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(num))
#     print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(num))
# elif num%5 == 0:
#     print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(num))
#     print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(num))   
# else:
#     print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(num))
#     print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(num))
#     print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(num))    


num = int(input("정수를 입력해주세요:"))

if num%2 == 0 :
    print("{}은 2로 나누어 떨어지는 숫자입니다.".format(num))
else:
    print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(num))    
if num%3 == 0 :
    print("{}은 3로 나누어 떨어지는 숫자입니다.".format(num))
else:
    print("{}은 3로 나누어 떨어지는 숫자가 아닙니다.".format(num))
if num%4 == 0 :
    print("{}은 4로 나누어 떨어지는 숫자입니다.".format(num))
else:
    print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(num))
if num%5 == 0 :
    print("{}은 5로 나누어 떨어지는 숫자입니다.".format(num))
else:
    print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(num))            