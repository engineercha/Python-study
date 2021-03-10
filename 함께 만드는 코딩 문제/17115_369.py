numbers=[i for i in range(1,100)]
while(True):
    upto=int(input("1~99중 몇까지 369를 할까요?: "))
    if upto>0 and upto<100: break

for i in range(upto):
    ox=numbers[i]//10   #십의 자리
    xo=numbers[i]%10    #일의 자리
    if ox!=0 and xo!=0 and (ox)%3==0 and (xo)%3==0 : numbers[i]='XX'    #십의 자리와 일의 자리가 0이 아니고, 3의 배수인 경우
    elif ox!=0 and (ox)%3==0: numbers[i]='X '                           #십의 자리가 0이 아니고, 3의 배수인 경우
    elif xo!=0 and (xo)%3==0: numbers[i]=' X'                           #일의 자리가 0이 아니고, 3의 배수인 경우
    
    if i%6==0: print()
    print(f'{numbers[i]:2}',end=' ')