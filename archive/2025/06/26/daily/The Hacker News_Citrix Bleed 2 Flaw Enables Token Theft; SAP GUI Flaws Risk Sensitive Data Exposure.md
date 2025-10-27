---
title: Citrix Bleed 2 Flaw Enables Token Theft; SAP GUI Flaws Risk Sensitive Data Exposure
url: https://thehackernews.com/2025/06/citrix-bleed-2-flaw-enables-token-theft.html
source: The Hacker News
date: 2025-06-26
fetch_date: 2025-10-06T22:55:56.345786
---

# Citrix Bleed 2 Flaw Enables Token Theft; SAP GUI Flaws Risk Sensitive Data Exposure

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Citrix Bleed 2 Flaw Enables Token Theft; SAP GUI Flaws Risk Sensitive Data Exposure](https://thehackernews.com/2025/06/citrix-bleed-2-flaw-enables-token-theft.html)

**Jun 25, 2025**Ravie LakshmananData Privacy / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0hWG2QFXy25EJg7fwCJuaBN77GZKrc3dfykmDL7vyHsN3MLxpMwUDM6UtYSBBkYD9hEbt8SZYBwxVMz9R4ZR9gCHgFZYdA6cH-i1gsF_fs9z2Tm0nqbtpdYFrDp9luBRWPbRY7kSiO-4tJIx8MpgLDNIwaQR5z-GTTdaV4Ju6aXvKj8CueuCfuJRHTPku/s790-rw-e365/update.jpg)

Cybersecurity researchers have detailed two now-patched security flaws in [SAP Graphical User Interface](https://learning.sap.com/learning-journeys/introducing-sap-abap-platform-fundamentals/introducing-the-sap-gui-1) (GUI) for Windows and Java that, if successfully exploited, could have enabled attackers to access sensitive information under certain conditions.

The vulnerabilities, tracked as [CVE-2025-0055](https://nvd.nist.gov/vuln/detail/CVE-2025-0055) and [CVE-2025-0056](https://nvd.nist.gov/vuln/detail/CVE-2025-0056) (CVSS scores: 6.0), were patched by SAP as part of its [monthly updates for January 2025](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/january-2025.html).

"The research discovered that SAP GUI input history is stored insecurely, both in the Java and Windows versions," Pathlock researcher Jonathan Stross [said](https://pathlock.com/blog/security-alerts/cve-2025-0055-and-2025-0056/) in a report shared with The Hacker News.

SAP GUI user history [allows](https://help.sap.com/docs/sap_gui_for_windows/63bd20104af84112973ad59590645513/2b6697d3e4144c3dbb0815c84ab01418.html) users to access previously entered values in input fields with the goal of saving time and reducing errors. This historical information is stored locally on devices. This can include usernames, national IDs, social security numbers (SSNs), bank account numbers, and internal SAP table names.

The vulnerabilities identified by Pathlock are rooted in this input history feature, allowing an attacker with administrative privileges or access to the victim's user directory on the operating system to access the data within a predefined directory based on the SAP GUI variant.

* SAP GUI for Windows - %APPDATA%\LocalLow\SAPGUI\Cache\History\SAPHistory<WINUSER>.db
* SAP GUI for Java - %APPDATA%\LocalLow\SAPGUI\Cache\History or $HOME/.SAPGUI/Cache/History (Windows or Linux) and $HOME/Library/Preferences/SAP/Cache/History (macOS)

The issue is that the inputs are saved in the database file using a weak XOR-based encryption scheme in the case of SAP GUI for Windows, which makes them trivial to decode with minimal effort. In contrast, SAP GUI for Java stores these historical entries in an unencrypted fashion as Java serialized objects.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As a result, depending on the user input provided in the past, the disclosed information could include anything between non-critical data to highly sensitive data, thereby impacting the confidentiality of the application.

"Anyone with access to the computer can potentially access the history file and all sensitive information it stores," Stross said. "Because the data is stored locally and weakly (or not at all) encrypted, exfiltration through HID injection attacks (like USB Rubber Ducky) or phishing becomes a real threat."

Pathlock also pointed out the two vulnerabilities served as a foundation for a third information disclosure flaw ([CVE-2025-0059](https://nvd.nist.gov/vuln/detail/CVE-2025-0059), CVSS score: 6.0) in SAP NetWeaver Application Server ABAP, which is based on SAP GUI for HTML. However, it does not have a patch.

To mitigate any potential risks associated with information disclosure, it's advised to disable the input history functionality and delete existing database or serialized object files from the aforementioned directories.

### Citrix Patches CVE-2025-5777

The disclosure comes as Citrix [patched](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX693420) a critical-rated security flaw in NetScaler ADC (CVE-2025-5777, CVSS score: 9.3) that could be exploited by threat actors to gain access to susceptible appliances.

The shortcoming stems from insufficient input validation that may enable unauthorized attackers to grab valid session tokens from memory via malformed requests, effectively bypassing authentication protections. However, this only works when Netscaler is configured as a Gateway or AAA virtual server.

The vulnerability has been [codenamed](https://doublepulsar.com/citrixbleed-2-electric-boogaloo-cve-2025-5777-c7f5e349d206) Citrix Bleed 2 by security researcher Kevin Beaumont, owing to its similarities to [CVE-2023-4966](https://thehackernews.com/2023/11/lockbit-ransomware-exploiting-critical.html) (CVSS score: 9.4), which came under active exploitation in the wild two years ago.

It has been [addressed](https://www.netscaler.com/blog/news/critical-security-updates-for-netscaler-netscaler-gateway-and-netscaler-console/) in the following versions -

* NetScaler ADC and NetScaler Gateway 14.1-43.56 and later releases
* NetScaler ADC and NetScaler Gateway 13.1-58.32 and later releases of 13.1
* NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1-37.235 and later releases of 13.1-FIPS and 13.1-NDcPP
* NetScaler ADC 12.1-FIPS 12.1-55.328 and later releases of 12.1-FIPS

Secure Private Access on-prem or Secure Private Access Hybrid deployments using NetScaler instances are also affected by the vulnerabilities. Citrix is recommending that users run the following commands to terminate all active ICA and PCoIP sessions after all NetScaler appliances have been upgraded -

```` ```
kill icaconnection -all
kill pcoipConnection -all
``` ````

The company is also urging customers of NetScaler ADC and NetScaler Gateway versions 12.1 and 13.0 to move to a support version as they are now End Of Life (EOL) and no longer supported.

While there...