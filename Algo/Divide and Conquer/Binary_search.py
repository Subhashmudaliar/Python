#Binary search
def binary_search(arr,low,high,key):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr,low,mid-1,key)
        else:
            return binary_search(arr,mid+1,high,key)
    else:
        return -1
#Driver function
arr = [9,8,7,6,5]
arr.sort()
print("Element is present at index",binary_search(arr,0,len(arr)-1,77))
