from typing import Dict

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        prime_count, ok = self.getPrimeCount(t)
        if not ok:
            return "-1"

        factor_count = self.getFactorCount(prime_count)
        if self.sumValues(factor_count) > len(num):
            return self.construct(factor_count)

        prime_prefix = self.getPrimeCountFromString(num)

        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = len(num)
            if self.isSubset(prime_count, prime_prefix):
                return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])

            prime_prefix = self.subtract(prime_prefix, self.kFactorCounts[d])

            space = len(num) - 1 - i

            if i > first_zero:
                continue

            for bigger in range(d + 1, 10):

                remain = self.subtract(
                    self.subtract(prime_count, prime_prefix),
                    self.kFactorCounts[bigger]
                )

                factors = self.getFactorCount(remain)

                if self.sumValues(factors) <= space:
                    ones = space - self.sumValues(factors)
                    return (
                        num[:i]
                        + str(bigger)
                        + "1" * ones
                        + self.construct(factors)
                    )

        factors = self.getFactorCount(prime_count)

        return (
            "1" * (len(num) + 1 - self.sumValues(factors))
            + self.construct(factors)
        )

    kFactorCounts = {
        0: {},
        1: {},
        2: {2: 1},
        3: {3: 1},
        4: {2: 2},
        5: {5: 1},
        6: {2: 1, 3: 1},
        7: {7: 1},
        8: {2: 3},
        9: {3: 2},
    }

    def getPrimeCount(self, t: int):
        cnt = {2: 0, 3: 0, 5: 0, 7: 0}

        for p in [2, 3, 5, 7]:
            while t % p == 0:
                cnt[p] += 1
                t //= p

        return cnt, t == 1

    def getPrimeCountFromString(self, num: str):
        cnt = {2: 0, 3: 0, 5: 0, 7: 0}

        for ch in num:
            for p, f in self.kFactorCounts[int(ch)].items():
                cnt[p] += f

        return cnt

    def getFactorCount(self, cnt: Dict[int, int]):
        res = {}

        c8 = cnt[2] // 3
        rem2 = cnt[2] % 3

        c9 = cnt[3] // 2
        c3 = cnt[3] % 2

        c4 = rem2 // 2
        c2 = rem2 % 2

        c6 = 0

        if c2 == 1 and c3 == 1:
            c2 = 0
            c3 = 0
            c6 = 1

        if c3 == 1 and c4 == 1:
            c2 = 1
            c6 = 1
            c3 = 0
            c4 = 0

        res[2] = c2
        res[3] = c3
        res[4] = c4
        res[5] = cnt[5]
        res[6] = c6
        res[7] = cnt[7]
        res[8] = c8
        res[9] = c9

        return res

    def construct(self, factors):
        ans = []

        for d in range(2, 10):
            ans.append(str(d) * factors.get(d, 0))

        return "".join(ans)

    def isSubset(self, a, b):
        for k, v in a.items():
            if b.get(k, 0) < v:
                return False
        return True

    def subtract(self, a, b):
        res = dict(a)

        for k, v in b.items():
            res[k] = max(0, res.get(k, 0) - v)

        return res

    def sumValues(self, mp):
        return sum(mp.values())
        