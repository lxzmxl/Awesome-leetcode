# [Next Permutation][title]

## Description

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

**Example 1:**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 2:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Tags:** Arrays, Sort


## 思路

我们可以这样想这个问题，假设把list里面的元素合到一起，组成一个数字，那么这道题相当于是说，求这些元素组成的数字比当前数字
下一个更大的排列；如果已经是最大的，那么只需要将list反转即可。

所以我们可以这样实现，首先，判断是否是最大，如果list元素从大到小排列，则此时list元素组成的数字最大，则将list元素反转即可。

如果不是这样，因为要找下一个更大的而不是最大的，那么就需要从个位遍历，即我们从右向左查找，找到第一个并它右边一个元素小的数字，
标记这个元素，并将这个元素之后的按照从小到大的顺序排列，顺序遍历之后的排列，将第一个比这个元素大的数字和这个元素互换，这样一来
就组成了下一个更大的排列。

```python
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
              
```


[title]: https://leetcode-cn.com/problems/next-permutation/

