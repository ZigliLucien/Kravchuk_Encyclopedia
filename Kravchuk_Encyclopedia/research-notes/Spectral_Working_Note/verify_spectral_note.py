"""Numerical checks for the spectral working note (NumPy/SciPy)."""
import math
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal
from scipy.special import gammaln, betaln
for N in (4,10,20,50,100):
    n=np.arange(0,N+1,2,dtype=float)
    y=(n-N/2)/math.sqrt(N)
    a=lambda k:np.where((k>=0)&(k<N),2*(k+1)*(N-k),0.)
    diag=(a(n-1)**2+a(n)**2)/N**4
    off=a(n[:-1])*a(n[:-1]+1)/N**4
    _,hv=eigh_tridiagonal(diag,off,select='i',select_range=(len(n)-1,len(n)-1))
    lc=gammaln(N+1)-gammaln(n+1)-gammaln(N-n+1)
    ij=n[:,None]+n[None,:]
    G=np.exp(lc[:,None]+lc[None,:]+N*np.log(4)-np.log(np.pi)
        +betaln((ij+1)/2,(2*N-ij+1)/2)-N*np.log(8)+np.log(N))
    val,v=eigh(G,subset_by_index=(len(n)-1,len(n)-1))
    f=np.exp(-math.sqrt(8)*y*y/2);f/=np.linalg.norm(f)
    factor=math.exp(N*math.log(8)/2)/math.sqrt(N)
    lower=math.sqrt(float(f@G@f))*factor
    top=math.sqrt(float(val[-1]))*factor
    overlap=abs(float(hv[:,0]@v[:,0]))
    print(f'N={N}: trial={lower:.12g}, eigenvalue={top:.12g}, overlap={overlap:.12g}')
