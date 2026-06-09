class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)
        

    def findMedian(self) -> float:
        sorted_array = []
        i = 0
        temp_heap = self.maxHeap.copy()  
        sorted_array = []

        while temp_heap:
            sorted_array.append(-heapq.heappop(temp_heap))

        n = len(sorted_array)

        if n == 0:
            return None
        elif n == 1:
            return sorted_array[0]
        elif n % 2 == 0:
            return (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2
        else:
            return sorted_array[n // 2]


        
        