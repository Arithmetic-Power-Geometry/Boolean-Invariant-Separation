from __future__ import annotations
import itertools, json, os
from .core import fingerprint, inputs

def truth_table_from_int(code,n):
    return tuple((code >> i) & 1 for i in range(1 << n))

def truth_int(tt):
    return sum((int(v)&1)<<i for i,v in enumerate(tt))

def algebraic_degree(tt,n):
    a=list(tt); N=1<<n
    for j in range(n):
        step=1<<j
        for mask in range(N):
            if mask & step:
                a[mask] ^= a[mask ^ step]
    return max((mask.bit_count() for mask,v in enumerate(a) if v), default=0)

def pn_input_maps(n):
    xs=inputs(n)
    idx={x:i for i,x in enumerate(xs)}
    maps=[]
    for perm in itertools.permutations(range(n)):
        for flips in itertools.product((0,1),repeat=n):
            maps.append(tuple(idx[tuple(x[perm[j]]^flips[j] for j in range(n))] for x in xs))
    return maps

def transform_code(code,mapping):
    out=0
    for dst,src in enumerate(mapping):
        out |= ((code>>src)&1)<<dst
    return out

def pn_class_map(n):
    maps=pn_input_maps(n)
    total=1 << (1 << n)
    canon=[-1]*total
    representatives=[]
    for code in range(total):
        if canon[code] != -1:
            continue
        orbit={transform_code(code,m) for m in maps}
        rep=min(orbit)
        representatives.append(rep)
        for member in orbit:
            canon[member]=rep
    assert all(x>=0 for x in canon)
    return canon, representatives

def audit_dimension(n):
    canon,reps=pn_class_map(n)
    by_fp={}
    collision_pairs=set()
    total=1 << (1 << n)
    for code in range(total):
        tt=truth_table_from_int(code,n)
        fp=fingerprint(tt,n,algebraic_degree(tt,n))
        rep=canon[code]
        old=by_fp.get(fp)
        if old is None:
            by_fp[fp]=rep
        elif old != rep:
            collision_pairs.add(tuple(sorted((old,rep))))
    return {
        "n":n,
        "functions":total,
        "phi_classes":len(by_fp),
        "pn_classes":len(reps),
        "cross_pn_phi_collision_pairs":len(collision_pairs),
        "phi_complete_for_pn":not collision_pairs and len(by_fp)==len(reps),
    }

def main():
    rows=[audit_dimension(n) for n in (1,2,3,4)]
    assert all(r["phi_complete_for_pn"] for r in rows), rows
    os.makedirs("artifacts",exist_ok=True)
    payload={
      "equivalence":"PN: input permutation + independent input complementation; no output complement",
      "dimensions":rows
    }
    with open("artifacts/small_dimension_audit.json","w") as h:
        json.dump(payload,h,indent=2)
    print(json.dumps(payload,indent=2))

if __name__=="__main__":
    main()
