import json
from string import Template

text_file = open('template_text.txt', 'r')
template_obj=Template(text_file.read())
json_file = open('placeholders.json','r')
dict = json.load(json_file)
print(template_obj.substitute(**dict))


# ----
import json
from string import Template
import sys

file1 = sys.argv[1]
text_file = open(file1, 'r')
content = text_file.read()
template_obj=Template(content)

json_file = open(sys.argv[2],'r')
dict = json.load(json_file)
result = template_obj.substitute(dict)
dict = {"key1": "val1", "key2": "val2"}
template_obj.substitute(**dict)
template_obj.substitute(key1=val1, key2=val2)
print(result)

python main.py template_text.txt placeholders.json
