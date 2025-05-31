from airdo_reserve_playwright import reserve


def main():
    print("==========================")
    print("航空券自動予約システム")
    print("1. 予約\n2. 設定\n0. 終了")
    print("==========================")
    option = input("選択してください: ")
    match option:
        case "0":
            print("システムを終了します。")
            return
        case "1":
            print("予約を選択しました")
            reserve()
            print("予約が完了しました")
        case "2":
            print("設定を選択しました")
            # Call the settings function here
        case _:
            print("無効な選択です。もう一度やり直してください。")
    print("==========================")
    main()


if __name__ == "__main__":
    # import sys

    # Add the src directory to the Python path
    # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
    main()
