from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    """Helper to build a linked list from a Python list for local testing."""
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    """Helper to convert a linked list back to a Python list for easy printing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result




class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


if __name__ == "__main__":
    test = Solution()
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    merged_head = test.mergeTwoLists(l1, l2)
    print(linked_list_to_list(merged_head))
