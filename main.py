def generator():
    for _ in [34, 234, 102]:
        yield

gen_iterator = generator().__iter__()
for _ in range(1, 4):
    print(gen_iterator.__next__())

print(type(gen_iterator))
print(iter([34, 234, 102]))