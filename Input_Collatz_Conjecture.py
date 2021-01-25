def main():
    print("""Welcome to Input Collatz Conjecture:
    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: 
    start with any positive integer n. Then each term is obtained from the previous term as follows: 
    if the previous term is even, the next term is one half of the previous term. 
    If the previous term is odd, the next term is 3 times the previous term plus 1. 
    The conjecture is that no matter what value of n, the sequence will always reach 1.
    """)
    i = int(input('Input any positive integer and receive the sequence of the Collatz Conjecture: '))
    def collatz(i):
        while i > 1:
            if i %2==0 :
                i = i/2
                print(i)
            else:
                i = 3*i + 1
                print(i)        
    collatz(i)
    a = input("Press ENTER to close the program")
main()    
