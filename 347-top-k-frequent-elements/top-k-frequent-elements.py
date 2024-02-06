class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # Create a min heap to maintain the k most frequent elements
        heap = []

        for num, freq in count.items():
            # Push the element and its frequency into the heap
            heapq.heappush(heap, (freq, num))

            # If the heap size exceeds k, remove the least frequent element
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the k most frequent elements from the heap
        result = [elem[1] for elem in heap]

        return result