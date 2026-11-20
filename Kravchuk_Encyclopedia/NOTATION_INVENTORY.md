# Kravchuk Encyclopedia: notation inventory for editorial decisions

This is a notation decision worksheet. The author-approved basic finite-matrix notation has now been propagated through the master exposition; other entries remain candidates for review.

## Scope and reading key

The inventory is based on the current master source, its included chapters and appendices, and the source dictionaries integrated into them. It is not a claim to catalogue every dummy variable in every archived research manuscript. Original-source symbols below are reported from the Encyclopedia's explicit dictionaries unless otherwise stated.

Sources such as “Ch. 6” mean both the topical chapter in `06-chapter.tex` and its printed chapter number. The Introduction is now unnumbered front matter, so Chapters 1–18 match their filenames; the source-conventions chapter is Chapter 19. “PQ” means `chapters/pq-source-summary.tex`, integrating `sources/KravPQ.tex` and `sources/KravSums.tex`; “Sums” means `chapters/kravchuk-sums.tex`, included in PQ. “Kocik dictionary” means the explicit source-to-book dictionary in `main.tex` and the integrated Kocik material.

- **Alias**: the same object, with the stated coordinates and conventions.
- **Scaled**: related by normalization, coordinate change, restriction or parameter interchange; not safe for literal replacement.
- **Collision**: the same symbol, or a dangerously similar form, has different meanings.
- **Distinct**: a separately defined object; no competing name found in the audited definitions. This does not assert global uniqueness in all retained source files.
- **Local**: a contextual variable or construction, not a proposed global name.

The three columns are intentionally retained. Status and normalization warnings appear in the names column. A semicolon in column one groups related notation, not necessarily equal objects.

## Author-approved fixed notation

These explicit choices take precedence over the general source-priority rule. Subscripts $N$ may be retained when the order needs to be displayed.

| Notation | Name(s) and fixed convention | Source(s) |
|---|---|---|
| $R,L,A$ | Keep the finite raising and lowering matrices and $A=R+L$, with the existing basis-index conventions. | Author's explicit decision; Ch. 6 |
| $\Lambda=[L,R]$ | Keep the diagonal commutator matrix, with ordinary commutator and entries $N-2j$. | Author's explicit decision; Ch. 6 |
| $\Phi$ | Keep the raw generating-function matrix: $(1+v)^{N-j}(1-v)^j=\sum_{n=0}^N\Phi_{nj}v^n$. | Author's explicit decision; Ch. 1 |
| $J$ | Keep the reversal operator, $Je_j=e_{N-j}$. | Author's explicit decision; Ch. 8 |
| $\sigma$ | Use the diagonal sign operator, $\sigma e_j=(-1)^je_j$; replaces the current parity notation $D_N$ in the exposition when substitutions are applied. | Author's explicit decision; Ch. 8 |
| $S=\Phi B$ | Keep the symmetric weighted Kravchuk matrix, with $B=\operatorname{diag}(\binom Nj)$. This is not the orthogonal normalization of $\Phi$. | Author's explicit decision; Ch. 16 |

Applied in the master exposition: parity is now $\sigma_N$, reversal is $J_N$, and the reserved anticommuting matrix is $T_N$. Former conflicting uses of $T_N$ for a transition matrix and a full tensor transform are now $\mathsf P_N$ and $\mathbf H_N$. Original source files and standalone research-note manuscripts have not been rewritten.

## Approved editorial rule: priority over Kocik notation

The author has decided that conflicting notation in Kocik's Feynman–Krawtchouk treatment is to yield to the more standard notation used in the other sources. Kocik's notation is not a competing candidate when such a conflict exists. This rule governs the Encyclopedia's exposition of that material; retained original source files are left unchanged for provenance.

This is a source-priority decision, not an assertion that all other sources agree. Where the other sources themselves conflict, the preferred symbol still needs to be selected. Source dictionaries remain as translation aids, not parallel notation systems in the main exposition. The fixed basic-notation substitutions have been applied; remaining source conflicts await decisions.

| Notation in the Kocik dictionary | Name(s) and preferred Encyclopedia treatment | Source(s) |
|---|---|---|
| Total order $n$; row $p$; column $q$ | Translate to $N,n,j$, respectively, as already recorded in the current dictionary. | Main notation dictionary |
| Matrix $K$ | Translate to raw Krawtchouk matrix $\Phi_N$ under the current dictionary; do not identify with weighted $S_N$ or orthogonal $U_N$. | Main notation dictionary; Chs. 1, 14 |
| Kac matrix $M$ | Translate to $A_N$. | Main notation dictionary; Ch. 6 |
| Commutator operator $N=[L,R]$ | Translate to $\Lambda_N$ in the fixed-order matrix realization; reserve scalar $N$ for order. | Main notation dictionary; Ch. 6 |
| Binomial metric $\Gamma$ | Translate to $B_N$ for this object under the current dictionary; distinguish PQ's norm matrix $\Gamma$. | Main notation dictionary; PQ |
| Pascal matrix $B$ | Translate to $P_N$; distinguish both diagonal binomial and probability-weight matrices. | Main notation dictionary; Ch. 14 |
| Half-commutator | Use ordinary commutator $[X,Y]=XY-YX$ in the Encyclopedia and adjust all factors of two accordingly. | Main notation dictionary; Ch. 6 |
| Split-quaternion units $i,F,G$, Hadamard $H$, and their descendants | These symbols have no priority over conflicting notation in the other sources. Choose unambiguous replacements after checking the remaining inventory; preserve the actual algebra and distinguish group from differential lifts. | Chs. 6–9; remaining notation worksheet |

