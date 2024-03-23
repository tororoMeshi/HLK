# test/test_main.py
import unittest

import requests


class TestLogShipperServer(unittest.TestCase):
    def test_get_logs(self):
        # 仮にサーバーが localhost の 8080 ポートで実行されているとします
        # response = requests.get('http://192.168.10.113:8080')
        # response = requests.get('http://localhost:8081')
        response = requests.get("http://192.168.100.203:30042", timeout=5)
        # ステータスコードが 200 であることを確認
        self.assertEqual(response.status_code, 200)
        # 応答内容を検証（実際のログ内容に基づいて適宜調整が必要です）
        # ここでは応答の内容に特定のログメッセージが含まれているかを確認する例を示します
        self.assertIn("expected log message", response.text)


if __name__ == "__main__":
    unittest.main()
