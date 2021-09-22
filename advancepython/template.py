from jinja2 import Template

# name=input("Enter the name")
# tm=Template("hello {{name}}")
#
# msg=tm.render(name=name)
# print(msg)
name="john"
age=25
tn=Template("my name is {{name}} and my age is {{age}}")
# msg=tn.render(name=name,age=age)
print(tn.render(name=name,age=age))