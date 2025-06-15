import os
import sys
import time
from pages.ReservationFormPage import ReservationFormPage
from pages.FlightSelectionPage import FlightSelectionPage
from pages.SearchPage import SearchPage
from enums.FlightDirection import FlightDirection
from enums.AirportCode import AirportCode
from config.EnvConfig import EnvConfig
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright
from datetime import datetime

env_config = EnvConfig()


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
        search_page = SearchPage(page)
        search_page.go_to()
        # 航空券を検索
        search_page.search(
            AirportCode[os.getenv("DEPARTURE_AIRPORT")],
            AirportCode[os.getenv("ARRIVAL_AIRPORT")],
            datetime.fromisoformat(os.getenv("DEPARTURE_DATE")).date(),
            datetime.fromisoformat(os.getenv("RETURN_DATE")).date(),
        )
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
        page.screenshot(path="screenshot/success.png", full_page=True)
        if env_config.is_execute_reservation:
            page.get_by_role("button", name="予約する").click()
    except Exception as e:
        page.screenshot(
            path=f"screenshot/fails-{datetime.now().strftime("%Y%m%d_%H%M%S")}.png",
            full_page=True,
        )
        raise e


def reserve() -> None:
    """
    予約を実行する関数
    """
    load_dotenv(override=True)
    with sync_playwright() as playwright:
        run(playwright)


def get_browser_executable_path() -> str:
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


if __name__ == "__main__":
    while True:
        try:
            reserve()
            break
        except Exception as e:
            print(f"予約に失敗しました: {e}")
            time.sleep(5)
    print("予約が完了しました。")
