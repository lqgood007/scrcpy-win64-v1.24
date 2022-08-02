import os

s = os.popen("adb devices")
a = s.read()

print(a)
list = a.split('\n')
print(list)
if len(list) <=1 :
    print('no devices')
    pass
# if len(list)>
"""

List of devices attached
R5CN710WMYD	device
\n
\n


"""
print(str(a)=='List of devices attached\n\n')
