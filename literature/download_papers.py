#!/usr/bin/env python3
"""Download the open full-text PDFs used by the paper evidence audit.

The PDFs are kept in literature/pdfs/ and intentionally ignored by Git.  This
script records SHA-256 hashes and byte sizes in a generated JSON manifest so the
exact local copies used for review can be reproduced and checked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DEFAULT_MANIFEST = ROOT / "papers.json"
DEFAULT_OUTPUT = ROOT / "pdfs"
DEFAULT_GENERATED = ROOT / "download_manifest.generated.json"
USER_AGENT = "Mozilla/5.0 (compatible; P-SMS-literature-audit/1.0)"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data.get("papers"), list):
        raise ValueError(f"Invalid manifest: {path}")
    return data


def validate_pdf(path: Path) -> None:
    with path.open("rb") as handle:
        magic = handle.read(5)
    if magic != b"%PDF-":
        raise ValueError(f"Downloaded file is not a PDF: {path}")


def download(url: str, destination: Path, timeout: int) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=destination.name + ".", suffix=".part", dir=destination.parent
    )
    os.close(fd)
    tmp_path = Path(tmp_name)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response, tmp_path.open(
            "wb"
        ) as output:
            while True:
                block = response.read(1024 * 1024)
                if not block:
                    break
                output.write(block)
        validate_pdf(tmp_path)
        tmp_path.replace(destination)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--generated-manifest", type=Path, default=DEFAULT_GENERATED)
    parser.add_argument(
        "--key",
        action="append",
        default=[],
        help="Download only this BibTeX key. Repeat for multiple papers.",
    )
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--timeout", type=int, default=90)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = read_manifest(args.manifest)
    selected = set(args.key)
    records: list[dict[str, Any]] = []
    failures = 0

    for paper in source["papers"]:
        key = str(paper["key"])
        if selected and key not in selected:
            continue

        filename = str(paper["filename"])
        target = args.output_dir / filename
        url = paper.get("pdf_url")
        record: dict[str, Any] = {
            "key": key,
            "title": paper.get("title"),
            "status": paper.get("status"),
            "source_url": url,
            "landing_url": paper.get("landing_url"),
            "local_path": str(target.relative_to(ROOT)),
        }

        if not url:
            record["download_status"] = "manual_required"
            record["note"] = paper.get("manual_note")
            if target.exists():
                try:
                    validate_pdf(target)
                    record.update(
                        {
                            "download_status": "manual_present",
                            "bytes": target.stat().st_size,
                            "sha256": sha256_file(target),
                        }
                    )
                except Exception as exc:  # noqa: BLE001
                    failures += 1
                    record["download_status"] = "invalid_manual_file"
                    record["error"] = str(exc)
            records.append(record)
            print(f"MANUAL {key}: {target}")
            continue

        try:
            if target.exists() and not args.overwrite:
                validate_pdf(target)
                action = "kept"
            else:
                download(str(url), target, args.timeout)
                action = "downloaded"
            record.update(
                {
                    "download_status": action,
                    "bytes": target.stat().st_size,
                    "sha256": sha256_file(target),
                }
            )
            print(f"OK {key}: {action} -> {target}")
        except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
            failures += 1
            record["download_status"] = "failed"
            record["error"] = str(exc)
            print(f"ERROR {key}: {exc}", file=sys.stderr)
        records.append(record)

    generated = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_manifest": str(args.manifest),
        "records": records,
    }
    args.generated_manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.generated_manifest.open("w", encoding="utf-8") as handle:
        json.dump(generated, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    print(f"Wrote {args.generated_manifest}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
