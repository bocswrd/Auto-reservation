from selenium.webdriver.common.by import By


class InputCustomerInfoPage:
    """Page Object for the Input Customer Info Page."""

    def __init__(self, driver):
        """
        Initialize the page object.

        :param driver: WebDriver instance
        """
        if driver is None:
            raise ValueError("Driver instance cannot be None")
        if driver.title != 'お客様情報入力｜北海道発着の飛行機予約ならAIRDO（エア・ドゥ）':
            raise ValueError(f"Unexpected page title. Title: {driver.title}.")
        self.driver = driver

    # Locators
    FIRST_NAME_INPUT = (By.ID, "FirstName1")
    LAST_NAME_INPUT = (By.ID, "lastName1")
    AGE_INPUT = (By.ID, "age-1")
    EMAIL_INPUT = (By.ID, "input-mail-req")
    EMAIL_CONFIRM_INPUT = (By.ID, "input-conf-req")
    PHONE_INPUT = (By.ID, "telNumber")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def set_reservationInfo(self, first_name, last_name, age, email, phone_number):
        """
        予約情報を入力します
        Args:
            first_name (str): 搭乗者の名
            last_name (str): 搭乗者の姓
            age (str): 搭乗者の年齢
            email (str): 搭乗者のメールアドレス
            phone_number (str): 搭乗者の電話番号
        Returns:
            None
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.AGE_INPUT).send_keys(age)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.EMAIL_CONFIRM_INPUT).send_keys(email)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone_number)

    def click_submit(self):
        """
        「確認画面へ進む」ボタンをクリックします
        Returns:
            None
        """
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
