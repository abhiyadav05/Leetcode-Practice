class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])
        q = len(queries)
        timeIndex = sorted([(queries[i], i) for i in range(q)])
        mp = {}
        result = [0] * q
        i = 0
        j = 0
        m = len(logs)
        for curtime, ind in timeIndex:
            start = curtime - x
            end = curtime
            while j < m and logs[j][1] <= end:
                server = logs[j][0]
                mp[server] = mp.get(server, 0) + 1
                j += 1
            while i < m and logs[i][1] < start:
                server = logs[i][0]
                mp[server] -= 1

                if mp[server] == 0:
                    del mp[server]

                i += 1
            result[ind] = n - len(mp)

        return result