# Integration of KrawtchoukFeynman.pdf

## Archived source
- Original supplied PDF: `sources/KrawtchoukFeynman.pdf` (36 pages).
- Jerzy Kocik, *Krawtchouk matrices from the Feynman path integral and from the split quaternions*.
- Verified record: https://doi.org/10.48550/arXiv.1604.00109 (2016).

## Distribution into the current book
Chapter numbers below include the numbered introduction.

| Current chapter | Existing section | Integrated content |
| --- | --- | --- |
| 7: Lie Algebras | so(2,1) explained | Pure split space, Lorentz metric, commutators, adjoint matrices |
| 7 | so(2,1) spinors | Real spinors, adjoint vectors, double covering, rotations and boosts |
| 7 | Quaternions and Clifford algebras | Multiplication, conjugation, norm, zero divisors, matrix and Clifford realizations |
| 7 | S and so(2,1) tensors | Group versus infinitesimal lifts; distinction between Phi, S, and orthogonal U |
| 7 | Three-dimensional simple Lie algebras | Compact and split real forms, complexification, global group caveats |
| 8: Lie Groups and Reflections | Reflections | Non-null reflections, Hadamard conjugation and time orientation |
| 8 | Krawtchouk matrices as group elements | GL(2,R) formulation; determinant correction to the source |
| 9: Representations | Splitting formula | Symmetric powers, derivative representation, master equation and reversal symmetries |
| 10: Quantum Probability and Tensor Algebra | Flip operator and quantum random walk | Cube flips, orbit-average normalization and stochastic versus unitary evolution |
| 10 | Krawtchouk matrices as eigenvectors | Tensor diagonalization and full-cube versus symmetric-sector multiplicities |

## Editorial conventions and corrections
- Ordinary commutator XY-YX throughout the book; the source's half-commutator is explicitly distinguished.
- H has determinant -2. No nonzero real scalar multiple is in SL(2,R).
- SL(2,R) double covers SO^+(1,2), not every component of SO(1,2).
- Phi_N, S_N=Phi_N B_N, and the binomially normalized orthogonal involution U_N are distinguished.
- Orbit averages, not unnormalized orbit sums, yield the book's A_N on the symmetric tensor sector.

## Scope and verification
This is a focused integration of Section 7's foundational split-quaternion and tensor-representation material, with its cube/quantum context. It is not a complete transcription or integration of all 36 pages. Remaining path-integral, twiston, generalized-parameter and later spectral developments require separate treatment; existing placeholders for those topics are retained.

Exact arithmetic checks: split-unit products, both elementary Hadamard identities, all three displayed Lorentz-generator metric identities; reversal symmetries and weighted orthogonality for N=1 through 8. Existing N=3,5 appendix tables and Chapter 3 updates are preserved.

The main PDF has not been rebuilt. The current deliverable is the updated LaTeX source and archived input PDF.


## Consolidation after source comparison

- Kept project notation, including the already established Pascal matrix P_N (not a new C_N). Renamed powers-of-two Pascal weights W_N to avoid the parity matrix D_N. Added a central article-to-book dictionary in main.tex.
- Developed the elementary-symmetric-function/energy identity once in current Chapter 5; the twiston section in current Chapter 10 now gives only its model, interpretation, example, and source corrections.
- Developed signed paths in current Chapter 3, with an explicit amplitude/probability caveat.
- Extended the existing binomial-basis section in current Chapter 15 with its generating-function proof and explicit complementary-column eigenvectors of Phi_N, including the even-order central column and multiplicities. The basic binomial-column identity was already present before this consolidation.
- Kept the coefficient proof of the master equation in Random Walks, the tensor explanation in Representations, and replaced repeated derivations/normalizations elsewhere by cross-references.
- Verification: exact Pascal/eigenvector/completeness/multiplicity checks and exhaustive subset-energy/signed-path checks for N=0 through 8; source environments, references and citation keys checked. Prior N=3,5 appendices preserved byte-for-byte.
- Backup: project-archive/before-twiston-consolidation.zip.
- main.pdf has not been rebuilt; source-only validation is not a TeX compilation or visual-layout check.


## Continued selective integration: cross rules and conventions
- Added cross-order and adjacent-entry identities to First View and Cross Properties, with proofs from the existing generating function.
- Added a separate weighted-path coefficient array in Random Walks; retained the source generating function but corrected the incompatible step-weight description in Section 6.2. No general orthogonality/stochastic interpretation is claimed.
- Added the differential-operator dictionary in auxiliary variables xi, eta. In the book polynomial representation d rho(i)=L-R, not R-L; the Euler operator NI is distinguished from Lambda_N.
- Added vector/covector binomial metrics in Hilbert Space Structure, with weighted self-adjointness and column normalization, referencing the existing U_N rather than redefining it.
- Exact symbolic checks passed for cross identities through N=6, parameter identities through N=4, metrics and differential signs through N=6. Cross-references, labels and environments validated; existing appendices unchanged.
- Backup: project-archive/before-cross-identities-integration.zip. main.pdf is still not rebuilt; no TeX compiler is available in this sandbox.
