'''OX퀴즈의 결과가 주어졌을 때 점수를 계산하는 프로그램을 작성해보세요.

1) 'O'의 점수는 그 때까지 연속된 O의 개수를 점수로 가집니다 (ex. O → 1점, OOO → 1 + 2 + 3 = 6점)
2) 'X'의 점수는 0점 입니다.'''

while True:
    wrong=0
    result=input("OX퀴즈 결과를 입력하세요: ")
    for char in result:
        if char not in ['O','o','X','x']: wrong+=1
    if wrong==0: break

o_result=result.replace('X','').replace('x','')     #x는 제외한 결과

max_score=sum(i for i in range(1,len(result)+1))    #최대 점수(o,x 개수에 의해 결정)
score=sum(i for i in range(1,len(o_result)+1))      #실제 점수(o 개수에 의해 결정)
print(f'{score}/{max_score}')


'''끝말잇기 게임

1) 두 번째 단어 입력부터는 앞의 단어의 마지막 글자와 동일한 글자로 시작되어야 합니다. 만약 다른 글자로 시작하게 된다면 게임을 종료합니다.
2) 앞에서 입력했던 단어와 동일한 단어를 입력한다면 게임을 종료합니다.'''

print("""\n[끝말잇기] (0: 게임종료)
    ※ 두음법칙 적용되지 않음""")
words=[]    #입력된 단어들 리스트에 저장
count=1

while True:
    word=input(f'{count:2}번째 입력>> ')
    if word=='0': break
    if len(words)>0:       #첫번째 단어는 조건 안 따짐
        if word[0]!=(words[-1])[-1]: print("틀린 단어를 입력하셨습니다. 게임을 종료합니다."); break
        if word in words: print("이미 앞에서 나온 단어를 입력하셨습니다."); break
    words.append(word)     #정상인 단어는 리스트에 추가
    count+=1

print(words)