from __future__ import annotations
import argparse,csv,itertools,json,os
from collections import defaultdict
from .core import *

def all_degree_le2_functions(n):
    linear_terms=list(range(1,n+1))
    quad_terms=list(itertools.combinations(range(1,n+1),2))
    monomials=[("c",None)]+[("l",i) for i in linear_terms]+[("q",e) for e in quad_terms]
    for mask in range(1<<len(monomials)):
        c=mask&1; linear=[]; quadratic=[]
        for k,(kind,obj) in enumerate(monomials[1:],start=1):
            if (mask>>k)&1:
                (linear if kind=="l" else quadratic).append(obj)
        degree=2 if quadratic else (1 if linear else 0)
        tt=truth_from_anf(n,c,tuple(linear),tuple(quadratic))
        yield mask,c,tuple(linear),tuple(quadratic),degree,tt

def tt_int(tt):
    return sum((int(v)&1)<<i for i,v in enumerate(tt))

def input_maps(n):
    xs=inputs(n); idx={x:i for i,x in enumerate(xs)}
    out=[]
    for perm in itertools.permutations(range(n)):
        for flips in itertools.product((0,1),repeat=n):
            out.append(tuple(idx[tuple(x[perm[j]]^flips[j] for j in range(n))] for x in xs))
    return out

def transform_code(code,mapping):
    out=0
    for dst,src in enumerate(mapping):
        out |= ((code>>src)&1)<<dst
    return out

def pn_map_for_family(codes,n):
    maps=input_maps(n); family=set(codes); canon={}; reps=[]
    for code in sorted(family):
        if code in canon: continue
        orbit={transform_code(code,m) for m in maps}
        assert orbit <= family
        rep=min(orbit); reps.append(rep)
        for x in orbit: canon[x]=rep
    assert len(canon)==len(family)
    return canon,reps

def cheap_key(tt,n,degree):
    return (weight(tt),sensitivity_profile(tt,n),influence_profile(tt,n),degree,fourier_level_energy(tt,n))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--n",type=int,default=5); args=ap.parse_args()
    n=args.n
    if n!=5: raise SystemExit("Frozen exhaustive degree<=2 workflow currently supports n=5.")
    records=list(all_degree_le2_functions(n))
    by_code={tt_int(r[-1]):r for r in records}
    canon,pn_reps=pn_map_for_family(by_code,n)

    # Progressive hashing: expensive D/certificates are evaluated only inside cheap collisions.
    cheap=defaultdict(list)
    for r in records: cheap[cheap_key(r[-1],n,r[4])].append(r)

    rich_groups=defaultdict(list)
    expensive_evaluations=0
    for group in cheap.values():
        if len(group)<2: continue
        for r in group:
            fp=fingerprint(r[-1],n,r[4]); expensive_evaluations+=1
            rich_groups[fp].append(r)

    survivors=[]
    for fp,group in rich_groups.items():
        classes=defaultdict(list)
        for r in group: classes[canon[tt_int(r[-1])]].append(r)
        if len(classes)>1:
            survivors.append({
              "fingerprint_bucket_size":len(group),
              "pn_class_count":len(classes),
              "representatives":[{
                "truth_table_hex":hex(rep),
                "mask":members[0][0],
                "constant":members[0][1],
                "linear":list(members[0][2]),
                "quadratic":[list(e) for e in members[0][3]],
                "interaction_degree_sequence":list(graph_degree_sequence(n,members[0][3]))
              } for rep,members in sorted(classes.items())]
            })

    os.makedirs("artifacts",exist_ok=True)
    summary={
      "n":n,"degree_max":2,"functions_scanned":len(records),
      "pn_classes_in_family":len(pn_reps),
      "cheap_fingerprint_classes":len(cheap),
      "expensive_fingerprint_evaluations":expensive_evaluations,
      "rich_cross_pn_collision_groups":len(survivors)
    }
    with open("artifacts/quadratic_search_summary.json","w") as h: json.dump(summary,h,indent=2)
    with open("artifacts/quadratic_collision_groups.json","w") as h: json.dump(survivors,h,indent=2)
    with open("artifacts/quadratic_collision_groups.csv","w",newline="") as h:
        w=csv.writer(h); w.writerow(["group","pn_class_count","truth_table_hex","linear","quadratic","interaction_degree_sequence"])
        for gi,g in enumerate(survivors):
            for r in g["representatives"]:
                w.writerow([gi,g["pn_class_count"],r["truth_table_hex"],r["linear"],r["quadratic"],r["interaction_degree_sequence"]])
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
