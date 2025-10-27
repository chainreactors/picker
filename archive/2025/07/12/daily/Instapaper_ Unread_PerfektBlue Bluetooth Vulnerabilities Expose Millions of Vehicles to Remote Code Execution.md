---
title: PerfektBlue Bluetooth Vulnerabilities Expose Millions of Vehicles to Remote Code Execution
url: https://thehackernews.com/2025/07/perfektblue-bluetooth-vulnerabilities.html
source: Instapaper: Unread
date: 2025-07-12
fetch_date: 2025-10-07T00:02:12.007205
---

# PerfektBlue Bluetooth Vulnerabilities Expose Millions of Vehicles to Remote Code Execution

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

# [PerfektBlue Bluetooth Vulnerabilities Expose Millions of Vehicles to Remote Code Execution](https://thehackernews.com/2025/07/perfektblue-bluetooth-vulnerabilities.html)

**Jul 11, 2025**Ravie LakshmananVulnerability / Vehicle Security

[![PerfektBlue Bluetooth Vulnerabilities](data:image/png;base64... "PerfektBlue Bluetooth Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgG8ORDJjuYTEkPibMASamzKQyPySh0uci4rOAMuh1bsYWy5mc0oUvDgs0Q0vQn7CcWgTwYiSIhqOQM5PN9jcTB9bMPFR21VaPwYbgbeWaaT7XXsHKH4Fn8uNxnsTvMByBtXpC5T9q9ThXthOOVqVdd4BMA4Oji3klcAwojc-YkhNI9IF2fgJ14SAFZArd1/s790-rw-e365/car-hacking.jpg)

Cybersecurity researchers have discovered a set of four security flaws in OpenSynergy's [BlueSDK](https://www.opensynergy.com/blue-sdk/) Bluetooth stack that, if successfully exploited, could allow remote code execution on millions of transport vehicles from different vendors.

The vulnerabilities, dubbed **PerfektBlue**, can be fashioned together as an exploit chain to run arbitrary code on cars from at least three major automakers, Mercedes-Benz, Volkswagen, and Skoda, according to PCA Cyber Security (formerly PCAutomotive). Outside of these three, a fourth unnamed original equipment manufacturer (OEM) has been confirmed to be affected as well.

"PerfektBlue exploitation attack is a set of critical memory corruption and logical vulnerabilities found in OpenSynergy BlueSDK Bluetooth stack that can be chained together to obtain Remote Code Execution (RCE)," the cybersecurity company [said](https://perfektblue.pcacybersecurity.com).

While infotainment systems are often seen as isolated from critical vehicle controls, in practice, this separation depends heavily on how each automaker designs internal network segmentation. In some cases, weak isolation allows attackers to use IVI access as a springboard into more sensitive zones—especially if the system lacks gateway-level enforcement or secure communication protocols.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The only requirement to pull off the attack is that the bad actor needs to be within range and be able to pair their setup with the target vehicle's infotainment system over Bluetooth. It essentially amounts to a one-click attack to trigger over-the-air exploitation.

"However, this limitation is implementation-specific due to the framework nature of BlueSDK," PCA Cyber Security added. "Thus, the pairing process might look different between various devices: limited/unlimited number of pairing requests, presence/absence of user interaction, or pairing might be disabled completely."

The list of [identified vulnerabilities](https://pcacybersecurity.com/resources/advisory/perfekt-blue) is as follows -

* **CVE-2024-45434** (CVSS score: 8.0) - Use-After-Free in AVRCP service
* **CVE-2024-45431** (CVSS score: 3.5) - Improper validation of an L2CAP channel's remote CID
* **CVE-2024-45433** (CVSS score: 5.7) - Incorrect function termination in RFCOMM
* **CVE-2024-45432** (CVSS score: 5.7) - Function call with incorrect parameter in RFCOMM

Successfully obtaining code execution on the In-Vehicle Infotainment (IVI) system enables an attacker to track GPS coordinates, record audio, access contact lists, and even perform lateral movement to other systems and potentially take control of critical software functions of the car, such as the engine.

Following responsible disclosure in May 2024, patches were [rolled out](https://www.opensynergy.com/perfektblue/) in September 2024.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh21BUApddoyZw-aFikhT4cIGBZqZ4pdZebdx3QY3TnAj3-SvYr-vjer0zeiHHZfAEridFiRO0Rp2rpoToL8QnpbAvqyM3_U78CGfOTBUYpvdPoxNQ5f8UUTTKV1deecdRj5El1B6m_ECQhsjjnXNM-3lHu8eR8qBfS33C5FpdmCxFdjjUWv93LsDbMuG3T/s790-rw-e365/ID4.jpg)

"PerfektBlue allows an attacker to achieve remote code execution on a vulnerable device," PCA Cyber Security said. "Consider it as an entrypoint to the targeted system which is critical. Speaking about vehicles, it's an IVI system. Further lateral movement within a vehicle depends on its architecture and might involve additional vulnerabilities."

Earlier this April, the company presented a series of vulnerabilities that could be exploited to remotely break into a Nissan Leaf electric vehicle and take control of critical functions. The findings were [presented](https://www.blackhat.com/asia-25/briefings/schedule/index.html#remote-exploitation-of-nissan-leaf-controlling-critical-body-elements-from-the-internet-44048) at the Black Hat Asia conference held in Singapore.

"Our approach began by exploiting weaknesses in Bluetooth to infiltrate the internal network, followed by bypassing the secure boot process to escalate access," it said.

"Establishing a command-and-control (C2) channel over DNS allowed us to maintain a covert, persistent link with the vehicle, enabling full remote control. By compromising an independent communication CPU, we could interface directly with the [CAN bus](https://docs.arduino.cc/learn/communication/can/), which governs critical body elements, including mirrors, wipers, door locks, and even the steering."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

CAN, short for Controller Area Network, is a communication protocol mainly used in vehicles and industrial systems to facilitate communication between multiple electronic control units (ECUs). Should an attacker with physical access to the car be able to tap into it, the scenario opens the door for injection attacks and impersonation of trusted devices.

"One notorious example involves a small electronic device hidden inside an innocuous object (like a portable speaker)," the Hungarian company [said](https://pcacybersecurity.com/blog/real-world-car-theft-attack-surface-analysis). "Thieves covertly plug this device into an exposed CAN wiring junction on the car."

"Once connected to the car's CAN bus, the rogue device mimi...