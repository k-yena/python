# 1~10까지 합
sum=0   # 초기화 : 방이름 짓고 값 넣어줌
for i in range(1,10+1):
    sum=sum+i
print(sum) 

# 구구단
for i in range(2,9+1):
    for j in range(1,9+1):  
        print("{}*{}={}".format(i,j,i*j),end=" ")
    print()

# 별 찍기
# ***
# **
# *
for i in range(3,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()        


# 홀짝찍기 continue 사용해서
for i in range(1,10+1):
    if i%2 == 0:
        continue
    else:
        print(f"{i}는 홀수")

print("===========")

for i in range(1,10+1):
    if i%2 == 1:
        continue
    else:
        print(f"{i}는 짝수")


        

