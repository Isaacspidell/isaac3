import random
a = random.randint(1, 100)
b = random.randint(1, 100)
aa=str(a)
bb=str(b)
c=int(input("what is "+aa+" + "+bb))
if(c==a+b):
    print("Correct")
else:
    print("Wrong You Bad Mather")