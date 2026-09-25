from __future__ import annotations
import argparse,csv,itertools,json,os
from collections import defaultdict
from .core import *

def all_degree_le2_functions(n):
    linear_terms=list(range(1,n+1))
    quad_terms=list(itertools.combinations(range(1,n+1),2))
    monomials=[("c",None)]+[("l",i) for i in linear_terms]+[("q",e) for e in quad_terms]
    for mask in range(1<<len(monomials)):
        c=(mask&1)
        linear=[]
        quadratic=[]
        for k,(kind,obj) in enumerate(monomials[1:],start=1):
            if (mask>>k)&1:
                if kind=="l": linear.append(obj)
                else: quadratic.append(obj)
        degree=2 if quadratic else (1 if linear else 0)
        yield mask,c,tuple(linear),tuple(quadratic),degree

def cheap_key(tt,n,degree):
    return (weight(tt),sensitivity_profile(tt,n),influence_profile(tt,n),degree,fourier_level_energy(tt,n))

def canonical_pn_truth(tt,n):
    xs=inputs(n)
    idx={x:i for i,x in enumerate(xs)}
    best=None
    for perm in itertools.permutations(range(n)):
        for flips in itertools.product((0,1), repeat=n):
            transformed=[]
            for x in xs:
                y=tuple(x[perm[j]]^flips[j] for j in range(n))
                transformed.append(tt[idx[y]])
            t=tuple(transformed)
            if best is None or t<best: best=t
    return best

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--n",type=int,default=5)
    args=ap.parse_args()
    n=args.n
    if n!=5:
        raise SystemExit("This exhaustive degree<=2 workflow is currently frozen for n=5.")
    buckets=defaultdict(list)
    count=0
    for mask,c,lin,quad,deg in all_degree_le2_functions(n):
        tt=truth_from_anf(n,c,lin,quad)
        buckets[cheap_key(tt,n,deg)].append((mask,c,lin,quad,deg,tt))
        count+=1
    survivors=[]
    for key,items in buckets.items():
        if len(items)<2: continue
        rich=defaultdict(list)
        for rec in items:
            mask,c,lin,quad,deg,tt=rec
            rich[fingerprint(tt,n,deg)].append(rec)
        for fp,group in rich.items():
            if len(group)<2: continue
            pn=defaultdict(list)
            for rec in group:
                pn[canonical_pn_truth(rec[-1],n)].append(rec)
            if len(pn)>1:
                survivors.append({
                    "fingerprint_bucket_size":len(group),
                    "pn_class_count":len(pn),
                    "representatives":[{
                        "mask":rec[0],
                        "constant":rec[1],
                        "linear":list(rec[2]),
                        "quadratic":[list(e) for e in rec[3]],
                        "degree":rec[4]
                    } for rec in [v[0] for v in pn.values()]]
                })
    os.makedirs("artifacts",exist_ok=True)
    summary={"n":n,"degree_max":2,"functions_scanned":count,"collision_groups":len(survivors)}
    with open("artifacts/quadratic_search_summary.json","w") as h:
        json.dump(summary,h,indent=2)
    with open("artifacts/quadratic_collision_groups.json","w") as h:
        json.dump(survivors,h,indent=2)
    with open("artifacts/quadratic_collision_groups.csv","w",newline="") as h:
        w=csv.writer(h); w.writerow(["group","pn_class_count","representative_mask","linear","quadratic"])
        for gi,g in enumerate(survivors):
            for r in g["representatives"]:
                w.writerow([gi,g["pn_class_count"],r["mask"],r["linear"],r["quadratic"]])
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
