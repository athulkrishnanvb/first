class Add:
    def ad(self,a,b):
        return a+b
class Mul:
    def mul(self,a,b):
        return a*b
class Sub:
    def sub(self,a,b):
        return a-b
class Div(Add,Mul,Sub):
    def div(self,a,b):
        return a/b
    
obj=Div()
print(obj.ad(2,3))
print(obj.mul(4,5))
print(obj.sub(8,3))
print(obj.div(10,2))
