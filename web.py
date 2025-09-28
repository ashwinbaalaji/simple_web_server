from django.shortcuts import render
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f9f9f9;
            text-align: center;
        }
        h1 {
            color: #333;
            margin: 20px 0;
        }
        table {
            width: 70%;
            margin: 0 auto;
            border-collapse: collapse;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            background: white;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #2c3e50;
            color: white;
            text-align: center;
        }
        .app { background-color: #ffcccc; }
        .trans { background-color: #cce5ff; }
        .internet { background-color: #ccffcc; }
        .network { background-color: #ffe5b4; }
        footer {
            margin-top: 30px;
            font-size: 14px;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>

    <table>
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
        </tr>
        <tr class="app">
            <td>Application Layer</td>
            <td>HTTP<br>HTTPS<br>FTP<br>DNS<br>Telnet<br>SSH</td>
        </tr>
        <tr class="trans">
            <td>Transport Layer</td>
            <td>TCP<br>UDP</td>
        </tr>
        <tr class="internet">
            <td>Internet Layer</td>
            <td>IP<br>ICMP<br>IPv4<br>IPv6</td>
        </tr>
        <tr class="network">
            <td>Network Access Layer</td>
            <td>Ethernet<br>Wi-Fi (IEEE 802.11)</td>
        </tr>
    </table>

    
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('',8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
