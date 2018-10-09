import math

a = 16807 
m = 32749
q = m//a
r = m%a

def algorithm(a, m):
  i = 1
  x = a
  count = 0
  while(x != 1):
    if (m%x < m//x) and (math.gcd(i, m-1) == 1):
      print(str(x) + " is a full-period modulus-compatible multipler")
      count += 1
      print("There are " + str(count) + " full-period modulus-compatible multipliers")
    i += 1
    x = algorithm2(x)
  
def algorithm2(x):
  t = a * (x%q) - r * (x//q)
  if t > 0:
    return t
  else:
    return t + m
    

    
algorithm(a, m)