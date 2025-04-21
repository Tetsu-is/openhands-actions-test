# OpenHands resolverを導入する方法

## OpenHandsの概要
### できること
- issueを使って実装タスクやバグ修正を命令できます。
- sandboxに必要な依存関係をカスタマイズできます。
- `.openhands_instructions`を使って前提知識を読み込ませることができます。

### 仕組み
- github actionsのworkflowでissueのラベル付与や@openhands-agentのメンションをトリガーにして実行します。
- resolverがissueの内容を読み込みます。
- dockerを使ってsandbox環境を作り、タスクを実行します。
- 実行結果をpull requestとして出力します。

### 事前準備
- githubのPATを作成します。read/write scope for "contents", "issues", "pull requests", and "workflows"
- LLMのAPIキーを設定します。

## 導入手順
[openhands-resolver.ymlの例](https://github.com/All-Hands-AI/OpenHands/blob/main/.github/workflows/openhands-resolver.yml)
1. リポジトリに`.github/workflows/openhands-resolver.yml`を作成します。
2. repositoryの設定から必要なシークレットを設定します。
   - `LLM_API_KEY`: LLMのAPIキー（必須）
   - `LLM_BASE_URL`: LLMのベースURL（オプション）
   - `PAT_TOKEN`: GitHubのPersonal Access Token（オプション）
   - `PAT_USERNAME`: GitHubのユーザー名（オプション）

3. ワークフローのトリガー設定を行います。
   - Issueにラベルが付与された時
   - Pull Requestにラベルが付与された時
   - Issueコメントが作成された時
   - Pull Requestレビューコメントが作成された時
   - Pull Requestレビューが提出された時

4. エージェントを実行します (github actionsのworkflowのトリガーになるものであればどんなものでもOK)。
   - Issueに`fix-me`ラベルを付与します。
   - コメントで`@openhands-agent`をメンションします。

5. 実行結果の確認を行います。
   - 成功時：ドラフトPRが自動作成されます。
   - 失敗時：変更内容がブランチとして保存されます。
   - 実行ログはGitHub Actionsのログで確認できます。

## custom sandboxの設定方法
[openhands-resolver.ymlの例](https://github.com/Tetsu-is/openhands-actions-test/blob/main/.github/workflows/openhands-resolver.yml)

sandboxのビルドは二段階になっています。base-container-imageでプロジェクトに必要な依存関係をインストールします。runtime-container-imageではbase-container-imageをベースにして開発環境を含んだimageをビルドします。

デフォルトのbase-container-imageはnikolaik/python-nodejs:python3.12-nodejs22になっているので、pythonやnodejs以外を使う場合は
`base container image`を変更する必要があります。
1. sandbox用のdocker imageを作成します。
   - a. workflow内でDockerfileからimageをビルドします。
   - b. registryからimageを取得します。
      - gcloudの認証
      - docker pull
2. `openhands.resolve_issue`の実行時オプションで`--base-container-image`にimageを指定します。

## チューニング方法
1. プロジェクトのルートに`.openhands_instrcutions`を配置してプロジェクトの情報を与えます。

   LLMへのpromptはissueに書かれている情報と`.openhands_instructions`に書いた内容から生成されるようになっているので`.openhands_instructions`にはリポジトリに関する一般的な情報を記載します。公式にはサンプルを用意していないので有志の例や私が試したときの結果を参考に書いています。OpenHandsの他のモードにはmicroagentという特定のタスクやドメイン知識に特化したpromptを設定するツールがあるので、microagentの例は参考にできると思います。

   [.openhands_instructionsの例](https://github.com/zachmayer/caretEnsemble/blob/main/.openhands_instructions)

   [OpenHandsのmicroagentのrepository説明の例](https://github.com/All-Hands-AI/OpenHands/blob/main/.openhands/microagents/repo.md)

   
   記載する内容
   
   - セットアップ方法
   - プロジェクト構成
   - makeコマンドの説明
   ```
   ## General Setup
   - run `make setup`

   ## Makefile targets:
   - make setup: setup dependencies
   - make lint: run lint
   - make format: format code

   ## Repository Structure:
   Frontend:
   - Located in `frontend/` directory
   - Setup: Run `npm install` to install dependencies in `frontend/` directory
   - Testing: Run `npm run test`

   Backend:
   - Located in `backend/` directory
   - Setup: Run `pip install -r requirements.txt` to install dependencies in `backend/` directory
   - Testing: Run `pytest backend/tests/`

   ## Code Style:
   - name React components with UpperCamelCase
   - python test code must be in `backend/tests/` directory
   - python test code must be named like `test_*.py`
   ```

## 注意事項
- base-container-imageでパス関連を決めた場合はruntime-container-imageのビルドでworking directoryが変わるので相対パスなどには気をつける必要があります。
- runtime-container-imageのビルドでaptコマンドを使用するのでbase imageにはdebian系しか使えません。