## A. Polynomial families and their normalizations

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| $K_n(j;N)$ | Symmetric ordinary-coefficient Krawtchouk polynomial: $[v^n](1+v)^{N-j}(1-v)^j$. **Collision** with the factorial-normalized $K_n(x,N)$ in PQ. | Ch. 1, “Krawtchouk polynomials”; throughout symmetric chapters |
| $k_n(x,N)$ | Monic centered Krawtchouk polynomial; $x=N-2j$, $k_n(N-2j,N)=n!K_n(j;N)$. **Scaled**, not a literal alias. | Chs. 1, 5, 11, 13; Appendix 2 |
| $K_n(x,N)$ in PQ | General-parameter exponential-coefficient family: $\sum K_n(x,N)v^n/n!=(1+2qv)^{N-j}(1-2pv)^j$. At $p=q=1/2$, this is $k_n(x,N)$, not the earlier $K_n(j;N)$. **Collision/scaled**. | PQ, “The two source conventions”; `KravPQ.tex` convention |
| $\Phi^N_{nj}$ | Symmetric sums-paper coefficient; $\Phi^N_{nj}=K_n(j;N)=(\Phi_N)_{nj}$. **Alias at entry level**, not a matrix-to-scalar equality. | PQ; sums-paper convention in `KravSums.tex` |
| $\phi^N_{nj}$ | General sums-paper coefficient: $[z^n](1+z)^{N-j}(1-rz)^j$. **Scaled** relative to the PQ family: $K_n(N-2j,N)=n!(2q)^n\phi^N_{nj}$, $r=p/q$ in PQ parameters. | PQ, source dictionary |
| $Q_n^{(p)}(j;N)$ | Biased ordinary-coefficient family: $[v^n](1+pv)^{N-j}(1-qv)^j$, $q=1-p$. Orthogonal for $\operatorname{Bin}(N,p)$. **Scaled**: $Q_n^{(1/2)}=2^{-n}K_n$. | Ch. 13, “Nonsymmetric case”; Ch. 3 cumulative trials |
| $K_n^{\mathrm{PQ}}(N-2j,N)=2^n n!Q_n^{(q)}(j;N)$ | **Derived bridge**, using PQ's $q=1-p$ and the parameter convention in the preceding row. The superscript “PQ” here is an inventory label, not a current source notation. Parameter exchange is essential. | Comparison of PQ generating function and Ch. 13 generating function |
| $Q_n(\boldsymbol\nu)$ | Scalar-degree polynomial of a multinomial count vector, generated using one centered contrast $\xi_r-\mu$. **Collision** with $Q_n^{(p)}$ in typography; not generally a complete multi-index Krawtchouk family. | Ch. 5, “Krawtchouk polynomials and multinomial distribution” |
| $p_{n,N}(j)$ | Binomial-measure orthonormal polynomial $K_n(j;N)/\sqrt{\binom Nn}$. **Scaled**. | Ch. 11, “Bilinear kernels and the Mehler limit” |
| $\psi_{n,N}(j)$ | Counting-measure orthonormal function $\sqrt{w_N(j)}p_{n,N}(j)$. **Scaled**; distinguish polynomial and weighted function. | Ch. 8, “Hilbert space structure” |
| $p_n(j)$ | Monic polynomial in the lattice coordinate $j$: $(-1)^n n!K_n(j;N)/2^n$. **Scaled**; not $p_{n,N}$. | Ch. 17, “Zeros of Krawtchouk polynomials” |
| $k_{N+1}(x,N)$ | Terminal monic polynomial $\prod_{j=0}^N(x-(N-2j))$. Vanishes on the support; not an additional positive-norm orthogonal mode. | Ch. 13 terminal-polynomial remark; Ch. 17 |
| $\operatorname{He}_n(\xi)$ | Probabilists' Hermite polynomial, generated by $e^{\xi t-t^2/2}$. **Distinct normalization**. | Ch. 11, “Hermite polynomials” |
| $H_n(x,t)$ | Time-dependent Hermite/heat polynomial, generated by $e^{ux-tu^2/2}$; $H_n(x,1)=\operatorname{He}_n(x)$. Do not silently read it as the physicists' one-variable $H_n$. | Ch. 11, “Discrete stochastic differential equations”; main notation section |
| ${}_2F_1$; $(t)_n$ | Gauss hypergeometric function; rising factorial. The rising factorial at $t=-N$ encodes termination, and is not a binomial coefficient. | Ch. 15, hypergeometric and bilinear formulas |

