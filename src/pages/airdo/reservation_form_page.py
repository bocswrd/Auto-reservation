from playwright.sync_api import Page


class ReservationFormPage:
    """
    予約フォームページのクラス
    Attributes:
        __page (Page): PlaywrightのPageオブジェクト
        AGE_INPUT (str): 年齢入力フィールドのセレクター
        EMAIL_INPUT (str): メールアドレス入力フィールドのセレクター
    """
    
    def __init__(self, page: Page):
        self.__page = page

    # Locators
    AGE_INPUT = "#age-1"
    EMAIL_INPUT = "#input-conf-req"

    def enter_individual_to_form(
        self,
        last_name: str,
        first_name: str,
        age: str,
        email: str,
        phone_number: str,
    ) -> None:
        """
        搭乗者情報をフォームへ入力する

        Args:
            last_name (str): 姓
            first_name (str): 名
            age (str): 年齢
            email (str): メールアドレス
            phone_number (str): 電話番号
        """
        self.enter_name(last_name, first_name)
        self.enter_age(age)
        self.enter_email(email)
        self.enter_phone_number(phone_number)

    def enter_name(self, last_name: str, first_name: str) -> None:
        """
        名前を入力する
        Args:
            last_name (str): 姓
            first_name (str): 名
        """
        self.__page.get_by_role("textbox", name="例）サトウ").fill(last_name)
        self.__page.get_by_role("textbox", name="例）イチロウ").fill(first_name)

    def enter_age(self, age: str) -> None:
        """
        年齢を入力する
        Args:
            age (str): 年齢
        """
        self.__page.fill(self.AGE_INPUT, age)

    def enter_email(self, email: str) -> None:
        """
        メールアドレスを入力する

        Args:
            email (str): メールアドレス
        """
        self.__page.get_by_role("textbox", name="例）sample@airdo.jp").fill(
            email
        )
        # 確認用メールアドレスも同じ値を入力する
        self.__page.fill(self.EMAIL_INPUT, email)

    def enter_phone_number(self, phone_number: str) -> None:
        """
        電話番号を入力する

        Args:
            phone_number (str): 電話番号
        """
        self.__page.get_by_role("textbox", name="例）09012345678").fill(
            phone_number
        )

    def submit_form(self):
        """
        フォームを送信する
        予約確認画面に遷移する
        """
        self.__page.get_by_role("button", name="確認画面に進む").click()
