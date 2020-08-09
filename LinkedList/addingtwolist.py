class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        ans = head
        up = 0

        while l1 or l2 or up:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            up, add = divmod(v1 + v2 + up, 10)
            head.next = ListNode(add)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next