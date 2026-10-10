def my_zip(L, R):
    for i in range(min(len(L), len(R))):
        yield L[i], R[i]


# ==============================================================================
s = 'abcd'
t = (10, 20, 30, 40, 50)
g = my_zip(s, t)
print(g)
for a, b in g:
    print((a, b))
