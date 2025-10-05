import time
import logging

logger = logging.getLogger(__name__)

def retry(func:callable, retries:int=3, delay:int|float=2) -> any:
    """
    指定した関数を最大retries回まで再試行するユーティリティ関数。

    引数:
        func (callable): 実行する関数。引数なしで呼び出されることを想定。
        retries (int, オプション): 最大再試行回数。デフォルトは3。
        delay (intまたはfloat, オプション): 再試行間の待機時間（秒）。デフォルトは2秒。

    例外:
        funcの実行がretries回すべて失敗した場合、最後に発生した例外を再送出する。

    戻り値:
        funcの戻り値を返す。成功した場合は即座に返し、失敗した場合は再試行する。
    """
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Retry {i+1}/{retries} failed: {e}")
            if i < retries - 1:
                time.sleep(delay)
            else:
                raise
