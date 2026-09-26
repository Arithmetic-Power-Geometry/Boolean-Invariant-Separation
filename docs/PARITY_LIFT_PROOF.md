# Parity-Lift Closure Theorem

## Definitions

Let (f:{0,1}^n -> {0,1}). For m>=1 let (P_m(z)=z_1 XOR ... XOR z_m) and define

`L_m(f)(x,z)=f(x) XOR P_m(z)`.

Let Phi consist of weight, exact deterministic decision-tree depth, output-labelled pointwise certificate profiles, pointwise sensitivity profile, sorted individual influence profile, algebraic degree, and Fourier energy by level.

## Lemma 1 — certificates under disjoint XOR

For Boolean functions A(x) and B(z) on disjoint variables,

`C_(A XOR B)(x,z) = C_A(x) + C_B(z)`.

Minimum certificates for A and B combine to certify their XOR. Conversely, if the part of an XOR certificate lying in either variable block failed to certify that factor, changing that factor while holding the other block fixed would change the XOR without violating the purported certificate. Hence both parts must be certificates and the sizes add.

For parity, every input has certificate complexity m. Because nonzero parity is balanced, the output-labelled lifted certificate profiles are obtained from the base values by adding m with equal parity multiplicities. Equality of the base profiles is therefore preserved.

## Lemma 2 — parity-lift identities

For m>=1:

1. (L_m(f)) is balanced.
2. (s_{L_m(f)}(x,z)=s_f(x)+m).
3. Old-variable influences are unchanged and every fresh parity variable has influence 1.
4. Every pointwise certificate value increases by m.
5. The Fourier level-energy polynomial satisfies (E_{L_m(f)}(t)=t^m E_f(t)).
6. For a non-affine quadratic base function, the algebraic degree remains 2.
7. (D(L_m(f))=D(f)+m).

The sensitivity and influence identities follow directly because every fresh parity coordinate flips the output. In sign representation, the parity factor has Fourier support only on its full m-set, so tensoring shifts Fourier level by m. Adding fresh linear terms does not change a quadratic base degree.

## Lemma 3 — deterministic XOR composition

For nonconstant Boolean functions A and B on disjoint variable sets,

`D(A XOR B) = D(A) + D(B)`.

The upper bound follows by computing A and B optimally and XORing their outputs. For the lower bound, use the deterministic decision-tree recurrence. Against an arbitrary tree, answer each query so that the decision-tree depth of the current residual in that variable block falls by at most one. If a leaf were reached in fewer than (D(A)+D(B)) queries, at least one residual block would remain nonconstant, giving two completions reaching the same leaf with different XOR outputs. This is impossible. Thus equality holds. Since (D(P_m)=m), the parity-lift depth identity follows.

## Theorem — persistent aggregate collision

Let

`f = x2 x3 XOR x4 XOR x1 x4 XOR x1 x5`

and

`g = x1 x2 XOR x2 x3 XOR x4 XOR x1 x4 XOR x1 x5`.

For every m>=0,

`Phi(L_m(f)) = Phi(L_m(g))`

while (L_m(f)) and (L_m(g)) are not PN-equivalent.

For m=0 this is the explicit five-variable witness. For m>=1, equality of the fingerprint follows componentwise from the identities above. The quadratic interaction graphs gain exactly m isolated vertices and otherwise remain unchanged. Their base edge counts are 3 and 4, so the graphs remain non-isomorphic under every lift.

Therefore a PN-inequivalent pair with identical Phi exists in every dimension n>=5. Combined with the exhaustive n<=4 audit, the first failure dimension is exactly n=5.

## Computational checks

The symbolic theorem is complemented by exact regression checks for m=0,1,2, corresponding to n=5,6,7. These checks verify full-Phi equality and the interaction-graph inequivalence certificate; they are not used as a substitute for the all-dimensions proof.
