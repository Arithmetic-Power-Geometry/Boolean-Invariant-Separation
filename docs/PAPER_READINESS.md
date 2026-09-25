# Paper Readiness Gate

The manuscript should not be drafted from exploratory state. Start the paper when every mandatory gate below is green.

## Gate A — reproducibility

- [x] Frozen n=5 witness is covered by regression tests.
- [x] Parity lifts through n=7 are covered by exact regression tests.
- [x] Exhaustive n<=4 PN audit is implemented and passes in CI.
- [ ] One final, non-cancelled CI run completes the exhaustive 65,536-function degree<=2 n=5 census.
- [ ] Structural collision analysis completes in the same run.
- [ ] Workflow artifact is uploaded and inspected.

## Gate B — mathematics

- [x] Exact fingerprint Phi is frozen.
- [x] Pointwise certificate XOR-additivity is proved.
- [x] Sensitivity, influence, Fourier-level energy, weight, and degree closure under parity lift are proved.
- [x] PN inequivalence of every frozen parity lift follows from the quadratic interaction graph.
- [x] Deterministic decision-tree parity-lift identity is reduced to standard deterministic composition/direct-sum theory.
- [x] Infinite same-Phi PN-inequivalent family for every n>=5 follows from the closure lemmas.
- [ ] Check the proof text against primary references and add precise citations for composition results.

## Gate C — novelty audit

Search and record primary prior art for:
1. PN/NPN Boolean matching and complete/partial signatures;
2. sensitivity/influence signatures in Boolean matching;
3. Fourier/spectral signatures for Boolean equivalence;
4. decision-tree and certificate composition;
5. quadratic Boolean functions represented/classified by graphs or matrices;
6. any published invariant tuple identical or essentially equivalent to Phi;
7. any prior first-failure result at n=5 for such a heterogeneous tuple;
8. any prior infinite PN-inequivalent family preserving this simultaneous tuple.

The paper-level claim is not that any component invariant or parity composition law is new. The candidate contribution is the simultaneous heterogeneous invariant system, its exact finite threshold, an explicit minimal quadratic witness, and the all-dimensions collision construction.

## Decision rule

WRITE PAPER only when:
- Gate A is fully green;
- the proof has survived reference checking;
- the targeted audit finds no prior result subsuming the exact main claim.

If the census exposes a stronger recurring construction, freeze that theorem before drafting so the manuscript is not obsolete on arrival.
