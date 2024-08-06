

# 다음 리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는
# 프로그램을 만들어 보세요.
li = [1,2,3,4,1,2,3,1,4,1,2,3]
result = {}
for i in li :
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1    
print(result.keys())
print(result)
        
   



# ":".join[1,2,3,4]