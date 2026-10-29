"""Recompute Gaussian--Krawtchouk rules; requires mpmath, not a TeX package."""
import csv, json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps = 90
rules, rows = [], []
for N in (5, 10, 15):
    for n in sorted({(N+1)//2, N}):
        J = mp.matrix(n)
        for a in range(n):
            J[a,a] = mp.mpf(N)/2
            if a:
                J[a,a-1] = J[a-1,a] = mp.sqrt(a*(N-a+1))/2
        nodes, U = mp.eigsy(J)
        weights = [U[0,a]**2 for a in range(n)]
        def kpoly(x, degree):
            a, b = mp.mpf(1), x
            if degree == 0: return a
            for k in range(1, degree):
                a, b = b, x*b-k*(N-k+1)*a
            return b
        errors = []
        for degree in range(2*n):
            exact = sum(mp.mpf(math.comb(N,j))*mp.power(mp.mpf(j)/N,degree)/2**N for j in range(N+1))
            approx = sum(weights[a]*mp.power(nodes[a]/N,degree) for a in range(n))
            errors.append(abs(exact-approx))
        residual = max(abs(kpoly(N-2*z,n))/max(1,mp.factorial(n)*mp.binomial(N,n)) for z in nodes)
        cd_error = max(abs(weights[a]-1/sum(kpoly(N-2*nodes[a],k)**2/(mp.factorial(k)**2*mp.binomial(N,k)) for k in range(n))) for a in range(n))
        assert max(errors) < mp.mpf('1e-80')
        assert residual < mp.mpf('1e-80') and cd_error < mp.mpf('1e-80')
        assert all(w > 0 for w in weights)
        rule = dict(N=N,n=n,nodes=[mp.nstr(z,65) for z in nodes],weights=[mp.nstr(w,65) for w in weights],max_scaled_moment_error=mp.nstr(max(errors),8),max_normalized_root_residual=mp.nstr(residual,8),max_christoffel_weight_error=mp.nstr(cd_error,8))
        rules.append(rule)
        for a in range(n):
            rows.append(dict(N=N,n=n,index=a+1,node_j=rule['nodes'][a],weight_probability=rule['weights'][a]))
        print(N,n,'moment error',mp.nstr(max(errors),8),'root residual',mp.nstr(residual,8))
output = Path(__file__).resolve().parent
(output/'gaussian-krawtchouk-rules.json').write_text(json.dumps(dict(decimal_working_precision=90,rules=rules),indent=2))
with (output/'gaussian-krawtchouk-rules.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]))
    writer.writeheader(); writer.writerows(rows)
