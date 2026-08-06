# GitHub and Overleaf Workflow

Date: 2026-08-06

## Local Repository

`/home/jixian/Desktop/FT/CVPR` is an independent Git repository on branch
`main`. The selected GitHub destination is:

```text
owner:      giltchcity
repository: myncv---rpsl---daicma
visibility: public (current GitHub setting)
remote:     https://github.com/giltchcity/myncv---rpsl---daicma.git
```

The repository exists and is readable over HTTPS. The first authenticated push
from this WSL installation uses GitHub CLI/browser authentication because no SSH
key or HTTPS credential helper was configured initially.

GitHub repository name:

```text
myncv---rpsl---daicma
```

Keep this repository paper-only. Do not add datasets, `.4dmap`, bags, generated
PLY sequences, model weights, or the complete research workspace.

The baseline implementation is published separately at:

```text
https://github.com/giltchcity/session_update_baseline_project
```

Do not copy that source tree back into this Overleaf-facing repository.

## Recommended Order

1. Create the GitHub repository.
2. Add it as local remote `origin`.
3. Make the first intentional commit and push the publication branch.
4. In Overleaf, connect the GitHub account.
5. Create a new Overleaf project using **Import from GitHub** and select this
   repository.
6. Set `manuscript/main.tex` as the Overleaf main document.
7. Use Overleaf's explicit pull/push synchronization controls; synchronization
   is not automatic.

Important: Overleaf's GitHub synchronization cannot link an already-existing
Overleaf project to an already-existing GitHub repository. Starting with the
GitHub repository and importing it into a new Overleaf project avoids that
restriction.

## Repository Hygiene for Overleaf

- Keep the total project comfortably below 100 MB.
- Prefer fewer than 100 changed files per synchronization operation.
- Do not use Git LFS or Git submodules; Overleaf does not support them inside a
  synchronized project.
- Avoid symlinks; Overleaf converts them to regular files.
- Keep generated experiment data outside `CVPR/` and copy only final compact
  figures/tables into `manuscript/figures/`.
- Resolve merge conflicts on GitHub/local Git before asking Overleaf to sync
  again.

## Alternative: Overleaf as a Second Git Remote

If direct GitHub synchronization is unavailable, Overleaf's Git integration can
expose the project as a Git remote. A local repository can then use both:

```text
origin    -> GitHub
overleaf  -> Overleaf Git URL
```

This route also requires an eligible Overleaf plan and token-based Git
authentication. Do not configure the second remote until the Overleaf project
and its Git URL exist.

## Pending Connection Information

Before submission, confirm:

```text
target CVPR year/template:
whether the GitHub repository should remain public:
```
