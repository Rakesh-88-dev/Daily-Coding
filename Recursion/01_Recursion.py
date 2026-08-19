n=0
def printNumber(n):
    if n==4:
        return
    print(n)
    n=n+1
    printNumber(n)
if __name__ == "__main__":
    printNumber(0)        