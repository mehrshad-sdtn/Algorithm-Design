def insertion_sort(array):
    
    for i in range(len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] >= current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current    
    return array



array = [10, 5, 8, 2, 6, 12, 1, 23]
print(insertion_sort(array))       

        