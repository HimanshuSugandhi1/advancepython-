from jinja2 import *
persons=[
    {
    "name":"Himanshu",'age':' 22'},
    {'name':'Shital','age':' 45'},
    {'name':'manish','age':' 50'}]

file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)
template =env.get_template('showperson')
output=template.render(persons=persons)
print(output)