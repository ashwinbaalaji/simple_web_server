from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''<html>
<head>
<title>TCP/IP Model</title>
</head>
<body align="center">

<pre>
1. *Application Layer*

   * HTTP (HyperText Transfer Protocol)
   * FTP (File Transfer Protocol)
   * SMTP (Simple Mail Transfer Protocol)
   * DNS (Domain Name System)
   * Telnet

2. *Transport Layer*

   * TCP (Transmission Control Protocol)
   * UDP (User Datagram Protocol)

3. *Internet Layer*

   * IP (Internet Protocol)
   * ICMP (Internet Control Message Protocol)
   * ARP (Address Resolution Protocol)

4. *Network Access Layer (Link Layer)*

   * Ethernet
   * Wi-Fi
   * PPP (Point-to-Point Protocol)
   </pre>
</body>



</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()