# Simplise API Client for Python

Simplise API は、人とAIのためのインフォメーション マネジメント サービスです

## 概要

Simplise API は、現代のアプリケーション開発に必要な包括的な機能を提供するクラウドネイティブプラットフォームです。AIネイティブなアーキテクチャで設計され、開発者と AI エージェントの両方が効率的に利用できます。

## データ検証

このクライアントライブラリは、APIリクエストとレスポンスの型安全性を確保するために**Pydantic**を使用しています。以下の利点があります：

- **型安全性**: APIとのやり取りにおけるデータの整合性を実行時に保証
- **バリデーション**: 不正なデータの早期検出とエラーハンドリング
- **文書化**: モデル定義がAPIインターフェースの自己文書化として機能

### バリデーションが適用される箇所

- `ActionLogicAPI.post()` - action-logicエンドポイントのリクエスト/レスポンス
- `Action.execute()` - アクション実行のリクエスト/レスポンス
- `Action.execute_logic()` - JsonLogicルール実行のリクエスト/レスポンス

データバリデーションに失敗した場合、`pydantic.ValidationError`が発生します。

## 使用例
```python
from simplise_api_client import SimpliseClient, action

client = SimpliseClient(api_key="your-api-key")

# ライブラリ モデルを利用した実行
result = client.action.execute(
    action.decimal.add(10, action.input("value")),
    action.decimal.mul(3, 4)
)

# JsonLogic Rule 実行
result = client.action.execute_logic(
    {
        "decimal.add": [
            "10",
            {"input": ["value"]},
            {"decimal.mul": ["3", "4"]}
        ]
    },
    {"value": "5"}
)

print(result)
```

