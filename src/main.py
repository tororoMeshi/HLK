# http.serverモジュールからBaseHTTPRequestHandlerとHTTPServerクラスをインポート
from http.server import BaseHTTPRequestHandler, HTTPServer
# ファイルシステムパス操作のためのpathlibモジュールからPathクラスをインポート
from pathlib import Path

# HTTPリクエストを処理するためのカスタムハンドラクラス
class LogShipperHandler(BaseHTTPRequestHandler):
    # ログファイルが格納されているディレクトリのパス
    log_dir = "/var/log/pods"

    # GETリクエストを処理するメソッド
    def do_GET(self):
        # 200 OKレスポンスをクライアントに送信
        self.send_response(200)
        # レスポンスのContent-Typeヘッダーを設定
        self.send_header("Content-type", "text/plain; charset=utf-8")
        # ヘッダーの送信を完了
        self.end_headers()
        # 指定されたディレクトリ内のファイルを走査
        for filepath in Path(self.log_dir).iterdir():
            # ファイルの場合のみ処理を実行
            if filepath.is_file():
                # ファイルを開いて内容を読み取り
                with filepath.open("r") as f:
                    # ファイルの内容をレスポンスとして送信
                    self.wfile.write(f.read().encode())

# HTTPサーバーを起動する関数
def run(server_class=HTTPServer, handler_class=LogShipperHandler, port=8080):
    # サーバーのアドレスとポートを設定
    server_address = ("", port)
    # HTTPサーバーインスタンスを作成
    httpd = server_class(server_address, handler_class)
    # サーバーの起動メッセージを表示
    print(f"Starting httpd on port {port}...")
    # サーバーを永久に実行
    httpd.serve_forever()

# スクリプトが直接実行された場合にサーバーを起動
if __name__ == "__main__":
    run()

