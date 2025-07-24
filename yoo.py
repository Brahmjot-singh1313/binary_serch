def bin(arr, t):
    # sorting the array
    arr.sort()

    # initializing two ppinter's 
    l = 0 # it will track from lesft to the end
    r = len(arr)-1 # it will track right from start point

    # initalizing a while loop
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == t:
            return mid
        elif t > arr[mid]:
            l = mid + 1
        elif t < arr[mid]:
            r = mid - 1
    return -1

print(bin([1,2,3,5,6,8], 6))
