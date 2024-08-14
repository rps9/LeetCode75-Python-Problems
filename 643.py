class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Keep a running sum so you only have to do two operations each iteration instead of k operation for sum
        average = float('-inf')
        running_sum = sum(nums[0:k])
        window_size = len(nums) - k + 1

        # Slide the window through the array keeping track of the sum
        for i in range(window_size):
            average = max(running_sum / k, average)
            if i != window_size-1:
                running_sum = running_sum - nums[i] + nums[i+k]

        return average
