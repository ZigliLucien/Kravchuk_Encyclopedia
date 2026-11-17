# Bibliography integration and review

## Provenance and scope
The supplied `KrawtchoukReferences_bibliography.tex` is archived unchanged in this directory. All 50 records are integrated verbatim into `bibliography/references.tex`, followed by the previously existing `KocikFeynman` record. The main document inputs this one bibliography. Keys `ref01` through `ref50` are preserved; no chapter citations have been reassigned or added merely on the basis of a title.

## Verification status
The supplied 50 entries are **not independently verified by this integration**. A prior batch lookup failed during result processing, and its results were not recoverable in this turn; it is not treated as completed verification. No metadata corrections or DOI additions have been inferred from memory. The existing KocikFeynman entry retains its previously verified status.

## Review flags from the supplied text (not asserted corrections)
- ref02: check the supplied author spelling `Marcellin` and the accented TeX form.
- ref06: check the title wording `Approximation on a Kravchuk functions` against an authoritative record.
- ref23: the supplied arXiv identifier lacks final journal publication details; preserve the preprint citation until reconciled.
- ref24: contains the historical phrase `to appear`; verify final publication information before replacing it.
- ref25, ref35, ref36, ref37, ref38, ref40: preprint/proceedings details warrant individual checks; do not substitute later versions without establishing equivalence.
- ref27: verify the supplied journal volume `150` together with the year and pages; no replacement value has been asserted.
- ref31, ref33, ref46: verify author spellings as supplied before normalizing names.
- ref42: preserve the stated edition and cited pages until checked against that edition.
- ref44 and ref45: preserve the software annotations as supplied; determine later whether these belong in bibliographic text or editorial notes.
- Several entries give only an initial page rather than a page range. Do not invent missing terminal pages.

## Duplicate checks
There are no repeated citation keys within the 50 supplied entries, no key collision with KocikFeynman, and no exact repeated title among the supplied records after basic TeX/whitespace normalization. This does not establish the absence of preprint/journal-version duplicates or variant-title duplicates. Supporting-paper bibliographies are not merged into the book by this change.

## Build status
Source integration and structural checks only; `main.pdf` has not been rebuilt. The book's existing `amsbook` class is unchanged.

## Backup
`project-archive/before-bibliography-integration.zip` preserves the preceding project state.
