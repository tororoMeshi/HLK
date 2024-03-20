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
pip install -r requirements.txt

# テストの実行
echo "Running tests..."
python test_main.py

# 仮想環境のデアクティベート
echo "Deactivating virtual environment..."
deactivate

echo "Test process completed."
