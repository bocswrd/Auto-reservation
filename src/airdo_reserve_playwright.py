import os
import sys
from pages.ReservationFormPage import ReservationFormPage
from pages.FlightSelectionPage import FlightSelectionPage
from enums.FlightDirection import FlightDirection
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright
from datetime import datetime


def run(playwright: Playwright) -> None:
    """
    Playwrightを使用して、AirDoの予約サイトにアクセスし、航空券を予約する関数

    Args:
        playwright (Playwright): Playwrightのインスタンス
    """
    browser = playwright.chromium.launch(
        headless=True,
        executable_path=get_browser_executable_path(),
    )
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
            document.querySelector('input[type="hidden"][name="returnDate"]').value = '{os.getenv("RETURN_DATE")}';
            """
        )
        page.get_by_role("button", name="検索する").click()

        # 航空券を選択する
        flight_selection_page = FlightSelectionPage(page)
        cheapest_outbound_flight = flight_selection_page.find_cheapest_flight(
            flight_selection_page.get_flight_prices(
                FlightDirection.OUTBOUND,
                int(os.getenv("OUTBOUND_TAKEOFF_HOUR")),
                int(os.getenv("OUTBOUND_TAKEOFF_MINUTE")),
                int(os.getenv("OUTBOUND_LANDING_HOUR")),
                int(os.getenv("OUTBOUND_LANDING_MINUTE")),
            )
        )
        if cheapest_outbound_flight is None:
            raise ValueError("往路のフライトが見つかりませんでした。")
        flight_selection_page.select_cheapest_flight(*cheapest_outbound_flight)

        cheapest_return_flight = flight_selection_page.find_cheapest_flight(
            flight_selection_page.get_flight_prices(
                FlightDirection.RETURN,
                int(os.getenv("RETURN_TAKEOFF_HOUR")),
                int(os.getenv("RETURN_TAKEOFF_MINUTE")),
                int(os.getenv("RETURN_LANDING_HOUR")),
                int(os.getenv("RETURN_LANDING_MINUTE")),
            )
        )
        if cheapest_return_flight is None:
            raise ValueError("復路のフライトが見つかりませんでした。")
        flight_selection_page.select_cheapest_flight(*cheapest_return_flight)
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
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(
            path=f"fails-screenshot-{timestamp}.png", full_page=True
        )
        raise e


def reserve() -> None:
    """
    予約を実行する関数
    """
    load_dotenv(override=True)
    with sync_playwright() as playwright:
        run(playwright)


def get_browser_executable_path():
    """
    exe実行時に、ブラウザの実行ファイルパスを取得する関数

    Returns:
        str: ブラウザの実行ファイルパス
         - exe実行時は指定、通常のPython実行時はNone
    """
    if getattr(sys, "frozen", False):
        # exe実行時（PyInstaller実行環境）
        return "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    else:
        # 開発環境（通常のPython実行時）
        return None  # None指定でplaywrightが通常のdriverを自動使用
