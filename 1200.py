def minimumAbsDifference(arr):
    arr.sort()
    minimum = float('inf')
    final = []
    for i, n in enumerate(arr[:-1]):
        if (arr[i + 1] - n) <= minimum:
            if (arr[i + 1] - n) < minimum:
                final = []
                minimum = arr[i + 1] - n
            final.append([n, arr[i+1]])
    return final
