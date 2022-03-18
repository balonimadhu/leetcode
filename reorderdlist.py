class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        q = deque()
        node = head
        while True :
            node = node.next
            if not node :
                break
            q.append(node)
        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next
            if head and q:
                temp = q.popleft()
                head.next = temp
                head = head.next
        head.next = None