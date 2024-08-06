dict_a = {"name": "구름"}
print(dict_a)    

del dict_a["name"]
print(dict_a)

print("--"*40)

numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for i in numbers:
    if i in counter:
        counter[i] = counter[i]+1
    else:
        counter[i]=1

print(counter)

type("문자열") is str #문자열인지 확인
type([]) is list #리스트인지 확인
type({}) is dict #딕셔너리인지 확인

print("--"*40)

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의검",
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
    


