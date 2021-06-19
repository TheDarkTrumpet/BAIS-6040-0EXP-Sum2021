from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import pandas as pd
import json


class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = re.match("^\/api\/(.*)", self.path)

        if path is not None:
            fileroot = path.groups()[0]
            try:
                api_file = self.load_file(fileroot)
                api_file_json = api_file.to_json()

            except:
                self.return_error()
        else:
            self.get_api_index()

    def load_file(self, fileroot):
        full_file = f"../data/{fileroot}.csv"
        file = pd.read_csv(full_file)
        return file

    def return_api_index(self):
        pass

    def return_error(self):
        self.send_response(500)

    def return_api_json(self, api_json):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(api_json)


if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8000), APIHandler)
    print("Web Server Started: http://localhost:8000")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print(f"Server requested to be stopped...")

    webServer.server_close()
    print(f"Web server stopped...")
