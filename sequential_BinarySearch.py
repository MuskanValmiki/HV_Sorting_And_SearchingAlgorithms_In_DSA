arr = [3, 4, 5, 6, 7, 8, 9, 10]
user = int(input("enter the no:"))

def binary_search(arr, user, lowest_element, highest_element):  
    while lowest_element <= highest_element:
        mid = lowest_element + (highest_element - lowest_element)//2
        if arr[mid] == user:
            return mid
        elif arr[mid] < user:
            lowest_element = mid + 1
        else:
            highest_element = mid - 1
    return -1
out_put = binary_search(arr, user, 0, len(arr)-1)
if out_put != -1:
    print(user, "Element is present at index " + str(out_put))
else:
    print(user,"Not Found")
    
    