class cal:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
   def div(self): 
        result=self.first/self.second
        return result

num1=float(input("첫번째 수: "))
num2=float(input("두번째 수: "))
a=cal(num1, num2)  
print("add:",a.add())
print("div:",a.div())


class perfectcal(cal):  #클래스 상속; perfectcal=자식클래스, cal=부모클래스
    def modulo(self):
        result=self.first%self.second
        return result
    def div(self):      #메소드 오버라이딩
        result=self.first//self.second
        return result

b=perfectcal(num1,num2)
b=print("modulo:",b.modulo())
b=print("div2:",b.div(),end='\n\n')


'''객체변수: 독립적으로 값을 유지, 다른 객체에 영향x
클래스변수: 모든 객체에 공유'''

class Food:
    favorite="뿌링클"

a=Food()
b=Food()
print("a:",a.favorite,":",id(a.favorite))
print("b:",b.favorite,":",id(b.favorite))

Food.favorite="치즈김밥"
print("f:",Food.favorite,":",id(Food.favorite))
print("a:",a.favorite,":",id(a.favorite))


#오늘의 미션
class calc:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    
    def add(self):
        result=self.first+self.second
        return result

    def sub(self):
        result=self.first-self.second
        return result

    def mul(self):
        result=self.first*self.second
        return result

    def div(self):
        result=self.first/self.second
        return result

    def pow(self):
        result=self.first**self.second
        return result

n1=float(input("첫번째 수: "))
n2=float(input("두번째 수: "))
a=calc(n1,n2)


class calc_v2(calc):
    def add_abs(self):
        result=abs(self.first+self.second)
        return result

    def sub_abs(self):
        result=abs(self.first-self.second)
        return result

    def pow(self):        
        result=self.second**self.first
        return result

b=calc_v2(n1,n2)
print("add:",a.add(),"(*abs:%f)"%b.add_abs())
print("sub:",a.sub(),"(*abs:%f)"%b.sub_abs())
print("mul:",a.mul())
print("div:",a.div())
print("pow:",a.pow(),"opp:",b.pow(),end='\n\n')

print(type(a.add()))