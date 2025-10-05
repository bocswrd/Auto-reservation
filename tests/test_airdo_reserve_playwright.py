import os
import pytest
from unittest.mock import patch
from airdo_reserve_playwright import run


@patch("dotenv.load_dotenv", lambda: None)
@patch.dict(
    os.environ,
    {
        "EXECUTE_RESERVATION": "false",
        "DEPARTURE_AIRPORT": "HND",
        "ARRIVAL_AIRPORT": "SPK",
        "DEPARTURE_DATE": "2025-10-21",
        "RETURN_DATE": "2025-10-22",
        "OUTBOUND_TAKEOFF_HOUR": "18",
        "OUTBOUND_TAKEOFF_MINUTE": "0",
        "OUTBOUND_LANDING_HOUR": "20",
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
def test_airdo_reserve(page):
    """AirDo予約フローのテスト"""
    try:
        run(page)
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")
