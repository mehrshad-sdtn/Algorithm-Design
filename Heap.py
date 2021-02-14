
def bubble_up_max(node, heap):
    heap.append(node)
    i = len(heap) - 1
   
    while (heap[i // 2] < node) :
        new_i = i // 2
        heap[new_i], heap[i] = heap[i],  heap[new_i]
        i = new_i
    

def bubble_up_min(node, heap):
    heap.append(node)
    i = len(heap) - 1
   
    while (heap[i // 2] > node) :
        new_i = i // 2
        heap[new_i], heap[i] = heap[i],  heap[new_i]
        i = new_i

def sift_down_max(node, heap):
    i = 0
    while True:
        if (heap[i] < heap[2 * i + 1]):
            new_i = i * 2 + 1
            heap[new_i], heap[i] = heap[i],  heap[new_i]
            i = new_i

        elif (heap[i] < heap[2 * i + 1]):
             new_i = i * 2 + 2
             heap[new_i], heap[i] = heap[i],  heap[new_i]
             i = new_i
        else:
            break

def sift_down_min(node, heap):
    i = 0
    while True:
        if (heap[i] > heap[2 * i + 1]):
            new_i = i * 2 + 1
            heap[new_i], heap[i] = heap[i],  heap[new_i]
            i = new_i

        elif (heap[i] > heap[2 * i + 1]):
             new_i = i * 2 + 2
             heap[new_i], heap[i] = heap[i],  heap[new_i]
             i = new_i
        else:
            break



def heapify(initial, param):
    heap = []
    for node in (initial):
        if param == "max":
             bubble_up_max(node, heap)
        elif param == "min":
            bubble_up_min(node, heap)     

    return heap    


def print_tree(heap):
    for index, node in enumerate(heap):
        if index * 2 + 2 < len(heap):
             print(node, "-> (", heap[index * 2 + 1], ",", heap[index * 2 + 2], ")")




if __name__ == "__main__":
    size = int(input("size of the array?"))
    initial_array = [int(input("enter an element:")) for i in range(size)]

    param = input("min heap or max heap? ")
    heap = (heapify(initial_array, param=param))
    print(heap)
    print_tree(heap)


