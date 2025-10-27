---
title: AsyncRAT Campaign Uses Python Payloads and TryCloudflare Tunnels for Stealth Attacks
url: https://thehackernews.com/2025/02/asyncrat-campaign-uses-python-payloads.html
source: The Hacker News
date: 2025-02-06
fetch_date: 2025-10-06T20:40:01.372302
---

# AsyncRAT Campaign Uses Python Payloads and TryCloudflare Tunnels for Stealth Attacks

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

# [AsyncRAT Campaign Uses Python Payloads and TryCloudflare Tunnels for Stealth Attacks](https://thehackernews.com/2025/02/asyncrat-campaign-uses-python-payloads.html)

**Feb 05, 2025**Ravie LakshmananMalware / Network Security

[![TryCloudflare Tunnels](data:image/png;base64... "TryCloudflare Tunnels")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjssruf140lZU7nUexNUTbi3ZPB2S1wr3aYRTgIa77kjvkDL5JJjr8qZzuhO1tETDOXH5o2smCK4QHn2XSluNa3AJQHXUyqLtfuZTh4SQTPxBjbu985QDlCr65ytPgRhOAR7-ukrd0gO8Ou7Kcwzh3joqKiK8YFUcS07pYaEY-EPL-dXSmetQIXUDChqIHp/s790-rw-e365/malware.png)

A malware campaign has been observed delivering a remote access trojan (RAT) named AsyncRAT by making use of Python payloads and TryCloudflare tunnels.

"AsyncRAT is a remote access trojan (RAT) that exploits the async/await pattern for efficient, asynchronous communication," Forcepoint X-Labs researcher Jyotika Singh [said](https://www.forcepoint.com/blog/x-labs/asyncrat-reloaded-python-trycloudflare-malware) in an analysis.

"It allows attackers to control infected systems stealthily, exfiltrate data and execute commands while remaining hidden – making it a significant cyberthreat."

The starting point of the multi-stage attack chain is a phishing email that contains a Dropbox URL that, upon clicking, downloads a ZIP archive.

Present within the file is an internet shortcut (URL) file, which serves as a conduit for a Windows shortcut (LNK) file responsible for taking the infection further, while a seemingly benign decoy PDF document is displayed to the message recipient.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Specifically, the LNK file is retrieved by means of a TryCloudflare URL embedded within the URL file. TryCloudflare is a [legitimate service](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/trycloudflare/) offered by Cloudflare for exposing web servers to the internet without opening any ports by creating a dedicated channel (i.e., a subdomain on trycloudflare[.]com) that proxies traffic to the server.

The LNK file, for its part, triggers PowerShell to execute a JavaScript code hosted on the same location that, in turn, leads to a batch script (BAT) capable of downloading another ZIP archive. The newly downloaded ZIP file contains a Python payload designed to launch and execute several malware families, such as AsyncRAT, Venom RAT, and [XWorm](https://www.seqrite.com/blog/xworm-malware-analysis-new-infection-tactics/).

It's worth noting that a [slight](https://thehackernews.com/2024/08/cybercriminals-abusing-cloudflare.html) [variation](https://www.forcepoint.com/blog/x-labs/asyncrat-python-trycloudflare-malware) of the same infection sequence was discovered last year propagating AsyncRAT, GuLoader, PureLogs Stealer, Remcos RAT, Venom RAT, and XWorm. A similar attack leveraging [CVE-2024-38213](https://thehackernews.com/2024/08/microsoft-issues-patches-for-90-flaws.html), a now-patched Windows Mark-of-the-Web (MotW) bypass vulnerability, was also [documented](https://fieldeffect.com/blog/what-happens-when-rats-go-undetected) by Canadian cybersecurity company Field Effect in November 2024.

"This AsyncRAT campaign has again shown how hackers can use legitimate infrastructures like Dropbox URLs and TryCloudflare to their advantage," Singh noted. "Payloads are downloaded through Dropbox URLs and temporary TryCloudflare tunnel infrastructure, thereby tricking recipients into believing their legitimacy."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimpRrL-4nLzVS4EC2jiAlR-YlnArsObQMASBKqJbseQsb2AYBhWMmgRUx6LP2xIcRZe58dAVn6kN14xA5vfC9oJAzyrg28I1rCn4wqJkoAbK3SXVMS2-kmAqd8ZWExNyNzOVaQB5gTJazo-NvvF0mwggnLUnHzlN8cDMAL3XiN-ndwzLqZQMOQSHDDfYgW/s790-rw-e365/asynchrat.jpg)

The development comes amid a [surge in phishing campaigns](https://abnormalsecurity.com/blog/account-compromise-phishing-as-a-service) using phishing-as-a-service ([PhaaS](https://thehackernews.com/2025/01/new-sneaky-2fa-phishing-kit-targets.html)) toolkits to conduct account takeover attacks by directing users to bogus landing pages mimicking the login pages of trusted platforms like Microsoft, Google, Apple, and GitHub.

Social engineering attacks conducted via emails have also been [observed](https://abnormalsecurity.com/blog/segs-fail-attackers-exploit-vendors-credential-phishing) leveraging compromised vendor accounts to harvest users' Microsoft 365 login credentials, an indication that threat actors are taking advantage of the interconnected supply chain and the inherent trust to bypass email authentication mechanisms.

Some of other recently documented phishing campaigns in recent weeks are below -

* Attacks [targeting organizations across Latin America](https://cofense.com/blog/malware-alert-fake-judicial-review-emails-deliver-sapphirerat-targeting-latin-american-victims) that make use of official legal documents and receipts to distribute and execute SapphireRAT
* Attacks [exploiting legitimate domains](https://cofense.com/blog/threat-actors-exploit-government-website-vulnerabilities-for-phishing-campaigns), including those belonging to government websites (".gov"), to host Microsoft 365 credential harvesting pages
* Attacks [impersonating tax agencies and related financial organizations](https://www.proofpoint.com/us/blog/threat-insight/security-brief-threat-actors-take-taxes-account) to target users in Australia, Switzerland, the U.K., and the U.S. to capture user credentials, make fraudulent payments, and distribute malware like AsyncRAT, MetaStealer, Venom RAT, XWorm
* Attacks that [leverage](https://abnormalsecurity.com/resources/targeting-microsoft-adfs-phishing-bypass-mfa-for-account-takeover) spoofed Microsoft Active Directory Federation Services (ADFS) login pages to gather credentials and multi-factor authentication (MFA) codes for follow-on financially motivated email attacks
* Attacks that [employ](https://thehacker...