#            *
#           ***
#          *****
#            e
#            e
#            e
#            e
#        eeeee
#        e
#   *    e
#  **    e
# ***eeeee
#  **
#   *

def pattern(n):
    if(n%2 == 0) :
        print("This pattern is not for even input...")
        return

    for i in range(1 , int(n/2 + 2)):
        print(" "*(2*n + int(n/2) - i ) , end="")
        print("*"*(2*i -1))

    for i in range(n-1):
        print(" "*(2*n) , end="")
        print(" "*(int(n/2) - 1), end="")
        print("e")
    
    print(" "*(n+int(n/2 )), end="")
    print("e"*(n))
    print(" "*(n ) , end="")
    print(" "*(int(n/2)), end="")
    print("e")

    for i in range(1,n+1):
        if(i <= int(n/2)):
            print(" "*(int(n/2 - i + 1)), end="")
            print("*"*(i),end="")

            print(" "*(n -1),end="")
            print("e")
        elif(i == int(n/2 + 1)):
            print("*"*(int(n/2 + 1)) , end="")
            print("e"*(n))
        else:
            print(" "*(i - int(n/2) - 1),end="")
            print("*"*(n-i + 1))


pattern(5)
