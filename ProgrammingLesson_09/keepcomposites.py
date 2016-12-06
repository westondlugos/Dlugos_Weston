nums = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]


def gFactor(nums):
    for i in range(2,nums):
        if nums % i == 0:
            return 1
    return 0


def removePrimes():
    for i in nums:
        if gFactor(i) == 0:
            nums.remove(i)

removePrimes()

print(nums)
            
