def findMedian(a, p, r):
    L = []
    for i in range(p, r + 1):
        L.append(a[i])
    L.sort()
    return L[(r - p + 1) // 2]


def partition(a, p, r, x):
    for i in range(p, r + 1):
        if a[i] == x:
            a[i], a[r] = a[r], a[i]
            break
    i = p - 1
    for j in range(p, r):
        if a[j] <= a[r]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def KthSmallest(a, p, r, k):
    n = r - p + 1
    median = []
    i = 0
    while i < n // 5:
        median.append(findMedian(a, p + 5 * i, p + 5 * i + 4))
        i += 1
    if i * 5 < n:
        median.append(findMedian(a, p + 5 * i, p + 5 * i + (n % 5 - 1)))
        i += 1
    if i == 1:
        medOfmed = median[i - 1]
    else:
        medOfmed = KthSmallest(median, 0, i - 1, i // 2)
    q = partition(a, p, r, medOfmed)
    i = q - p + 1
    if i == k:
        return a[q]
    elif i > k:
        return KthSmallest(a, p, q - 1, k)
    else:
        return KthSmallest(a, q + 1, r, k - i)


def QuickSort(a, p, r):
    if p >= r:
        return
    med = KthSmallest(a, p, r, (r - p + 1) // 2)
    q = partition(a, p, r, med)
    QuickSort(a, p, q - 1)
    QuickSort(a, q + 1, r)


def Sort(arr):
    QuickSort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    a = [1, 34, 6432, 23, 45, 45]
    Sort(a)
    print(a)
