from playwright.sync_api import Page


class ScreenshotManager:

    def __init__(self, page: Page, enable_screenshot: bool = True):
        self.page = page
        self.enable_screenshot = enable_screenshot

    def save_screenshot(self, filename: str) -> None:
        """
        スクリーンショットを撮影する
        Args:
            filename (str): スクリーンショットの保存先ファイル名
        """
        if self.enable_screenshot:
            self.page.screenshot(
                path=filename,
                full_page=True,
                animations="disabled",
                caret="hide",
            )
