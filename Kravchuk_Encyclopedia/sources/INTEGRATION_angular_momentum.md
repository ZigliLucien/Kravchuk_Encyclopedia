# Angular momentum integration

Location: chapters/06-chapter.tex, section sec:angular-momentum, immediately after finite raising/lowering matrices and before the split-real-form discussion. A cross-reference was added in the representations chapter's Hilbert-space discussion.

Dictionary uses the existing column-vector convention and binomial metric: C=B_N^(1/2), Mhat=C^(-1) M C. The operator sometimes called N is [L,R]=Lambda_N, distinct from the scalar order N and Euler operator NI. With spin s=N/2 and magnetic number m=s-j: J_+=hbar Lhat, J_-=hbar Rhat, J_x=hbar Ahat/2, J_y=hbar(Lhat-Rhat)/(2i), J_z=hbar Lambda_N/2. Raising the book's index lowers magnetic number. All operators are Hermitian in the normalized basis; the raw versions are self-adjoint for the existing B_N^(-1) metric.

Developed: ladder coefficients, all commutators, scalar Casimir, highest weight and irreducibility, symmetric N-spin-1/2 tensor realization, SU(2)/SO(3) distinction, and compact versus split real forms. Small spin-1/2 and spin-one examples included.

Krawtchouk transform: J_x U_N=U_N J_z. With the explicitly fixed J_y convention, U_N=exp(-i*pi*J_y/(2*hbar)) D_N, where D_N=diag((-1)^j) is the existing parity matrix. U_N is an axis-change matrix with column phases, not a bare quarter-turn rotation. The Wigner d relation uses m'=s-j, m=s-k and d_(m',m)(pi/2)=(-1)^k U_(j,k).

Validation: 72 exact matrix checks for orders N=0..8: three cyclic commutators, Casimir, adjoint ladders, transform intertwining, orthogonality, and independently constructed symmetric-power rotation phases. A separate numerical matrix-exponential check had maximum error about 6.11e-16. Active input graph, labels, references and environments checked. No TeX compilation or visual-layout check.

This section is a derivation from the book's fixed matrix conventions, not a claim of new bibliography verification. It does not overwrite general-p,q Appell notation from the preferred supplied summary. The bibliography and document class are unchanged. Backup: project-archive/before-angular-momentum-integration.zip.
