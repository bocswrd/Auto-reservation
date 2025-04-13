# Locatorの選び方

## 一覧
優先度の降順に並んでいる。
|Locator|壊れにくさ|可読性|主な使いどころ|詳細|
|---|---|---|---|---|
|[`page.get_by_role()`](https://playwright.dev/python/docs/locators#locate-by-role)|*****|*****|全般|迷ったらこれ|
|[`page.get_by_test_id()`](https://playwright.dev/python/docs/locators#locate-by-test-id)|*****|****|全般(テスト専用)|テスト専用の属性。HTML改修にも強い。|
|[`page.get_by_label()`](https://playwright.dev/python/docs/locators#locate-by-label)|****|****|フォーム入力|フォーム入力に適している|
|[`page.get_by_placeholder()`](https://playwright.dev/python/docs/locators#locate-by-placeholder)|****|****|フォーム入力|プレースホルダーでフォーム要素を特定。|
|[`page.get_by_alt_text()`](https://playwright.dev/python/docs/locators#locate-by-alt-text)|****|***|画像|`alt`属性が正しく使われている画像向け。|
|[`page.get_by_title()`](https://playwright.dev/python/docs/locators#locate-by-title)|***|***|補足情報のある要素|`title`属性に頼るので実装依存。|
|[`page.get_by_text()`](https://playwright.dev/python/docs/locators#locate-by-text)|***|*****|ラベルやリンク|視覚的にはわかりやすいが文言変更に弱い。|
|[`page.locator("css=...")`](https://playwright.dev/python/docs/locators#locate-by-css-or-xpath)|**|**|全般|非推奨。最後の手段。|
|[ `page.locator("xpath=...")`](https://playwright.dev/python/docs/locators#locate-by-css-or-xpath)|*|*|複雑なDOM構造|非推奨。最後の手段。|

> 壊れにくさ: DOMの構造変更に対する コードへの影響度

## ユースケース別

### フォーム入力

| 条件 | おすすめロケーター|
|---|---|
|フォームにラベル（`<label>`）がある| ✅ `get_by_label()`|
|ラベルがない or ラベルが別要素にある| ✅ `get_by_role()`（+ `name=` でテキスト指定）              |
|アクセシビリティがきちんとしてるサイト| ✅ `get_by_role()`（安定性＆意図明確）|
|独自UIで構造が複雑| `get_by_placeholder()` や`get_by_test_id()` の検討も|

| 比較ポイント | `get_by_label()` | `get_by_role()` |
|--------------|------------------|-----------------|
| HTMLラベルに依存 | ✅ 必要 | ❌ 不要（ARIAなどでOK） |
| 可読性・シンプルさ | ◎ | ○（やや詳細） |
| 意図の明確さ | ○ | ◎（ロール+名前で明示） |
| アクセシビリティ要素に強い | △ | ◎ |
| テキスト変更の影響 | ラベル変更に弱い | name変更に弱い |


