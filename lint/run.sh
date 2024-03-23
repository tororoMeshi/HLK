#!/bin/bash
set -eux

# 仮想環境の作成
echo "Creating virtual environment..."
python3 -m venv venv

# 仮想環境のアクティベート
echo "Activating virtual environment..."
source venv/bin/activate

# 必要なパッケージのインストール
echo "Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# インポートを整理します。
echo "Running isort..."
isort ../

# コードをフォーマットします。
echo "Running black..."
black ../

# 仮想環境のデアクティベート
echo "Deactivating virtual environment..."
deactivate

echo "Formatting complete!"
