import os
import re
import time
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    """
    Playwrightを使用して、AirDoの予約サイトにアクセスし、航空券を予約する関数

    Args:
        playwright (Playwright): Playwrightのインスタンス
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Airdoの予約サイトにアクセス
    page.goto("https://www.airdo.jp/")
    # 航空券を検索
    page.locator('select[name="from"]').select_option("HND")
    page.get_by_role("button", name="検索する").click()
    # 検索結果から航空券を選択
    page.get_by_role("row", name="ADO 011 763 06:55 - 08:25 ◯ ¥").get_by_role(
        "cell"
    ).nth(1).click()
    page.get_by_role("cell", name="△ ¥26,320").click()
    page.locator("#form-cart").get_by_role("button", name="次へ").click()
    page.get_by_role("button", name="ログインせずに次へ進む").click()
    # 予約者情報の入力
    page.get_by_role("textbox", name="例）サトウ").fill(os.getenv("LAST_NAME"))
    page.get_by_role("textbox", name="例）イチロウ").fill(
        os.getenv("FIRST_NAME")
    )
    page.locator("#age-1").fill(os.getenv("AGE"))
    page.get_by_role("textbox", name="例）sample@airdo.jp").fill(
        os.getenv("E_MAIL")
    )
    page.locator("#input-conf-req").fill(os.getenv("E_MAIL"))
    page.get_by_role("textbox", name="例）09012345678").fill(
        os.getenv("TEL_NUMBER")
    )
    page.get_by_role("button", name="確認画面に進む").click()
    # 予約の確定
    page.locator("label").click()
    page.screenshot(path="screenshot.png", full_page=True)
    page.get_by_role("button", name="予約する").click()


start = time.time()

load_dotenv()

with sync_playwright() as playwright:
    run(playwright)

end = time.time()
print(f"実行時間: {end - start:.4f} 秒")
