from playwright.sync_api import Playwright
from contextlib import contextmanager


class DriverManager:
    """
    Playwrightのドライバー管理クラス
    """

    def __init__(
        self,
        playwright: Playwright,
        headless: bool = False,
        executable_path: str = None,
    ):
        self.playwright = playwright
        self.headless = headless
        self.executable_path = executable_path
        self.browser = None
        self.context = None

    @contextmanager
    def launch(self):
        """
        ブラウザを起動し、コンテキストとページを作成する
        Returns:
            Page: Playwrightのページインスタンス
        """
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            executable_path=self.executable_path,
        )
        self.context = self.browser.new_context(
            ignore_https_errors=True,
            color_scheme="light",
            screen={
                "width": 1920,
                "height": 1080,
            },
            viewport={
                "width": 1920,
                "height": 1080,
            },
            locale="ja-JP",
            timezone_id="Asia/Tokyo",
        )
        try:
            yield self.context.new_page()
        finally:
            self.context.close()
            self.browser.close()
