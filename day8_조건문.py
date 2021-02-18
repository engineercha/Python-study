height=float(input("키를 입력하세요: "))
height/=100
weight=float(input("몸무게를 입력하세요: "))

bmi=weight/height**2

if bmi>=25:
    print("BMI %.2f로 비만입니다."%bmi)
elif bmi>=23:
    print("BMI %.2f로 과체중입니다."%bmi)
elif bmi>=18.5:
    print("BMI %.2f로 정상체중니다."%bmi)
else: print("BMI %.2f로 저체중니다."%bmi)