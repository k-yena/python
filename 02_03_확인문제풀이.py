# 02-03
'''
=

+=
-=
*=
/=
%=
**=

int
float
str


'''
# 변수 초기화(선언(변수명 짓기(특수공예 원칙!!)), 값 할당)
str_input = input("원의 반지름 입력> ")
num_input = float(str_input)
# print(str_input)
# print(type(str_input))
print()
print("반지름:",num_input)
print("둘레:",2*3.14*num_input)
print("넓이:",3.14*num_input**2)
