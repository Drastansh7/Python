"""
def pattern1():
    print("p1")
def pattern2():
    print("p2")
def pattern3():
    print("p3")
def pattern4():
    print("p4")





while True:
    num = int(input("1 for pattern1 \n2 for pattern2 \n3 for pattern3 \n4 for pattern4 \n"))
    if num==1:
        pattern1()
    elif num==2:
        pattern2()
    elif num == 3:
        pattern3()
    elif num==4:
        pattern4()
    else :
        break
"""

'''
class Pattern:

    def pattern1(self):
        print("p1")
    def pattern2(self):
        print("p2")
    def pattern3(self):
        print("p3")
    def pattern4(self):
        print("p4")





while True:
    p = Pattern()
    num = int(input("1 for pattern1 \n2 for pattern2 \n3 for pattern3 \n4 for pattern4 \n"))
    if num==1:
        p.pattern1()
    elif num==2:
        p.pattern2()
    elif num == 3:
        p.pattern3()
    elif num==4:
        p.pattern4()
    else :
        break
'''


def addition(i,j):

    return i+j

print(addition(10,19))

