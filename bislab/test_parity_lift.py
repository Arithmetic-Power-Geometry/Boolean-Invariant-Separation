from __future__ import annotations
import argparse,json,os
from .core import *

F_LINEAR=(4,)
F_QUAD=((2,3),(1,4),(1,5))
G_LINEAR=(4,)
G_QUAD=((1,2),(2,3),(1,4),(1,5))

def parity_extension(linear,m,offset=5):
    return tuple(linear)+tuple(range(offset+1,offset+m+1))

def check(m):
    n=5+m
    fl=parity_extension(F_LINEAR,m)
    gl=parity_extension(G_LINEAR,m)
    f=truth_from_anf(n,linear=fl,quadratic=F_QUAD)
    g=truth_from_anf(n,linear=gl,quadratic=G_QUAD)
    pf=fingerprint(f,n,2); pg=fingerprint(g,n,2)
    return {
      "m":m,"n":n,"fingerprint_equal":pf==pg,
      "weight":pf[0],"D":pf[1],
      "C0_profile_equal":pf[2]==pg[2],
      "C1_profile_equal":pf[3]==pg[3],
      "sensitivity_equal":pf[4]==pg[4],
      "influence_equal":pf[5]==pg[5],
      "degree_equal":pf[6]==pg[6],
      "fourier_level_energy_equal":pf[7]==pg[7],
      "f_graph_degree_sequence":list(graph_degree_sequence(n,F_QUAD)),
      "g_graph_degree_sequence":list(graph_degree_sequence(n,G_QUAD)),
      "pn_inequivalent_graph_certificate":graph_degree_sequence(n,F_QUAD)!=graph_degree_sequence(n,G_QUAD)
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--max-m",type=int,default=2); args=ap.parse_args()
    # Exact D/certificate computation grows exponentially; m<=2 is a regression test,
    # while arbitrary-m closure is a theorem target, not inferred from computation.
    rows=[check(m) for m in range(args.max_m+1)]
    assert all(r["fingerprint_equal"] and r["pn_inequivalent_graph_certificate"] for r in rows), rows
    os.makedirs("artifacts",exist_ok=True)
    with open("artifacts/parity_lift_checks.json","w") as h: json.dump(rows,h,indent=2)
    print(json.dumps(rows,indent=2))

if __name__=="__main__": main()
