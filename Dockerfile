# 使用するPythonのベースイメージ
FROM python:3.12-slim-bookworm

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナ内にコピー
COPY src/main.py ./main.py

# コンテナ起動時にPythonスクリプトを実行
CMD ["python", "./main.py"]

