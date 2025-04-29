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
    try:
        # Airdoの予約サイトにアクセス
        page.goto("https://www.airdo.jp/")
        # 航空券を検索
        # 出発地・目的の選択
        page.locator('select[name="from"]').select_option(
            os.getenv("DEPARTURE_AIRPORT")
        )
        page.locator('select[name="to"]').select_option(
            os.getenv("ARRIVAL_AIRPORT")
        )
        # 日付指定
        page.evaluate(
            f"""
            document.querySelector('input[type="hidden"][name="departureDate"]').value = '{os.getenv("DEPARTURE_DATE")}';
            """
        )
        page.evaluate(
            f"""
            document.querySelector('input[type="hidden"][name="returnDate"]').value = '{os.getenv("RETURN_DATE")}';
            """
        )
        page.get_by_role("button", name="検索する").click()

        # 航空券を選択する
        flight_selection_page = FlightSelectionPage(page)
        flight_selection_page.select_cheapest_flight(
            *flight_selection_page.find_cheapest_flight(
                flight_selection_page.get_flight_prices(FlightDirection.OUTBOUND)
            )
        )
        flight_selection_page.select_cheapest_flight(
            *flight_selection_page.find_cheapest_flight(
                flight_selection_page.get_flight_prices(FlightDirection.RETURN)
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
    except Exception as e:
        page.screenshot(path="screenshot.png", full_page=True)
        print(f"An error occurred: {e}")


start = time.time()

load_dotenv()

with sync_playwright() as playwright:
    run(playwright)

end = time.time()
print(f"実行時間: {end - start:.4f} 秒")
