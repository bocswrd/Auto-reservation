from playwright.sync_api import Page
from datetime import date
from enums.AirportCode import AirportCode


class SearchPage:
    """
    航空券検索ページのクラス
    Attributes:
        __URL (str): 検索ページのURL
        __page (Page): PlaywrightのPageオブジェクト
    """
    
    __URL = "https://www.airdo.jp/"

    def __init__(self, page: Page):
        self.__page = page

    @property
    def url(self) -> str:
        """
        getter

        Returns:
            str: 検索ページのURL
        """
        return self.__URL

    def go_to(self) -> None:
        """
        航空券検索ページへ遷移する
        """
        self.__page.goto(self.__URL)

    def search(
        self,
        departure_airport: AirportCode,
        arrival_airport: AirportCode,
        departure_date: date,
        return_date: date,
    ) -> None:
        """
        航空券を検索する

        Args:
            departure_airport (AirportCode): 出発地の空港コード
            arrival_airport (AirportCode): 目的地の空港コード
            departure_date (date): 出発日
            return_date (date): 帰着日
        """
        # TODO: 検索ページに遷移していることを強制したい
        # 出発地・目的地の選択
        self.__page.locator('select[name="from"]').select_option(
            departure_airport.name
        )
        self.__page.locator('select[name="to"]').select_option(
            arrival_airport.name
        )

        # 日付指定
        self.__page.evaluate(
            f"""
            document.querySelector('input[type="hidden"][name="departureDate"]').value = '{date.isoformat(departure_date)}';
            document.querySelector('input[type="hidden"][name="returnDate"]').value = '{date.isoformat(return_date)}';
            """
        )

        self.__page.get_by_role("button", name="検索する").click()
