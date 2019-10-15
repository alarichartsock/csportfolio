import time

def time_decorator(fn):
    
    def foo(n):
        start = time.time()
        x = fn(n)
        end = time.time()
        return x, end-start
    return foo

@time_decorator
def sum_squares(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            sum += i * j;
    return sum

for i in range(5):
    x,y = sum_squares(100)
    print(f"Sum us {x} required {y:07} seconds")

def hum(x):
    if x < 0:
        raise Exception
        return
    else:
        return x*x

print(hum(-1))