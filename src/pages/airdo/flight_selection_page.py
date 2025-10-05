import re
from playwright.sync_api import Page, Frame
from datetime import datetime, time
from enums import FlightDirection


class FlightSelectionPage:
    """
    航空券選択ページのクラス

    Attributes:
        __FRAME_URL_ID (str): iframeのURLの一部
        outward_flight_selector (str): 往路のフライトセレクター
        homeward_flight_selector (str): 復路のフライトセレクター
        __page (Page): PlaywrightのPageオブジェクト
        frame (Frame): 航空券情報を取得するためのiframe
    """

    __FRAME_URL_ID = "select.html"
    outward_flight_selector = "#anc-s1"
    homeward_flight_selector = "#anc-s2"

    def __init__(self, page: Page):
        self.__page = page
        self.frame = self.get_target_frame()

    def get_target_frame(self) -> Frame:
        """
        航空券情報を取得するためのiframeを取得する

        Raises:
            Exception: iframeが見つからない場合
            Exception: 目的のiframeが見つからない場合

        Returns:
            _type_: 航空券情報を取得するためのiframe
        """
        frames = self.__page.frames
        if len(frames) == 0:
            raise Exception("No frames found")

        for frame in frames:
            if self.__FRAME_URL_ID in frame.url:
                return frame

        raise Exception("No target frame found")

    def get_flight_prices(
        self,
        direction_selector: FlightDirection,
        takeoff_hour: int,
        takeoff_minute: int,
        landing_hour: int,
        landing_minute: int,
    ) -> dict:
        """
        フライト情報と価格を取得する

        Args:
            direction_selector(enums.FlightDirection): 往復路のセレクター

        Returns:
            dict: フライト情報と価格の辞書
        """
        outward_flight = self.frame.wait_for_selector(direction_selector.value)
        outward_flight_DoValue = outward_flight.wait_for_selector(
            "div.tab-content.current"
        )

        flights = outward_flight_DoValue.query_selector_all("tr")
        flight_prices = {}
        for flight in flights:
            flight_time_element = flight.query_selector("div.time")
            if not flight_time_element:
                continue
            flight_time_text = flight_time_element.inner_text().strip()
            flight_times = flight_time_text.split(" - ")
            takeoff_time = datetime.strptime(flight_times[0], "%H:%M").time()
            landing_time = datetime.strptime(flight_times[1], "%H:%M").time()

            # 指定時間外のフライト情報は取得しない
            if (
                takeoff_time < time(takeoff_hour, takeoff_minute, 0)
                or time(landing_hour, landing_minute, 0) < landing_time
            ):
                continue

            if flight_time_element.inner_text().strip() == "":
                continue

            flight_name_element = flight.query_selector("div.flight")
            if not flight_name_element:
                continue
            flight_name = flight_name_element.inner_text().strip()

            price_elements = flight.query_selector_all("div.price")
            for price_element in price_elements:
                price_text = price_element.inner_text().strip()
                if re.match(r"¥[\d,]+", price_text):
                    price = int(price_text.replace("¥", "").replace(",", ""))
                    if flight_name not in flight_prices:
                        flight_prices[flight_name] = []
                    flight_prices[flight_name].append(price)

        return flight_prices

    def find_cheapest_flight(self, flight_prices: dict) -> tuple:
        """
        最安値のフライトを探す

        Args:
            flight_prices (dict): フライト情報と価格の辞書

        Returns:
            tuple: 便名と価格の辞書
        """
        cheapest_flight = None
        cheapest_price = float("inf")

        for flight, prices in flight_prices.items():
            min_price = min(prices)
            if min_price < cheapest_price:
                cheapest_price = min_price
                cheapest_flight = flight

        return cheapest_flight, cheapest_price

    def select_cheapest_flight(
        self, cheapest_flight: str, cheapest_price: int
    ) -> None:
        """
        最安値のフライトを選択する

        Args:
                cheapest_flight (str): 最安値のフライト名
                cheapest_price (int): 最安値の価格
        """
        # HACK: 便名を指定する必要がある
        self.__page.wait_for_selector(f"text=¥{cheapest_price:,}")
        self.__page.get_by_role("row", name=cheapest_flight).get_by_role(
            "cell", name=f"¥{cheapest_price:,}"
        ).click()

    def buy_flight(self) -> None:
        """フライトを購入する"""
        self.__page.locator("#form-cart").get_by_role(
            "button", name="次へ"
        ).click()

    def __str__(self) -> str:
        """
        文字列化メソッド

        Returns:
            str: frame_url_idの文字列表現
        """
        return f"FlightSelectionPage(frame_url={self.frame.url})"
