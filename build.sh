#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$SCRIPT_DIR/main.spec" ]; then
    pyinstaller "$SCRIPT_DIR/main.spec"
else
    # specファイルが存在しない場合は、新規作成して実行する
    echo "Spec file not found, creating a new one."
    pyinstaller --onefile "$SCRIPT_DIR/src/main.py"
fi