# Print Name 5 times
# def printName(n):
#     if n==6: #base case
#         return
#     print('Rakesh')
#     n=n+1
#     printName(n)
# if __name__ == "__main__":
#     printName(1)

# # Print number linearly from 1 to n

# def printNumber(i,n):
#     if i>n: #base case
#         return
#     print(i)
#     printNumber(i+1,n)

# if __name__ == "__main__":
#     printNumber(1,5)    

# Print number linearly from n to 1

def printNumber(i,n):
    if i < n:
        return
    print(i)
    printNumber(i-1,n)
if __name__ == "__main__":
    printNumber(5,1)    
        