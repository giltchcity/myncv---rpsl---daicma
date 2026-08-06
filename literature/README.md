# Literature PDF Audit Workspace

This directory makes the paper's literature review reproducible without
redistributing third-party PDFs in the public repository.

## Why PDFs are not committed

Most papers may be downloaded legally for personal research from arXiv, author
pages, conference proceedings, or institutional subscriptions. That does not
necessarily grant permission to republish the PDF inside this repository.
Therefore:

- official/open download locations are versioned in `papers.json`;
- the Gaussian-specific audit set is versioned in `gaussian_papers.json`;
- newly added traditional dynamic/multi-session papers are versioned in
  `traditional_additions.json`;
- PDFs are downloaded to the ignored directory `literature/pdfs/`;
- the downloader records the exact byte size and SHA-256 of each local copy;
- technical conclusions and short source excerpts are versioned in the
  repository evidence ledgers;
- OASIS-Map, GS-LTS, GS-DIFF, and other unreviewed work are explicitly marked as
  preprints until their status changes.

## Download the core papers

From the repository root:

```bash
python3 literature/download_papers.py
```

Download selected core papers only:

```bash
python3 literature/download_papers.py \
  --key schmid2024khronos \
  --key qian2022pocd \
  --key qian2023povslam
```

## Download the newly added traditional mapping papers

```bash
python3 literature/download_papers.py \
  --manifest literature/traditional_additions.json \
  --generated-manifest literature/traditional_additions_download_manifest.generated.json
```

Selected additions only:

```bash
python3 literature/download_papers.py \
  --manifest literature/traditional_additions.json \
  --generated-manifest literature/traditional_additions_download_manifest.generated.json \
  --key xu2019midfusion \
  --key strecke2019emfusion \
  --key bescos2021dynaslam2
```

## Download the Gaussian audit set

```bash
python3 literature/download_papers.py \
  --manifest literature/gaussian_papers.json \
  --generated-manifest literature/gaussian_download_manifest.generated.json
```

The current manuscript retains only three representative Gaussian papers:

```bash
python3 literature/download_papers.py \
  --manifest literature/gaussian_papers.json \
  --generated-manifest literature/gaussian_download_manifest.generated.json \
  --key li2025fourdgsslam \
  --key yugay2026game \
  --key cheng2025ltgaussian
```

Force a fresh download by adding `--overwrite`.

The commands create local PDFs and generated hash manifests. These outputs are
ignored by Git. The generated manifests record the exact SHA-256 hash of every
audited local PDF.

## Papers requiring manual access

Entries with `pdf_url: null` cannot be fetched reliably from a stable public PDF
endpoint. Obtain the author manuscript or an institutional-access copy and save
it using the exact `filename` from the corresponding JSON manifest. Re-run the
downloader; it will validate the PDF and add its hash to the generated manifest.

Current manual entries include:

- `pomerleau2014longterm.pdf`
- `lazaro2018efficient.pdf`
- `breitfuss2024rbif.pdf`

All papers in `gaussian_papers.json` currently have an open arXiv or author PDF.

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
statement is not an implemented component. A method that removes dynamics to
recover a static map must not be described as retaining dynamic history, and a
pairwise Gaussian change detector must not be described as a multi-session SLAM
system.
