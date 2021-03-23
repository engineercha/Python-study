#string = 0
result=[]   #문자열을 저장하는 변수로, int 타입이 아니라 리스트로 선언함

while True:
    string = input()
    if string == "-": continue
    if string == ";": break
    num = int(input())
    for i in range(num): result.append(string)  #string을 result에 추가하는 것을 num번 반복하라
                                                #즉, num개의 string이 result에 저장됨

print("Result =",end='')
for i in result: print(i, end='')   #result에 있는 모든 요소 i를 반복해 출력함

print("\n참고로 result는",result,"이렇게 생김")