def factorila(n):
    if n == 1:
        return 1
    return n * factorila(n-1)

if __name__ == "__main__":
    print(factorila(5))