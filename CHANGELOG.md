# Change log

## Project consolidation
- Recovered nested chapter sources and retained the user-edited outer main.tex.
- Preserved the original archive and supplied sums-paper sources.
- Added project status, missing-material checklist, and working conventions.
- Did not insert missing introduction or moments updates.

## Introduction update
- Installed the newly uploaded source project, including chapters/00-introduction.tex and its main.tex include.
- Verified all 25 includes. Preserved overwritten source versions and the uploaded archive.
- Retained the user-supplied compiled main.pdf; no compilation performed here.

## Matrix material integrated into the Encyclopedia
- Added conventions, generators, recurrence intertwinings, raw/orthogonal transforms, and symmetric-matrix definitions in their topical chapters.
- Added all twenty full matrices for N=2,4,7,8 to Appendix A using separate source fragments.
- Added cross-references and updated CONTENTS.md; prior versions preserved in project-archive/.
- Existing main.pdf predates this source integration and has not been recompiled.


## Split-quaternion article integration
Archived `sources/KrawtchoukFeynman.pdf` and developed ten existing sections across current Chapters 7--10, emphasizing Section 7. Added a verified bibliography entry, determinant/component corrections, and explicit normalization reconciliation. See `sources/INTEGRATION_KrawtchoukFeynman.md` for the source-to-topic map, checks, and remaining scope. Main PDF not rebuilt.


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


## Supplied bibliography integrated
Added all 50 supplied entries with keys ref01--ref50 unchanged, plus the existing KocikFeynman entry, in bibliography/references.tex. Main document now inputs one unified 51-entry bibliography. Original source archived byte-for-byte in sources/KrawtchoukReferences_bibliography.tex. Review flags and explicit unverified status recorded in sources/BIBLIOGRAPHY_REVIEW.md; no metadata corrections or chapter citations inferred. Citation keys, preserved entry text and LaTeX environments checked. Backup: project-archive/before-bibliography-integration.zip. main.pdf not rebuilt.


## Foundations and martingales completion
Completed nine previously blank sections across six chapters, including Pascal/generating-function foundations, Grassmann traces, all three martingale sections, the exact discrete stochastic equation, biased orthogonal polynomials and generator, and exponential expansions. The scalar multinomial family is explicitly not claimed to be a complete multivariate system. Exact checks: 2,036; labels, references and chapter environments checked. See sources/INTEGRATION_foundations_martingales.md. Existing main.pdf not rebuilt. Backup: project-archive/before-foundations-martingales-integration.zip.


## Gaussian summation and visible gap markers
Added uppercase topic NEEDS TO BE DONE notices at remaining gaps (28 visible markers after developing the quadrature chapter). Gaussian quadrature is now formulated for the finite binomial sum, with separate support parameter N and node count n, proofs and error formula, and six high-precision rules for N=5,10,15. TeX tables, 65-digit CSV/JSON, and a reproducible mpmath script included. See sources/INTEGRATION_gaussian_summation.md. Main PDF not rebuilt. Backup: project-archive/before-gaussian-summation.zip.


## Terminal integral zeros
Added the approved recurrence remark and an Integral zeros discussion: centered terminal factorization, parity-dependent quadratic products, spacing-two spectrum, normalization and zero-norm distinction, with a cross-reference to the terminal Gaussian rule. Exact recurrence/factorization checks for N=0 through 20. Backup: project-archive/before-terminal-integral-zeros.zip. Main PDF not rebuilt.


## Source and reference integration audit
Checked 36 active TeX files and all input/include dependencies; 51 bibliography keys, zero unresolved citations/references or duplicate labels, balanced environments. All 50 supplied entry texts are preserved, but all remain uncited and metadata review is pending. Corrected stale preface/source-register descriptions, added martingale and quadrature provenance notes, and generated GAP_REVIEW.md (28 visible gap notices) plus sources/INTEGRATION_AUDIT.md and machine-readable audit results. No new bibliographic verification, TeX compilation or PDF rebuild. Backup: project-archive/before-source-integration-audit.zip.


## Kravchuk sums and attached estimates
Preserved the attached KravEstimate.tex unchanged in sources/. Added Section sec:kravchuk-sums in the transforms chapter, covering signed sums, raw/weighted square sums, entrywise absolute sums, boundary columns and a boundary asymptotic, with proofs. Corrected the attachment's missing summation and near-boundary factor two explicitly; original source untouched. Selected formulas from retained local sums manuscripts integrated, not their bibliography claims. Exact arithmetic checks through N=32; 4,084 counted checks, plus signed-total assertions. See sources/INTEGRATION_KravEstimate.md. Main PDF not rebuilt. Backup: project-archive/before-kravchuk-sums.zip.
