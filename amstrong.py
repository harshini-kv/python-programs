x = n = 153
s = 0
c = len(str(n))  

while n:
    a = n % 10
    s = s + a ** c  
    n = n // 10

if x == s:
    print("armstrong")   
else:
    print("not armstrong")
    
