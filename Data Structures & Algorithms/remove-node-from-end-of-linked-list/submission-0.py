# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_len = 0
        dummy = ListNode(0, head)
        while head:
            total_len += 1
            head = head.next
        print("total_len: ", total_len)
        head = dummy.next
        if total_len <= n:
            return 

        idx = 0
        while head:
            if idx == total_len - n - 1:
                head.next = head.next.next
                break
            idx += 1
            head = head.next
        return dummy.next

