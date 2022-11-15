def function_check(*args):
    # one, two, three = args
    # print(one, two, three)
    print(args, "how this is possible")
    print(f"{args}args")

function_check("firt", "second", "third", ["jnd", "dmdk", "dmlddlm"], {"dkdk": "dlkdmlmd"})

def intro(**data):
    """
        **kwargs stands for keyword arguments. The only difference from args is that
        it uses keywords and returns the values in the form of a dictionary


        like **kwargs returns {Firstname="Sita"} it consists of keyword
        {'Firstname': 'John', 'Lastname': 'Wood', 'Email': 'johnwood@nomail.com',
         'Country': 'Wakanda', 'Age': 25, 'Phone': 9876543210}

        whereas *args will return only values check function_check() function output
        ('firt', 'second', 'third', ['jnd', 'dmdk', 'dmlddlm'], {'dkdk': 'dlkdmlmd'})
    """
    print("\nData type of argument:", data)

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


