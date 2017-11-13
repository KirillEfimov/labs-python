def find_min(arr):
    m = arr[0]
    for x in arr:
        if x < m:
            m = x
    return m


def find_mean(arr):
    # return sum(arr)/len(arr)
    n, s = 0, 0
    for x in arr:
        n += 1
        s += x
    return s/n


x = list(range(10))
print(find_min(x))
print(find_mean(x))
