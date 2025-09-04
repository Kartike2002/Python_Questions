# Q1
'''def even(n):
    if n%2==0:
        return 1
    
    
print(even(40))    
    
#Q2

def greater(a,b,c):
    if (a>b):
        print(a)
    elif (b>c):
        print(b)
    else :
        print(c)

# Q3


def isPrime(n):
    flag=0
    for i in range(2, n+1):
        if n % i == 0:
            flag=1
            break
    if flag== 1:
        return 0
    else:
        return 1


a = isPrime(13)
print(a)


# Q4

def isleap(year):
    if (year % 400 == 0):
        print(" is a leap year.", year)
    elif (year % 100 == 0):
        print(" is not a leap year.", year)
    elif (year % 4 == 0):
        print("is a leap year.", year)
    else:
        print("is not a leap year", year)
        
        
        
print(isleap(2023))      

'''

#Q5

def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i 
    return f 
    
print(fact(5))    
        
        
