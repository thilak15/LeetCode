# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverseLinkedList(orginalHead):
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
        return True
