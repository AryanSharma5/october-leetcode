class Solution:
    def bitwiseComplement(self, N: int) -> int:
        ans = ''
        for i in bin(N)[2:]:
            if i=='0':
                ans += '1'
            else:
                ans += '0'
        return int(ans, 2)