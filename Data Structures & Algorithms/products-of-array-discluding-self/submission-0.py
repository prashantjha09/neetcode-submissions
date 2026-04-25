class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        sufix_product = [1]
        for i in range(len(nums)):
            prefix_product.append(prefix_product[i]*nums[i])


        for i in reversed(range(len(nums))):
            index = len(nums)-(1+i)

            sufix_product.append(sufix_product[index] * nums[i])
        sufix_product =list(reversed(sufix_product))
        return [prefix_product[i]*sufix_product[i+1] for i in range(len(nums))]

        