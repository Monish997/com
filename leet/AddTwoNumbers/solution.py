# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = 0, 0
        h1, h2 = l1, l2
        m1, m2 = 1, 1
        while h1:
            n1 = n1 + h1.val * m1
            h1 = h1.next
            m1 *= 10
        while h2:
            n2 = n2 + h2.val * m2
            h2 = h2.next
            m2 *= 10
        s = n1 + n2
        ret = ListNode()
        curr = ret
        while True:
            curr.val = s % 10
            s //= 10
            if s > 0:
                curr.next = ListNode()
                curr = curr.next
            else:
                break
        return ret


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    soln = Solution().addTwoNumbers(l1, l2)
    while soln:
        print(soln.val, end=" -> " if soln.next else "\n")
        soln = soln.next
