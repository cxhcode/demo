# -*- coding: utf-8 -*-



with open("C:\\Users\\admin\\Pictures\\test.txt", 'r') as f:
    done = False
    while not done:
        aLine = f.readline()
        if aLine != '':
            print(aLine)
        else:
            done = True
