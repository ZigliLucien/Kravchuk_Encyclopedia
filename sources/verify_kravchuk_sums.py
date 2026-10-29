"""Exact verification of selected Kravchuk sums; standard library only."""
from math import comb, isqrt
from fractions import Fraction
import json
from pathlib import Path

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def matrix(N):
    return [[sum((-1)**r*choose(j,r)*choose(N-j,n-r) for r in range(n+1)) for j in range(N+1)] for n in range(N+1)]

checks, examples = 0, []
for N in range(33):
    K=matrix(N)
    rows=[sum(a) for a in K]
    cols=[sum(K[n][j] for n in range(N+1)) for j in range(N+1)]
    rsq=[sum(x*x for x in a) for a in K]
    csq=[sum(K[n][j]**2 for n in range(N+1)) for j in range(N+1)]
    cm=[sum(abs(K[n][j]) for n in range(N+1)) for j in range(N+1)]
    assert sum(rows)==2**N
    for n in range(N+1):
        assert rows[n]==(comb(N+1,n+1) if n%2==0 else 0)
        assert rsq[n]==sum(comb(N+1,2*k+1)*comb(2*k,k)*choose(N-2*k,n-k) for k in range(min(n,N//2)+1))
        assert sum(K[n][j]**2*comb(N,j) for j in range(N+1))==2**N*comb(N,n)
        checks+=3
    for j in range(N+1):
        assert cols[j]==(2**N if j==0 else 0)
        assert csq[j]==Fraction(comb(2*j,j)*comb(2*N-2*j,N-j),comb(N,j))
        assert sum(Fraction(K[n][j]**2,comb(N,n)) for n in range(N+1))==Fraction(2**N,comb(N,j))
        assert cm[j]**2*comb(N,j)<=4**N
        checks+=4
    assert sum(rsq)==sum(comb(N+1,2*k+1)*comb(2*k,k)*2**(N-2*k) for k in range(N//2+1))
    checks+=1
    if N>=1:
        assert cm[0]==cm[N]==2**N
        assert cm[1]==2*comb(N-1,(N-1)//2)
        checks+=2
    if N>=3:
        assert sum(cm)>=2**(N+1)+4*comb(N-1,(N-1)//2)
        checks+=1
    if N>2:
        k=(N-isqrt(N))//2
        while (N-2*k)**2<N: k-=1
        while N-2*(k+1)>=0 and (N-2*(k+1))**2>=N: k+=1
        assert cm[2]==4*(choose(N-2,k)-choose(N-2,k-1))
        checks+=1
    if N in (5,10,15,20,32):
        examples.append(dict(N=N,signed_total=sum(rows),square_total=sum(rsq),absolute_total=sum(cm),boundary_pair_0=2**(N+1),boundary_pair_1=4*comb(N-1,(N-1)//2),boundary_pair_2=2*cm[2]))
result=dict(orders_checked='0..32',exact_identity_and_bound_checks=checks,numerical_rows=examples)
print(json.dumps(result,indent=2))
if __name__=='__main__':
    Path(__file__).with_name('kravchuk-sums-checks.json').write_text(json.dumps(result,indent=2))
