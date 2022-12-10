class DetectSquares(object):

    def __init__(self):
        self.points = []
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.points.append((point[0], point[1]))

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        n = len(self.points)
        count = 0
        counter = Counter(self.points)
        for i in range(n):
            if self.points[i][0] == point[0]:
                length = abs(self.points[i][1] - point[1])
                if length == 0:
                    continue
                if counter[(point[0] - length, point[1])] and counter[(point[0] - length, self.points[i][1])]:
                    count += counter[(point[0] - length, point[1])] * counter[(point[0] - length, self.points[i][1])]
                if counter[(point[0] + length, point[1])] and counter[(point[0] + length, self.points[i][1])]:
                    count += counter[(point[0] + length, point[1])] * counter[(point[0] + length, self.points[i][1])]
                    
        return count

