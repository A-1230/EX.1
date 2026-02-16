a= 5
b=6
result= a+b
print("a+b=",result)
c=2
d=result*c
print("d=",d)
if d>20:
    print("d is greater than 20")
else:
    print("d is less than 20")
class myclass:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
            print("name:",self.name)
            print("id:",self.id)
s1=myclass("reetu",5)
s1.display()
