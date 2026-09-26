# Boolean Invariant Separation

Reproducible software and exact computational artifacts for studying when a heterogeneous collection of Boolean-function invariants ceases to determine structure up to PN equivalence (permutation and independent complementation of input variables).

## Fingerprint

For a Boolean function (f:{0,1}^n -> {0,1}), the project uses

`Phi(f) = (weight, D, C0-profile, C1-profile, sensitivity-profile, influence-profile, algebraic-degree, Fourier-level-energy)`.

The components record Hamming weight, exact deterministic decision-tree depth, output-labelled pointwise certificate-complexity profiles, the complete pointwise sensitivity profile, the sorted individual-influence profile, algebraic degree over GF(2), and Walsh-Fourier energy aggregated by level.

## Main verified results

- **Exact completeness through four variables.** Exhaustive PN-orbit computation gives 3, 6, 22, and 402 PN classes for n=1,2,3,4 respectively, with exactly the same number of Phi classes and no cross-PN collisions.
- **First failure at n=5.** The full five-variable degree-at-most-2 ANF family contains 65,536 functions, 133 PN classes, and three cross-PN full-Phi collision groups.
- **Explicit minimal witness.**
  - `f = x2 x3 XOR x4 XOR x1 x4 XOR x1 x5`
  - `g = x1 x2 XOR x2 x3 XOR x4 XOR x1 x4 XOR x1 x5`
- **Common fingerprint of the witness.** Weight 16; decision-tree depth 4; both output-labelled certificate profiles (3^{x12},4^{x4}); sensitivity profile (1^{x4},2^{x12},3^{x12},4^{x4}); five influences equal to 1/2; algebraic degree 2; unnormalized Fourier-level energy `(0,128,384,384,128,0)`.
- **Structural separation.** The witness interaction graphs have 3 and 4 quadratic edges and different degree sequences, certifying PN inequivalence.
- **Persistent failure.** XOR with parity on fresh variables preserves equality of the full fingerprint for the witness while the quadratic interaction-graph separation persists. Consequently, a PN-inequivalent same-Phi pair exists in every dimension n>=5.
- **Strongest census collision.** One full-Phi class contains three PN classes whose interaction graphs have 3, 4, and 5 edges; the three representatives also differ in connectivity and triangle structure.

## Reproduce

```bash
python -m pip install -r requirements.txt
pytest -q
python -m bislab.verify_witness
python -m bislab.test_parity_lift --max-m 2
python -m bislab.small_dimension_audit
python -m bislab.exhaustive_quadratic_search --n 5
python -m bislab.analyze_collisions
```

Machine-readable outputs are written to `artifacts/`. The GitHub Actions workflow runs the regression tests, witness verification, parity-lift checks, exhaustive n<=4 audit, exhaustive five-variable quadratic census, and structural collision analysis.

A frozen successful workflow artifact is preserved under `frozen-artifacts/run-15/` together with its manifest.

## Citation

Akhtar, M. A. K. (2026). *When Aggregate Boolean Invariants Stop Determining Structure: A Minimal PN-Equivalence Failure and an Infinite Collision Family* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22974740

Citation metadata is also available in `CITATION.cff`.

## License

Software in this repository is released under the Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
