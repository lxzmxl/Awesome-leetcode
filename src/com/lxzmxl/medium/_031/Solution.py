package com.lxzmxl.medium._031;

/**
 * <pre>
 *     author: lxzmxl

 *     time  : 2019/04/01
 *     desc  :
 * </pre>
 */
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums
        if sorted(temp,reverse=True) == nums:
            nums.reverse()
        else:
            for i in range(len(nums)-1,0,-1):
                if nums[i]>nums[i-1]:
                    nums[i:len(nums)]=sorted(nums[i:len(nums)])
                    for j in range(i,len(nums)):
                        if nums[j]>nums[i-1]:
                            temp_v = nums[j]
                            nums[j]=nums[i-1]
                            nums[i-1]=temp_v
                            return


