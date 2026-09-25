import json, os
from .core import *

N=5
F_LINEAR=(4,)
F_QUAD=((2,3),(1,4),(1,5))
G_LINEAR=(4,)
G_QUAD=((1,2),(2,3),(1,4),(1,5))

def main():
    f=truth_from_anf(N, linear=F_LINEAR, quadratic=F_QUAD)
    g=truth_from_anf(N, linear=G_LINEAR, quadratic=G_QUAD)
    pf=fingerprint(f,N,2)
    pg=fingerprint(g,N,2)
    assert pf==pg, "Frozen witness no longer collides."
    df=graph_degree_sequence(N,F_QUAD)
    dg=graph_degree_sequence(N,G_QUAD)
    assert df!=dg, "Quadratic interaction degree sequences unexpectedly agree."
    result={
      "n":N,
      "f_anf":"x2*x3 XOR x4 XOR x1*x4 XOR x1*x5",
      "g_anf":"x1*x2 XOR x2*x3 XOR x4 XOR x1*x4 XOR x1*x5",
      "fingerprint_equal": True,
      "weight": pf[0],
      "deterministic_depth": pf[1],
      "C0_profile": list(pf[2]),
      "C1_profile": list(pf[3]),
      "sensitivity_profile": list(pf[4]),
      "influence_profile": list(pf[5]),
      "degree": pf[6],
      "fourier_level_energy": list(pf[7]),
      "f_interaction_degree_sequence": list(df),
      "g_interaction_degree_sequence": list(dg),
      "pn_inequivalent_certificate":"quadratic interaction graphs have different degree sequences"
    }
    os.makedirs("artifacts",exist_ok=True)
    with open("artifacts/witness.json","w") as h:
        json.dump(result,h,indent=2)
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
