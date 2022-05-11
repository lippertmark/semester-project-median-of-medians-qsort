def median_of_tree(arr, starte, stop):
    if len(arr) == 0 or starte<0 or stop>len(arr) or starte >stop:
        raise IndexError
    size = stop - starte + 1
    if size <2:
        return stop
    elif arr[starte]>=arr[stop]:
        return starte
    elif arr[stop]>=arr[starte]:
        return stop

def partion(arr, starte, stop, pivot):
    if pivot<starte or pivot > stop:
        raise IndexError
    if len(arr) == 0 or starte<0 or stop>len(arr) or starte >stop:
        raise IndexError
    pivot_value = arr[pivot]
    arr[pivot], arr[stop] = arr[stop], arr[pivot]
    curr_pivot_index = starte
    for i in range(starte, stop):
        if arr[i]<pivot_value:
            arr[i], arr[curr_pivot_index] = arr[curr_pivot_index], arr[i]
            curr_pivot_index+=1
    arr[stop], arr[curr_pivot_index] = arr[curr_pivot_index], arr[stop]
    return curr_pivot_index

def Sort(arr):
    quick_sort(arr, 0, len(arr)-1)

def quick_sort(arr, starte, stop):
    if starte <0:
        raise IndexError
    if starte >=stop:
        return
    meddian = median_of_tree(arr, starte, stop)
    pivot_index = partion(arr, starte, stop, meddian)
    quick_sort(arr, starte, pivot_index-1)
    quick_sort(arr, pivot_index+1, stop)
