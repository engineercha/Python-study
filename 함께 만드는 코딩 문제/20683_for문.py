nums=[i for i in range(1,101)]

# 1~100
for i in nums:
    if i==100: print(i)
    else: print(i, end=',')

# 1~100 중 짝수
for i in nums:
    if i%2==0:
        if i==100: print(i)
        else: print(i, end=',')

# 1~100 중 홀수
for i in nums:
    if i%2!=0:
        if i==100: print(i)
        else: print(i, end=',')

# 100~1출력
nums.reverse()
for i in nums:
    if i==1: print(i)
    else: print(i, end=',')

# 3,5의 공배수
for i in nums:
    if i%3!=0 and i%5!=0: continue
    else: last=i; break
nums.sort()
for i in nums:
    if i==last: print(i)
    elif i%3==0 and i%5==0: print(i, end=',')

# 3과 5의 배수
for i in nums:
    if i==last: print(i)
    elif i%3==0: print(i, end=',')
    elif i%5==0: print(i, end=',')