arr=[5,6,7,8,9,10]
user= int(input("enter the no: "))
def binary_search(arr,user,low,high):
    if low<=high:
        mid = low + (high - low)//2
        if arr[mid]==user:
            return mid
        elif arr[mid] < user:
            return binary_search(arr,user,mid+1,high)
        else:
            return binary_search(arr,user,low,mid-1)
    return -1
result = binary_search(arr, user, 0, len(arr)-1)
if result != -1:
    print(user, "Element is present at index " + str(result))
else:
    print(user,"Not Found")