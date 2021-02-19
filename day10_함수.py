def getsum(x):
    sum=0
    for i in range(x+1):
        sum+=i
    return sum


num=int(input("정수를 입력하세요: "))
print(getsum(num))