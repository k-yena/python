class Calc:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num1-self.num2


class CalcChild(Calc):
    def divide(self):              # 매개변수(num2)를 다시 설정할 필요가 없음(재정의)
        if self.num2 == 0:
            print("0으로 나누면 안돼요")
        else:
            return self.num1-self.num2