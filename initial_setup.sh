#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# カラーコードの定義
blue() {
    echo -e "\e[34m$1\e[0m"
}

# リポジトリのルートディレクトリに移動
cd "$(git rev-parse --show-toplevel)"

blue "Start initial setup"

# 仮想環境の構築
source update_library.sh

# ブラウザをインストールする
blue "Installing browser..."
playwright install

# Visual Studio Code拡張機能をインストールする
blue "Installing vscode extensions..."
code --install-extension ms-python.python #Python
code --install-extension ms-python.black-formatter #Black Formatter
code --install-extension ms-python.flake8 #Flake8

blue "Setup is completed!"
