# Literature PDF Audit Workspace

This directory makes the paper's literature review reproducible without
redistributing third-party PDFs in the public repository.

## Why PDFs are not committed

Most papers may be downloaded legally for personal research from arXiv, author
pages, conference proceedings, or institutional subscriptions. That does not
necessarily grant permission to republish the PDF inside this repository.
Therefore:

- official/open download locations are versioned in `papers.json`;
- PDFs are downloaded to the ignored directory `literature/pdfs/`;
- the downloader records the exact byte size and SHA-256 of each local copy;
- technical conclusions and short source excerpts are versioned in
  `../06_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`;
- OASIS-Map is explicitly marked as an under-review preprint until its status
  changes.

## Download the open PDFs

From the repository root:

```bash
python3 literature/download_papers.py
```

Download selected papers only:

```bash
python3 literature/download_papers.py \
  --key schmid2024khronos \
  --key qian2022pocd \
  --key qian2023povslam
```

Force a fresh download:

```bash
python3 literature/download_papers.py --overwrite
```

The command creates:

```text
literature/pdfs/*.pdf
literature/download_manifest.generated.json
```

Both are ignored by Git. The generated manifest records the exact SHA-256 hash
of every audited local PDF.

## Papers requiring manual access

Entries with `pdf_url: null` cannot be fetched reliably from a stable public PDF
endpoint. Obtain the author manuscript or an institutional-access copy and save
it using the exact `filename` from `papers.json`. Re-run the downloader; it will
validate the PDF and add its hash to the generated manifest.

Current manual entries:

- `pomerleau2014longterm.pdf`
- `lazaro2018efficient.pdf`

## Full-text reading rule

Before adding or changing a technical sentence in the manuscript:

1. read the problem definition and assumptions;
2. inspect the representation and actual optimized variables;
3. inspect the method section implementing the claimed capability;
4. inspect the evaluation protocol and reported outputs;
5. inspect limitations, discussion, and conclusion;
6. add or update the corresponding entry in the full-text evidence audit;
7. use restrained wording when the evidence is only the absence of an evaluated
   feature.

A sentence in another paper's related-work section is not evidence of the cited
method's own contribution. An author criticism is not a capability. A future-work
statement is not an implemented component.
