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
chrome_options.headless = False  # これでブラウザが表示される
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Chromeドライバーのセットアップ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.airdo.jp/"
try:
    driver.get(url)

    # 航空券を検索する
    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "ticket-search")))
    # 「出発地」・「到着地」を指定
    Select(driver.find_element(By.NAME, "from")).select_by_value("HND")
    Select(driver.find_element(By.NAME, "to")).select_by_value("SPK")

    search_button.click()

    # HACK: webdriverwaitで待機する
    time.sleep(5)  # 画面遷移待ち（適宜調整）

    # 遷移後のページの情報を取得
    element = driver.find_element(By.XPATH, '//*[@id="tabSpS2"]/div/ul/li[9]')
    print(element.get_attribute("textContent"))
    print(element.text)
    # クリック前のクラスを取得
    before_class = element.get_attribute("class")
    print(f"クリック前: {before_class}")

    # クリックを実行
    # element.click()
    # driver.execute_script("arguments[0].click();", element)
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    driver.execute_script("document.querySelector('.rsv-select .table-calendar td:not(.select-disable), .list-calendar li:not(.select-disable)').click();")

    # クリック後のクラスを取得
    after_class = element.get_attribute("class")
    print(f"クリック後: {after_class}")


    button = driver.find_element(By.CSS_SELECTOR, "#form-cart button[type='submit']")
    button.click()

finally:
    driver.quit()
