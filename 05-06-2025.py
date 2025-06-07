import re

txt="Shanmugapriyan is a student"

x=re.search(r"\w+",txt)

print(x.group())


















