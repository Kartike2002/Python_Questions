#Q1
x=int(input("Enter the number"))
match x:
    case x if (x>99 and x<1000):
        print("Yes a three digit")
    case y: 
        print("Not a three digit")     
        
#Q2
x=int(input("Enter the number"))
match x:
    case x if x>0:
        print("Postive") 
    case x if x<0:
        print("Negative")
    case x if x==0:
        print("zero")               
        
#Q3
print("Case 1-- for odd-even ")        
print("Case 2-- for Postive and non postive")        
print("Case 3-- for Simple intrest ")        
print("Case 4-- for find the root of quardic equation ")
choice=int(input("Enter the number"))
match choice:
    case 1:
        if (choice%2==0):
            print("Even")
        else:
            print("Odd")
    case 2:
        if(choice>0):
         print("Postive") 
        if(choice<0):
            print("non postive")        
    case 3:
        p=int(input("Enter the principle"))
        r=int(input("Enter the der"))
        t=int(input("Enter the time"))
        per=p*r*t/100
        print(per)        
    case 4:
        print("enter the root a,b,c")
        a,b,c=int(input()),int(input()),int(input())
        d=b**2-4*a*c
        if d>0:
            print("root is real and distinct")
        elif d==0:
            print("Two real and equal")
        else :
            print("Two root imaginary") 


#Q4


x=eval(input("Enter a number in from of int,float,complex,bool"))
match x:
    case x if type(x)==int:
        print("Monday")
    case x if type(x)==float:
        print("Tuesday")
    case x if type(x)==complex:
        print("Wednessday")                         
    case x if type(x)==bool:
        print("Thursday")        
        
#Q5
x=int(input("Enter the string"))
match x:
    case x if x in "mysirg":
        print("one")
    case x if x in "eduction":
        print("Two")
    case x if x in "services":
        print("Three")                