# Simplise API Client for Python

Simplise API は、人とAIのためのインフォメーション マネジメント サービスです

## 概要

Simplise API は、現代のアプリケーション開発に必要な包括的な機能を提供するクラウドネイティブプラットフォームです。AIネイティブなアーキテクチャで設計され、開発者と AI エージェントの両方が効率的に利用できます。

## 使用例
```python
from simplise_api_client_python import SimpliseClient, action

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

