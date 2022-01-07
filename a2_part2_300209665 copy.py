

import math


def min_enclosing_rectangle(radius,x,y):
    '''
Preconditions: (number,number,number)->(number,number)
Radius must be greater than 0
    '''
    if radius<0:
        return None
    else:
        x=(x-radius)
        y=(y-radius)
    return (x,y)
    

def vote_percentage(results):
    '''
Preconditions: Contains at least one yes/no/abstained
(None)-> (float)
    '''
    x=(results).count('yes')
    y=(results).count('no')
    n=x+y
    return x/n


def vote():
    '''
Preconditions: (None)-> None
Must contain at least one yes/no/abstained 
    '''
    results=input("Enter yes, no and abstained votes one by one and then press enter \n")
    x= vote_percentage(results)
    if x==1.0 :
        print('The proposal passes unanimously')
    elif (x) >= (2/3) :
        print('The propsal passes with super majority')
    elif (x)>= 0.5:
        print('The proposal passes with simple majority')
    else:
        print('The proposal fails')
        
    
    
