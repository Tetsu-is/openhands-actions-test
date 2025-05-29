# FastAPI 3層アーキテクチャ

このプロジェクトは、FastAPIを使用した3層アーキテクチャ（Model-View-Controller）に基づいて設計されています。

## アーキテクチャ概要

### 1. Model層 (`src/model.py`)
- **役割**: ドメインモデルとデータの永続化を担当
- **主要クラス**: `Item`
- **機能**:
  - アイテムデータの格納（`_item_list`配列）
  - アイテムの作成（`create`メソッド）
  - アイテムの読み込み（`read`メソッド）
  - データのカプセル化（外部から直接配列にアクセスできない）

### 2. View層 (`src/view.py`)
- **役割**: リクエストとレスポンスのデータ構造を定義
- **主要クラス**:
  - `ItemCreateRequest`: アイテム作成リクエストの構造
  - `ItemCreateResponse`: アイテム作成レスポンスの構造
  - `ItemReadRequest`: アイテム読み込みリクエストの構造
  - `ItemReadResponse`: アイテム読み込みレスポンスの構造
- **機能**: Pydanticを使用したデータバリデーションとシリアライゼーション

### 3. Controller層 (`src/controller.py`)
- **役割**: ビジネスロジックとリクエスト処理を担当
- **主要関数**:
  - `create_item_controller`: アイテム作成処理
  - `read_items_controller`: アイテム読み込み処理
- **機能**:
  - リクエストの解析
  - Modelを使用したデータ操作
  - Viewを使用したレスポンス生成

### 4. エントリーポイント (`src/main.py`)
- **役割**: FastAPIアプリケーションの設定とエンドポイントの定義
- **機能**:
  - FastAPIアプリケーションの初期化
  - CORSミドルウェアの設定
  - エンドポイントの定義（Controller層の関数を呼び出し）

## API エンドポイント

### POST /items/
- **説明**: 新しいアイテムを作成
- **リクエスト**: `{"name": "アイテム名"}`
- **レスポンス**: `{"message": "Item added", "item": "アイテム名"}`

### GET /items/
- **説明**: 全てのアイテムを取得
- **レスポンス**: `{"items": ["アイテム1", "アイテム2", ...]}`

## テスト構成

各層に対応するテストファイルが用意されています：

- `src/tests/test_model.py`: Model層のテスト
- `src/tests/test_view.py`: View層のテスト
- `src/tests/test_controller.py`: Controller層のテスト
- `src/tests/test_main.py`: 統合テスト（API エンドポイントのテスト）

## 実行方法

### 依存関係のインストール
```bash
make setup
```

### サーバーの起動
```bash
make run
```

### テストの実行
```bash
make test
```

## アーキテクチャの利点

1. **関心の分離**: 各層が明確な責任を持つ
2. **テスタビリティ**: 各層を独立してテスト可能
3. **保守性**: 変更の影響範囲が限定される
4. **拡張性**: 新機能の追加が容易
5. **再利用性**: 各層のコンポーネントを他の部分で再利用可能
