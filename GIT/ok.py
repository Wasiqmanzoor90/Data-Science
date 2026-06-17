def evenodd(x):
    if x % 2==0:
        print("Even number")
    else:
        print("Odd number")
        
        
        
def pal():
    word  = input("Enter an word:-")
    rev = ""

    for ch in word:
   
        rev = ch+rev
        
    if rev == word:
        print("Palindrome")
    else:
        print("Not Palimdrome")
        