# -*- coding: utf-8 -*-


class User(object):
    pass

print(type(User))
print(type(User()))
print(User)
print(User())
MyShinyClass = type('MyShinyClass', (), {})
print(MyShinyClass)


#
# with open("C:\\Users\\admin\\Pictures\\test.txt", 'r') as f:
#     done = False
#     while not done:
#         aLine = f.readline()
#         if aLine != '':
#             print(aLine)
#         else:
#             done = True
