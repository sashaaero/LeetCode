def minimumAbsDifference(arr):
    arr.sort()
    minimum = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        minimum = min(minimum, arr[i+1] - arr[i])
    final = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == minimum:
            final.append([arr[i],arr[i+1]])
    return final