## B. Finite matrices, lifts, and coordinate systems

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| $\Phi_N$; source $K$ | Raw Krawtchouk matrix $(K_n(j;N))_{n,j=0}^N$. **Alias** for the source matrix $K$ under the book's dictionary. Not $S_N$ or $U_N$. | Ch. 1; Chs. 8, 14; main Kocik dictionary |
| $B_N$; source $\Gamma$ | Diagonal binomial matrix $\operatorname{diag}\binom Nj$. **Alias** under the Kocik dictionary. **Collision** with the weighted $B$ and norm matrix $\Gamma$ in PQ. | Chs. 1, 8, 14; main Kocik dictionary |
| $S_N$ | Symmetric weighted matrix $\Phi_N B_N$. **Distinct/scaled**; symmetry is not orthogonality, and its eigenvalues are not those of $\Phi_N$. | Ch. 16, “Symmetric matrices”; Appendix 3 |
| $U_N$ | Orthogonal symmetric transform $2^{-N/2}B_N^{-1/2}\Phi_NB_N^{1/2}$. **Scaled** raw transform. | Ch. 14, “Orthogonal transformation associated to K”; Chs. 6, 9 |
| $R_N$; $R=\eta\partial_\xi$ | Basis-index raising matrix/operator, $R_Ne_j=(N-j)e_{j+1}$. **Same action in specified coordinates**, not the angular-momentum $J_+$. | Ch. 6, finite matrices and differential-operator dictionary |
| $L_N$; $L=\xi\partial_\eta$ | Basis-index lowering matrix/operator, $L_Ne_j=je_{j-1}$. **Same action in specified coordinates**. | Ch. 6 |
| $A_N$; source $M$; $d\rho_N(F)$ | Kac matrix $R_N+L_N$. **Alias** under the integrated source and representation dictionaries. | Chs. 2, 6, 8, 13; main Kocik dictionary |
| $\Lambda_N$; $\mathsf N_N$; source operator $N$; $d\rho_N(G)$ | Diagonal commutator $[L_N,R_N]=\operatorname{diag}(N-2j)$. **Aliases** in the fixed-order representation. Not the scalar $N$. | Chs. 6, 8, 13; main Kocik dictionary |
| $\mathbf H=\xi\partial_\xi-\eta\partial_\eta$ | Cartan differential operator with matrix $\Lambda_N$. **Approved:** boldface Cartan operator; oscillator $\mathcal H$ remains distinct. | Ch. 6, “Differential-operator dictionary” |
| $\mathcal E$ | Euler operator $\xi\partial_\xi+\eta\partial_\eta=NI$ on degree $N$. **Distinct** from $\Lambda_N$ and the preceding Cartan operator. | Ch. 6 differential-operator dictionary |
| $C=B_N^{1/2}$; $\widehat M=C^{-1}MC$ | Binomial basis change; matrix of an arbitrary operator in orthonormal coordinates. **Local/scaled**. This local basis-change symbol should not be assigned a second global meaning without checking source conventions. | Ch. 6 angular-momentum dictionary |
| $\widehat R,\widehat L,\widehat A,\widehat\Lambda$ | Orthonormal-coordinate versions of $R_N,L_N,A_N,\Lambda_N$; $\widehat L=\widehat R^*$. **Scaled**, not entrywise aliases. | Ch. 6 |
| $P_N$; source $B$ | Triangular Pascal matrix $(\binom{k}{i})_{i,k=0}^N$. **Alias** under the Kocik dictionary. Not the diagonal $B_N$, nor a stochastic $P$. | Ch. 14, “Binomial bases and dual transforms”; main dictionary |
| $c^{(k)}$ | Column $k$ of $P_N$, entries $\binom{k}{i}$. **Distinct/local**. | Ch. 14 |
| $J_N$; $\rho_N(F)$ | Reversal matrix, $J_Ne_j=e_{N-j}$. **Alias**; not the generator $d\rho_N(F)=A_N$. | Ch. 8; Ch. 14 |
| $\sigma_N$; $\rho_N(G)$ | Parity matrix $\sigma_Ne_j=(-1)^je_j$. **Alias**; not the generator $d\rho_N(G)=\Lambda_N$. | Ch. 8 |
| $W_N$ | Powers-of-two diagonal $\operatorname{diag}(2^0,\ldots,2^N)$; $P_N^{-1}\Phi_NP_N=J_NW_N$. **Distinct** from parity and binomial weights. | Ch. 14 |
| $\widehat\Phi_{nj}$ in PQ | Ordinary coefficient $K_n(N-2j,N)/n!$ of PQ's general family. **Collision risk** with hats denoting orthonormal basis changes elsewhere. | PQ, “Orthogonality and inversion” |
| $B$ in PQ | Probability-weight matrix $\operatorname{diag}(\binom Nj p^{N-j}q^j)$. **Collision** with source Pascal $B$; not $B_N$. | PQ, orthogonality and inversion |
| $\Gamma$ in PQ | Squared-norm matrix $\operatorname{diag}(\binom Nn(4pq)^n)$. **Collision** with source $\Gamma=B_N$ in the Kocik dictionary. | PQ; main Kocik dictionary |
| $A^{[N]}$; $P^{[N]}$ | Degree-$N$ induced matrix in the stochastic occupation basis. **Distinct coordinate convention**: do not identify entrywise with an arbitrary symmetric-power matrix. | Ch. 3, “Induced matrices and multinomial chains” |
| $\rho_N(g)$ | Multiplicative group representation on homogeneous polynomials: $p(x,y)\mapsto p(ax+cy,bx+dy)$. | Ch. 8, “Splitting formula” |
| $d\rho_N(X)$ | Differential/additive Lie-algebra representation. **Distinct** from $\rho_N(X)$ as a multiplicative substitution. | Chs. 6, 8 |
| $H^{\otimes N}$ | Full-cube Hadamard tensor transform. Restriction in orbit-average coordinates has matrix $\Phi_N$. **Restriction**, not equality of full matrices. | Ch. 9, “Hadamard compression” |
| $\mathcal A_N=\sum_rF_r$ | Full-cube adjacency operator; symmetric-sector matrix is $A_N$. **Restriction**; dimension changes from $2^N$ to $N+1$. | Ch. 9 |
| $\mathcal G_N=\sum_rG_r$ | Full-cube diagonal sign-sum operator; symmetric-sector matrix is $\Lambda_N$. **Restriction**. | Ch. 9 |
| $s_j$; $a_j=s_j/\binom Nj$; $q_j=s_j/\sqrt{\binom Nj}$ | Orbit sums; orbit averages; orthonormal orbit vectors. **Scaled** bases. Raw transform matrices depend on this choice. | Ch. 9 |
| $e_j$; $\xi^{N-j}\eta^j$; $x^{N-j}y^j$ | Coordinate basis and its homogeneous-monomial realization. **Alias by realization**; two different pairs of auxiliary variables remain in use. | Chs. 6, 8 |
| $f_j=\sqrt{\binom Nj}\,e_j$; $\lvert j\rangle$ | Orthonormal basis for the $B_N^{-1}$ column metric; orthonormal coordinate ket. **Scaled**, not the same coordinates as $e_j$. | Ch. 6 |
| $\phi_j$ | Column $j$ of $\Phi_N$. **Collision risk** with sums-paper scalar $\phi^N_{nj}$. | Ch. 8, column/covector metrics |
| $v_k^\pm$ | Explicit eigenvectors of raw $\Phi_N$ built from complementary Pascal columns. **Distinct** from eigenvectors of weighted $S_N$. | Ch. 14 |

