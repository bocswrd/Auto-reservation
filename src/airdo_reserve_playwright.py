import os
import re
import time
from pages.ReservationFormPage import ReservationFormPage
from pages.FlightSelectionPage import FlightSelectionPage
from enums.FlightDirection import FlightDirection
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    """
    Playwrightを使用して、AirDoの予約サイトにアクセスし、航空券を予約する関数

    Args:
        playwright (Playwright): Playwrightのインスタンス
    """
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    # Airdoの予約サイトにアクセス
    page.goto("https://www.airdo.jp/")
    # 航空券を検索
    # TODO: 出発地・目的の選択
    page.locator('select[name="from"]').select_option("HND")
    # TODO: 日付指定
    page.locator("#date-out").click()
    page.locator(
        "div:nth-child(2) > .fc-view-container > .fc-view > table > .fc-body > tr > td > .fc-scroller > .fc-day-grid > div > .fc-content-skeleton > table > thead > tr > td:nth-child(6)"
    ).first.click()
    page.get_by_role("button", name="検索する").click()

    # 航空券を選択する
    flight_selection_page = FlightSelectionPage(page)
    flight_selection_page.select_cheapest_flight(
        *flight_selection_page.find_cheapest_flight(
            flight_selection_page.get_flight_prices(
                FlightDirection.OUTBOUND
            )
        )
    )
    flight_selection_page.select_cheapest_flight(
        *flight_selection_page.find_cheapest_flight(
            flight_selection_page.get_flight_prices(
                FlightDirection.RETURN
            )
        )
    )
    flight_selection_page.buy_flight()

    page.get_by_role("button", name="ログインせずに次へ進む").click()
    # 予約者情報の入力
    reservation_form_page = ReservationFormPage(page)
    reservation_form_page.enter_individual_to_form(
        os.getenv("LAST_NAME"),
        os.getenv("FIRST_NAME"),
        os.getenv("AGE"),
        os.getenv("E_MAIL"),
        os.getenv("TEL_NUMBER"),
    )
    reservation_form_page.submit_form()
    # 予約の確定
    page.locator("label").click()
    page.screenshot(path="screenshot.png", full_page=True)
    # page.get_by_role("button", name="予約する").click()


start = time.time()

load_dotenv()

with sync_playwright() as playwright:
    run(playwright)

end = time.time()
print(f"実行時間: {end - start:.4f} 秒")
