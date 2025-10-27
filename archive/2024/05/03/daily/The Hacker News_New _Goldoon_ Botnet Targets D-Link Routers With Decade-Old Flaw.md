---
title: New "Goldoon" Botnet Targets D-Link Routers With Decade-Old Flaw
url: https://thehackernews.com/2024/05/new-goldoon-botnet-targets-d-link.html
source: The Hacker News
date: 2024-05-03
fetch_date: 2025-10-06T17:17:55.908906
---

# New "Goldoon" Botnet Targets D-Link Routers With Decade-Old Flaw

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

# [New "Goldoon" Botnet Targets D-Link Routers With Decade-Old Flaw](https://thehackernews.com/2024/05/new-goldoon-botnet-targets-d-link.html)

**May 02, 2024**Ravie LakshmananBotnet / Vulnerability

[![Botnet](data:image/png;base64... "Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4v5FPWul2o3NA4tu-hE7TeA9riytUfYgvzYOOHYovfEf98OL0GhMOdfL9X8zp0AulqUZX8Hlm9yCmS_hj8E6ZAcoV5-reRixNq44xFiAFmVQrITXumlWmgEastltq14878stV86ttxbcVsPqh173g_wGzO5QU0XsiCpJIa8rC8x4hCE7hKv3q-SdzTFtW/s790-rw-e365/souter.png)

A never-before-seen botnet called **Goldoon** has been observed targeting D-Link routers with a nearly decade-old critical security flaw with the goal of using the compromised devices for further attacks.

The vulnerability in question is [CVE-2015-2051](https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10282) (CVSS score: 9.8), which affects D-Link DIR-645 routers and allows remote attackers to [execute arbitrary commands](https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10051) by means of specially crafted HTTP requests.

"If a targeted device is compromised, attackers can gain complete control, enabling them to extract system information, establish communication with a C2 server, and then use these devices to launch further attacks, such as distributed denial-of-service (DDoS)," Fortinet FortiGuard Labs researchers Cara Lin and Vincent Li [said](https://www.fortinet.com/blog/threat-research/new-goldoon-botnet-targeting-d-link-devices).

Telemetry data from the network security company points to a spike in the botnet activity around April 9, 2024.

It all starts with the exploitation of CVE-2015-2051 to retrieve a dropper script from a remote server, which is responsible for responsible for downloading the next-stage payload for different Linux system architectures, including aarch64, arm, i686, m68k, mips64, mipsel, powerpc, s390x, sparc64, x86-64, sh4, riscv64, DEC Alpha, and PA-RISC.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The payload is subsequently launched on the compromised device and acts as a downloader for the Goldoon malware from a remote endpoint, after which the dropper removes the executed file and then deletes itself in a bid to cover up the trail and fly under the radar.

Any attempt to access the endpoint directly via a web browser displays the error message: "Sorry, you are an FBI Agent & we can't help you :( Go away or I will kill you :)"

Goldoon, besides setting up persistence on the host using various autorun methods, establishes contact with a command-and-control (C2) server to await commands for follow-up actions.

This includes an "astounding 27 different methods" to pull off DDoS flood attacks using various protocols like DNS, HTTP, ICMP, TCP, and UDP.

"While CVE-2015-2051 is not a new vulnerability and presents a low attack complexity, it has a critical security impact that can lead to remote code execution," the researchers said.

The development comes as botnets continue to evolve and exploit as many devices as possible, even as cybercriminals and advanced persistent threat (APT) actors alike have demonstrated an interest in compromised routers for use as an anonymization layer.

"Cybercriminals rent out compromised routers to other criminals, and most likely also make them available to commercial residential proxy providers," cybersecurity company Trend Micro [said](https://www.trendmicro.com/en_us/research/24/e/router-roulette.html) in a report.

"Nation-state threat actors like Sandworm used their own dedicated proxy botnets, while APT group Pawn Storm had access to a criminal proxy botnet of Ubiquiti EdgeRouters."

[![Botnet](data:image/png;base64... "Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigwcIu5JsqwLO7wnfSc3FReNl2SnZucIWpM_Ttoa1zCxLUgz-hTImdEjF2WWM7Kc3WF7Kw1LK_F8HWy1XfRjnUzF8qLmsGxIe-gLldoqGQAGTHmxJJKXsQhC2XhYK34gpAGzW1DCDfn8j3LyUAejCWA6-dEMgN8OaeSAxpD8MMrXqlCwEeyHI57QjdysDa/s790-rw-e365/ttp.png)

In using the hacked routers as proxies, the objective is to hide traces of their presence and make detection of malicious activities more difficult by blending their activity in with benign normal traffic.

Earlier this February, the U.S. government took steps to dismantle parts of a botnet called [MooBot](https://thehackernews.com/2024/02/us-government-disrupts-russian-linked.html) that, among other internet-facing devices like Raspberry Pi and VPS servers, primarily leveraged Ubiquiti EdgeRouters.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Trend Micro said it observed the routers being used for different purposes, such as Secure Shell (SSH) brute forcing, pharmaceutical spam, employing server message block (SMB) reflectors in NTLMv2 hash relay attacks, proxying stolen credentials on phishing sites, multi-purpose proxying, cryptocurrency mining, and sending spear phishing emails.

Ubiquiti routers have also come under assault from another threat actor that infects these devices with a malware dubbed [Ngioweb](https://research.checkpoint.com/2018/ramnits-network-proxy-servers/), which are then used as exit nodes in a commercially available [residential proxy botnet](https://blog.netlab.360.com/linux-ngioweb-v2-going-after-iot-devices-en/).

The findings further underscore the use of various malware families to wrangle the routers into a network that threat actors could control, effectively turning them into [covert listening posts](https://thehackernews.com/2024/05/new-cuttlefish-malware-hijacks-router.html) capable of monitoring all network traffic.

"Internet routers remain a popular asset for threat actors to compromise since they often have reduced security monitoring, have less stringent password policies, are not updated frequently, and may use powerful operating systems that allows for installation of malware such as cryptocurrency miners, proxies, distributed denial of service (DDoS malw...