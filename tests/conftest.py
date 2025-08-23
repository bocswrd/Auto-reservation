import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """Playwrightのインスタンスをセットアップ"""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="module")
def browser(playwright_instance):
    """
    ブラウザのインスタンスをセットアップ
    Args:
        playwright_instance: Playwrightのインスタンス
    """
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """
    ブラウザコンテキストをセットアップ
    Args:
        browser: ブラウザのインスタンス
    """
    context = browser.new_context(
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
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """
    ページのインスタンスをセットアップ
    Args:
        context: ブラウザコンテキストのインスタンス
    """
    page = context.new_page()
    yield page
