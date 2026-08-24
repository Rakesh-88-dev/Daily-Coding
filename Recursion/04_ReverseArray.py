def reverseArray(arr,index):
    if index < 0:
        return []
    return [arr[index]]+reverseArray(arr,index-1)

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    print(reverseArray(arr,len(arr)-1))



# Optimal Way (No extra space)
def reverseArray(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    reverseArray(arr, left + 1, right - 1)


arr = [1, 2, 3, 4, 5]

reverseArray(arr, 0, len(arr) - 1)

print(arr)


def reverseArray(arr, i, n):
    if i >= n // 2:
        return

    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

    reverseArray(arr, i + 1, n)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    reverseArray(arr, 0, n)

    print(arr)