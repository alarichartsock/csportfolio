def reverse(i):
    n = str(i)
    r = ""
    for i in range(len(n)):
        new = n[len(n)-i-1]
        r = r + new
    return int(r)

print(reverse(124567))