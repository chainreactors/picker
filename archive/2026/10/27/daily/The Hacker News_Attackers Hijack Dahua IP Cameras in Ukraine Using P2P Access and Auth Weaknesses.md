---
title: Attackers Hijack Dahua IP Cameras in Ukraine Using P2P Access and Auth Weaknesses
url: https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html
source: The Hacker News
date: 2026-10-27
fetch_date: 2026-10-28T07:49:46.606767
---

# Attackers Hijack Dahua IP Cameras in Ukraine Using P2P Access and Auth Weaknesses

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Attackers Hijack Dahua IP Cameras in Ukraine Using P2P Access and Auth Weaknesses](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html)

**Ravie Lakshmanan**Oct 27, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjISG9SXb2aeE6Zy-bIbnuaqwUNmGof7xU8RQl0vGZIcxcgNE3YXpuvG7rJKSTn_q9J8d_2DEv6rU2zxoX615DIYePz9rMA2TiLT6Fo1q2leGoyH85hJuIUta8j8FEN2mY5AGaO6zH5o6MkCHZ9Sv7OpjrZ6LE1yZygl9R4hUgt7xWJMMeGXRI4UJziuPCW/s1700-nu-rw-lo-l85-e365/hackers-camera.jpg)

The Computer Emergency Response Team of Ukraine (CERT-UA) has issued an alert warning of unauthorized remote access to video surveillance systems manufactured by Dahua.

"Cases of compromising IP cameras and DVRs with access to the video stream, changing the device configuration and creating third-party accounts have been recorded," the State Special Communications Service of Ukraine (SSSCIP) [said](https://cip.gov.ua/ua/news/khakeri-mozhut-otrimati-kontrol-nad-kamerami-ta-videoreyestratorami-cherez-khmarnii-dostup) in an alert issued last week.

The primary initial access vector used in the attacks is via [Easy4IP](https://dahuawiki.com/Mobile/Easy4IP_View_Device), a peer-to-peer (P2P) platform that allows users to remotely monitor homes or small businesses by connecting their Dahua IP cameras, NVRs, and DVRs via a smartphone app or web browser by scanning a QR code or entering the hardware Serial Number (SN).

The agency has warned that the [serial numbers have a predictable structure](https://labs.itresit.es/2025/10/29/dahua-beyond-cve-2025-31702-p2p-relay-exposure/) containing a 10-character model prefix that's identical for all units of the same device family and a five-character hexadecimal counter that's incremented almost sequentially (e.g., 7K01F36PCA003E8).

This, in turn, allows attackers to guess them at scale through a brute-force attack and identify if they are connected to the cloud without hitting rate limits or lockouts. As a result, all devices with active P2P functionality are at risk even if they cannot be accessed directly via the internet.

"The assumption that the serial number is unknown to anyone is not a reason to consider the device secure," CERT-UA said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

Authentication barriers are overcome by leveraging weak or known passwords, or by exploiting authentication bypass vulnerabilities in outdated firmware versions, such as CVE-2021-33044 and CVE-2021-33045. CERT-UA has shared the following indicators of compromise associated with the activity -

* Presence of unknown accounts
* Unauthorized configuration changes
* Audit logs containing authentication events using the manufacturer's native protocol (DVRIP) and from a local address (127.0.0.1), a sign of P2P access.

To counter the threat, it's advised to disable the P2P feature if not required, avoid exposing them directly to the internet, and keep the software up-to-date.

The agency has not disclosed who was targeted, when these infections occurred, how many devices had been infected, or who was responsible for the activity. However, the findings share similarities with two clusters of activity that Hunt.io disclosed as targeting IP cameras in Ukraine and Russia.

One of the campaigns, [attributed](https://hunt.io/blog/russian-speaking-operator-ukrainian-camera-toolkit) to a Russian-speaking operator, singled out internet-exposed cameras in Ukraine using known Dahua and Hikvision vulnerabilities, ultimately compromising 58 devices. The activity involved the exploitation of the following flaws by integrating [Ingram](https://github.com/jorhelp/Ingram), a publicly available webcam vulnerability scanner -

* [CVE-2017-7921](https://nvd.nist.gov/vuln/detail/cve-2017-7921) - An authentication bypass vulnerability in Hikvision
* [CVE-2020-25078](https://nvd.nist.gov/vuln/detail/CVE-2020-25078) - A credential disclosure vulnerability in D-Link
* [CVE-2020-25169](https://nvd.nist.gov/vuln/detail/CVE-2020-25169) - An unauthenticated information disclosure vulnerability in Reolink
* [CVE-2021-33044](https://nvd.nist.gov/vuln/detail/cve-2021-33044) / [CVE-2021-33045](https://nvd.nist.gov/vuln/detail/cve-2021-33045) - Authentication bypass vulnerabilities in Dahua that allow passwordless login
* [CVE-2021-36260](https://nvd.nist.gov/vuln/detail/CVE-2021-36260) - An unauthenticated remote code execution vulnerability in Hikvision.

In parallel, the threat actor is also said to have undertaken scanning and exploitation of TP-Link and MikroTik routers and cameras using vulnerabilities like CVE-2024-53375 and CVE-2024-57049 across 15 European countries, including Ukraine, Poland, Romania, Moldova, Hungary, Czechia, Slovakia, Bulgaria, Germany, France, the Netherlands, Italy, Spain, the U.K., and Austria.

The second campaign, codenamed Operation CameraSwarm and attributed to a lone threat actor, is believed to have compromised over 14,530 Dahua IP cameras between June 17 and July 22, 2026, using a combination of credential brute-force attacks and the exploitation of the CVE-2021-33044-CVE-2021-33045 chain.

The attack scans for TCP port 37777, which is the default proprietary management and video streaming port used by Dahua, followed by collecting serial numbers, breaking into those devices by employing the aforementioned two exploitation methods, and then deploying a persistent backdoor account ("[p2pwn](https://github.com/thebadinteger/p2pwn) / p2password") on nearly 2,000 cameras in a manner that can survive password change and a factory reset.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

"1,923 cameras carry a persistent backdoor account (p2pwn / p2password), installed over RPC after either bypass," Hunt.io [noted](https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised) at the time. "It is stored independently of the admin password...