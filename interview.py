def Multiply(x):
    if(symbol=="" and len(x)==1):
     print(x)
    else:
     num = x.split(symbol)
     mul=1
     l=len(num)
     for i in range(0,l):
      if(int(num[i])<0):
       print("negatives")
       quit()
      else:
       mul = mul*int(num[i])
     print(mul)
s= input("enter the string")
symbol= input("enter delimeter")
if (s=="" and symbol==""):
     print('0')
else:
 Multiply(s)
    
