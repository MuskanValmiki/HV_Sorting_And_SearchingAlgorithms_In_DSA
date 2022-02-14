def selectionsort(list):
    size=len(list)
    i=0
    while i<size-1:
        min_index=i
        j=min_index
        while j<size:
            if list[j]<list[min_index]:
                min_index=j
            j+=1
        if i!=min_index:
            list[i],list[min_index]=list[min_index],list[i]
        i+=1
    print(element)
element=[78,2,12,15,8,6]
selectionsort(element)

