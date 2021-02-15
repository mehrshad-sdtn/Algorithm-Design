def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def selection_sort(array):
    for i in range(len(array)):
       current_min = i
       for j in range(i, len(array)):
           if array[current_min] < array[j]:
               current_min = j
       swap(array, current_min, i)
    return array
    
        
if __name__ == '__main__':        
    array = [1, 5, 2, 3, 12, 8, 5, 78, 1, 45, 1.5]
    print(selection_sort(array))