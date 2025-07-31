# action_bool と SimpliseClient.action.execute の統合テスト

このディレクトリには、`action_bool`と`SimpliseClient.action.execute`を組み合わせた統合テストが含まれています。

## ファイル構成

### 1. 基本テスト
- `test_bool.py` - `action_bool`関数の基本的なテストケース

### 2. 統合テスト（モック）
- `test_bool_integration_mock.py` - モックAPIを使用した統合テスト

### 3. 統合テスト（実際のAPI）
- `test_bool_integration_real.py` - 実際のSimplise APIを使用した統合テスト

### 4. サンプルコード
- `../../examples/action_bool_example.py` - 実際の使用例を示すサンプル

## テストの実行方法

### 基本テスト + モックテストの実行
```bash
# 基本テストのみ
pytest tests/actions/data/test_bool.py -v

# モック統合テスト
pytest tests/actions/data/test_bool_integration_mock.py -v

# 両方同時に実行
pytest tests/actions/data/test_bool*.py -v
```

### 実際のAPIテストの実行
実際のAPIキーが必要です：

```bash
# 環境変数を設定
export SIMPLISE_API_KEY="your_actual_api_key"

# テスト実行
pytest tests/actions/data/test_bool_integration_real.py -v
```

### サンプルコードの実行
```bash
# 環境変数を設定
export SIMPLISE_API_KEY="your_actual_api_key"

# サンプル実行
python examples/action_bool_example.py
```

## テスト内容

### action_bool(0) の検証
- `action_bool(0)` が `{"bool": ["0"]}` に正しく変換される
- API実行時に `"false"` が返される（ゼロは偽値）

### その他の値の検証
- 真値: `1`, `"hello"`, `True`, `42`, `-1` → `"true"`
- 偽値: `0`, `""`, `False` → `"false"`

### リクエスト形式の検証
- multipart/form-data形式で送信
- Authorizationヘッダーが正しく設定
- タイムアウト設定が適用

## 検証されている機能

1. **action_bool関数の正しい動作**
   - 様々な型の値を正しくOperation形式に変換

2. **SimpliseClient.action.executeの正しい動作**
   - Operationを正しいAPIリクエスト形式に変換
   - 認証ヘッダーの適切な設定
   - レスポンスの正しい処理

3. **統合的な動作**
   - action_boolとSimpliseClient.action.executeの組み合わせ
   - 実際のAPIとの互換性確認

これらのテストにより、`action_bool(0)`を`SimpliseClient.action.execute`で実行した際に、期待通り`"false"`が返されることが確認されています。
