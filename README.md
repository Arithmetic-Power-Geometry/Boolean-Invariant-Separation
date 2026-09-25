# Boolean Invariant Separation Lab

This repository is a computation-first laboratory for studying when broad collections of classical Boolean-function invariants cease to determine Boolean structure up to PN equivalence (permutation and complementation of input variables).

## Frozen concept

For a Boolean function f:{0,1}^n -> {0,1}, define the heterogeneous fingerprint

Phi(f) = (weight, D, C0-profile, C1-profile, sensitivity-profile, influence-profile, algebraic-degree, Fourier-level-energy).

The project asks two questions:

1. **Finite completeness threshold.** For which smallest n do PN-inequivalent functions share the same Phi fingerprint?
2. **Asymptotic blindness.** Can one construct infinite PN-inequivalent families whose classical aggregate fingerprints agree while their interaction topology diverges?

The current verified witness occurs at n=5 among quadratic functions:

- f = x2 x3 XOR x4 XOR x1 x4 XOR x1 x5
- g = x1 x2 XOR x2 x3 XOR x4 XOR x1 x4 XOR x1 x5

The software independently verifies that these two functions agree in weight, exact deterministic decision-tree complexity, side-specific pointwise certificate distributions, full sensitivity distribution, individual influence multiset, algebraic degree, and Fourier energy by degree, while their quadratic interaction graphs are non-isomorphic. This certifies PN inequivalence for the pair.

## Research discipline

This repository intentionally does **not** claim that graph representations of quadratic Boolean functions, sensitivity signatures, influence signatures, or Boolean matching are new. Those are established topics. The research target is the simultaneous separation and, more importantly, whether it extends to an asymptotic family or hierarchy not reducible to existing Boolean-matching or quadratic-equivalence theory.

## Reproduce locally

```bash
python -m pip install -r requirements.txt
python -m bislab.verify_witness
python -m bislab.exhaustive_quadratic_search --n 5
pytest -q
```

Generated outputs are written to `artifacts/`.

## Workflow

GitHub Actions runs the tests, verifies the frozen n=5 witness, exhaustively scans the degree-at-most-2 ANF family at n=5, and uploads the generated CSV/JSON artifacts.

## Status

- n=5 explicit simultaneous-invariant collision: verified by code.
- PN inequivalence of the frozen witness: verified by non-isomorphic quadratic interaction graphs.
- Exhaustive degree-at-most-2 scan: implemented.
- Infinite-family theorem: open.
- Publication-level novelty: **not claimed yet**; it depends on the theorem-level extension and a full prior-art audit.

## License

Apache-2.0.
