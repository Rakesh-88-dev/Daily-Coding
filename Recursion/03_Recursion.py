#Functional and parametrized recursion
# Sum of first N numbers

# def sumNum(i,sum):
#     if i < 1:
#         print(sum)
#         return
#     sumNum(i-1,sum+i)

# if __name__ == "__main__":
#     sumNum(4,0)

# Functional Recursion

def functionalSum(n):
    if n == 0:
        return 0
    return n + functionalSum(n-1)

if __name__ == "__main__":
    n=5
    print(functionalSum(n))

    