import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n=len(moveTime)
        m=len(moveTime[0])
        dir=[(0,1),(1,0),(-1,0),(0,-1)]

        pq=[]
        heapq.heappush(pq,(0,0,0,0))
        dist=[[[float('inf')]*2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0]=0
        while pq:
            tp=heapq.heappop(pq)
            d=tp[0]
            l=tp[1]
            r=tp[2]
            c=tp[3]
            # if(d!=dist[r][c][l]): continue
            if(r==n-1 and c==m-1):
                return d
            for ele in dir:
                nr=r+ele[0]
                nc=c+ele[1]
                if(nr>=0 and nr<n and nc>=0 and nc<m):
                    move=2
                    if(l%2==0):
                        move=1
                        
                    st=max(d,moveTime[nr][nc])
                    nd=st+move
                    nl=1-l
                    if(nd<dist[nr][nc][nl]):
                        dist[nr][nc][nl]=nd
                        heapq.heappush(pq,(nd,nl,nr,nc))
        
        return 0





        