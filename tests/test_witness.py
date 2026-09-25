from bislab.core import *
from bislab.verify_witness import N,F_LINEAR,F_QUAD,G_LINEAR,G_QUAD

def test_frozen_witness_collision_and_inequivalence():
    f=truth_from_anf(N,linear=F_LINEAR,quadratic=F_QUAD)
    g=truth_from_anf(N,linear=G_LINEAR,quadratic=G_QUAD)
    assert fingerprint(f,N,2)==fingerprint(g,N,2)
    assert graph_degree_sequence(N,F_QUAD)!=(graph_degree_sequence(N,G_QUAD))
