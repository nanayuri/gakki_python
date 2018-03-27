import re


def checkModify(s):
    return re.sub(r'\b(\w)(\w+)(\w)\b', lambda x:x.group(1) + x.group(2).lower() + x.group(3), s)


print(checkModify('YuiARAGaKi is YUi aRAgakI'))