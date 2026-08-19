class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r] |= 1 << (s - 2)

        LEFT = 0b00001111   
        MID = 0b00111100      
        RIGHT = 0b11110000     

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left_free = (mask & LEFT) == 0
            mid_free = (mask & MID) == 0
            right_free = (mask & RIGHT) == 0

            if left_free and right_free:
                ans += 2
            elif left_free or mid_free or right_free:
                ans += 1

        return ans