# '''클래스=붕어빵 틀
# 객체=만들어진 붕어빵'''

# #클래스 생성
# class waffle:
#     pass        #아무 코드도 안 정해졌을 때 코드 대신 넣어줌

# #객체 생성
# choco=waffle()
# banana=waffle() #banana는 객체면서, waffle의 인스턴트임

# #클래스
# class calculator:
#     def setdata(self, first, second):    #self는 setdata 메소드를 호출한 객체 a를 전달함
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first + self.second
#         return result

# a=calculator()
# a.setdata(6,3)  #setdata 함수에 초기값을 알려줌
# print(a.first, a.second, a.add())

# b=calculator()
# b.setdata(20,10)
# print(b.first, b.second, type(b.first))


#오늘의 문제: 계산기 클래스
class cal:
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

a=cal(float(input("첫번째 수: ")), float(input("두번째 수: ")))
print("add:",a.add())
print("sub:",a.sub())
print("mul:",a.mul())
print("div:",a.div())