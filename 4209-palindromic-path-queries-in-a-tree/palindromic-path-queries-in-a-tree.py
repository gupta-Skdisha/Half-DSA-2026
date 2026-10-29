class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        parent[0] = 0
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

        for u in reversed(order):
            largest = 0

            for v in graph[u]:
                if parent[v] != u:
                    continue

                size[u] += size[v]

                if size[v] > largest:
                    largest = size[v]
                    heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0

        stack = [(0, 0)]

        while stack:
            u, chain_head = stack.pop()

            while u != -1:
                head[u] = chain_head
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        base = 1

        while base < n:
            base *= 2

        seg = [0] * (2 * base)

        def char_mask(ch):
            return 1 << (ord(ch) - ord('a'))

        for u in range(n):
            seg[base + pos[u]] = char_mask(chars[u])

        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(index, value):
            index += base
            seg[index] = value

            index //= 2

            while index:
                seg[index] = seg[2 * index] ^ seg[2 * index + 1]
                index //= 2

        def range_xor(left, right):
            left += base
            right += base

            result = 0

            while left <= right:
                if left % 2 == 1:
                    result ^= seg[left]
                    left += 1

                if right % 2 == 0:
                    result ^= seg[right]
                    right -= 1

                left //= 2
                right //= 2

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:

                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])

                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])

            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                ch = parts[2]

                chars[u] = ch
                update(pos[u], char_mask(ch))

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                answer.append(
                    mask == 0 or (mask & (mask - 1)) == 0
                )

        return answer