import os

path = os.getcwd()
print(type(path))
try:
    os.mkdir(path + '\\' + 'results')
except:
    pass
print('1')