'''
list_a = [0,1,2,3,4,5,6,7]
list_a.extend(list_a)  # [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7] 
list_a.append(10)  # [0,1,2,3,4,5,6,7,10]
list_a.insert(3,0) # [0,1,2,0,3,4,5,6,7]
list_a.remove(3) # [0,1,2,4,5,6,7]
list_a.pop(3) # [0,1,2,4,6,5,7]
list_a.clear() # [ ]

'''



'''
# 다음 반복문 내부에 if 조건문의 조건식을 채워서 100이상의 숫자만 출력하게 만들어보세요.
numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number >= 100:
        print("-100이상의 수:",number)

'''



'''
# # 1부터 10까지 중 홀수

# for i in range(1,10+1) :   
#     if i % 2 == 1 :
#         print(i)
'''



'''
# 1부터 10까지 중 3의 배수
for i in range(1,10+1):
    if i %3 ==0:
        print(i)

'''



'''
# 1부터 10까지 중 3의 배수의 누적합
tot=0
for i in range(1,10+1):
    if i % 3 == 0:
        tot += i
print(tot)        

'''



'''
#빈칸을 채워서 실행 결과에 해당하는 프로그램들을 완성하세요.
numbers = [273,103,5,32,65,9,72,800,99]

        
for i in numbers: 
    if i % 2 == 0:
        print("{}는 짝수입니다.".format(i))
    else:        
        print("{}는 홀수입니다.".format(i))



for i in numbers:
    # print("{}는 {} 자릿수입니다".format(i,len(str(i))))
    print(f"{i}는 {len(str(i))} 자릿수입니다")


'''





'''
# < 따로 다시 해보기!!! >
# 다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 보세요
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]    # 초기화 단계

for number in numbers:
    output[(number+2)%3].append(number)  # output[index를 찾아라 index 0,1,2 가 나오도록]

print(output)    

'''


# 다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 보세요.
# 짝수번째 요소를 제곱하는 것입니다.

numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0,len(numbers)//2):  # 0~3+1
    # j가 1,3,5,7이 나오려면 
    # 어떤 식을 사용해야 할까요?
    j = 2*i+1
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2

print(numbers)    


'''
# 1부터 10까지 더하는 프로그램
tot=0
for i in range(1,10+1):
    tot += i 
print(tot)

'''