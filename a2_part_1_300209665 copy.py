
import math
import random


def elementary_school_quiz(flag, n):
    '''
Preconditions: flag is 0 or 1, n is 1 or 2
    '''
    score=0
    while flag!=1:
        if n!=2:
            for flag in range(0,1):
                x=random.randint(0,9)
                y=random.randint(0,9)
                print(f" {y} - {x} ?")
                ans= int(input())
                if ans==(y-x):
                    score = score + 1
                else:
                    pass
        else:
            for flag in range (0,2):
                x=random.randint(0,9)
                y=random.randint(0,9)
                print(f" {y} - {x} ?")
                ans=int(input())
                if ans == (y-x):
                    score= score+1
                else:
                    pass
        return score
            
             
    while flag==1:
        if n!=2:
            for flag in range(0,1):
                x=random.randint(0,9)
                y=random.randint(0,9)
                print(f"{x} ^ {y}")
                ans= int(input())
                if ans==(x**y):
                    score=score+1
                else:
                    pass
        else:
            for flag in range (0,2):
                x=random.randint(0,9)
                y=random.randint(0,9)
                print(f"{x}^{y}")
                ans=int(input())
                if ans==(x**y):
                    score=score+1
                else:
                    pass
        return score



def high_school_quiz(a,b,c):
    '''
Preconditions:
a,b,c are real numbers
(number,number,number)-> None
    '''
    a=float(a)
    b=float(b)
    c=float(c)
    d= (b**2-4*a*c)
    if d<0:
        x = float(-b+ math.sqrt(abs(d)))/(2*a)
        y = float(-b- math.sqrt(abs(d)))/(2*a)
        print(f"has the following complex roots: \n{x} + i {y} \nand \n{x} - i {y}")
    elif d==0:
        if a>0 or a<0:
            print (f"The quadratic equation {a}*x^2 + {b}*x + {c} = 0")
            x = float(-b+ math.sqrt(d))/(2*a)
            print(f"has only one solution: \n{x}")
        elif a== 0 and b==0 and c==0:
            print(f"The quadratic equation {a}*x^2 + {b}*x + {c} = 0")
            print("is satisfied for all numbers x")
        else:
            print(f"The quadratic equation {a}*x^2 + {b}*x + {c} = 0")
            print("is satisfied for no number x")
    elif a==0:
        if b>0 or b<0:
            print(f"The linear equation {b}*x + {c} = 0")
            x= (-1*c)/b
            print(f"has the following root/solution {x}")
    else:
        print (f"The quadratic equation {a}*x^2 + {b}*x + {c} = 0")
        x = float(-b+ math.sqrt(d))/(2*a)
        y = float(-b- math.sqrt(d))/(2*a)
        print(f"has the real roots are: \n{x} and {y}")



print("☆Welcome to my math quiz generator☆")


name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

score=0

if status=='1':
    print(f"☆{name}, welcome to my quiz generator for elementary school students☆")
    flag= int(input(f"{name}, what would you like to practice? \n0 for subtraction \n1 for exponentiation \n"))
    n= int(input("How many equations would you like to do? Enter 0, 1 or 2: "))
    if n==1:
        print(f"{name}, here is your question:")
    elif n==2:
        print(f"{name}, here are your two questions:")
    elif n==0:
        print("Zero questions. OK.")
    else:
        print("Invalid choice. Only 0, 1 and 2 are accepted.")
    score=elementary_school_quiz(flag,n)
    if score==2 and n==2 or score==1 and n==1:
        print(f"Congrats, {name}! you'll probably get an A tomorrow.")
    elif score==1 and n==2:
        print(f"You did ok {name}, but I know you can do better!")
    elif score ==0:
        print(f"I think you need some more practice, {name}")
        



elif status=='2':
    print(f"☆{name}, welcome to my quiz generator for high school students☆")
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        question=str.lower(question)
        if question == "yes":
            flag=True 
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a=float(input("Enter a number for the coefficient a: "))
            b= float(input("Enter a number for the coefficient b: "))
            c= float(input("Enter a number for the coefficient c: "))
            (high_school_quiz(a,b,c))

else:
    print(f"{name}, you are not a target audience for this software.")

print('Goodbye,' +name+ '!')
    

