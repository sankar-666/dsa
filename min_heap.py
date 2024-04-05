class MinHeap: 
    def __init__(self, initial_values=None):
        if initial_values is None:
            self.heap = []
        else:
            self.__build_heap(initial_values)

    def __build_heap(self, arr):
        self.heap = arr
        for i in range(int(self.__parent(len(self.heap) -1 )), -1, -1):
            self.__shift_down(i)

    # __ to make this function private
    def __shift_down(self, current_idx):
        end_idx = len(self.heap) - 1
        left_idx = self.__left_child(current_idx)
        while left_idx <= end_idx:
            right_idx = self.__right_child(current_idx)
            if right_idx <= end_idx and self.heap[right_idx] < self.heap[left_idx]:
                idx_to_shift = right_idx
            else:
                idx_to_shift = left_idx
            if self.heap[current_idx] > self.heap[idx_to_shift]:
                temp = self.heap[current_idx] 
                self.heap[current_idx] = self.heap[idx_to_shift]
                self.heap[idx_to_shift] = temp 
                current_idx = idx_to_shift
                left_idx = self.__left_child(current_idx)
            else:
                return

    # __ to make this function private
    def __shift_up(self, current_idx):
        parent_idx = int(self.__parent(current_idx))
        while current_idx > 0 and self.heap[parent_idx] > self.heap[current_idx]:
            temp = self.heap[parent_idx] 
            self.heap[parent_idx] = self.heap[current_idx]
            self.heap[current_idx] = temp
            current_idx = parent_idx
            parent_idx = int(self.__parent(current_idx))

    def peek(self):
        if len(self.heap) < 1:
            print("Heap is Empty")
        else:
            return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] 
        self.heap.pop()
        self.__shift_down(0)
    
    def insert(self, val):
        self.heap.append(val)
        self.__shift_up(len(self.heap) - 1)
    
    def display(self):
        print(self.heap)

    # __ to make this function private
    def __parent(self, idx):
        return (idx - 1) / 2

    # __ to make this function private
    def __left_child(self, idx):
        return (idx * 2) + 1
    
    # __ to make this function private
    def __right_child(self, idx):
        return (idx * 2) + 2


heap = MinHeap([6, 2, 8])


heap.insert(1)
heap.insert(5)
heap.insert(15)
heap.display()
# print(heap.peek())
heap.remove()
heap.display()