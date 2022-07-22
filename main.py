import json
from string import Template

text_file = open('template_text.txt', 'r')
template_obj=Template(text_file.read())
json_file = open('placeholders.json','r')
dict = json.load(json_file)
print(template_obj.substitute(**dict))