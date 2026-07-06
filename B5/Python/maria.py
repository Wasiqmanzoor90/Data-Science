def add(n1,n2):
    print(n1+n2)
    
    
    
def primeno(n):
   
    if n <=1:
        print("Not Prime")
    else:
        for i in range(2,n):   #2,6
                #6/2
            if n%i==0:
                print(n,"Not Prime")
                break
        else:
            print(n,"Prime number")
            
            
            


