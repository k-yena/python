'''
False
True
False
True
True
False

3번

1. 치킨 or 햄버거 --> o (?)
2. h브랜드 and 10만원 이하 --> a
3. 65 < a or 5>b --> o

'''


a = int(input("> 1번쨰 숫자: "))
b = int(input("> 2번째 숫자: "))
print()

if a > b :
    print("처음 입력했던 {}가 {}보다 더 큽니다".format(a,b))
if a < b :
     print("두 번째로 입력했던 {}가 {}보다 더 큽니다".format(b,a))    