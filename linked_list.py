class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def appendAfter(self, afterValue, data):
        temp = self.head
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return
        
        if afterValue == temp.data:
            new_node.next = temp
            self.head = new_node
            return
        
        if afterValue == self.tail.data:
            self.tail.next = new_node
            self.tail = new_node
            return

        while temp is not None and temp.data != afterValue:
            temp = temp.next
        
        if temp is None:
            print(f"{afterValue} not found in the linked list.")
            return

        new_node.next = temp.next
        temp.next = new_node

        # If the new node is added after the current tail, update the tail
        if new_node.next is None:
            self.tail = new_node


    def display(self):
        if self.head is None:
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, data):
        temp = self.head
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
        
        while temp.next is not None and temp.next.data != data:
            temp = temp.next

        # Check if the node was not found
        if temp.next is None:
            print(f"{data} not found in the linked list.")
            return
        
        # Update the next reference to bypass the node to be deleted
        temp.next = temp.next.next

    # we can use a 2 pointer approch with first and second pointer
    def removeDuplicates(self):
        first = self.head

        while first is not None and first.next is not None:
            second = first.next
            
            while second is not None and second.data == first.data:
                second = second.next
                
            first.next = second
            first = first.next

            if second is None:
                # Update tail when reaching the end of the list
                self.tail = first

        # Set the last node's next to None to terminate the list properly
        if first is not None:
            first.next = None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        self.head = prev


linkedlist = LinkedList()



linkedlist.append(10)
linkedlist.append(20)
linkedlist.append(20)
linkedlist.append(20)
linkedlist.append(30)
linkedlist.append(30)
linkedlist.append(30)
linkedlist.append(30)
linkedlist.append(30)
linkedlist.append(40)
linkedlist.removeDuplicates()
linkedlist.display()
linkedlist.reverse()
linkedlist.display()