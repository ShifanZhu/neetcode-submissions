# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        result = ListNode(0)
        
        # This pointer moves forward as we build the merged list
        merged_list = result

        # Compare nodes from both lists until one list is empty
        while list1 and list2:
            if list1.val <= list2.val:
                # Attach the smaller node from list1
                merged_list.next = list1
                list1 = list1.next
            else:
                # Attach the smaller node from list2
                merged_list.next = list2
                list2 = list2.next

            # Move the merged list pointer forward
            merged_list = merged_list.next

        # Attach any remaining nodes from list1
        if list1:
            merged_list.next = list1

        # Attach any remaining nodes from list2
        if list2:
            merged_list.next = list2

        # Return the merged list, skipping the dummy node
        return result.next