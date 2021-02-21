#딕셔너리
'''인덱스 접근이 불가하고, key를 통해 value값을 얻음'''

dic={1:"python", 2:"C", 3:"java"}
ex_dic={"a":"python", "b":"java", "c":"C"}
print(dic[1])
print(ex_dic["a"])

#key 추가
ex_dic["e"]="C++"
print(ex_dic)
ex_dic.update({"b":"javascript","d":"C#"})  #딕셔너리 내 기존 key값이 존재하면 새 value값으로 대체됨
print(ex_dic)

#key 삭제
del ex_dic["e"]
print(ex_dic)

#key 분리
print()
print(ex_dic.keys())
print("before:",ex_dic.values())  #dict_values([]) 형식으로 출력됨
print("after :",list(ex_dic.values()))