class solution:
    def deletenode(head,x):
        node = list.head
        x-=1
        while x!=0:
            node = node.next
            x-=1
        if head is None or node is None:
            return
        if head == None:
            head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        del node
