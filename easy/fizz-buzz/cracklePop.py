"""
From https://www.recurse.com/apply/retreat
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop.
If it's divisible by both 3 and 5, print CracklePop.
"""

def crackle_pop() -> str:
    for n in range(1, 101):
        div = False
        p = str(n)
        if n%3 == 0:
            div = True
            p = "Crackle"
        if n%5 == 0:
            if div:
                p = "CracklePop"
            else:
                p = "Pop"
        print(p)
        
if __name__ == "__main__":
    crackle_pop()  
