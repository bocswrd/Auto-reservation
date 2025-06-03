import os
import pytest
from unittest.mock import patch
from playwright.sync_api import sync_playwright
from airdo_reserve_playwright import run


@pytest.fixture(scope="module")
def playwright_instance():
    """Playwrightのインスタンスをセットアップ"""
    with sync_playwright() as playwright:
        yield playwright


@patch("dotenv.load_dotenv", lambda: None)
@patch.dict(
    os.environ,
    {
        "DEPARTURE_AIRPORT": "HND",
        "ARRIVAL_AIRPORT": "SPK",
        "DEPARTURE_DATE": "2025-07-10",
        "RETURN_DATE": "2025-07-15",
        "OUTBOUND_TAKEOFF_HOUR": "6",
        "OUTBOUND_TAKEOFF_MINUTE": "0",
        "OUTBOUND_LANDING_HOUR": "8",
        "OUTBOUND_LANDING_MINUTE": "30",
        "RETURN_TAKEOFF_HOUR": "18",
        "RETURN_TAKEOFF_MINUTE": "0",
        "RETURN_LANDING_HOUR": "20",
        "RETURN_LANDING_MINUTE": "30",
        "LAST_NAME": "ヤマダ",
        "FIRST_NAME": "タロウ",
        "AGE": "30",
        "E_MAIL": "test@example.com",
        "TEL_NUMBER": "09012345678",
    },
    clear=True,
)
def test_airdo_reserve(playwright_instance):
    """AirDo予約フローのテスト"""
    try:
        run(playwright_instance)
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")
