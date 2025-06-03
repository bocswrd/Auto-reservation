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
1. [poetryをインストールする](#poetryのインストール手順)
1. [Visual Studio Code内の環境構築](#初回セットアップ用shellを起動する)
    1. 仮想環境の構築
    1. ブラウザのインストール
    1. 拡張機能をインストールする

### [poetryのインストール手順](https://python-poetry.org/docs/#installing-with-the-official-installer)
Powershellを起動する
``` powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
``` powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\$env:USERNAME\AppData\Roaming\Python\Scripts", "User")
```
Powershellを再起動する
``` powershell
Start-Process powershell; exit
```
以下のコマンドを実行し、`poetry`のバージョンが表示されたらインストール完了
``` powershell
poetry --version
```

### Visual Studio Code内の環境構築
#### 初回セットアップ用Shellを起動する
* 以下コマンドを実行する
``` bash
source initial_setup.sh
```

## 使用方法
### 実行コマンド
``` bash
poetry python main.py
```

### パッケージの更新
``` bash
poetry install
```

### codegenを用いたスクリプトの生成(Playwright)
``` bash
Playwright codegen {操作対象URL} -o {出力ファイル名.py}
```

### テスト実行(pytest)
``` bash
poetry pytest {実行ファイル名}.py
```

### exeファイルのビルド
``` bash
./build.sh
```

## 構成

## 依存関係

## トラブルシューティング
### venvディレクトリがプロジェクト配下に作成されない場合
以下コマンドを実行する
``` bash
rm -rf "$(poetry env info --path)"
poetry config virtualenvs.in-project true
poetry install
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