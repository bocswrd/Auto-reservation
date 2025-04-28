#!/bin/bash

echo "Updating library..."

# リポジトリのルートディレクトリに移動
cd "$(git rev-parse --show-toplevel)"

# 仮想環境がアクティブな場合は非アクティブ化
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Deactivating virtual environment..."
    # NOTE: 拡張機能が原因でエラーが発生する可能性があるが、無視して問題ない
    deactivate || true
fi

# 仮想環境を再構築
echo "Rebuilding virtual environment..."
rm -rf .venv/
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt

echo "Library updated successfully!"
