import math
n=12;
n1=n*n;
n2=int(str(n1)[::-1]);
n3=int(math.sqrt(n2));
n4=int(str(n3)[::-1]);
if(n==n4):
    print("adam");
else:
    print("Not found");
