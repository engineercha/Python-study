while(True):
    n=int(input("정수를 입력하세요(종료:0): "))
    if n==0: break

    divisors=[] #약수를 담음.
    sum=0       #자신을 제외한 약수의 합을 담음.

    for i in range(1,n):    #divisors[]에 n은 포함되지 않도록 함.
        if n%i==0: divisors.append(i)

    for i in range(len(divisors)):
        sum+=divisors[i]

    if sum==n: print("완전수입니다.\n")
    else: print("완전수가 아닙니다.\n")
