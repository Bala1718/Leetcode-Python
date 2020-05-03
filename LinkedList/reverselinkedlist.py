def reverseList(self, head):
    if (head == None):
        return None
    if( head.next == None):
        return head
    ret = head
    tmp = head
    
    head = head.next
    ret.next = None
    while (head!=None):
        tmp = head
        head = head.next
        tmp.next = ret
        ret = tmp
    return ret
