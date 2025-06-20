# SPACE AI MAKER - Backend

本リポジトリはSPACE AI MAKERのバックエンドのリポジトリである。

## 改訂履歴

| 日付         | 改訂者 | 改訂内容                      |
|------------|-----|---------------------------|
| 2025/05/20 | 今村  | 新規作成                      |
| 2025/06/20 | 今村  | 「.envファイル」節を追記        |

## 開発環境

主な開発環境の種類とバージョンは以下のとおりである。

* Mac
    * Sonoma 4.6.1 (M1)
* Node
    * v22.15.0
* Python
    * 3.11.12
* Docker
    * Docker version 20.10.17, build 100c701
* Google Chrome (Webブラウザ)
    * 135.0.7049.115（Official Build） （arm64）

## ブランチ戦略

* `main`：本リポジトリのマスターブランチ。リリースごとにdevelopをマージしていく。
* `develop`：開発機能をメインで取り込むブランチ。各機能の開発をマージする際は`develop`にマージすること。
* `feature/xxx`：新規機能を開発する際に指定するブランチ。
* `fix/xxx`：バグなどによる修正をする際に指定するブランチ。
* `doc/xxx`：ドキュメント系の作成や修正をする際に指定するブランチ。

状況に応じて上記を使い分けること。  
上記に含まれないようなコミットをする場合は各々で適当なブランチ名とすること。

## 環境構築手順

### 1. Docker Desktopのインストール

Docker Desktopをインストールする。

Windowsの場合：https://docs.docker.jp/desktop/install/windows-install.html

Macの場合：https://docs.docker.jp/desktop/install/mac-install.html

インストール後、以下のコマンドを実行して正常にインストールされたかを確認する。

```
$ docker -v
Docker version 20.10.17, build 100c701
```

```
$ docer-compose -v
Docker Compose version v2.10.2
```

### 2. Gitクライアントのインストール

以下のURLからそれぞれのOSに沿ったForkのインストーラーをダウンロードする。

* https://git-fork.com/

※Gitクライアントについて、Forkを指定しているがSourceTreeなどでも可。  
(自分の使いやすいものでOK)

### 3. Pythonのインストール

以下のURLからPythonの3.11.9をインストールする。(mock用)

* https://www.python.org/downloads/release/python-3119/

本来は、3.11.12をインストールしたいが、以下を見る限り3.11.10 ~ 12のインストーラーはなさそう。

* https://www.python.org/downloads/release/python-31112/

### 4. ソースコードのClone

Forkの左のメニューにある「Repository」右クリックして、「Clone...」を選択する。

![スクリーンショット 2025-04-29 16 09 29](https://github.com/user-attachments/assets/aa9c9043-39ad-4c34-8f88-40b2f0587c0c)

「URL」に「`git@github.com:SFgenAI-dev2504/back.git`」を記載し、適宜「Location」にクローン場所を記載する。  
(※画像はフロントエンドのリポジトリのもの)

![スクリーンショット 2025-04-29 16 10 07](https://github.com/user-attachments/assets/d9334137-e477-4d69-80e1-d3f8ead4f06b)
(※画像はフロントエンドのリポジトリのもの)

「Clone」ボタンをクリックする。

![スクリーンショット 2025-04-29 16 10 32](https://github.com/user-attachments/assets/8b99ce0a-69df-4458-8a66-4c86cd9b4b0f)
(※画像はフロントエンドのリポジトリのもの)

「Location」に指定した場所のソースコードがコピーされる。

### 4. Webアプリの起動

以下のコマンドを実行して、イメージをビルドしてコンテナを起動する。(※基本初回のみ)

```docker
$ docker-compose up --build
```

### その他

Dockerコンテナの中でコマンドを実行したい場合は、以下のコマンドを実行する。

```
// apiのコンテナに入る場合
$ docker-compose exec api bash
```

以下のようにコンテナ内に入ることができる。

```
root@<コンテナID>:/app#
```

例えば、Pythonのバージョン、ライブラリの一覧を見たい時などはコンテナ内で以下を実行する。

```
$ python --version
Python 3.11.12
```

```
$ pip list
Package                Version
---------------------- -------
blinker                1.9.0
click                  8.1.8
Flask                  2.3.3
Flask-SQLAlchemy       3.1.1
greenlet               3.2.1
itsdangerous           2.2.0
Jinja2                 3.1.6
MarkupSafe             3.0.2
mysql-connector-python 8.3.0
pip                    24.0
setuptools             65.5.1
SQLAlchemy             2.0.40
typing_extensions      4.13.2
Werkzeug               3.1.3
wheel                  0.45.1
```

## .envファイル

本リポジトリでは.envファイルで環境変数を設定している。
値がわからない場合は開発担当者に確認すること。

```
OPENAI_API_KEY=xxx
SERVER_IMAGE_PATH=yyy
```

## トラブルシューティング

トラブルシューティングを記載する。

### docker-compose up --build で「Error response from daemon: Ports are not available ... address already in use」が発生する

Macで以下のようなエラーが発生した場合、ControlCeという機能(Monterey以降実装された機能)が5001番ポートで起動されている可能性がある。

```
Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5001 -> 0.0.0.0:0: listen tcp 0.0.0.0:5001: bind: address already in use
```
