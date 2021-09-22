from jinja2 import Template
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getAge(self):
        return self.age
    def getName(self):
        return self.name

person=Person('peter',26)
tn=Template("my name is {{per.getName()}} and i am {{per.getAge()}}")
msg=tn.render(per=person)
print(msg)