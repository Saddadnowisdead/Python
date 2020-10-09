d = {'Books': 11, 'Toys': 2, 'Discs': 43, 'Boats': 1, 'Knifes': 75}

print("Unsorted:")
for i in d: print(i, d[i])
print('\n')
di = sorted(d.values())
print("Sorted:")
for i in range(len(d)): print(di[i])



