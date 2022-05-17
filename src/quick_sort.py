def findMedian(arr, left, right):
    array_of_median = []
    for i in range(left, right + 1):
        array_of_median.append(arr[i])
    array_of_median.sort()
    return array_of_median[(right - left + 1) // 2]

def partition(arr, left, right, med):
    for i in range(left, right + 1):
        if arr[i] == med:
            arr[i], arr[right] = arr[right], arr[i]
            break
    i = left - 1
    for j in range(left, right):
        if arr[j] <= arr[right]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def KthSmallest(arr, left, right, med):
    n = right - left + 1
    median = []
    i = 0
    while i < n// 5:
        median.append(findMedian(arr, left + 5 * i, left + 5 * i + 4))
        i += 1
    if i * 5 < n:
        median.append(findMedian(arr, left + 5 * i, left + 5 * i + (n % 5 - 1)))
        i += 1
    if i == 1:
        medOfmed = median[i - 1]
    else:
        medOfmed = KthSmallest(median, 0, i - 1, i // 2)
    partition_of_arr = partition(arr, left, right, medOfmed)
    i = partition_of_arr - left + 1
    if i == med:
        return arr[partition_of_arr]
    elif i > med:
        return KthSmallest(arr, left, partition_of_arr - 1, med)
    else:
        return KthSmallest(arr, partition_of_arr + 1, right, med - i)

def QuickSort(arr, left, right):
    if left >= right:
        return
    med = KthSmallest(arr, left, right, ( right - left +1 )//2)
    partition_of_arr = partition(arr, left, right, med)
    QuickSort(arr, left, partition_of_arr - 1)
    QuickSort(arr, partition_of_arr + 1, right)

def Sort(arr):
    QuickSort(arr, 0, len(arr)-1)

if __name__ == '__main__':
    a = [1, 34, 6432, 23, 45, 45]
    Sort(a)
    print(a)