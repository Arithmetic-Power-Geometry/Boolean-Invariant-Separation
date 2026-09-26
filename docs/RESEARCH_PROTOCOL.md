# Research protocol

## Object

Boolean functions (f:{0,1}^n -> {0,1}), compared under PN equivalence: permutation and independent complementation of input variables. Output complementation is not included.

## Aggregate fingerprint

Phi(f) records:

1. Hamming weight;
2. exact deterministic decision-tree depth D;
3. sorted pointwise 0-certificate profile;
4. sorted pointwise 1-certificate profile;
5. sorted pointwise sensitivity profile;
6. sorted individual influence profile;
7. algebraic degree over GF(2);
8. Walsh-Fourier energy aggregated by subset cardinality.

Integer Walsh energies are stored to avoid floating-point equality decisions.

## Exact finite audit

For n<=4, all Boolean functions are exhaustively assigned to PN orbits and Phi classes. The verified counts are:

| n | Functions | Phi classes | PN classes | Cross-PN collisions |
|---:|---:|---:|---:|---:|
| 1 | 4 | 3 | 3 | 0 |
| 2 | 16 | 6 | 6 | 0 |
| 3 | 256 | 22 | 22 | 0 |
| 4 | 65,536 | 402 | 402 | 0 |

Thus Phi is PN-complete through four variables.

## Five-variable quadratic census

The degree-at-most-2 ANF family on five variables has 16 coefficients and therefore 65,536 functions. Exact enumeration yields 133 PN classes and three cross-PN full-Phi collision groups. The first failure dimension is therefore n=5.

## Structural certificate

For degree-at-most-two ANFs, associate a simple graph whose vertices are variables and whose edges are the nonzero quadratic monomials (x_i x_j). Input complementation changes only lower-degree terms, while variable permutation relabels vertices. Non-isomorphic interaction graphs therefore certify PN inequivalence.

For the explicit witness, the two graphs have 3 and 4 edges and degree sequences `(1,1,1,1,2)` and `(1,1,1,2,3)`.

## Parity lift

For (P_m(z)=z_1 XOR ... XOR z_m), define (L_m(f)(x,z)=f(x) XOR P_m(z)). The closure identities used by the project show that equal base fingerprints remain equal after the lift, while the witness interaction graphs acquire only isolated vertices. The 3-versus-4 edge separation therefore persists for every m>=0.

Consequently, same-Phi PN-inequivalent pairs exist in every dimension n>=5.

## Verification

The repository provides independent code paths for the explicit witness, the exhaustive lower-dimensional audit, the five-variable quadratic census, collision-topology analysis, and finite parity-lift regression checks. Symbolic arguments for the parity lift are recorded in `docs/PARITY_LIFT_PROOF.md`.
