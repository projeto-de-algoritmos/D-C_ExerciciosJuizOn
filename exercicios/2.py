# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.merge_lists(lists, 0, len(lists) - 1)

    def merge_lists(self, lists, left, right):
        if left == right:
            return lists[left]
        elif left < right:
            mid = (left + right) // 2
            left_merged = self.merge_lists(lists, left, mid)
            right_merged = self.merge_lists(lists, mid + 1, right)
            return self.merge_two_lists(left_merged, right_merged)

    def merge_two_lists(self, l1, l2):
        dummy = Solution.ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return dummy.next