class Fact:

    def calc(self, num):
        n = 1
        for i in range(2, num+1):
            n *= i

        print(n)


obj = Fact()
obj.calc(5)
