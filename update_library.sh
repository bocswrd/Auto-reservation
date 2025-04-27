# deactivate
rm -rf .venv/  # 仮想環境を削除
python -m venv .venv    # 仮想環境を再作成
source .venv/Scripts/activate
pip install -r requirements.txt # ライブラリをインストール
