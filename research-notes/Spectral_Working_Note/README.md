# Spectral working note: integrated algebra version

Main file: Krawtchouk_Spectral_Working_Note.tex (standalone AMS article).
Lie_Algebra_Section.tex is a reusable extract already integrated in the main file; do not input it a second time.

The earlier long-form generation job failed without producing a draft. This source is the self-contained working note built from the conversation, the uploaded Feinsilver–Fitzgerald source, the 1999 Atakishiyev–Vicent–Wolf paper, and the supplied preliminary notes. It is separate from the sums paper and has not been included automatically in the Encyclopedia's main.tex.

Included material:
- exact finite sl(2) representation and T as an enveloping-algebra element;
- sign conjugation, positive parity blocks, and the common Perron eigenvector theorem;
- Gaussian Rayleigh quotients and a compact-window proof of the asymptotic lower bound;
- exact Mehler expansion of the candidate limiting kernel;
- quadratic oscillator sl(2), unitary dilation, squeezing, and imaginary-time evolution;
- normalization/coordinate dictionary for Atakishiyev–Vicent–Wolf;
- numerical evidence and the global estimates still needed for a full asymptotic equivalence.

Conventions: lattice parity and continuum Hermite parity are distinct; H_N is the positive finite operator, whereas the oscillator Hamiltonian is denoted script H. The dilation parameter is (1/4)log(2) in the AVW coordinate, but (1/2)log(sqrt(8)) when relating the standard y-coordinate oscillator to frequency sqrt(8).

Checks performed: exact finite commutators, T formula, anticommutation, positivity and commutation for N=4,6,10,12; continuum brackets on polynomial tests; symbolic Mehler coefficients; numerical table and Perron overlaps for N=4,10,20,50,100; LaTeX labels, citations, and environment nesting. The included Python script reproduces the numerical table.

No PDF compilation was performed: no pdflatex, tectonic, or latexmk binary was available. Compile the AMS source twice, or use latexmk -pdf where available.

Proof status: the liminf lower bound is established; the matching upper bound and global finite-to-continuum convergence remain open in this note. Bibliographic details are grounded in verified DOI records; the 1997 article is credited as an antecedent, not represented as fully read. The supplied unpublished notes are cited as such, without asserting public publication or novelty.
