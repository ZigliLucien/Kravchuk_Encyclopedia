# Kravchuk Encyclopedia - Review Report (2026-11-09)

Originals of every changed file are archived in project-archive/pre-review-2026-11-09.zip.

## 1. Title/content mismatches fixed
- Biography was inside the (archived) Introduction; moved to Appendix 6 (label app:biography), with chronology table and primary-source section (ref28). Introduction now points there.
- kravchuk-sums.tex was input at end of Ch. 14 (transforms); moved to pq-source-summary (KravSums source chapter), before "Scope of this integration".
- Ch. 15.1 now contains what its title promises: hypergeometric form K_n(j;N)=binom(N,n) 2F1(-n,-j;-N;2) (eq:K-hypergeometric) and the bilinear formula with closed kernel (eq:closed-bilinear).

## 2. Notation unified (also stated in front-matter Notation section)
- Binomial weight: pi_N (Ch. 5) -> w_N; pi_p (Ch. 13) -> w_{N,p}.
- Ch. 3 biased family C_n(i;N,p) -> Q_n^{(p)} via eq:biased-generating, with Q^{(1/2)} = 2^{-n} K_n.
- Ch. 11: oscillator H -> \mathcal H; OU generator G -> \mathcal L_OU (H=F+G and split unit G kept for the spin algebra). Remark added: analytic Mehler limit via the closed 2F1 kernel.

## 3. Appendices
- App. 1: added N=1, N=6 full tables; Phi_N for N=9..14 (all checked in exact arithmetic). Range now N=1..14.
- App. 2: general K_2..K_5 lattice formulas verified symbolically - correct.
- App. 3: numerical spectra of S_N, N=1..10, with residual check.
- App. 4: multivariate remarks pointing to Sec. 5.3 and sec:ency-sfa-ii.
- App. 5: still placeholder; depends on undefined Sec. 10.4.
- App. 6: biography (see above).

## 4. Recommended reorderings NOT applied (author decision)
- Move Ch. 13 (biased p case) earlier, right after the symmetric basics, since Ch. 3 now uses Q_n^{(p)}.
- Merge the empty Ch. 10 and Ch. 12 or drop until written.
- Reconsider placing pq-source-summary as an appendix-like source chapter rather than between Ch. 18 and the appendices.

## 5. Remaining placeholders ("NEEDS TO BE DONE")
Chapters 10, 12, 15.2 (addition formulas), 18; Sections 2.3-2.4, 9.3-9.5, 14.4, 16.2, 16.4; Appendix 5.

## 6. Build status — corrected
The actual fatal build error was the AMS matrix default of ten columns, not a demonstrated timeout. The largest tables have fifteen columns. Added \setcounter{MaxMatrixCols}{15} to main.tex and moved graphicx into the package block.

The corrected master compiles successfully (87 pages). The remote compiler cannot access local image files; the full portrait page was therefore typeset separately and merged in place of its blank page. The distributed source retains the original local-image inclusion for ordinary local builds. Matrix tables and portrait were visually checked. Original versions were archived before replacement.

Unfinished sections listed above remain marked; this correction does not claim their mathematical content has been supplied.

Final layout check: rewrote the two overlong general lattice formulas in Appendix 2 in equivalent centered-factor form. The final 87-page PDF passes the structural checker with no off-page glyphs; the portrait, largest matrix table and corrected formula page were visually inspected.