| $T_N$ | **Fixed:** skew-symmetric anticommuting matrix $(\Lambda_N-NI)R_N+(\Lambda_N+NI)L_N$, with $T_NS_N=-S_NT_N$. Not the transition matrix or the full tensor Hadamard transform. | Ch. 16, “The matrix T” |
| $\mathsf P_N=A_N/N$ | Column-stochastic Ehrenfest transition matrix, renamed from the conflicting $T_N$; backward matrix is its transpose. | Ch. 2, “Transition probabilities” |

## C. Probability, weights, martingales, and kernels

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| $b_j=\binom Nj$ | Unnormalized binomial multiplicity. **Alias** for an entry of $B_N$, not a probability. **Collision** with Jacobi off-diagonal $b_r$ in Ch. 17. | Ch. 9; Ch. 14; Sums |
| $w_N(j)$ | Symmetric binomial probability $2^{-N}\binom Nj$. **Scaled** binomial multiplicity. | Main conventions; Chs. 3, 5, 8, 11 |
| $w_{N,p}(j)$ | Biased binomial probability $\binom Njp^jq^{N-j}$. PQ instead weights $j$ by $\binom Njq^jp^{N-j}$; the parameter letters must be interchanged. | Main conventions; Chs. 3, 13; PQ |
| $\mu_N$; $\mathcal S_N[f]$ | Discrete measure $\sum_jw_N(j)\delta_j$; integration/summation functional against it. **Same probability law, different mathematical types**. | Ch. 17 |
| $\Pi_N(\mathbf n)$ | Stationary multinomial probability $N!\prod_a\eta_a^{n_a}/\prod_a n_a!$. **Distinct multivariate analogue**, not the binary $w_N$ without specialization. | Ch. 3, induced matrices |
| $\boldsymbol\eta$ | Stationary one-site probability vector. **Collision risk** with scalar auxiliary $\eta$ in Ch. 6 and Lorentz metric $\eta$ there. | Ch. 3 |
| $J_{ab}=\eta_aP_{ab}$ | Stationary input-output one-site joint law. **Distinct** from reversal matrix $J_N$, angular momenta $J_a$, and Jacobi matrix $\mathcal J_{N,n}$. | Ch. 3 |
| $c_{ab}$ | Contingency-table counts with row and column margins $\mathbf n,\mathbf m$. **Local**. | Ch. 3 |
| $P$ in Ehrenfest model | Backward transition operator $(Pf)(j)=(N-j)f(j+1)/N+jf(j-1)/N$. Its matrix on function columns is $A_N^T/N$; the forward matrix on probability columns is $A_N/N$. **Transpose warning**. | Ch. 3, first and final sections |
| $P$ in induced-chain model | Row-stochastic one-site matrix. **Collision of scope** with the preceding occupation-level $P$, not the Pascal $P_N$. | Ch. 3, SFA II and cumulative trials |
| $Q$ in $P_t=e^{tQ}$ | One-site continuous-time Markov generator. **Collision** with quadratic form $Q$ and polynomial families $Q_n$. | Ch. 3 |
| $\mathcal L_N$ | Occupation generator induced from one-site $Q$. **Distinct** from finite lowering matrix $L_N$. | Ch. 3 |
| $\mathcal L_p$ | Biased birth-death refresh generator with eigenvalues $-n$ on $Q_n^{(p)}$. At $p=1/2$ it is half the sign-flip generator with eigenvalues $-2n$. **Time-scaling warning**. | Ch. 13 |
| $\mathcal K(j\mid i)$ | Cumulative-trial transition probability from $i$ successes to $j$. Backward operator has the same symbol. **Distinct** from a polynomial $K_n$ and from a density-ratio kernel. | Ch. 3, cumulative Bernoulli trials |
| $b(j;m,p)$ | Binomial probability mass for $m$ trials. **Collision risk** with binomial multiplicity $b_j$ and quadrature $b_r$. | Ch. 3 |
| $\alpha$; $\beta$ | Save-success probability; retry-success probability. **Local model parameters**. | Ch. 3 |
| $r=\alpha(1-\beta)$ | Nonconstant one-site eigenvalue/correlation; occupation eigenvalues are $r^n$. **Collision** with sums-paper ratio $r=q_{\rm S}/p_{\rm S}$. | Ch. 3; Ch. 11 |
| $r_1,\ldots,r_{q-1}$ | Nonconstant one-site eigenvalues in a multistate chain. **Generalization** of the binary spectral $r$. | Ch. 3 |
| $m_{r,N}(k,\ell)$ | Finite density-ratio/Poisson kernel $\sum_nr^np_{n,N}(k)p_{n,N}(\ell)$. Transition probability equals $m_{r,N}(k,\ell)w_N(\ell)$. **Not** the raw transition matrix. | Chs. 11, 15 |
| $m_r(x,y)$ | Gaussian Mehler density ratio relative to $d\mu=w(x)dx$. **Limit analogue**, not the Lebesgue-measure oscillator kernel. | Ch. 11 |
| $\epsilon_a$; $X_m=\sum_{a=1}^m\epsilon_a$ | Independent symmetric signs; centered random-walk sum. At time $N$, count $J=(N-X_N)/2$. **Coordinate relation**, not equality of random variables. | Chs. 4, 5, 9 |
| $M_m(v)$ | Product martingale $\prod_{a=1}^m(1+v\epsilon_a)$. **Collision risk** with source Kac matrix $M$ and PQ scalar function $M(z)$. | Ch. 5 |
| $\mathcal F_m$ | Filtration generated by the first $m$ signs. **Distinct** from any Fourier-transform notation in separate lecture notes. | Ch. 5 |
| $E_n(m)$; $e_n(\epsilon_1,\ldots,\epsilon_m)$ | Iterated symmetric sum; $E_n(m)=k_n(X_m,m)/n!$. **Alias at a random configuration**. | Ch. 5; Ch. 4 elementary symmetric functions |
| $E_n$ in twiston model | Interaction energy $K_n(j;N)$ for a fixed sign configuration. **Same symmetric-sum construction**, different probabilistic context from $E_n(m)$. | Ch. 9, “Twistons” |
| $e_n(z_1,\ldots,z_N)$ | Elementary symmetric polynomial. For signs with $j$ negatives it equals $K_n(j;N)$. **Specialization**, not a general identity for arbitrary $z_a$. | Ch. 4 |
| $\mathcal G_{\boldsymbol\nu}(v)$ | Product generating function for a finite-valued multinomial sample and one scalar contrast. **Collision risk** with full-cube $\mathcal G_N$. | Ch. 5 |
| $Y_a$; $\xi_r$; $p_r$; $\mu$; $\sigma^2$ | Finite-valued observations; possible values; category probabilities; mean; variance. **Local**. Scalar $\mu$ here is not Gaussian measure $\mu$ in Ch. 11. | Ch. 5 |
| $\boldsymbol\nu$ | Count vector in Ch. 5, but spectral occupation multi-index in Ch. 3. **Collision of role**, not always the same indexing set. | Chs. 3, 5 |

