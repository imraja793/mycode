def prefix_decorator(prefix):
    def decorator(main_func):
        def inner_func(*args, **kwargs):
            print(prefix, "our function works", main_func)
            return main_func(*args, **kwargs)
        return inner_func
    return decorator

@prefix_decorator('parameterized decorator')
def check_dec(a, b):
    print("checkdeck working", a,b)

check_dec(5, 10)





a = "kfmffkfoo"

x = [i for i in a.lower() if a.count(i) < 2]
print(x)

def fact(n):
    print(f"calculating for{n}")
    if n==0:
        return 1
    f = n*fact(n-1)
    print(f, n, "end result")
    return f

print(fact(5))

