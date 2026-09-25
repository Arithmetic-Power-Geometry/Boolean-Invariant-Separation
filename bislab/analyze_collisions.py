from __future__ import annotations
import argparse, itertools, json, os
from collections import Counter, defaultdict
from .core import graph_degree_sequence

def edges(n):
    return list(itertools.combinations(range(1,n+1),2))

def graph_signature(n,quad):
    E={tuple(sorted(e)) for e in quad}
    deg=[0]*n
    nbr=[set() for _ in range(n)]
    for a,b in E:
        deg[a-1]+=1; deg[b-1]+=1
        nbr[a-1].add(b-1); nbr[b-1].add(a-1)
    triangles=0
    for a,b,c in itertools.combinations(range(n),3):
        if b in nbr[a] and c in nbr[a] and c in nbr[b]: triangles+=1
    components=[]
    seen=set()
    for v in range(n):
        if v in seen: continue
        stack=[v]; seen.add(v); size=0
        while stack:
            u=stack.pop(); size+=1
            for w in nbr[u]:
                if w not in seen: seen.add(w); stack.append(w)
        components.append(size)
    return {
      "edges":len(E),
      "degree_sequence":list(sorted(deg)),
      "components":sorted(components),
      "triangles":triangles,
    }

def edge_symmetric_difference(a,b):
    A={tuple(sorted(x)) for x in a}; B={tuple(sorted(x)) for x in b}
    return len(A^B)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="artifacts/quadratic_collision_groups.json")
    args=ap.parse_args()
    with open(args.input) as h: groups=json.load(h)
    analyses=[]
    hist=Counter()
    for gi,g in enumerate(groups):
        reps=g["representatives"]
        annotated=[]
        for r in reps:
            sig=graph_signature(5,r["quadratic"])
            annotated.append({**r,"graph_signature":sig})
        pairwise=[]
        for i,j in itertools.combinations(range(len(annotated)),2):
            d=edge_symmetric_difference(annotated[i]["quadratic"],annotated[j]["quadratic"])
            key=(tuple(annotated[i]["graph_signature"]["degree_sequence"]),
                 tuple(annotated[j]["graph_signature"]["degree_sequence"]),d)
            hist[str(key)]+=1
            pairwise.append({"i":i,"j":j,"quadratic_edge_symmetric_difference":d})
        analyses.append({"group":gi,"pn_class_count":g["pn_class_count"],"representatives":annotated,"pairwise":pairwise})
    payload={
      "collision_group_count":len(groups),
      "pair_pattern_histogram":dict(hist),
      "groups":analyses
    }
    os.makedirs("artifacts",exist_ok=True)
    with open("artifacts/collision_structure_analysis.json","w") as h: json.dump(payload,h,indent=2)
    print(json.dumps({"collision_group_count":len(groups),"pair_pattern_histogram":dict(hist)},indent=2))

if __name__=="__main__": main()
