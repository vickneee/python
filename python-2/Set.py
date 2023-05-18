Lista = [1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 4, 1, 1]
print(Lista)

l1 = len(Lista)
x = set(Lista)
print(x)

Lista = x
l2 = len(Lista)
print(Lista)
print("Listassa oli", l1-l2, "dublikaatteja")

s = {1, 2, 3, 4, 1, 1, 1, 1, 1}
print(s)
