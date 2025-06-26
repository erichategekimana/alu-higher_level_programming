#!/usr/bin/python3
for i in range(00, 99):
    if i < 10:
        print("{}{}".format(0,(i)), end=', ')
    else:
        print(i, end= ', ')
