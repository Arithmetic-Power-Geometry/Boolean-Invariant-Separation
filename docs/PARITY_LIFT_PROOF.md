# Parity-Lift Closure Theorem

## Definitions

Let f:{0,1}^n -> {0,1}. For m>=1 let P_m(z)=z_1 XOR ... XOR z_m and define

L_m(f)(x,z)=f(x) XOR P_m(z).

Let Phi be the frozen fingerprint consisting of weight, exact deterministic decision-tree depth, output-labelled pointwise certificate profiles, pointwise sensitivity profile, sorted individual influence profile, algebraic degree, and Fourier energy by level.

## Lemma 1 — pointwise certificates add under disjoint XOR

For Boolean A(x), B(z) on disjoint variables and every input (x,z),

C_{A XOR B}(x,z)=C_A(x)+C_B(z).

### Proof

Upper bound: take a minimum certificate S_A for A at x and a minimum certificate S_B for B at z. Fixing S_A union S_B fixes both factors and therefore their XOR. Hence C_{A XOR B}(x,z)<=C_A(x)+C_B(z).

Lower bound: let S be any certificate for A XOR B at (x,z), and split it into S_A and S_B according to the disjoint variable sets. If S_A does not certify A(x), there is x' consistent with S_A with A(x') != A(x). Keeping z fixed gives an input consistent with S on which A XOR B changes, contradiction. Thus S_A certifies A(x). Symmetrically S_B certifies B(z). Therefore |S|>=C_A(x)+C_B(z).

Equality follows.

For parity P_m, every input has certificate complexity m. Hence
C_{L_m(f)}(x,z)=C_f(x)+m.

Because P_m is balanced for m>=1, for each fixed x exactly 2^{m-1} choices of z yield each output value. Consequently each base certificate value C_f(x)+m appears 2^{m-1} times in each output-labelled certificate profile of L_m(f). Therefore equality of the two base C0/C1 profiles (indeed equality of their union is enough after a nonzero parity lift) implies equality after lifting.

## Lemma 2 — deterministic decision-tree depth adds under XOR with parity

For every Boolean f and m>=1,

D(L_m(f))=D(f)+m.

### Proof

Upper bound: optimally compute f using D(f) queries, query all m parity variables, and XOR the results.

Lower bound: use adversary composition. A deterministic decision tree computing XOR_2(f,P_m) is a classical composition of an outer XOR with two disjoint inner functions. The standard deterministic decision-tree composition theorem gives
D(XOR_2 o (f,P_m))=D(f)+D(P_m).
Since D(P_m)=m, the lower bound is D(f)+m.

For this repository the identity is additionally regression-tested exactly for the frozen pair through m=2. The composition theorem itself is established decision-tree theory and is not a novelty claim.

## Lemma 3 — sensitivity

For every (x,z),
s_{L_m(f)}(x,z)=s_f(x)+m,
because flipping any fresh parity coordinate always flips the output. Thus the sensitivity multiset is shifted by m and replicated 2^m times.

## Lemma 4 — influences

Influences of the original variables are unchanged under multiplication by an independent sign parity factor. Each fresh parity coordinate has influence 1. Hence equality of sorted base influence profiles is preserved.

## Lemma 5 — Fourier level energy

In sign representation,
(-1)^{L_m(f)(x,z)}=(-1)^{f(x)}(-1)^{P_m(z)}.
Fourier coefficients tensor, while parity P_m has a single nonzero coefficient on the full m-set. Thus the level-energy generating polynomial satisfies

E_{L_m(f)}(t)=t^m E_f(t).

Hence equality of Fourier level-energy profiles is preserved.

## Lemma 6 — weight and degree

For m>=1, P_m is balanced, so L_m(f) is balanced independently of the base weight. For the frozen non-affine quadratic pair, adjoining only linear parity terms leaves algebraic degree equal to 2.

## Lemma 7 — PN inequivalence of the frozen lifts

The quadratic interaction graph of a degree-two ANF is unchanged except for m newly isolated vertices. Input complementation does not change its quadratic coefficients, and input permutation only relabels vertices.

The frozen f graph has 3 quadratic edges and the frozen g graph has 4. Appending isolated vertices preserves this difference. Hence L_m(f) and L_m(g) are PN-inequivalent for every m>=0.

## Theorem — infinite fingerprint collision family

Let f,g be the frozen five-variable pair in this repository. Then for every m>=0,

Phi(L_m(f)) = Phi(L_m(g))

while

L_m(f) is not PN-equivalent to L_m(g).

Therefore there is a PN-inequivalent pair with identical frozen fingerprint in every dimension n>=5.

Combined with the exhaustive repository audit showing Phi is PN-complete for n<=4, the finite threshold is n*=5.

## Novelty boundary

The individual direct-sum/composition facts for deterministic decision trees and certificate-complexity composition are established subjects. The research claim to audit is the simultaneous preservation of this specific heterogeneous fingerprint, its first PN failure at dimension five, and the resulting all-dimensions n>=5 collision family. This theorem is mathematically established here but remains a NOVELTY CANDIDATE until the targeted literature audit is complete.
