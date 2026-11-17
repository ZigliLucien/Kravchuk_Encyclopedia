# Gaussian--Krawtchouk summation and visible gap markers

All 30 existing TODO locations received visible uppercase topic markers; three were then replaced by the developed quadrature sections. A narrower unfinished classification of integral zeros has its own marker. There are now 28 visible NEEDS TO BE DONE markers, including partially unfinished appendix tables. The section "Krawtchouk transform" is a structural parent of developed subsections, not an empty topic.

The quadrature chapter uses N as the binomial support parameter and n as the Gaussian node count. Nodes are in the j coordinate, zeros of K_n(j;N). The measure is 2^-N binomial(N,j), not an unweighted sum. Rules: (N,n)=(5,3),(5,5),(10,5),(10,10),(15,8),(15,15). Their exactness degrees are 5,9,9,19,15,29. Off-lattice evaluations require a defined polynomial or function, not arbitrary discrete data without an interpolation convention.

Included derivations: monic recurrence, norms, symmetric Jacobi matrix, simple interior zeros, positivity and symmetry of weights, Gaussian exactness by division, Christoffel and derivative weights, smooth-function error, and the finite-support terminal rule. Integral-zero examples are not presented as a general classification.

Computed at 90-decimal precision with mpmath. JSON and CSV retain 65 significant digits; TeX tables show 18. All moments of (j/N)^r through degree 2n-1 checked, plus polynomial root residuals, independent Christoffel weights, and positivity. All scaled moment errors were below 1e-85. These are high-precision numerical checks, not rigorous interval enclosures. Reproduce with sources/compute_gaussian_krawtchouk.py (mpmath needed only to regenerate data; no extra TeX package required).

All labels, internal references, and chapter/table environments checked. No TeX compilation or visual layout check performed; main.pdf remains an older build. Historical backup: project-archive/before-gaussian-summation.zip.
