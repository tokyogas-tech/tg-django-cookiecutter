# 開発環境構築

## publickey設置
 
- プロジェクトの.certificatesにpubファイル作成
  - 自身のsshのpublickeyを、dev.pubとして配置する

## dockerイメージビルド

- docker-compose up -d --build
  - 暫くしたらsshでアクセス出来るようになる

```shell
$ ssh root@0.0.0.0 -p 2222
```

## docker内作業

### 初回処理

- docker内に入り、以下を実行して、packageのインストール/migrate等

```shell
$ . ./init.sh
```

- adminユーザーのパスワード変更(optional)

```shell
$ source /var/{{ cookiecutter.repo_name }}/.venv/bin/activate
$ cd /var/{{ cookiecutter.repo_name }}/src
$ python manage.py changepassword admin
```

### サーバー起動

- docker内に入り、以下を実行してrunserverを起動

```shell
$ source /var/{{ cookiecutter.repo_name }}/.venv/bin/activate
$ cd /var/{{ cookiecutter.repo_name }}/src
$ honcho start -f Procfile
```

- ブラウザでサイトが立ち上がっていることを確認

```shell
http://0.0.0.0:8000
```

## メールサーバー

- dockerでmailcatcherを立ち上げているので、以下のURLでメール確認可能

```shell
http://0.0.0.0:1080/
```

## RabbitMQ

- dockerでRabbitMQを立ち上げているので、以下のURLでQueue確認可能

```shell
http://0.0.0.0:15672/
```

## pre-commit使用方法

- Macへpre-commitをインストール

```shell
$ brew install pre-commit
```

- gitのhookとしてpre-commitをインストール

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## ruff使用方法

```shell
$ ruff check . --fix
```