#리스트
year_lst=[2,0,2,1]

for i in range(len(year_lst)):
    print(year_lst[i],end='')
print(" = ",end='')
for i in year_lst:
    print(i,end='')

#리스트에 값 삽입(=append(), insert())
print()
year_lst.append(2)      #맨 뒤에 2를 삽입
print(year_lst)
year_lst.insert(4,0)    #4번째 인덱스에 0을 삽입
print(year_lst)

#리스트의 값 제거(=del, remove())
print()
del year_lst[1]         #1번째 인덱스를 제거
print(year_lst)
year_lst.remove(2)      #첫번째 2를 제거
print(year_lst)