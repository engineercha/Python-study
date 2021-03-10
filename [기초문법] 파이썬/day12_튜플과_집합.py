#튜플
'''리스트와 달리 ()로 둘러싸이고, 값의 추가/삭제/수정이 불가능함.
대신, 튜플의 추가/반복이 가능하고 함수의 리턴값을 한꺼번에 여러 개 받을 수 있음'''
ex1_tuple=(1,9)
ex2_tuple=("today",2,22)
ex3_tuple=(1,2,3)
ex4_tuple=(11,12,13,14)

#튜플 추가/반복(=+, *)
print()
print(ex3_tuple + ex4_tuple)    
print(ex3_tuple*2)

#반환값
print()
def getminmax(x_lst):
    return min(x_lst), max(x_lst)

x_lst=(5,3,9,8,17,-1)
print(getminmax(x_lst))


#집합
'''집합은 {}나 ([])로 둘러싸이고, 순서가 없고 중복된 값을 허락하지 않음,
따라서 인덱스를 통한 접근이 불가능함.'''
set1={1,2,3}
set2={3,4,5}
set3=set([4,2,5,3,1])
set4=set("hello world")

print()
print(type(set1))
print(set1, set2)
print(set3, set4, end='\n\n')

#교집합
print(set1&set2, set1.intersection(set2), sep=' = ')

#합집합
print(set1|set2,"=",set1.union(set2))

#차집합
print(set1-set2,"=",set1.difference(set2))

#집합에 값 추가(=add(), update())
print("\nbefore:",set1,set2)
set1.add(4)
set2.update([10,9,8])       #여러 값을 추가할 때
print("after:",set1,set2)

#집합의 값 제거(=remove())
print("\nbefore:",set1)
set1.remove(4)
print("after:",set1)