import re

strings = "hello world I anm your friend_tom"
result = re.findall(r"[hl]", strings)
print(result)