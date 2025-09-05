# Q1
"""
def ODD_Natural(n):
    for i in range(1, n+1):
        print(2*i-1)


print(ODD_Natural(5))


# Q2

def isPrime(n):
 n = 1
 prime_flag = 0
 if(n > 1):
    for i in range(2,n+1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
 else:
    print("False")
   
isPrime(2)    
    
#Q3

def isPrime(a,b):
 n = 1
 prime_flag = 0
 for i in range(a,b+1):
  if(n > 1):
    for i in range(2,n+1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
 else:
    print("False")
   
"""

#Q4

def FibN(n):
    a=-1
    b=1
    while(n):
        c=a+b
        print(c)
        a=b
        b=c
        n-=1
        
FibN(10)   

#Q5

     
         
    