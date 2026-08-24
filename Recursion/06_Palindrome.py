def isPalindrome(s, i):
    n = len(s)

    if i >= n // 2:
        return True

    if s[i] != s[n - i - 1]:
        return False
    return isPalindrome(s, i + 1)


if __name__ == "__main__":
    s = "madam"
    print(isPalindrome(s, 0))