## D. Lie algebras, spin, and oscillator notation

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| $F$ | Real flip matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$; split-quaternion unit; one-site bit flip. **Aliases in the chosen realization**. | Chs. 6–9 |
| $G$ | Diagonal split unit $\operatorname{diag}(1,-1)$. **Distinct** from generating functions $G_N$, $G_{N,j}$ and $\mathcal G$. | Chs. 6–9 |
| $H=F+G$ | Unnormalized two-dimensional Hadamard matrix. **Distinct** from $H_n(x,t)$ and from oscillator $\mathcal H$. | Main conventions; Chs. 7–9 |
| $i$ | Real split-quaternion matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. **Collision** with lattice index $i$ and visually with scalar imaginary unit $\mathrm i$. | Ch. 6; Ch. 7 |
| $\mathrm i$ | Scalar imaginary unit. Typographically distinguished from the preceding real matrix, but not a safe plain-text replacement. | Ch. 6 angular momentum; Ch. 7 complex normalization |
| $\mathbb H_s$ | Split-quaternion algebra, realized as $M_2(\mathbb R)$. **Distinct**. | Ch. 6 |
| $q=a+bi+cF+dG$; $\overline q$; $\operatorname N(q)$ | Generic split quaternion, its conjugate, and norm $a^2+b^2-c^2-d^2$. **Collision**: $q$ also means complementary probability and number of states. | Ch. 6 |
| $Q(t,x,y)$ | Lorentz quadratic form $t^2-x^2-y^2$ on pure split quaternions. **Collision** with Markov generator $Q$. | Ch. 6 |
| $\eta=\operatorname{diag}(1,-1,-1)$ | Lorentz metric matrix. **Collision** with homogeneous auxiliary variable $\eta$ and stationary vector $\boldsymbol\eta$. | Ch. 6 |
| $[X,Y]$ | Ordinary commutator $XY-YX$. The integrated source also uses a half-commutator; factors of two must not be dropped. **Convention warning**. | Main Kocik dictionary; Ch. 6 |
| $\operatorname{ad}_X$ | Adjoint Lie-algebra action $Y\mapsto[X,Y]$. **Distinct** from multiplicative conjugation by a group element. | Ch. 6 |
| $r_u(v)$ | Reflection $-uvu^{-1}$ for a non-null pure quaternion $u$. **Distinct** from spectral parameter $r$. | Ch. 7 |
| $J_+=\hbar\widehat L$; $J_-=\hbar\widehat R$ | Angular-momentum raising and lowering. **Scaled and oppositely named relative to the lattice-index direction**: raising magnetic number lowers $j$. | Ch. 6 angular-momentum dictionary |
| $J_x,J_y,J_z$ | Hermitian spin operators, with $J_x=\hbar\widehat A/2$, $J_z=\hbar\widehat\Lambda/2$. **Scaled** finite generators, not reversal $J_N$. | Ch. 6 |
| $s=N/2$; $m=s-j$ | Spin and magnetic quantum number. **Collision of scope**: $m$ elsewhere denotes time, a count, or an index. | Ch. 6 |
| $\lvert s,m\rangle=\lvert j\rangle$ | Spin basis and orthonormal occupation basis under $m=s-j$. **Alias by relabeling**. | Ch. 6 |
| $d^{(s)}_{m',m}(\theta)$ | Wigner small-$d$ rotation matrix element. Related to $U_N$ at a quarter turn by a stated parity factor, not a literal alias. | Ch. 6 |
| $\mathcal H=\tfrac12(x^2-D^2)$ | Harmonic-oscillator Hamiltonian. **Actual unresolved collision** with Cartan $\mathcal H$ in Ch. 6; the front matter's reservation is not yet globally enforced. | Main conventions; Ch. 11 |
| $D=d/dx$ | Spatial differentiation operator. **Collision** with diagonal sign operator $D$ in Ch. 4; distinguish finite parity $\sigma_N$. | Ch. 11; PQ; Ch. 4 |
| $\mathcal L_{\mathrm{OU}}$ | Ornstein–Uhlenbeck generator $D^2/2-xD$ for Gaussian variance $1/2$. **Distinct** from $\mathcal L_p$ and $L_N$. | Ch. 11 |
| $U:f\mapsto w^{1/2}f$ | Unitary change from Gaussian-weighted to Lebesgue $L^2$. **Collision risk** with finite orthogonal transform $U_N$; related constructions, not the same operator. | Ch. 11 |
| $w(x)=\pi^{-1/2}e^{-x^2}$; $d\mu=w(x)dx$ | Gaussian density and probability measure, variance $1/2$. **Distinct mathematical types**; $\mu$ also denotes a mean in Ch. 5. | Ch. 11 |
| $B_t$ | Standard Brownian motion. **Collision risk** with binomial matrix $B_N$ and source matrices $B$. | Ch. 11 |

## E. Sums, transforms, and quadrature

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| $\operatorname{RowS}_n$; $\operatorname{ColS}_n$ | **Approved:** unweighted signed sum of row n and column n, respectively. Replaces former $R_n$ and $C_j$ (with the column index relabeled). Level N is suppressed. | Sums; author notation decision |
| $\operatorname{SqRowS}_n$; $\operatorname{SqColS}_n$ | **Approved:** sum of squared entries of row n and column n. Replaces former Q superscript row/column notation; these are not squares of the signed sums. | Sums; author notation decision |
| $A_n^{\mathrm{row}}$; $A_j^{\mathrm{col}}$ | Raw row/column sums of absolute values. **Collision risk** with Kac matrices $A_N$. | Sums |
| $T_1(N)$; $T_2(N)$; $T_{\mathrm{abs}}(N)$ | Whole-matrix signed, square, and absolute-value totals. **Distinct** from tensor transform $\mathbf H_N$. | Sums |
| $r_N$ | Integer threshold $\lfloor(N-\sqrt N)/2\rfloor$ for a boundary-column absolute-sum formula. **Distinct** from spectral $r$ and sums ratio $r$. | Sums |
| $\widehat f_n$ | Coefficients in the raw symmetric $K_n(j;N)$ basis; norm denominator $\binom Nn$. **Scaled/context-dependent**, not automatically PQ's coefficients. | Ch. 5 orthogonal functionals |
| $\widetilde f(n)$ | Coefficients in PQ's factorial-normalized $K_n(x,N)$ basis. **Distinct** from $\widehat f_n$ unless coordinates and normalizations are converted. | PQ, “Operator coefficients and positivity” |
| $M(z)$; $V(z)$ | PQ coefficient-extraction functions $M(z)=pe^z+qe^{-z}$, $V(z)=\sinh z/M(z)$. **Local**; $M$ is also a source Kac matrix. | PQ |
| $\mu_N$; $\mathcal S_N$ | Binomial quadrature measure and weighted-sum functional. Repeated here to distinguish them from $S_N$. **Collision risk**, not alias. | Ch. 17 |
| $h_r$ | Squared norm of monic lattice polynomial $p_r$: $(r!)^2\binom Nr/4^r$. **Scaled** raw Krawtchouk norm. | Ch. 17 |
| $\mathcal J_{N,n}$ | Symmetric Jacobi matrix for the $n$-node quadrature rule. **Distinct** from reversal $J_N$ and angular momentum $J_a$. | Ch. 17 |
| $b_r=\tfrac12\sqrt{r(N-r+1)}$ | Jacobi off-diagonal entry. **Actual collision** with $b_j=\binom Nj$ when indices are renamed. | Ch. 17 versus Ch. 9 and Sums |
| $z_1,\ldots,z_n$; $\lambda_1,\ldots,\lambda_n$ | Gaussian quadrature nodes and weights. **Local**; $z$ is also a generating-function variable. | Ch. 17 |
| $D=\operatorname{diag}(z_1,\ldots,z_N)$ | Diagonal scalar/sign operator used in determinant and exterior-power identities. **Collision** with differentiation $D$. | Ch. 4 |
| $\mathsf X$; $\bigwedge^n\mathsf X$ | General linear map and its multiplicative exterior power; renamed from T to reserve T for the anticommuting matrix. **Distinct** from tensor Hadamard $\mathbf H_N$ and differential/additive exterior action. | Ch. 4 |

## F. Parameters and coordinates requiring explicit scope

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| $N$ | Total order, number of binary sites, or sample size. Source $N$ can instead mean the commutator operator; the Kocik dictionary renames that operator $\Lambda_N$. **Major collision**. | Throughout; main dictionary; Ch. 6 |
| $n$ | Usually polynomial degree or row index. In the integrated Kocik source, total order $n$ maps to book $N$. | Ch. 1; main Kocik dictionary |
| $j$ | Usually lattice count/column index; $x=N-2j$. Must not also denote physical spin without changing conventions. | Throughout symmetric chapters; Ch. 6 |
| $p,q$ | Complementary probabilities in Ch. 13; PQ uses opposite roles for which count is weighted by $p$; Kocik source uses $p,q$ as matrix indices. **Major scope collision**. | Ch. 13; PQ; main dictionary |
| $p_{\rm S},q_{\rm S}$ | Sums-paper probability parameters, related to PQ by $p_{\rm S}=q$, $q_{\rm S}=p$. These explicit subscripts distinguish source roles. | PQ parameter warning |
| $q$ as state count; $d$ as state count | Number of categories is $q$ in Ch. 3, $d$ in Ch. 5. **Same type of parameter, different symbols**; scalar-contrast and full multi-index models remain different constructions. | Chs. 3, 5 |
| $x=N-2j$ | Centered finite-lattice coordinate. **Scaled** relative to the continuum $x$ of Ch. 11. | Chs. 1, 13; PQ |
| $\xi=x/\sqrt N$ | Variance-one central-limit coordinate for probabilists' Hermite polynomials. **Collision risk** with auxiliary homogeneous $\xi$ and category values $\xi_r$. | Ch. 11 versus Chs. 5, 6 |
| $x_k=(N-2k)/\sqrt{2N}$; $\delta_N=\sqrt{2/N}$ | Oscillator-coordinate lattice and its spacing; Gaussian variance $1/2$. **Scaled**: probabilists' coordinate equals $\sqrt2x_k$. | Ch. 11 |
| $x,y$; $\xi,\eta$ | Homogeneous auxiliary variables are $x,y$ in Ch. 8 and $\xi,\eta$ in Ch. 6. **Aliases by renaming only within that construction**, not globally interchangeable with lattice/Gaussian coordinates. | Chs. 6, 8 |
| $v,z,u,w,t$ | Generating-function dummy variables in different sections; some also denote time or spatial coordinates. **Local**; never candidates for blind global replacement. | Chs. 1, 5, 11, 14, 15; PQ |
| $t$ | Brownian time, semigroup time with $r=e^{-t}$, hypergeometric parameter, or a Lorentz coordinate. **Scope collision**. | Chs. 6, 11, 15 |
| $G_{N,j}(v)$; $G_N(x,v)$ | Same centered symmetric generating function after $x=N-2j$. **Alias after coordinate conversion**; bare PQ $G(v)$ is generally biased. | Chs. 1, 11; PQ |

## G. Historical notation already changed, not active alternatives

These are recorded to avoid reintroducing an older convention from a previous PDF or research-note revision.

| Notation | Name(s), identification and status | Source(s) |
|---|---|---|
| Former $\pi_N$ | Symmetric binomial weight, now $w_N$ in the reviewed Encyclopedia. Not listed as an active master-source synonym. | Review report: Ch. 5 change |
| Former $\pi_p$ | Biased binomial weight, now $w_{N,p}$. | Review report: Ch. 13 change |
| Former $C_n(i;N,p)$ | Biased family replaced by the explicitly defined $Q_n^{(p)}$. Recheck the earlier generating function before mapping any archived occurrence. | Review report: Ch. 3 change |
| Former oscillator $H$; former OU $G$ | Now $\mathcal H$ and $\mathcal L_{\mathrm{OU}}$ in Ch. 11. The new $\mathcal H$ still collides with Ch. 6's Cartan differential operator. | Review report; current Chs. 6, 11 |

## First decisions to make

1. Choose distinct names for the Cartan differential operator and oscillator Hamiltonian: **the unresolved $\mathcal H$ collision is real**.
2. Decide whether the three Krawtchouk families (raw symmetric, monic centered, biased source) should have separate global symbols or explicit normalization labels.
3. Choose the probability convention for $p$: probability of the counted category or its complement. Record source translations rather than changing source parameters implicitly.
4. Separate binomial multiplicities, probability-weight matrices, and polynomial norm matrices before touching $B$ or $\Gamma$.
5. Keep raw $\Phi_N$, weighted symmetric $S_N$, and orthogonal $U_N$ distinct; they are not interchangeable notations.
6. Decide on different letters for row sums $R_n$ and raising matrices $R_N$, and for binomial multiplicity $b_j$ versus Jacobi entry $b_r$.
7. Keep group lifts, differential lifts, and full-tensor versus symmetric-sector operators explicitly distinguished.
8. Only then standardize auxiliary coordinates and local indices within their mathematical scopes.

After these choices, each approved substitution should be recorded with its scope, coordinate/normalization conversion, and source exceptions. A literal search-and-replace is appropriate only for genuine aliases whose scopes have been checked.

## Applied propagation and next decisions

See `NOTATION_PROPAGATION_REPORT.md` for the exact scope, changed files, verification, and ranked remaining notation decisions. $N$ subscripts are optional when level is fixed.

## Applied sum notation

The approved RowS, ColS, SqRowS, SqColS notation has been applied to `chapters/kravchuk-sums.tex`. Absolute-value sums retain their previous notation pending a separate choice. This source-only pass has not rebuilt main.pdf. Earlier audit recommendations about renaming signed/square sums are superseded by this decision.

## Applied H notation decision

The author has selected boldface $\mathbf H$ for the Cartan differential operator $\xi\partial_\xi-\eta\partial_\eta$, whose degree-N matrix is $\Lambda_N$. This replaces the earlier Cartan $\mathcal H$ in Chapter 6. The oscillator retains $\mathcal H=\tfrac12(x^2-D^2)$, and the one-site Hadamard matrix retains $H=F+G$.

To avoid a new collision, the recently introduced tensor-transform abbreviation $\mathbf H_N$ has been removed from Chapters 9 and the front matter: the full tensor transform is written explicitly as $H^{\otimes N}$. These decisions supersede earlier collision descriptions and recommendations in this worksheet. This source-only pass has not rebuilt main.pdf.

## Success-count notation in Chapter 3

Initial and final success (+1) counts are now $a,b$; corresponding negative-sign indices are $N-a,N-b$. Multinomial category indices formerly $a,b$ are now $u,v$. The binomial mass function formerly named $b$ is now $\operatorname{BinMass}$. Centered site variables use index $u$. Random success margins use $\mathsf S_{\mathrm{in}},\mathsf S_{\mathrm{out}}$, avoiding reversal $J$. The current Chapter 13 polynomial definition is retained, with an explicit reflected-coordinate bridge in Chapter 3; Chapter 13 itself is unchanged pending the author's review. This source-only pass has not rebuilt the PDF.

## Basic polynomial audit update

See `BASIC_POLYNOMIAL_NOTATION_AUDIT.md`. Chapters 1 and 14 now explicitly state $(\Phi_N)_{ij}=K_i(j;N)=k_i(N-2j,N)/i!$, the row/column orientation, and the lattice versus formal-series distinction. The PQ use of K for exponential coefficients remains an unresolved naming collision; Chapter 13 is unchanged. Source-only update; PDF not rebuilt.
