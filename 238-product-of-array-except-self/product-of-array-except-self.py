class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_products = [1] * length  # Product of elements to the left of nums[i]
        right_products = [1] * length  # Product of elements to the right of nums[i]
        answer = [1] * length

        # Fill left_products
        for i in range(1, length):
            left_products[i] = nums[i - 1] * left_products[i - 1]

        # Fill right_products
        for i in range(length - 2, -1, -1):
            right_products[i] = nums[i + 1] * right_products[i + 1]

        # Calculate the answer by multiplying left and right products
        for i in range(length):
            answer[i] = left_products[i] * right_products[i]

        return answer