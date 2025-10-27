---
title: Alert: Over 700,000 DrayTek Routers Exposed to Hacking via 14 New Vulnerabilities
url: https://thehackernews.com/2024/10/alert-over-700000-draytek-routers.html
source: The Hacker News
date: 2024-10-03
fetch_date: 2025-10-06T18:56:03.197970
---

# Alert: Over 700,000 DrayTek Routers Exposed to Hacking via 14 New Vulnerabilities

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

# [Alert: Over 700,000 DrayTek Routers Exposed to Hacking via 14 New Vulnerabilities](https://thehackernews.com/2024/10/alert-over-700000-draytek-routers.html)

**Oct 02, 2024**Ravie LakshmananVulnerability / Network Security

[![DrayTek Routers](data:image/png;base64... "DrayTek Routers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfAwA9qgWK-3YJzhQalw4VMQtpdw4rWDzJFRmF30l9w5o-rlQG1pK_d-o01MakzRoX18mbyqV6dHjU-0h4R07pt1U764DxLjI_ZzCfbtTXlapLh2jKIw2K70L-voewmphyGdbQB2foMvlCmCCJ_IEwTkONOUjE_szQ5coXWo0X70FhFDMtpr7mCHMzjLUa/s790-rw-e365/router-hacking.png)

A little over a dozen new security vulnerabilities have been discovered in residential and enterprise routers manufactured by DrayTek that could be exploited to take over susceptible devices.

"These vulnerabilities could enable attackers to take control of a router by injecting malicious code, allowing them to persist on the device and use it as a gateway into enterprise networks," Forescout Vedere Labs said in a technical [report](https://www.forescout.com/resources/draybreak-draytek-research/) shared with The Hacker News.

Of the 14 security flaws – collectively called DRAY:BREAK – two are rated critical, nine are rated high, and three are rated medium in severity. The most critical of the shortcomings is a flaw that has been awarded the maximum CVSS score of 10.0.

[![Router Vulnerabilities](data:image/png;base64... "Router Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXByBpjKNEmS9atnGN0gpRGpLBmXbLsOYo1F3gRqjs_lkvDR5YT3g2PeJsEXTeGAAwffL1YDAxezhOg1yz3JtGHZM0qdukiY02avVAYwScQlAFUMngBIrJcurM2wcM4I578_IVjHc1HfhzTZ9aElZMHaVr1LuA7Urx_Bf7AL5geQufG3Mu4PbPp8IEO3Ng/s790-rw-e365/router.png)

CVE-2024-41592 concerns a buffer overflow bug in the "GetCGI()" function in the Web user interface that could lead to a denial-of-service (DoS) or remote code execution (RCE) when processing the query string parameters.

Another critical vulnerability (CVE-2024-41585, CVSS score: 9.1) relates to a case of operating system (OS) command injection in the "recvCmd" binary used for communications between the host and guest OS.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The remaining 12 flaws are listed below -

* **CVE-2024-41589** (CVSS score: 7.5) - Use of the same admin credentials across the entire system, resulting in full system compromise
* **CVE-2024-41591** (CVSS score: 7.5) - A reflected cross-site scripting (XSS) vulnerability in the Web UI
* **CVE-2024-41587** (CVSS score: 4.9) - A stored XSS vulnerability in the Web UI when configuring a custom greeting message after logging in
* **CVE-2024-41583** (CVSS score: 4.9) - A stored XSS vulnerability in the Web UI when configuring a custom router name to be displayed to users
* **CVE-2024-41584** (CVSS score: 4.9) - A reflected XSS vulnerability in the Web UI's login page
* **CVE-2024-41588** (CVSS score: 7.2) - Buffer overflow vulnerabilities in the Web UI's CGI pages "/cgi-bin/v2x00.cgi" and "/cgi-bin/cgiwcg.cgi" leading to DoS or RCE
* **CVE-2024-41590** (CVSS score: 7.2) - Buffer overflow vulnerabilities in the Web UI's CGI pages leading to DoS or RCE
* **CVE-2024-41586** (CVSS score: 7.2) - A stack buffer overflow vulnerability in the Web UI's "/cgi-bin/ipfedr.cgi" page leading to DoS or RCE
* **CVE-2024-41596** (CVSS score: 7.2) - Multiple buffer overflow vulnerabilities in the Web UI leading to DoS or RCE
* **CVE-2024-41593** (CVSS score: 7.2) - A heap-based buffer overflow vulnerability in the Web UI's ft\_payloads\_dns() function leading to DoS
* **CVE-2024-41595** (CVSS score: 7.2) - An out-of-bounds write vulnerability in the Web UI leading to DoS or RCE
* **CVE-2024-41594** (CVSS score: 7.6) - An information disclosure vulnerability in the web server backend for the Web UI that could allow an threat actor to perform an adversary-in-the-middle (AitM) attack

Forescout's analysis [found](https://wigle.net/stats#ssidstats) that over 704,000 DrayTek routers have their Web UI exposed to the internet, making it an attack-rich surface for malicious actors. A majority of the exposed instances are located in the U.S., followed by Vietnam, the Netherlands, Taiwan, and Australia.

[![DrayTek Routers](data:image/png;base64... "DrayTek Routers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjalWBe9qXntWeDBs-WNkqA0CsLLaKu2fNVQ3Wf2XihwbuDdV_AZAvBJDjEP-JUbFvvjenkL1Fjo-D4eGp7Et1vGfQv4ITffihLWinoDseONpSGEzKvdKTMRIjmmN7VU9aGAnvAALnzNCd4kUl12RCsT0Uq1T_9kDnX6plOrdD1kkRKBGu0AKZHrEjKltrX/s790-rw-e365/device.png)

Following responsible disclosure, patches for all the identified flaws have been [released](https://www.draytek.com/support/resources/routers#version) by DrayTek, with the max-rated vulnerability also addressed in 11 end-of-life (EoL) models.

"Complete protection against the new vulnerabilities requires patching devices running the affected software," Forescout said. "If remote access is enabled on your router, disable it if not needed. Use an access control list (ACL) and two-factor authentication (2FA) if possible."

The development comes as cybersecurity agencies from Australia, Canada, Germany, Japan, the Netherlands, New Zealand, South Korea, the U.K., and the U.S. issued joint guidance for critical infrastructure organizations to help maintain a safe, secure operational technology (OT) environment.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The document, titled "Principles of operational technology cybersecurity," outlines six foundational rules -

* Safety is paramount
* Knowledge of the business is crucial
* OT data is extremely valuable and needs to be protected
* Segment and segregate OT from all other networks
* The supply chain must be secure
* People are essential for OT cyber security

"Quickly filtering decisions to identify those that impact the security of OT will enhance the making of robust, informed, and comprehensive decisions that promote safety, security and b...