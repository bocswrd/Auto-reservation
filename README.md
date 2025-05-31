# *Taurus*

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
1. Visual Studio Codeをインストールする
1. Git Bashをインストールする
1. [Visual Studio Code内の環境構築](#初回セットアップ用shellを起動する)
    1. 仮想環境の構築
    1. ブラウザのインストール
    1. 拡張機能をインストールする

### Visual Studio Code内の環境構築
#### 初回セットアップ用Shellを起動する
* 以下コマンドを実行する
``` bash
source initial_setup.sh
```

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

### テスト実行(pytest)
``` bash
pytest {実行ファイル名}.py
```

### exeファイルのビルド
``` bash
./build.sh
```

## 構成

## 依存関係

## トラブルシューティング
### 仮想環境が有効にならない場合
``` bash
cd "$(git rev-parse --show-toplevel)"
source .venv/Scripts/activate
```

### exe実行時、以下のエラーが出る場合
``` bash
playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist
```
 1. Chromeをダウンロードする
 2. `C:\Program Files\Google\Chrome\Application`に`chrome.exe`が存在することを確認する

## 貢献

## 教訓

## ライセンス

## 連絡先