def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp       
data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)

# def fun():
#     list=[10,14,2,11,6,8]
#     i=0
#     while i<len(list):
#         j=0
#         while j<len(list):
#             if list[i]>list[j]:
#                 temp=list[i]
#                 list[i]=list[j]
#                 list[j]=temp
#             j+=1
#         i+=1
#     return(list)
# print(fun())
