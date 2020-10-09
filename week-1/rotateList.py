# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        length = 0
        curr = head
        while curr is not None:
            length+=1
            curr = curr.next
        if k==0 or k%length==0:
            return head
        pointer = length - k%length
        curr = head
        prev = None
        while pointer!=0:
            prev = curr
            curr = curr.next
            pointer -= 1
        prev.next = None
        prev = curr
        while curr.next:
            curr = curr.next
        curr.next = head
        head = prev
        return head