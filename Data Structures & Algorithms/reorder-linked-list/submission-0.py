# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        values = []

        # 1. Store values
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # 2. Reorder values
        reordered = []
        l, r = 0, len(values) - 1

        while l <= r:
            if l == r:
                reordered.append(values[l])
            else:
                reordered.append(values[l])
                reordered.append(values[r])
            l += 1
            r -= 1

        # 3. Put values back
        curr = head
        i = 0
        while curr:
            curr.val = reordered[i]
            curr = curr.next
            i += 1