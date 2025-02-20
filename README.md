* 仮想環境のアクティベート
``` bash
venv\Scripts\activate
```

* インストール済みバッケージとバージョンの出力
``` bash
pip freeze > requirements.txt
```
* 出力したrequirements.txtを一括インストール
``` bash
pip install -r requirements.txt
```