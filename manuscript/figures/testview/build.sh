#!/bin/bash
# Builds figures/testview.pdf (and a PNG preview) from testview.html with the Windows Chrome of this
# WSL machine. Usage: bash build.sh [PREVIEW.png]
set -e
cd "$(dirname "$0")"
CHROME="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
HTML=$(wslpath -w "$PWD/testview.html"); URL="file:///${HTML//\\//}"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$(wslpath -w "$PWD/../testview.pdf")" "$URL"
if [ -n "$1" ]; then
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=3 --window-size=660,268 \
    --screenshot="$(wslpath -w "$1")" "$URL"
fi
