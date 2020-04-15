# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            
            if (arr[j] < arr[smallest_index]):
                
                smallest_index = j
            

            # TO-DO: swap
        c = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = c
        #OR
        #arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    

    return arr
    maximum = mar(arr)
    
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    
    count = [0 * i for i in range(maximum + 1)]
    
    for x in arr:
        count[x] += 1
        
    for i in range(len(count) - 1):
        count[i+1] = count[i+1] + count[i]
        
    for i in range(len(count)):
        count[i] -= 1
        
    final = [0 * i for i in range(len(arr))]
    
    for x in arr:
        fin_index = count[x]
        count[x] -= x
        
    return final