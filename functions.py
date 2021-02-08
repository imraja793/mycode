def function_check(*args):
    # one, two, three = args
    # print(one, two, three)
    print(args, "how this is possible")
    print(f"{args}args")

function_check("firt", "second", "third", ["jnd", "dmdk", "dmlddlm"], {"dkdk": "dlkdmlmd"})

def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
