from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from pages.InputCustomerInfoPage import InputCustomerInfoPage

import time
import os

load_dotenv()  # .env ファイルを読み込む

# Chromeのオプション設定
chrome_options = Options()
# chrome_options.add_argument("--headless")  # ヘッドレスモード（GUIなし）
chrome_options.headless = False  # これでブラウザが表示される
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("detach", True)  # ブラウザを閉じない

# Chromeドライバーのセットアップ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = "https://www.airdo.jp/"
try:
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # TODO: 出発地、到着地は動的に変更できるようにする
    # 「出発地」・「到着地」を指定
    Select(driver.find_element(By.NAME, "from")).select_by_value("HND")
    Select(driver.find_element(By.NAME, "to")).select_by_value("SPK")

    # 航空券を検索する
    wait.until(EC.element_to_be_clickable((By.ID, "ticket-search"))).click()

    # 画面遷移待ち
    wait.until(EC.title_is("便選択｜北海道発着の飛行機予約ならAIRDO（エア・ドゥ）"))

    # 予約する航空券を選択する
    # TODO: 条件に一致した航空券を選択できるようにする
    driver.find_element(
        By.XPATH,
        '//*[@id="tabS2"]/div[2]/div[1]/div/div/table/tbody/tr[1]/td/div/div[1]',
    ).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form-cart']/div/button[1]"))).click()
    driver.find_element(
        By.XPATH, "//div[@id='main']/article/div/div[5]/div/div/form/div/button"
    ).click()

    # 画面遷移待ち
    wait.until(EC.title_is("お客様情報入力｜北海道発着の飛行機予約ならAIRDO（エア・ドゥ）"))
    # お客様情報入力
    input_customer_info_page = InputCustomerInfoPage(driver)
    input_customer_info_page.set_reservationInfo(
        os.getenv("FIRST_NAME"),
        os.getenv("LAST_NAME"),
        os.getenv("AGE"),
        os.getenv("E_MAIL"),
        os.getenv("TEL_NUMBER"),
    )
    input_customer_info_page.click_submit()

    # チェックボタン押下
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.baggage-check-label"))).click()
    # TODO: チェックボックスを活性化させた後に処理を行う
    # 予約を確定する
    # driver.find_element(By.NAME, "reservation").click()


finally:
    print("処理が完了しました。")
    # driver.quit()
