import pytest
import time
from utils.retry import retry

def test_retry_success_first_try():
    """
    `retry`関数が最初の試行で成功した場合に、正しい結果を返すことをテストします。
    """
    def func():
        return "ok"
    assert retry(func) == "ok"

def test_retry_success_after_failures():
    """
    関数が最初の数回失敗した後、リトライによって最終的に成功することをテストします。
    このテストでは、funcが2回失敗した後、3回目で成功することを想定しています。
    retry関数が指定された回数だけリトライし、最終的に成功した結果を返すことを検証します。
    """
    calls = {"count": 0}
    def func():
        if calls["count"] < 2:
            calls["count"] += 1
            raise ValueError("fail")
        return "success"
    assert retry(func, retries=3, delay=0) == "success"

def test_retry_raises_after_max_retries():
    """
    `retry` 関数が最大リトライ回数を超えた場合に例外を送出することをテストします。

    このテストでは、常に例外を発生させる `func` を使用し、`retry` 関数にリトライ回数2回、遅延0秒で実行させます。
    最大リトライ回数に達した後、`RuntimeError` が送出されることを検証します。
    """
    def func():
        raise RuntimeError("always fail")
    with pytest.raises(RuntimeError):
        retry(func, retries=2, delay=0)

def test_retry_count(monkeypatch):
    """
    `retry`関数が指定された回数だけリトライすることをテストする

    このテストでは、例外を常に発生させる関数`func`を用意し、`retry`関数に3回リトライさせる。
    `time.sleep`をモンキーパッチして実際の遅延を回避し、例外が発生することを確認する。
    最終的に、関数が指定回数呼び出されたことを検証します。
    """
    called = []
    def func():
        called.append(time.time())
        raise Exception("fail")
    # monkeypatch time.sleep to avoid real delay
    monkeypatch.setattr(time, "sleep", lambda x: None)
    with pytest.raises(Exception):
        retry(func, retries=3, delay=1)
    assert len(called) == 3