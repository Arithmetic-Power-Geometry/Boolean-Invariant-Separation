from __future__ import annotations
import itertools
from functools import lru_cache

def inputs(n):
    return list(itertools.product((0,1), repeat=n))

def truth_from_anf(n, constant=0, linear=(), quadratic=()):
    out=[]
    for x in inputs(n):
        v=constant
        for i in linear:
            v ^= x[i-1]
        for i,j in quadratic:
            v ^= x[i-1] & x[j-1]
        out.append(v)
    return tuple(out)

def weight(tt):
    return sum(tt)

def sensitivity_profile(tt,n):
    xs=inputs(n)
    out=[]
    index={x:i for i,x in enumerate(xs)}
    for ix,x in enumerate(xs):
        s=0
        for j in range(n):
            y=list(x); y[j]^=1; y=tuple(y)
            s += tt[ix] != tt[index[y]]
        out.append(s)
    return tuple(sorted(out))

def influence_profile(tt,n):
    xs=inputs(n)
    index={x:i for i,x in enumerate(xs)}
    vals=[]
    for j in range(n):
        c=0
        for ix,x in enumerate(xs):
            y=list(x); y[j]^=1; y=tuple(y)
            c += tt[ix] != tt[index[y]]
        vals.append(c/len(xs))
    return tuple(sorted(vals))

def certificate_at(tt,n,ix):
    xs=inputs(n); x=xs[ix]; target=tt[ix]
    for k in range(n+1):
        for S in itertools.combinations(range(n),k):
            good=True
            for iy,y in enumerate(xs):
                if all(y[j]==x[j] for j in S) and tt[iy]!=target:
                    good=False; break
            if good:
                return k
    return n

def certificate_profiles(tt,n):
    c0=[]; c1=[]
    for ix,v in enumerate(tt):
        c=certificate_at(tt,n,ix)
        (c1 if v else c0).append(c)
    return tuple(sorted(c0)), tuple(sorted(c1))

def deterministic_depth(tt,n):
    xs=inputs(n)
    @lru_cache(None)
    def rec(sub):
        if len({tt[i] for i in sub})<=1:
            return 0
        best=n+1
        for j in range(n):
            a=tuple(i for i in sub if xs[i][j]==0)
            b=tuple(i for i in sub if xs[i][j]==1)
            if a and b:
                best=min(best,1+max(rec(a),rec(b)))
        return best
    return rec(tuple(range(1<<n)))

def fourier_level_energy(tt,n):
    w=[1 if b==0 else -1 for b in tt]
    N=1<<n
    h=1
    while h<N:
        for i in range(0,N,2*h):
            a=w[i:i+h]
            b=w[i+h:i+2*h]
            w[i:i+h]=[a[k]+b[k] for k in range(h)]
            w[i+h:i+2*h]=[a[k]-b[k] for k in range(h)]
        h*=2
    e=[0]*(n+1)
    for mask,val in enumerate(w):
        e[mask.bit_count()] += val*val
    return tuple(e)

def fingerprint(tt,n,degree):
    c0,c1=certificate_profiles(tt,n)
    return (
        weight(tt),
        deterministic_depth(tt,n),
        c0,c1,
        sensitivity_profile(tt,n),
        influence_profile(tt,n),
        degree,
        fourier_level_energy(tt,n),
    )

def interaction_edges(quadratic):
    return tuple(sorted(tuple(sorted(e)) for e in quadratic))

def graph_degree_sequence(n, quadratic):
    d=[0]*n
    for i,j in quadratic:
        d[i-1]+=1; d[j-1]+=1
    return tuple(sorted(d))
