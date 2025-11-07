---
title: Hackers Weaponize Windows Hyper-V to Hide Linux VM and Evade EDR Detection
url: https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html
source: The Hacker News
date: 2025-11-06
fetch_date: 2025-11-07T03:11:55.508278
---

# Hackers Weaponize Windows Hyper-V to Hide Linux VM and Evade EDR Detection

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Hackers Weaponize Windows Hyper-V to Hide Linux VM and Evade EDR Detection](https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html)

**Nov 06, 2025**Ravie LakshmananMalware / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGBz7Fh35GCGnvq_75iKz59PN9dxPcO-sdZAGTMvQPVJ9tzq2wM8w5LzPxk1ZR8TITolw6e66VvmGhhE4Mu66MyW71fGIK1jVGkZU0TTOP01chaZWdcGzVYPwPMDz5spgt8ZajT7HOTW8cRBpFmudNWD6XIlQiZto9DdeuUPYUvGh4kOISUNI0TDt7DLq7/s790-rw-e365/iwndows.jpg)

The threat actor known as **Curly COMrades** has been observed exploiting virtualization technologies as a way to bypass security solutions and execute custom malware.

According to a [new report](https://businessinsights.bitdefender.com/curly-comrades-evasion-persistence-hidden-hyper-v-virtual-machines) from Bitdefender, the adversary is said to have enabled the Hyper-V role on selected victim systems to deploy a minimalistic, Alpine Linux-based virtual machine.

"This hidden environment, with its lightweight footprint (only 120MB disk space and 256MB memory), hosted their custom reverse shell, CurlyShell, and a reverse proxy, CurlCat," security researcher Victor Vrabie, along with Adrian Schipor and Martin Zugec, said in a technical report.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Curly COMrades was [first documented](https://thehackernews.com/2025/08/new-curly-comrades-apt-using-ngen-com.html) by the Romanian cybersecurity vendor in August 2025 in connection with a series of attacks targeting Georgia and Moldova. The activity cluster is assessed to be active since late 2023, operating with interests that are aligned with Russia.

These attacks were found to deploy tools like CurlCat for bidirectional data transfer, RuRat for persistent remote access, Mimikatz for credential harvesting, and a modular .NET implant dubbed MucorAgent, with early iterations dating back all the way to November 2023.

In a follow-up analysis conducted in collaboration with Georgia CERT, additional tooling associated with the threat actor has been identified, alongside attempts to establish long-term access by weaponizing Hyper-V on compromised Windows 10 hosts to set up a hidden remote operating environment.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVWG3I-dFGA_IFii1cO7gPqPhd3-P32aFYCDK-B1tnobtmRHT17y0WfXA2h_fN1MFmee9kXckr18e3Y86PG1jIDQBjwgOCE9aKTg28x_BYCear1bkbKOyYM-1mX9k_xvI-lZzLBeDrvnrULgTBmZEz9UgCz4kAuLat7JFSkUsV92R5j6UqrIXfn1z1FG32/s790-rw-e365/apline.jpg)

"By isolating the malware and its execution environment within a VM, the attackers effectively bypassed many traditional host-based EDR detections," the researchers said. "The threat actor demonstrated a clear determination to maintain a reverse proxy capability, repeatedly introducing new tooling into the environment."

Besides using [Resocks](https://resocks.net/), [Rsockstun](https://github.com/llkat/rsockstun), [Ligolo-ng](https://www.kali.org/tools/ligolo-ng/), [CCProxy](https://ccproxy), [Stunnel](https://www.stunnel.org), and SSH-based methods for proxy and tunneling, Curly COMrades has employed various other tools, including a PowerShell script designed for remote command execution and CurlyShell, a previously undocumented ELF binary deployed in the virtual machine that provides a persistent reverse shell.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Written in C++, the malware is executed as a headless background daemon to connect to a command-and-control (C2) server and launch a reverse shell, allowing the threat actors to run encrypted commands. Communication is achieved via HTTP GET requests to poll the server for new commands and using HTTP POST requests to transmit the results of the command execution back to the server.

"Two custom malware families – CurlyShell and CurlCat – were at the center of this activity, sharing a largely identical code base but diverging in how they handled received data: CurlyShell executed commands directly, while CurlCat funneled traffic through SSH," Bitdefender said. "These tools were deployed and operated to ensure flexible control and adaptability."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Bitdefender](https://thehackernews.com/search/label/Bitdefender)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Russia](https://thehackernews.com/search/label/Russia)[virtualization](https://thehackernews.com/search/label/virtualization)[Windows 10](https://thehackernews.com/search/label/Windows%2010)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Br...