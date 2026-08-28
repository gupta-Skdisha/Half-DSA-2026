from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)

        # More than one odd frequency => impossible to form palindrome
        odd = [c for c in freq if freq[c] % 2 == 1]

        if len(odd) > 1:
            return ""

        # Characters for the left half
        half = Counter()

        for c in freq:
            half[c] = freq[c] // 2

        m = n // 2
        t = target[:m]

        middle = odd[0] if odd else ""

        def build(left):
            return left + middle + left[::-1]

        # ------------------------------------------------
        # CASE 1:
        # Can we use target's left half exactly?
        # ------------------------------------------------
        need = Counter(t)

        possible = True

        for c in need:
            if need[c] > half[c]:
                possible = False
                break

        if possible:
            candidate = build(t)

            # This handles cases like:
            # s = "aac", target = "abb"
            #
            # t = "a"
            # candidate = "aca"
            # "aca" > "abb"
            if candidate > target:
                return candidate

        # ------------------------------------------------
        # CASE 2:
        # Make the left half just larger than target's
        # left half.
        # ------------------------------------------------

        for i in range(m - 1, -1, -1):

            # We want target[:i] to remain unchanged.
            prefix = t[:i]
            prefix_count = Counter(prefix)

            # Check if target[:i] can be constructed
            possible = True

            for c, cnt in prefix_count.items():
                if cnt > half[c]:
                    possible = False
                    break

            if not possible:
                continue

            # Characters remaining after taking prefix
            remaining = half.copy()

            for c, cnt in prefix_count.items():
                remaining[c] -= cnt

            # Choose smallest character > t[i]
            for code in range(ord(t[i]) + 1, ord('z') + 1):
                c = chr(code)

                if remaining[c] > 0:
                    remaining[c] -= 1

                    # Fill the rest with smallest possible chars
                    suffix = []

                    for x in range(ord('a'), ord('z') + 1):
                        ch = chr(x)
                        suffix.append(ch * remaining[ch])

                    left = prefix + c + ''.join(suffix)

                    return build(left)

        return ""