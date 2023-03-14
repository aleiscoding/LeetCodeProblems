def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        
        rx = 0
        while x != 0:
            rx = rx * 10 + ( x % 10)
            x //= 10

        return rx == x

