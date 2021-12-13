import os
os.system("color")

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

class bcolors:
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    ENDC = "\033[0m"

for x in range(0, 20):
    print(f"fibonacci {x} is: {bcolors.OKCYAN}{fibonacci(x)}{bcolors.ENDC}")