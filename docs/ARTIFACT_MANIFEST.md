# Artifact manifest

Every release-quality workflow should produce machine-readable evidence for the claims used later in the manuscript.

| Artifact | Meaning |
|---|---|
| witness.json | Exact frozen n=5 witness and equality/separation checks |
| quadratic_search_summary.json | Exhaustive degree<=2 search scope and collision count |
| quadratic_collision_groups.json | PN-distinct collision representatives |
| quadratic_collision_groups.csv | Flat audit table for collision groups |

## Required next artifacts

Before a paper claims a first-failure threshold, add an exhaustive n<=4 certificate containing function counts, PN orbit counts, Phi class counts, and a zero-collision assertion.

Before an asymptotic theorem is claimed, add family-generation artifacts that independently verify each claimed n and record the structural separation statistic.

Artifacts are evidence. They do not by themselves establish literature novelty.
