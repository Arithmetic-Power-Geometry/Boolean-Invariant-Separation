# Artifact manifest

The reproducibility workflow produces machine-readable evidence for the reported computational results.

| Artifact | Contents |
|---|---|
| `witness.json` | Exact n=5 witness and equality/separation checks |
| `small_dimension_audit.json` | Exhaustive n<=4 function counts, Phi classes, PN classes, and zero-collision checks |
| `quadratic_search_summary.json` | Exact five-variable degree-at-most-2 search summary |
| `quadratic_collision_groups.json` | Cross-PN collision groups and representatives |
| `quadratic_collision_groups.csv` | Flat audit table for the collision groups |
| `collision_structure_analysis.json` | Interaction-graph structure of the collision representatives |
| `parity_lift_checks.json` | Exact finite regression checks for the parity lift |

## Frozen reproducibility archive

A successful complete workflow artifact is preserved at:

`frozen-artifacts/run-15/boolean-invariant-separation-artifacts.zip`

Its integrity metadata is stored in:

`frozen-artifacts/run-15/MANIFEST.json`

The archive contains the exact outputs used to verify the lower-dimensional completeness audit, five-variable quadratic census, explicit witness, structural collision analysis, and parity-lift regression checks.

## Interpretation

The computational artifacts establish exact finite claims and independently check the explicit constructions. The all-dimensions statement additionally uses the symbolic parity-lift argument documented in `PARITY_LIFT_PROOF.md`.
