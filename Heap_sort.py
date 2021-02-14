import Heap

def remove_from(heap, param):
    removed = heap.pop(0)
    last_element = heap.pop()
    heap.insert(0, last_element)
    heap = Heap.heapify(heap, param)
   
    return (removed, heap)
    

    
    

def heap_sort(initial, param):
    size = len(initial)
    final = []
    heap = Heap.heapify(initial, param)
    print(heap)
    for elem in range(0, size - 1):
        print(elem)
        result = remove_from(heap, param)
        removed = result[0]
        heap =result[1]
        final.insert(0, removed)

    final.insert(0, heap.pop(0))

            
    return final


# max heap sorts in ascending order
size = int(input("size of the array?"))
initial_array = [int(input("enter an element:")) for i in range(size)]
param = input("max or min heap?")
result_array = heap_sort(initial_array, param=param)
print(result_array)