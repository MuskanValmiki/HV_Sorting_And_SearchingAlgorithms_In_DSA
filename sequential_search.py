def sequential_search(input_list,n):
    for i in range(0 , n):
        if(input_list[i] == x):
            return i
    return -1

input_list = [5,9,10,6,12,8,7]
x=int(input("enter the number"))
n = len(input_list)

result = sequential_search(input_list,n)
if (result == -1):
    print("None")
else:
    print("element found at index:",result)
    
    
    