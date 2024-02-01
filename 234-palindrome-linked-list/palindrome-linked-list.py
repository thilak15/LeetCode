# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        """def reverseLinkedList(orginalHead):
            prev,curr=None,orginalHead

            while curr:
                next_node=curr.next
                new_node=ListNode(curr.val)
                new_node.next=prev
                prev=new_node
                curr=next_node
            return prev
        new_list=reverseLinkedList(head)

        curr1,curr2=head,new_list

        while curr1 is not None and curr2 is not None:
            if curr1.val!=curr2.val:
                return False
            curr1=curr1.next
            curr2=curr2.next
        return True"""
    # Time complexit is O(n)
    # Space Complexity O(n)
    # we can reduce the space complexit by just reversing the second half of the Linked list using two pointer concept(slow and fast)
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

