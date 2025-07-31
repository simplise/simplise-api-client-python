# simplise-api-client テスト仕様書

## テスト概要

`simplise-api-client`ライブラリの最低限のテストコードを作成しました。本テストスイートは、ライブラリの主要機能をカバーし、継続的な開発とメンテナンスを支援します。

## テスト構成

### ファイル構成
```
tests/
├── __init__.py           # テストパッケージ初期化
├── conftest.py          # テスト設定とフィクスチャ
├── test_base.py         # ベースクライアント機能のテスト
└── test_actions.py      # アクション機能のテスト
```

### テストカバレッジ

現在のテストカバレッジ: **78%**

| モジュール | カバレッジ | 説明 |
|-----------|-----------|------|
| `__init__.py` | 100% | パッケージ初期化 |
| `actions/__init__.py` | 100% | アクション初期化 |
| `actions/decimal.py` | 100% | 小数計算アクション |
| `actions/utils.py` | 100% | ユーティリティ機能 |
| `base.py` | 69% | ベースクライアント機能 |
| `type.py` | 88% | 型定義 |

## テスト項目

### SimpliseClient テスト (test_base.py)

- **初期化テスト**
  - デフォルト値での初期化
  - カスタム値での初期化
  - 関連オブジェクトの作成確認

### ActionLogicAPI テスト (test_base.py)

- **値の文字列化テスト**
  - 基本型（int, float, bool）の文字列化
  - ネストした構造の文字列化
  - 既存の文字列の保持
  
- **API リクエストテスト**
  - 成功レスポンスの処理
  - 入力データありのリクエスト
  - 入力データなしのリクエスト

### Action テスト (test_base.py)

- **ロジック実行テスト**
  - JsonLogicルールの実行
  - エラーハンドリング

### Operation テスト (test_actions.py)

- **基本操作テスト**
  - Operation クラスの初期化
  - 辞書形式への変換
  - ネストした操作の処理

### アクション関数テスト (test_actions.py)

- **ユーティリティ関数**
  - `action_input`: 入力参照の作成
  - `action_obj`: オブジェクト作成

- **小数計算関数**
  - `action_decimal_add`: 加算
  - `action_decimal_mul`: 乗算
  - `action_decimal_sub`: 減算
  - `action_decimal_div`: 除算
  - 複雑な計算の組み合わせ

## テスト実行方法

### 全テスト実行
```bash
python -m pytest tests/
```

### 特定のテストファイル実行
```bash
python -m pytest tests/test_base.py
python -m pytest tests/test_actions.py
```

### カバレッジレポート付き実行
```bash
python -m pytest tests/ --cov=src --cov-report=term-missing
```

### 詳細出力付き実行
```bash
python -m pytest tests/ -v
```

## 今後の拡張予定

### 追加すべきテスト項目

1. **統合テスト**
   - 実際のAPI呼び出しのモックテスト
   - エンドツーエンドのワークフローテスト

2. **エラーケーステスト**
   - ネットワークエラーの処理
   - 無効な入力データの処理
   - APIエラーレスポンスの処理

3. **パフォーマンステスト**
   - 大量データでのレスポンス測定
   - メモリ使用量の測定

4. **セキュリティテスト**
   - APIキーの適切な処理
   - 入力データの検証

### テストデータの拡張

- より複雑なJsonLogicルール
- 様々なデータ型でのテスト
- エッジケースのテストデータ

## メンテナンス

- テストの実行は継続的インテグレーション（CI）環境で自動化することを推奨
- 新機能追加時は対応するテストケースも同時に追加
- カバレッジは最低80%を維持目標とする
