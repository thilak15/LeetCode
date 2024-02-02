# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # The Problem asks to find the common intersection node not the value
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA is not pB:
            # If reaching the end of one list, continue from the beginning of the other list.
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        # Either both are None (no intersection) or both point to the intersection node.
        return pA
        # Time Complexity  O(N+M)  N,M-lenght of the ListA,ListB
        # Space Complexity O(1)
