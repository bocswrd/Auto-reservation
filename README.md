# プロジェクトタイトル

## プロジェクトの説明
航空券の予約を自動で行うツール

## 目次
 - [環境構築手順](#環境構築手順)
 - [使用方法](#使用方法)
 - [構成](#構成)
 - [依存関係](#依存関係)
 - [トラブルシューティング](#トラブルシューティング)
 - [貢献](#貢献)
 - [教訓](#教訓)
 - [ライセンス](#ライセンス)
 - [連絡先](#連絡先)

## 環境構築手順
### 概要
1. Pythonをインストールする
1. [仮想環境の構築](#仮想環境の構築)
1. [ブラウザのインストール](#ブラウザのインストール方法)
1. [Visual Studio Code拡張機能をインストールする](#visual-studio-code拡張機能をインストールする)

### 仮想環境の構築
1. Visual Studio Codeを開く
2. Git Bashで以下コマンドを実行する
``` bash
cd "$(git rev-parse --show-toplevel)"
source update_library.sh
```

### ブラウザのインストール方法
``` bash
playwright install
```

### Visual Studio Code拡張機能をインストールする
 - Python
 - Black Formatter
 - Flack8

## 使用方法
### 実行コマンド
``` bash
python airdo_reserve_playwright.py
```

### パッケージの更新
以下コマンドを実行する
``` bash
cd "$(git rev-parse --show-toplevel)"
source update_library.sh 
```

### インストール済みバッケージ・バージョンの出力
``` bash
pip freeze > requirements.txt
```

### codegenを用いたスクリプトの生成(Playwright)
``` bash
Playwright codegen {操作対象URL} -o {出力ファイル名.py}
```

## 構成

## 依存関係

## トラブルシューティング
### 仮想環境が有効にならない場合
``` bash
cd "$(git rev-parse --show-toplevel)"
source .venv/Scripts/activate
```

## 貢献

## 教訓

## ライセンス

## 連絡先