nums = [18 ,25,-5,8,27]
i = 0
while i<len(nums):
    j = i+1
    while j<len(nums) and nums[j]<=nums[i]:
        j+=1
    k = i
    while k<len(nums) and j<len(nums) and k<=j:
        nums[k] = nums[ j]
        k+=1
    i = j
print(nums)