
def bubble_up(node, heap):
    heap.append(node)
    i = len(heap) - 1
   
    while (heap[i // 2] < node) :
        new_i = i // 2
        heap[new_i], heap[i] = heap[i],  heap[new_i]
        i = new_i
    

def sift_down(node, heap):
    heap.append(node)
    i = len(heap) - 1
   
    while (heap[i // 2] > node) :
        new_i = i // 2
        heap[new_i], heap[i] = heap[i],  heap[new_i]
        i = new_i




def heapify(initial, param):
    heap = []
    for node in (initial):
        if param == "max":
             bubble_up(node, heap)
        elif param == "min":
            sift_down(node, heap)     

    return heap    


def print_tree(heap):
    for index, node in enumerate(heap):
        if index * 2 + 2 < len(heap):
             print(node, "-> (", heap[index * 2 + 1], ",", heap[index * 2 + 2], ")")



size = int(input("size of the array?"))
initial_array = [int(input("enter an element:")) for i in range(size)]

param = input("min heap or max heap? ")
heap = (heapify(initial_array, param=param))
print(heap)
print_tree(heap)


