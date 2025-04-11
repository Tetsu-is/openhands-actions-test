# OpenHands resolverを導入する方法

## OpenHandsの概要
### できること
- github actionsのworkflowとしてエージェントを動かす
- issueを使って実装タスクやバグ修正を命令する
- sandboxに必要な依存関係をカスタマイズする
- 前提知識をファイルを使って読み込ませる

### 事前準備
- githubのPATを作成する
- LLMのAPIキー

## 導入手順
[openhands-resolver.ymlの例](https://github.com/All-Hands-AI/OpenHands/blob/main/.github/workflows/openhands-resolver.yml)
1. リポジトリに`.github/workflows/openhands-resolver.yml`を作成する
2. repositoryの設定から必要なシークレットを設定する
   - `LLM_API_KEY`: LLMのAPIキー（必須）
   - `LLM_BASE_URL`: LLMのベースURL（オプション）
   - `PAT_TOKEN`: GitHubのPersonal Access Token（オプション）
   - `PAT_USERNAME`: GitHubのユーザー名（オプション）

3. ワークフローのトリガー設定
   - Issueにラベルが付与された時
   - Pull Requestにラベルが付与された時
   - Issueコメントが作成された時
   - Pull Requestレビューコメントが作成された時
   - Pull Requestレビューが提出された時

4. エージェントの起動方法
   - Issueに`fix-me`ラベルを付与
   - コメントで`@openhands-agent`をメンション
   - ワークフローを直接呼び出し

5. 実行結果の確認
   - 成功時：ドラフトPRが自動作成される
   - 失敗時：変更内容がブランチとして保存される
   - 実行ログはGitHub Actionsのログで確認可能

## custom sandboxの設定方法
[openhands-resolver.ymlの例](https://github.com/Tetsu-is/openhands-actions-test/blob/main/.github/workflows/openhands-resolver.yml)

デフォルトのimageはnikolaik/python-nodejs:python3.12-nodejs22になっているので、pythonやnodejs以外の依存関係を使う場合は
base imageを変更する必要があります。
1. sandbox用のdocker imageを作成する
   - a. workflow内でDockerfileからimageをビルドする
   - b. registryからimageを取得する
2. `openhands.resolve_issue`の実行時オプションで`--base-container-image`にimageを指定する

## チューニング方法
1. プロジェクトのルートに`.openhands_instrcutions`を配置してプロジェクトの情報を与える
2. .openhands/setup.shで環境変数やコマンド実行を設定する


## 注意事項＆コツ


## パフォーマンス

## 今後追加される機能

