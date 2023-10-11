import itertools
import time
start = time.time()


lexicographic_permutation_list = []
for i in itertools.permutations("0123456789"):
    permutation = "".join(i)
    permutation_int = int(permutation)
    lexicographic_permutation_list.append(permutation_int)

lexicographic_permutation_list.sort()
        
print(str(lexicographic_permutation_list[999999]))
print("Time taken(secs):", time.time() - start)
