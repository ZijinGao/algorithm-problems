from collections import defaultdict
def permutation(permutations): # [[4,2,1],[4,2,3],[2,1,3],[4,1,3]]
    n = len(permutations)
    mapping = defaultdict(set)
    for p in permutations:
        curr_set = set([p[-1]])
        for i in range( len(permutations[0]) - 2, -1, -1 ):
            mapping[p[i]].update(curr_set)
            curr_set.add(p[i])
    for i in range(1, n+1):
        if i not in mapping:
            mapping[i] = set()

    inter = []
    for num, after_list in mapping.items():
        t = (len(after_list), num)
        inter.append(t)
    
    inter.sort(reverse=True)
    original = [str(i[1]) for i in inter]
    print(" ".join(original))

test_count = int(input())
for i in range(test_count):
    list_count = int(input())
    permutations = []
    for l in range(list_count):
        permutations.append(list(map(int, input().split())))
    permutation(permutations)