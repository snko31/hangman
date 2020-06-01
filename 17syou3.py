import re

line="123 hi 3 4 hello."
m=re.findall("\d",line,re.IGNORECASE)
print(m)
