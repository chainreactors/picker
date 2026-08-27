---
title: Escargot v4.3.0-214-gfaee4437 Unauthenticated Remote Debugger Allows Arbitrary JavaScript Evaluation and Local File Disclosure
url: https://seclists.org/fulldisclosure/2026/Aug/109
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:24.876832
---

# Escargot v4.3.0-214-gfaee4437 Unauthenticated Remote Debugger Allows Arbitrary JavaScript Evaluation and Local File Disclosure

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](108)
[By Date](date.html#109)
[![Next](/images/right-icon-16x16.png)](110)

[![Previous](/images/left-icon-16x16.png)](108)
[By Thread](index.html#109)
[![Next](/images/right-icon-16x16.png)](110)

![](/shared/images/nst-icons.svg#search)

# Escargot v4.3.0-214-gfaee4437 Unauthenticated Remote Debugger Allows Arbitrary JavaScript Evaluation and Local File Disclosure

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:46:01 -0400

---

```
An unauthenticated remote debugger vulnerability exists in Escargot
v4.3.0-214-gfaee4437 when the application is compiled with ESCARGOT_DEBUGGER
support and the debug server is enabled using --start-debug-server. The
debugger accepts client connections without authentication or authorization
and provides access to privileged debugger functionality.

An attacker capable of reaching the debugger interface can establish a
debugger session and evaluate JavaScript expressions within the target
runtime. Testing confirmed the vulnerability by executing
read("/etc/passwd") through the debugger and retrieving the contents of the
local file.

Technical Details

The vulnerability occurs because Escargot exposes remote debugger
HTTP/WebSocket endpoints without requiring authentication before
establishing a debugger session.

The exposed debugger routes include:

/escargot-debugger
/devtools/page/1
/json
/json/list
/json/version

Requests to the debugger WebSocket endpoints are routed to the WebSocket
handshake implementation. The handshake performs WebSocket protocol
negotiation but does not authenticate or authorize the connecting client
before providing access to debugger functionality.

Once connected, the debugger accepts evaluation commands that execute
JavaScript expressions within the target Escargot runtime.

The affected functionality is conditionally compiled with:

#ifdef ESCARGOT_DEBUGGER

and enabled at runtime using:

--start-debug-server

Root CauseNo authentication protecting the remote debugger No authorization
check before debugger access Network connectivity treated as sufficient
trust Privileged JavaScript evaluation exposed to debugger clients Debugger
helper functions expose local runtime resources

Impact

Unauthorized Debugger Access:
An unauthenticated client capable of reaching the debugger can
establish an interactive debugging session.

Arbitrary JavaScript Evaluation:
The connected client can submit JavaScript expressions for evaluation
within the target Escargot runtime.

Local File Disclosure:
Files accessible through exposed runtime helper functions can be
retrieved. Testing confirmed disclosure of /etc/passwd.

Runtime State Exposure:
An attacker may inspect interpreter state and interact with other
functionality exposed through the debugger.

The PoC demonstrates JavaScript evaluation and local file disclosure. It
does not, by itself, establish arbitrary operating-system command execution
or native code execution.

Proof of Concept

Start a debugger-enabled Escargot build with the remote debugger enabled
and connect using the debugger client.

The following debugger commands were used:

b /tmp/rdf.js:2
c
p read("/etc/passwd")
c

Output

Connecting to: localhost:6516
Connection created!!!

Stopped at /tmp/rdf.js:1

(escargot-debugger) b /tmp/rdf.js:2
Breakpoint 1 at /tmp/rdf.js:2

(escargot-debugger) c
Stopped at breakpoint:1 /tmp/rdf.js:2

(escargot-debugger) p read("/etc/passwd")
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
...
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

(escargot-debugger) c
Print: debugger file read probe complete
Connection closed.

Server-side output confirmed that the debugger was listening and accepted
the connection:

Waiting for client connection 0.0.0.0:6516
Connected from: 127.0.0.1

debugger file read probe complete

The returned data matched the contents of /etc/passwd, confirming that the
debugger accepted an unauthenticated session, evaluated the supplied
JavaScript expression, and returned local file contents to the debugger
client.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](108)
[By Date](date.html#109)
[![Next](/images/right-icon-16x16.png)](110)

[![Previous](/images/left-icon-16x16.png)](108)
[By Thread](index.html#109)
[![Next](/images/right-icon-16x16.png)](110)

### Current thread:

* **Escargot v4.3.0-214-gfaee4437 Unauthenticated Remote Debugger Allows Arbitrary JavaScript Evaluation and Local File Disclosure** *Ron E (Aug 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")