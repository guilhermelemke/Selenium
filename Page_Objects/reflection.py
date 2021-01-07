class A:
    my_attr = 7

print(dir(A)[-1])
print(getattr(A, 'my_attr'))