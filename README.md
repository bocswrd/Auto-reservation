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
1. Chromeをインストールする
1. [ブラウザのインストール(Playwright)](#ブラウザのインストール方法playwright)
1. [Visual Studio Code拡張機能をインストールする](#visual-studio-code拡張機能をインストールする)
1. [仮想環境を作成し、ライブラリをインストールする](#仮想環境を作成しライブラリをインストールする)

### ブラウザのインストール方法(Playwright)
``` bash
playwright install
```

### Visual Studio Code拡張機能をインストールする
 - Python
 - Black Formatter
 - Flack8


### 仮想環境を作成し、ライブラリをインストールする
vs codeを開き、Git Bashで以下コマンドを実行する
``` bash
deactivate  # 仮想環境のディアクティベート
```

``` bash
rm -rf .venv/  # 仮想環境を削除
python -m venv .venv    # 仮想環境を再作成
source .venv/Scripts/activate
pip install -r requirements.txt # ライブラリをインストール
```

## 使用方法
### 実行コマンド
``` bash
python airdo_reserve.py
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
source .venv/Scripts/activate
```

## 貢献

## 教訓

## ライセンス

## 連絡先