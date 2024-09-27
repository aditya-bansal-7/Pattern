n = 5

#      @
#     @@@
#    @@@@@
#   @@@@@@@
#   *     *
#  **     **
# ***@@@@@***
#  **     **
#   *     *

for i in range(1,int(n/2 + 3)):
    print(" "*(n-i + 1) , end="")
    print("@"*(2*i - 1))

for i in range(1, int(n/2 + 1)):
    print(" "*(int(n/2 - i + 1)) , end="")
    print("*"*i, end="")
    print(" "*n,end="")
    print("*"*i)

print("*"*int(n/2 + 1), end="")
print("@"*n, end="")
print("*"*int(n/2 + 1))


for i in range(1, int(n/2 + 1)):
    print(" "*(i) , end="")
    print("*"*int(n/2 + 1 - i), end="")
    print(" "*n,end="")
    print("*"*int(n/2 + 1 - i))


