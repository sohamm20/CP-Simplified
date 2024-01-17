def generate(a):
    n = len(a)
    ans = list()
    for i in range(1 << n):
        curr = list()
        for j in range(n):
            if i & (1 << j) != 0:
                curr.append(a[j])
        ans.append(curr)
    return ans

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

subsets = generate(a)
for i in subsets:
    print(*i)
