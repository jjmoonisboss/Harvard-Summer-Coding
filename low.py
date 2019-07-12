def decreasing(l):
    # TODO: Return True if `l` is decreasing, otherwise False
    if len(l) < 2:
        return True
    else:
        for i in range(1,len(l),1):
            if l[i-1] < l[i]:
                return False
    return True 

print(decreasing([3, 2, 1]))
print(decreasing([5, 2, 2, 2, 1, 1,]))
print(decreasing([1, 2, 3]))
