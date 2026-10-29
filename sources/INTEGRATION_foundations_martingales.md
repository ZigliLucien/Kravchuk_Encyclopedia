# Foundations and martingales: selective completion

## Source basis
The supplied `sources/KravFeinsKocik.tex`, especially its probabilistic discussion and "Multivariate Krawtchouk polynomials" subsection, supplies the centered product martingale, coefficient recurrence, finite-valued count construction, and multinomial norm identity. The existing book generating function fixes normalization throughout. No external bibliographic metadata or priority claims were added. Exterior-power traces, the biased generator, and exponential expansions are presented with their own derivations, not as quotations of an unverified source theorem.

## Nine sections completed
- 1-1: Pascal subset proof, Vandermonde convolution, signed specialization.
- 1-3: generating-function differential identity, recurrence, low-degree values and endpoints.
- 4-2: exterior traces, principal minors, determinant and supertrace identities.
- 5-1: product martingale, iterated sums, adapted recursion.
- 5-2: orthogonality, exact norms, completeness on the binomial lattice, Parseval identity.
- 5-3: finite-valued/multinomial construction and its limitation: a scalar-parameter family is not a complete multi-index system for more than two outcomes.
- 11-2: exact discrete stochastic equation and the Brownian/Hermite counterpart; no unproved functional convergence assertion.
- 13-2: separately named biased family, binomial weight, recurrence and reversible generator, with explicit symmetric-limit scaling and rate convention.
- 14-2: finite exponential expansion, including a denominator-free complex-parameter version.

## Validation
2,036 exact checks: symmetric and biased orthogonality; biased recurrence and generator through N=6 at p=1/3, 2/5, 1/2; every sign-history update through N=6; a three-valued multinomial model through N=4. Unique labels, resolved internal references and balanced chapter environments checked. These are source/algebra checks, not a TeX compilation or visual-layout check. No pdflatex/latexmk executable is available. Existing main.pdf remains an older supplied build.

## Not changed or claimed complete
Bilinear/Mehler kernels, Heisenberg sections, Clebsch--Gordan/Racah material, supersymmetry, FFT, historical sections, and research-level asymptotic claims remain for further source-specific development. The missing moments-updated manuscript has not been invented or reconstructed. Existing appendix tables and the 51-entry bibliography were not edited.

Backup: project-archive/before-foundations-martingales-integration.zip.
