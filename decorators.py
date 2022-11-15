def make_new(obj):
    print(obj)
    def make_inner_new():
        print("here is the decorator function")
        obj()
    return make_inner_new


def decorate():
    print("decorate me")


a = make_new(decorate)
a()

@make_new
def check_decorate():
    print("decorator works")
    return True

check_decorate()
