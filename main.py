def generator():
    for i in [1, 25, 333, 1018]:
        yield i


iterrator = generator().__iter__()
for i in range(1, 5):
    print(iterrator.__next__())
print(iter([1, 25, 333, 1018]))
