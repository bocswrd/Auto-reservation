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

import time

# Chromeのオプション設定
chrome_options = Options()
# chrome_options.add_argument("--headless")  # ヘッドレスモード（GUIなし）
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.headless = False  # これでブラウザが表示される

# Chromeドライバーのセットアップ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # AIRDOのチケット検索ページにアクセス
    url = "https://www.airdo.jp/"  # 実際のURLに変更してください
    driver.get(url)

    # ボタンが表示されるまで待機
    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "ticket-search")))

    # 「出発地」を指定
    departure_select = Select(driver.find_element(By.NAME, "from"))
    departure_select.select_by_value("HND")

    # 「到着地」を指定
    departure_select = Select(driver.find_element(By.NAME, "to"))
    departure_select.select_by_value("SPK")


    # ボタンをクリック
    search_button.click()

    # ページ遷移を待つ
    time.sleep(5)  # 画面遷移待ち（適宜調整）

    # 遷移後のページの情報を取得
    # print(driver.page_source)
    print('complete')

finally:
    driver.quit()
