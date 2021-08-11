class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(abs(x))
            x = x[::-1]
            x = int(x)
            if (x <= 2**31 - 1):
                return x
            else:
                return 0
        else:
            x = str(abs(x))
            x = '-' + x[::-1]
            x = int(x)
            if (x >= -2**31):
                return x
            else:
                return 0