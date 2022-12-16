class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):    
            dist.append([sqrt(points[i][0] ** 2 + points[i][1] ** 2), points[i]]) #getting the  
        dist.sort()                        # √ of square numbers in points then appennding it
        out = []                           # sorting it to get the nearest pointt
        for i in range(k):        # appending answer then printing it
            out.append(dist[i][1])
        return out

