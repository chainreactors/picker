---
title: Apache Struts2 Core Arbitrary Code Execution via OGNL Sandbox	Escape
url: https://seclists.org/fulldisclosure/2026/Nov/7
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.073458
---

# Apache Struts2 Core Arbitrary Code Execution via OGNL Sandbox	Escape

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 Core Arbitrary Code Execution via OGNL Sandbox Escape

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 1 Nov 2026 22:23:31 +0000

---

```
Description
Apache Struts2 Core version 7.4.0 and below attempt to prevent arbitrary code execution via Object-Graph Navigation
Language (OGNL) through several different mechanisms but only in a cursory fashion -- the libraries only guard against
immediate calls evaluated by the OGNL engine via `SecurityMemberAccess`, but an allowed call that, instead, accepts
nested arguments and, itself, invokes reflection internally executes outside of the scope of said cursory protections,
thereby enabling attackers to bypass the limited protections entirely.

It should be noted that this attack, obviously, only works in locations where the information system runs the
input/output through an OGNL parser and executor.  Moreover, there is a key difference between Struts2 Core 6.x and
below and 7.x -- 7.x favours a whitelist-based approach that is coupled with some blacklisting, while 6.x and below
only check a blacklist (if anything at all).  This means that for successful exploitation in 6.x and below, attackers
can simply find a call that uses reflection and that isn't explicitly blacklisted (e.g., `java.beans.Statement` and
`java.beans.Expression`), embed the otherwise disallowed reflective call, and watch it run.  In 7.x, however, attackers
must use something that has been explicitly allowed, first, as the wrapper, which raises the bar for exploitation,
reducing the likelihood for most systems running 7.x (if someone does not realise that the Struts2 Core library only
provides cursory protections, they will not understand the risk and may accidentally add something like
`java.beans.Statement`), but does not reduce the impact or eliminate the risk.

Impact
Attackers can bypass the Apache Struts2 Core and OGNL library's protections against arbitrary code execution via
malicious OGNL through nested calls, thereby executing arbitrary code on the information system.  Importantly, through
this, attackers can bypass not only the class/method checks, but also the static/non-static checks, allowing attackers
to, for example, call to `ProcessBuilder`, dump the environment variables via `System.getenv(String)`, and various
other such calls.

Steps to Reproduce
Sample Query
The following will work on Apache Struts2 Core versions 6.x and below (assuming that `query` runs through the OGNL
parser, etc. -- this can happen on the request, but also if the string is reflected back in, say, a JSP via tags that
do as such) without much effort.  On Apache Struts2 Core 7.x, though, `java.beans.Expression` would need to be
whitelisted, first.

GET
/search.action?query=new+java.beans.Expression(new+java.beans.Expression(%40java.lang.ProcessBuilder%40class,'new',new+Object%5B%5D%7Bnew+String%5B%5D%7B'/bin/sh','-c','id+%3E+%3C%3CREPLACE+ME+--+a+fresh+marker+file+path%3E%3E'%7D%7D).getValue(),'start',new+Object%5B0%5D).getValue()
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Apache Struts2 Core Arbitrary Code Execution via OGNL Sandbox Escape** *Daniel Owens via Fulldisclosure (Nov 01)*

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