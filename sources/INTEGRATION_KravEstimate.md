# KravEstimate attachment: preservation, corrections and integration

## Preservation
The attached KravEstimate.tex is saved unchanged at sources/KravEstimate.tex.
SHA256: 3b9f4415a956720e8b2a4c5fcb59a212e8cbc412bf8bc12deda3c302522d32a4.
The source itself is not corrected in place.

## Book location
A new section titled "Kravchuk sums", label sec:kravchuk-sums, is included at the end of the Krawtchouk Transforms chapter. Its source is chapters/kravchuk-sums.tex. Before this change there was no dedicated sums section in the active book; Gaussian--Krawtchouk summation is a different topic. The two retained standalone sums manuscripts were not previously directly input.

## Attachment checked and corrected in the book
1. Weighted row/column square identities and Cauchy--Schwarz estimates are correct in the book normalization.
2. The whole-matrix upper bound in the attachment drops the summation over j in one display. The correct bound is 2^N times the sum of binomial(N,j)^(-1/2), not one free-j term.
3. The general absolute sum of the near-boundary column is 2*binomial(N-1,floor((N-1)/2)), not the single binomial coefficient stated there. For even N this equals binomial(N,N/2), in agreement with the attachment's even case.
4. Counting both distinct near-boundary columns, for N>=3, gives the lower bound 2^(N+1)+4*binomial(N-1,floor((N-1)/2)). The attachment's written improvement has only 2*binomial(...). Its final Stirling-scale expression matches the corrected doubled-column contribution, not its immediately preceding lower-bound display.
5. The intermediate reciprocal-binomial estimate in the attachment has an arithmetic inconsistency in its last simplification. The book instead gives an explicit correctly counted unimodality bound using 2/sqrt(N)+2/sqrt(binomial(N,2))+(N-5)/sqrt(binomial(N,3)), valid for N>=6. This establishes the stated leading asymptotic without relying on that simplification. No claim is made here that the attachment's final coarse constant 5 is false.
6. Endpoint coincidences are handled explicitly: N=0 has one entry; the two near-boundary columns coincide at N=2.

## Additional selected results from retained local manuscripts
The book now contains exact signed row/column/total sums, a partial-column antiderivative, a spatial antiderivative, weighted-square identities, exact unweighted row/column/total square sums, absolute row evaluation by sign intervals, exact first and second boundary absolute column sums, the middle-column value, and a three-term boundary asymptotic for the total absolute sum. Proofs are included. This is selective integration, not certification of every theorem or bibliographic attribution in the standalone manuscripts.

The sharper asymptotic is reproduced with its boundary argument: total/(2^(N+1)) = 1 + sqrt(2/(pi*N)) + 4/(sqrt(2*pi*e)*N) + O(N^(-3/2)). Boundary columns 0,1,2 and their reflections give the three terms; the remaining columns are bounded by the reciprocal-binomial tail. This avoids treating entrywise absolute sums as signed sums or as an induced matrix norm.

## Verification
4,084 counted exact identity/bound checks through N=32, plus the signed-total assertion for every order. Integer/rational arithmetic checked raw signed sums, row/column square formulas, both weighted norms, total square formulas, absolute column bounds, boundary values and improved lower bounds. Table orders: N=5,10,15,20,32. sources/verify_kravchuk_sums.py reproduces these checks using only the Python standard library. JSON and CSV data are included. Finite checks support normalization and arithmetic; the asymptotic proof is analytic, not inferred from these table values.

No new literature metadata, publication priority or external citations were invented. The bibliography remains unchanged. No TeX compilation or PDF refresh was performed. Backup of edited existing files: project-archive/before-kravchuk-sums.zip.
