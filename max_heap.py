class MaxHeap:
    def __init__(self, initial_value = None):
        if initial_value is None:
            self.heap = []
        else:
            self._build_heap(initial_value)
    
    def _build_heap(self, arr):
        self.heap = arr
        for i in range(int(self._parent(len(arr) - 1)), -1, -1):
            self._shift_down(i)

    def _shift_up(self, current_idx):
        parent_idx = int(self._parent(current_idx))

        while current_idx > 0 and self.heap[parent_idx] > self.heap[current_idx]:
            self.heap[parent_idx], self.heap[current_idx] = self.heap[current_idx], self.heap[parent_idx]
            current_idx = parent_idx
            parent_idx = int(self._parent(current_idx))

    def _shift_down(self, current_idx):
        end_idx = len(self.heap) - 1
        left_idx = int(self._left_child(current_idx))

        while left_idx <= end_idx:
            right_idx = int(self._right_child(current_idx))
            if right_idx <= end_idx and self.heap[right_idx] > self.heap[left_idx]:
                idx_to_shift = right_idx
            else:
                idx_to_shift = left_idx
            if self.heap[idx_to_shift] > self.heap[current_idx]:
                self.heap[idx_to_shift], self.heap[current_idx] = self.heap[current_idx], self.heap[idx_to_shift]
                current_idx = idx_to_shift
                left_idx = int(self._left_child(current_idx))
            else:
                return

    def _parent(self, idx):
        return (idx - 1) / 2

    def _left_child(self, idx):
        return (idx * 2) + 1
    
    def _right_child(self, idx):
        return (idx * 2) + 2
    
    def peek(self):
        if len(self.heap) < 1:
            print("Heap is empty")
            return
        print(self.heap[0])
    
    def display(self):
        print(self.heap)

    def remove(self):
        self.heap[-1] , self.heap[0] = self.heap[0], self.heap[-1]
        self.heap.pop()
        self._shift_down(0) 
    
heap = MaxHeap([1, 4, 5, 12, 2])
heap.display()
heap.remove()
heap.display()
