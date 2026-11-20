# Basic notation propagation and next priorities

## Applied scope

Applied to the master `main.tex` and included chapter exposition. Original files in `sources/`, supporting papers, archived versions, and standalone research-note manuscripts are preserved. Tables already use the approved basic symbols. Historical notation remains identifiable in source dictionaries and audit records; it is not promoted to an alternative convention.

The fixed family is

$A_N=R_N+L_N$, $\Lambda_N=[L_N,R_N]$, $\Phi_N$, $J_N$, $\sigma_N$, $B_N$, $S_N=\Phi_NB_N$, and $T_N$.

Subscripts can be omitted when level is clear. The raw generating convention for $\Phi_N$ is unchanged.

### Changes

- Parity $D_N$ becomes $\sigma_N$ in front matter and Chapters 6, 8, 14.
- Chapter 16's local sign operator $E$ becomes $\sigma_N$; reversal $J$ becomes $J_N$ there. Its identities are now $J_NS_N=S_N\sigma_N$ and $S_NJ_N=\sigma_NS_N$.
- Chapter 2's transition matrix, formerly $T_N$, becomes $\mathsf P_N=A_N/N$. The backward matrix is $\mathsf P_N^T$.
- Chapter 4's generic exterior-power map T becomes $\mathsf X$, leaving T reserved for the anticommuting matrix.
- Chapter 9's full tensor Hadamard transform, formerly $T_N$, becomes $\mathbf H_N=H^{\otimes N}$. Its symmetric-sector matrix in orbit-average coordinates remains $\Phi_N$.
- Chapter 16's placeholder for T is replaced with the existing research-note normalization, its entrywise definition, and a coefficient proof of anticommutation:

$$
T_N=(\Lambda_N-NI)R_N+(\Lambda_N+NI)L_N,
\qquad T_N^T=-T_N,
\qquad T_NS_N=-S_NT_N.
$$

The superdiagonal is $2(j+1)(N-j)$ and the subdiagonal its negative. Multiplying this T by a nonzero scalar would preserve anticommutation, but this particular scale/sign is the one now fixed by the displayed definition.

### Verification

- Verified the explicit T formula, skew symmetry and anticommutation in exact arithmetic for N=1,...,12.
- Gave a generating-polynomial proof in the chapter; finite computations are checks, not the proof for arbitrary N.
- Successfully rebuilt the 89-page master PDF. Restored the original portrait as a whole page, since the remote compiler cannot read mounted local image files.
- The PDF structural checker reports no off-page glyphs or structural problems; inspected the fixed-notation, rotation/parity, and T-definition pages.
- Original versions were archived before source changes. The previous PDF is archived before replacement.

## Next priorities, in order

| Priority | Conflict or distinction | Recommended decision for the next pass |
|---|---|---|
| 1 | Ch. 6's Cartan differential $\mathcal H$ versus Ch. 11's oscillator $\mathcal H$ | Keep the oscillator notation and give the Cartan differential realization its own symbol, explicitly linked to $\Lambda_N$. Exact replacement remains for author approval. |
| 2 | Symmetric $K_n(j;N)$, centered monic $k_n(x,N)$, and PQ's factorial-normalized biased $K_n(x,N)$ | Fix a family/normalization dictionary before replacing any polynomial symbols. The ordinary/factorial coefficient distinction must survive. |
| 3 | p and q exchange roles between Ch. 13 and PQ; r denotes both correlation and a probability ratio | Choose one global biased-probability convention; give the sums-paper ratio a different symbol from the spectral r. |
| 4 | B_N is fixed, but bare B is a probability matrix in PQ and a Pascal matrix in a source; Gamma has two source meanings | Preserve B_N for binomial multiplicities and P_N for Pascal. Give probability and norm matrices explicit distinct names after approval. |
| 5 | R_n denotes signed row sums as well as the level-n raising matrix; b_j denotes binomial multiplicities and Jacobi coefficients | Rename the statistics/coefficients, not the fixed raising matrices. Exact replacement symbols remain for approval. |
| 6 | D is differentiation in PQ/Ch. 11 but a diagonal sign/scalar map in Ch. 4; i is a real split unit, an index, or visually a scalar imaginary unit | Separate these contextual constructions without disturbing the fixed finite matrices. |
| 7 | Generic A is a one-site matrix in Ch. 3; A is also a temporary scalar in a bilinear formula | Rename local generic objects in the next pass if global exclusivity for bare basic symbols is desired. These have different types, but retaining them weakens the reservation. |
| 8 | Induced stochastic matrices versus symmetric-power matrices, group lifts versus differential lifts | Preserve the existing distinctions; do not collapse them as aliases. |

The symbols chosen provisionally to remove T collisions are **mathsf P_N** for the column transition and **bold H_N** for the tensor transform. These do not change their definitions or claim those names were used by the original sources.

## Subsequent H decision

Cartan uses $\mathbf H$; oscillator uses $\mathcal H$; one-site Hadamard uses $H$. The tensor transform is now written $H^{\otimes N}$, superseding the provisional $\mathbf H_N$ abbreviation. Applied to the master source; PDF not rebuilt in this pass.
