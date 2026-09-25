from __future__ import annotations
import json, os
from collections import defaultdict
from .core import fingerprint
from .exhaustive_quadratic_search import canonical_pn_truth

def truth_table_from_int(code,n):
    # inputs() is lexicographic; bit i corresponds to the i-th lexicographic input.
    return tuple((code >> i) & 1 for i in range(1 << n))

def algebraic_degree(tt,n):
    a=list(tt)
    N=1<<n
    # Möbius transform on the Boolean cube; index convention is immaterial for degree.
    for j in range(n):
        step=1<<j
        for mask in range(N):
            if mask & step:
                a[mask] ^= a[mask ^ step]
    return max((mask.bit_count() for mask,v in enumerate(a) if v), default=0)

def audit_dimension(n):
    by_fp={}
    pn_reps=set()
    collisions=[]
    for code in range(1 << (1 << n)):
        tt=truth_table_from_int(code,n)
        deg=algebraic_degree(tt,n)
        fp=fingerprint(tt,n,deg)
        canon=canonical_pn_truth(tt,n)
        pn_reps.add(canon)
        old=by_fp.get(fp)
        if old is None:
            by_fp[fp]=canon
        elif old != canon:
            collisions.append((code,old,canon))
            # A single collision is enough to refute completeness, but retain scan.
    return {
        "n":n,
        "functions":1 << (1 << n),
        "phi_classes":len(by_fp),
        "pn_classes":len(pn_reps),
        "cross_pn_phi_collisions":len(collisions),
        "phi_complete_for_pn":len(collisions)==0 and len(by_fp)==len(pn_reps),
    }

def main():
    rows=[audit_dimension(n) for n in (1,2,3,4)]
    assert all(r["phi_complete_for_pn"] for r in rows), rows
    os.makedirs("artifacts",exist_ok=True)
    with open("artifacts/small_dimension_audit.json","w") as h:
        json.dump({"equivalence":"PN: input permutation + independent input complementation; no output complement","dimensions":rows},h,indent=2)
    print(json.dumps(rows,indent=2))

if __name__=="__main__":
    main()
