import heapq as hp
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        adj=[[] for _ in range(n)]

        for ele in edges:
            u=ele[0]
            v=ele[1]
            l=ele[2]
            adj[u].append((v,l))
            adj[v].append((u,l))
        
        pq=[]
        dist=[float('inf')]*n
        dist[0]=0
        hp.heappush(pq,(0,0))
        ans=[-1]*n
        while pq:
            time,u=hp.heappop(pq)
            if(time>dist[u]):
                continue
            for ele in adj[u]:
                v=ele[0]
                t=ele[1]
                newDist=time+t
                if(dist[v]>newDist and newDist<disappear[v]):
                    dist[v]=newDist
                    ans[v]=newDist
                    hp.heappush(pq,(newDist,v))
        
        ans[0]=0
        return ans


        