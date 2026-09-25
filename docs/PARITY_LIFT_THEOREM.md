# Candidate parity-lift theorem

This note records a theorem candidate separately from verified computational facts.

Let f and g be Boolean functions on the same n variables with equal frozen fingerprint Phi. For m>=1 define

F_m(x,z) = f(x) XOR z_1 XOR ... XOR z_m,
G_m(x,z) = g(x) XOR z_1 XOR ... XOR z_m.

The following closure identities are the proof obligations.

## Weight

For m>=1 parity is balanced, hence F_m and G_m are balanced. More generally XOR with a fixed disjoint h preserves equality of weights whenever the two base weights agree.

## Sensitivity

At every (x,z),

s_{F_m}(x,z)=s_f(x)+m.

Therefore equal pointwise sensitivity multisets are shifted by m and replicated 2^m times.

## Influences

Every old-variable influence is unchanged. Every fresh parity variable has influence 1. Thus equal sorted influence profiles remain equal after appending m copies of 1.

## Fourier level energy

For sign functions, chi_{F_m}=chi_f chi_{parity_m}. Fourier coefficients tensor. Parity_m has its sole Fourier support at degree m. Hence the level-energy polynomial is shifted by m:

E_{F_m}(t)=t^m E_f(t).

The same holds for g.

## Algebraic degree

For quadratic non-affine base functions and linear parity variables, degree remains 2.

## Certificates

For disjoint XOR A(x) XOR B(z), a restricted product subcube is constant only when both restricted factors are constant (unless one factor has no free inputs). Consequently at a point,

C_{A XOR B}(x,z)=C_A(x)+C_B(z).

For m-bit parity, C_B(z)=m. Thus every pointwise certificate value is shifted by m; the output-labelled C0/C1 profiles require a careful multiplicity argument because parity is balanced. This is a formal proof obligation.

## Deterministic decision-tree depth

Candidate identity:

D(A XOR B)=D(A)+D(B)

for nonconstant Boolean functions on disjoint variable sets. For parity_m this gives D(F_m)=D(f)+m. This must be proved independently; finite tests are not a substitute.

## PN inequivalence for the frozen quadratic pair

Adding fresh parity variables adds no quadratic edges, so it appends m isolated vertices to each quadratic interaction graph. The base frozen graphs have different edge counts (3 versus 4), which is preserved. Therefore every lifted pair remains PN-inequivalent.

## Candidate conclusion

If the certificate and deterministic-depth closure lemmas are proved, the frozen n=5 witness immediately yields an infinite sequence of PN-inequivalent pairs with identical Phi for every n>=5.

This is a theorem candidate, not yet a novelty claim. It must be audited against direct-sum/XOR composition results in decision-tree complexity, certificate complexity, Boolean matching, and quadratic Boolean-function equivalence.
