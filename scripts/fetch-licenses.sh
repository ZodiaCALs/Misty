#!/bin/sh
# SPDX-FileCopyrightText: 2026 ZodiaCALs
# SPDX-License-Identifier: Apache-2.0
#
# Saves the official texts of the licences this repository uses in LICENSES/,
# where REUSE and most licence scanners look for them.
set -eu
cd "$(dirname "$0")/.."
mkdir -p LICENSES

if command -v reuse >/dev/null 2>&1; then
  reuse download Apache-2.0 CC-BY-ND-4.0 CC0-1.0
  echo "Licence texts saved in LICENSES/ by reuse."
  exit 0
fi

fetch() {
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$1" -o "$2"
  else
    wget -qO "$2" "$1"
  fi
}

fetch https://www.apache.org/licenses/LICENSE-2.0.txt LICENSES/Apache-2.0.txt
fetch https://creativecommons.org/licenses/by-nd/4.0/legalcode.txt LICENSES/CC-BY-ND-4.0.txt
fetch https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt LICENSES/CC0-1.0.txt
echo "Licence texts saved in LICENSES/."
