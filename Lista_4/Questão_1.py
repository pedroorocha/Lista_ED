listas = [
    [12,42,83,25,67,71,3,4,94,53],
    [100,48,19,61,86,33,13,43,84,28],
    [81,60,6,49,40,41,38,64,44,36],
    [45,27,11,89,63,39,9,58,52,17],
    [88,77,26,62,30,96,56,65,98,99],
    [76,73,16,95,35,87,68,69,51,92],
    [37,75,90,82,8,18,23,93,57,10],
    [15,97,14,29,7,24,31,59,78,85],
    [5,70,55,91,47,72,2,20,34,74],
    [50,66,32,22,54,79,21,1,80,46]
]

def insertion_sort(v):
    testes = trocas = 0
    for i in range(1, len(v)):
        key = v[i]
        j = i - 1
        while j >= 0:
            testes += 1
            if v[j] > key:
                v[j+1] = v[j]
                trocas += 1
                j -= 1
            else:
                break
        v[j+1] = key
    return testes, trocas

def selection_sort(v):
    testes = trocas = 0
    n = len(v)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            testes += 1
            if v[j] < v[min_i]:
                min_i = j
        if min_i != i:
            v[i], v[min_i] = v[min_i], v[i]
            trocas += 1
    return testes, trocas

def bubble_sort(v):
    testes = trocas = 0
    n = len(v)
    for i in range(n):
        for j in range(0, n-i-1):
            testes += 1
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                trocas += 1
    return testes, trocas

def shell_sort(v):
    testes = trocas = 0
    n = len(v)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = v[i]
            j = i
            while j >= gap:
                testes += 1
                if v[j-gap] > temp:
                    v[j] = v[j-gap]
                    trocas += 1
                    j -= gap
                else:
                    break
            v[j] = temp
        gap //= 2
    return testes, trocas

def merge_sort(v):
    testes = trocas = 0
    def merge(esq, dir):
        nonlocal testes, trocas
        res = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            testes += 1
            if esq[i] <= dir[j]:
                res.append(esq[i]); i += 1
            else:
                res.append(dir[j]); j += 1
            trocas += 1
        res.extend(esq[i:]); res.extend(dir[j:])
        return res
    def sort(lst):
        if len(lst) <= 1:
            return lst
        m = len(lst)//2
        return merge(sort(lst[:m]), sort(lst[m:]))
    v[:] = sort(v)
    return testes, trocas

def quick_sort(v):
    testes = trocas = 0
    def qs(l, r):
        nonlocal testes, trocas
        if l < r:
            p = v[r]
            i = l
            for j in range(l, r):
                testes += 1
                if v[j] <= p:
                    v[i], v[j] = v[j], v[i]
                    trocas += 1
                    i += 1
            v[i], v[r] = v[r], v[i]
            trocas += 1
            qs(l, i-1)
            qs(i+1, r)
    qs(0, len(v)-1)
    return testes, trocas

def heap_sort(v):
    testes = trocas = 0
    def heapify(n, i):
        nonlocal testes, trocas
        maior = i
        l = 2*i+1
        r = 2*i+2
        if l < n:
            testes += 1
            if v[l] > v[maior]: maior = l
        if r < n:
            testes += 1
            if v[r] > v[maior]: maior = r
        if maior != i:
            v[i], v[maior] = v[maior], v[i]
            trocas += 1
            heapify(n, maior)
    n = len(v)
    for i in range(n//2-1, -1, -1): heapify(n, i)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        trocas += 1
        heapify(i, 0)
    return testes, trocas

def counting_sort(v):
    testes = trocas = 0
    max_v = max(v)
    count = [0]*(max_v+1)
    for x in v:
        count[x] += 1
    i = 0
    for val in range(len(count)):
        while count[val] > 0:
            v[i] = val
            trocas += 1
            count[val] -= 1
            i += 1
    return testes, trocas

algoritmos = [
    ("Insertion", insertion_sort),
    ("Selection", selection_sort),
    ("Bubble", bubble_sort),
    ("Shell", shell_sort),
    ("Merge", merge_sort),
    ("Quick", quick_sort),
    ("Heap", heap_sort),
    ("Counting", counting_sort)
]

for nome, alg in algoritmos:
    print(f"\n{nome} Sort")
    for lista in listas:
        v = lista.copy()
        t, tr = alg(v)
        print(f"Testes={t:4d} | Trocas={tr:4d}")
