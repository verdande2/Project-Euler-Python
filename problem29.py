unique = []
for a in range(2,101):
    for b in range(2,101):
        if not a**b in unique:
            unique.append(a**b)
print(str(len(unique)))
