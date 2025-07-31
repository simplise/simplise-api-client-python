---
applyTo: "**/*.py"
---

# Coding Instructions

Python のコーディングに関するガイドライン。
Python のコードを生成する場合は必ずこのガイドラインに従うこと。

## コーディング規約と開発標準

以下の規約を厳守すること。

    設計原則:

        YAGNI (You Aren't Gonna Need It): 現在必要とされていない機能は実装しないこと。将来を予測した先行実装は避ける。
        DRY (Don't Repeat Yourself): コードの重複を避け、共通ロジックは関数やクラスに切り出して再利用すること。
        KISS (Keep It Simple, Stupid): 複雑な解決策よりも、シンプルで理解しやすいコードを優先すること。

    フォーマットと静的解析:

        フォーマッタ兼リンターは Ruff を使用する。設定は pyproject.toml に従うこと。
        コードを変更した場合は `uv run ruff format, uv run ruff check --fix` でフォーマットとチェックを実行し、警告やエラーを修正すること。

    型ヒント (Type Hinting):

        全ての関数・メソッドの引数と戻り値に型ヒントを付与すること。
        typing.Any, typing.Optional の使用は最小限に留めること。
        アプリ固有のデータ構造には、カスタム型（TypedDict, dataclasses等）を積極的に定義して使用すること。
        APIに渡したり受け取ったりするデータには、Pydanticモデルを使用して型チェックを行うこと。

    命名規則:

        変数・関数: snake_case
        クラス: PascalCase
        定数: UPPER_SNAKE_CASE

    モジュール構成:

        関心事を分離するため、機能ごとにモジュールを分割すること（例: actionsなど）。
        モジュール間の循環参照は禁止する。

    コメントとDocstring:

        全ての公開クラスと関数には、GoogleスタイルのDocstringを記述すること。
        Docstringは英語で記述し、それ以外のコメントは日本語で記述すること。
        Docstringの目的だけDocstringの下にコメントとして日本語で記述すること。

        AIが生成したコメントの先頭には [AI GENERATED] を付けること（ただしDocstring内は除く）。
        複雑なロジックには処理内容を説明するコメントを記述すること。

        例: add.py
        ```python
        """This module provides an addition operation."""
        # [AI GENERATED] This function adds two integers.
        def add(a: int, b: int) -> int:
            """Adds two integers and returns the result.

            Args:
                a (int): The first integer.
                b (int): The second integer.
            
            Returns:
                int: The sum of a and b.
            """
            # [AI GENERATED] Perform addition
            return a + b
        ```


    エラーハンドリング:

        try...except ブロックでは具体的な例外を捕捉し、汎用的な except Exception: は避けること。
        exceptionのメッセージは具体的で問題の特定に役立つ情報を含め、 logging を使用してログに記録すること。

    設定と秘匿情報:

        秘匿情報はコードに直接記述せず、.env ファイルで管理すること。
        .gitignore により、.env がリポジトリに含まれないことを確認すること。
        .env ファイルは `env.py` の `setup_environment` 関数を使用して読み込むこと。

    ロギング:

        ロギングには logging を使用すること。
        ログレベル（DEBUG, INFO, WARNING, ERROR）を適切に使い分け、デバッグや問題追跡に役立つ情報を出力すること。
        logging の設定は `logging_conf.py` に定義し、 `setup_logger` 関数を使用してアプリケーション全体で統一すること。