def rec_binarySearch(target, sequence, first, last):
    if first > last:
        return False
    else:
        mid = (last + first) // 2
        if sequence[mid] == target:
            return True
        elif target < sequence[mid]:
            return rec_binarySearch(target, sequence, first, mid-1)
        else:
            return rec_binarySearch(target, sequence, mid + 1, last)

sequence = list(range(0,20))
print(rec_binarySearch(10,sequence,0,20))
