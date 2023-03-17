def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    trl = newl = ListNode()
    while l1 or l2 or carry:
        suml = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = suml // 10
        trl.next = ListNode(suml % 10)
        trl = trl.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return newl.next
