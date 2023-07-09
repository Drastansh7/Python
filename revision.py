#
p= 1000
r=2
t=3
si =p*r*t/100
print(si)
def calc():
    p= 1000
    r=2
    t=3
    si =p*r*t/100
    print(si)
print("**********")
calc()

class calc1:
    def cals(self):
        p = 1000
        r = 2
        t = 3
        si = p * r * t / 100
        print(si)
obj = calc1() #object declration
obj.cals() # object calling

def notebook():
    cost_one = 100
    quantity = 4
    total_cost = cost_one*quantity
    print(total_cost)

notebook()

n = 123450
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)


n = 123434525
count = 0
sum_1 = 0
while n > 0:
    count += 1
    r = n % 10
    if r%2 == 0:
        sum_1 = sum_1 + r
    n = n//10
print(count)
print(sum_1)


n=3
while True:
    pin = int(input("Enter a number: "))
    if pin == 1234:
        print("Open")
        break
    else:
        if n > 1:
            n -= 1
        else:
            break
#break is a condition for loop








