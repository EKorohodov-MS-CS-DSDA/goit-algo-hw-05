def binary_search(arr, target):
    iterations = 0
    low = 0
    high = len(arr) - 1
    upper_bound = -1
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = mid
            high = mid - 1
    return iterations, arr[upper_bound]


if __name__ == "__main__":
    arr = [10,12,13,14,15,16,17,18,20]
    print(binary_search(arr, 11))
    print(binary_search(arr, 19))
    print(binary_search(arr, 13))
