import re

result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result.group(0))

result = re.split(r'y', 'Analytics')
print(result)

result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)