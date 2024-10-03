from typing import List

def canArrange(arr: List[int], k: int) -> bool:
    arra = arr.copy()
    res = []
    for a in arra:
        for b in [x for x in arra if x != a]:
            if (a+b) % k == 0 and (b, a) not in res:
                res.append((a,b))
    final = []
    seen = []
    for p in res:
        if p[0] in seen:
            continue
        elif p[1] in seen:
            continue
        else:
            seen.append(p[0])
            seen.append(p[1])
            final.append(p)
    print(seen)
    print(final)

canArrange([1,2,3,4,5,10,6,7,8,9], 5)