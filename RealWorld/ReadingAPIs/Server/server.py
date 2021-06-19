from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import pandas as pd


class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # /api/<something>   <--- We want this
        path = re.match("^\/api\/(.*)", self.path)

        if path is not None:
            fileroot = path.groups()[0]
            try:
                api_file = self.load_file(fileroot)
                api_file_json = api_file.to_json()
                self.return_api_json(api_file_json)
            except:
                self.return_error()
        else:
            self.return_api_index()

    def load_file(self, fileroot):
        full_file = f"Data/{fileroot}.csv"
        file = pd.read_csv(full_file)
        return file

    def return_api_index(self):
        with open("Content/index.html", "r") as index:
            index_file = index.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(index_file, "utf-8"))

    def return_error(self):
        self.send_response(500)
        self.end_headers()

    def return_api_json(self, api_json):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes(api_json, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8000), APIHandler)
    print("Web Server Started: http://localhost:8000")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print(f"Server requested to be stopped...")

    webServer.server_close()
    print(f"Web server stopped...")
