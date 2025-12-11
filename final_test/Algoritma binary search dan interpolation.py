def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # posisi ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # tidak ditemukan


# Contoh penggunaan
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70]
    x = 40

    result = binary_search(data, x)
    if result != -1:
        print(f"Binary Search: {x} ditemukan pada index {result}")
    else:
        print(f"Binary Search: {x} tidak ditemukan")


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:

        # Rumus untuk mencari posisi
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos  # ditemukan
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # tidak ditemukan


# Contoh penggunaan
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70]
    x = 50

    result = interpolation_search(data, x)
    if result != -1:
        print(f"Interpolation Search: {x} ditemukan pada index {result}")
    else:
        print(f"Interpolation Search: {x} tidak ditemukan")

