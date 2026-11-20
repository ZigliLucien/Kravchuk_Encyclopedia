# Basic polynomial and matrix notation: specific consistency audit

## Fixed symmetric convention

$$
(1+v)^{N-j}(1-v)^j=\sum_{n=0}^N K_n(j;N)v^n,
\qquad j=\#(-1),\quad N-j=\#(+1).
$$

$$
x=N-2j,\qquad k_n(x,N)=n!K_n((N-x)/2;N),
\qquad (\Phi_N)_{ij}=K_i(j;N)=k_i(N-2j,N)/i!.
$$

The equality involving general x uses polynomial extension. On the original lattice, no extension is needed. K has leading coefficient $(-2)^n/n!$ in j, and k is monic in x.

## Actual collisions and insufficiently explicit conventions

| Issue | Finding | Treatment |
|---|---|---|
| K used for two normalizations | Symmetric chapters use ordinary coefficients $K_n(j;N)$; PQ uses exponential coefficients $K_n(x,N)$ for a biased family. At symmetric parameters the latter is k, not the former K. Punctuation is too weak to distinguish them safely. | Unresolved naming decision. Retain explicit source labels until a separate name for the PQ family is approved. |
| Coordinate omitted in $k_n=n!K_n$ | Requires $x=N-2j$; equality with the same numerical argument is generally false. | Replaced the abbreviation in Chapter 1 by the full argument conversion. |
| Matrix entry indexing | $(\Phi_N)_{ij}$ is row-degree i, column-negative-count j. Reversing i and j transposes Phi and does not generally preserve entries. | Added explicit entry formulas in Chapters 1 and 14. |
| Source $\Phi^N_{ij}$ | Same symmetric scalar entry as $(\Phi_N)_{ij}$ under the stated sums-paper dictionary. Lowercase $\phi^N_{ij}$ is the general-parameter source coefficient, not the symmetric entry at arbitrary parameters. | Genuine symmetric entry alias; biased conversion still needs parameters and scaling. |
| Finite generating series off the lattice | The upper limit N is valid for integer j in 0,...,N. After setting x arbitrary, the generalized-binomial generating function is generally an infinite formal series. | Chapter 1 now distinguishes the lattice identity from coefficientwise polynomial extension. |
| Terminal polynomial | $k_{N+1}$ is not the zero polynomial. It vanishes at all N+1 lattice points; there is no extra matrix row in Phi_N. | Made the distinction explicit in Chapter 1; Chapter 13 remains unchanged. |
| “Symmetric transform” | Symmetric parameters do not mean the raw matrix Phi_N is symmetric. The symmetric matrix is S_N=Phi_N B_N. | Clarified wording in Chapter 1. |
| Hypergeometric conventions | The current Chapter 15 has $K_n(j;N)=\binom Nn\,{}_2F_1(-n,-j;-N;2)$. A source using just the hypergeometric factor is additionally divided by the binomial coefficient. | Current formula is consistent; do not import another source's K without checking its normalization. |
| Normalized modes | $p_{n,N}=K_n/\sqrt{\binom Nn}$ and $\psi_{n,N}=\sqrt{w_N}\,p_{n,N}$ are different types: a polynomial orthonormal for the binomial measure and a function orthonormal for counting measure. | Keep distinct. |

## Low-degree diagnostic

$$
K_0(j;N)=1,\quad K_1(j;N)=N-2j,\quad
K_2(j;N)=\frac{(N-2j)^2-N}{2}.
$$

$$
k_0(x,N)=1,\quad k_1(x,N)=x,\quad k_2(x,N)=x^2-N.
$$

For N=3, j=1 and x=1, $K_2(1;3)=-1$, while $k_2(1,3)=-2$. The corresponding hypergeometric factor without $\binom32$ is $-1/3$.

## Verification and scope

Exact arithmetic checked the coefficient/recurrence identity $k_n(N-2j,N)=n!(\Phi_N)_{nj}$ at all 506 entries for N=0,...,10; also checked $\Phi_N^2=2^NI$, symmetry of $\Phi_NB_N$, and the terminal factorization. Chapter 13 and the PQ family name were left unchanged. These were source-only clarifications; the PDF has not been rebuilt in this pass.
