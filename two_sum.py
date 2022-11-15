nums = [2,7,11,15]
target = 9


class GetSumOfTwoNos:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def calc(self):
        for i in self.nums:
            f = target - i
            if f in nums:
                print(f, i)
                break


obj = GetSumOfTwoNos(nums, target)
obj.calc()
