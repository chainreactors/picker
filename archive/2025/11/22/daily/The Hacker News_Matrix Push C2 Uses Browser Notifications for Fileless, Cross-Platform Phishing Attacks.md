---
title: Matrix Push C2 Uses Browser Notifications for Fileless, Cross-Platform Phishing Attacks
url: https://thehackernews.com/2025/11/matrix-push-c2-uses-browser.html
source: The Hacker News
date: 2025-11-22
fetch_date: 2025-11-23T03:27:35.055104
---

# Matrix Push C2 Uses Browser Notifications for Fileless, Cross-Platform Phishing Attacks

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

# [Matrix Push C2 Uses Browser Notifications for Fileless, Cross-Platform Phishing Attacks](https://thehackernews.com/2025/11/matrix-push-c2-uses-browser.html)

**Nov 22, 2025**Ravie LakshmananBrowser Security / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8zV9hPvOUBQV7bQvL21L0QPcaCbKUW3y1D4puHbsR7Ig3KTf_8W7V52Gs4drcN6P7Ss49eYUSYcC13N10xBKUzA8Pr1cmBpzbUbO5t31wLs9b-Vk1XAxdO5BWz9RxGUsFrSlTPKMKefHVtCI6zkkv-y85B7bPdPQBQkxq78PcrUQQjrfXNLRIsnBwFUeD/s790-rw-e365/mat-c2.jpg)

Bad actors are leveraging browser notifications as a vector for phishing attacks to distribute malicious links by means of a new command-and-control (C2) platform called Matrix Push C2.

"This browser-native, fileless framework leverages push notifications, fake alerts, and link redirects to target victims across operating systems," Blackfog researcher Brenda Robb [said](https://www.blackfog.com/new-matrix-push-c2-deliver-malware/) in a Thursday report.

In these attacks, prospective targets are tricked into allowing browser notifications through social engineering on malicious or legitimate-but-compromised websites.

Once a user agrees to receive notifications from the site, the attackers take advantage of the [web push notification mechanism](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Best_Practices) built into the web browser to send alerts that look like they have been sent by the operating system or the browser itself, leveraging trusted branding, familiar logos, and convincing language to maintain the ruse.

These include alerts about, say, suspicious logins or browser updates, along with a handy "Verify" or "Update" button that, when clicked, takes the victim to a bogus site.

What makes this a clever technique is that the entire process takes place through the browser without the need for first infecting the victim's system through some other means. In a way, the attack is like [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html) in that users are lured into following certain instructions to compromise their own systems, thereby effectively bypassing traditional security controls.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

That's not all. Since the attack plays out via the web browser, it's also a cross-platform threat. This essentially turns any browser application on any platform that subscribes to the malicious notifications to be enlisted to the pool of clients, giving adversaries a persistent communication channel.

Matrix Push C2 is offered as a malware-as-a-service (MaaS) kit to other threat actors. It's sold directly through crimeware channels, typically via Telegram and cybercrime forums, under a tiered subscription model: about $150 for one month, $405 for three months, $765 for six months, and $1,500 for a full year.

"Payments are accepted in cryptocurrency, and buyers communicate directly with the operator for access," Dr. Darren Williams, founder and CEO of BlackFog, told The Hacker News. "Matrix Push was first observed at the beginning of October and has been active since then. There's no evidence of older versions, earlier branding, or long-standing infrastructure. Everything indicates this is a newly launched kit."

The tool is accessible as a web-based dashboard, allowing users to send notifications, track each victim in real-time, determine which notifications the victims interacted with, create shortened links using a built-in URL shortening service, and even record installed browser extensions, including cryptocurrency wallets.

"The core of the attack is social engineering, and Matrix Push C2 comes loaded with configurable templates to maximize the credibility of its fake messages," Robb explained. "Attackers can easily theme their phishing notifications and landing pages to impersonate well-known companies and services."

Some of the supported notification verification templates are associated with well-known brands like MetaMask, Netflix, Cloudflare, PayPal, and TikTok. The platform also includes an "Analytics & Reports" section that allows its customers to measure the effectiveness of their campaigns and refine them as required.

"Matrix Push C2 shows us a shift in how attackers gain initial access and attempt to exploit users," BlackFog said. "Once a user's endpoint (computer or mobile device) is under this kind of influence, the attacker can gradually escalate the attack."

"They might deliver additional phishing messages to steal credentials, trick the user into installing a more persistent malware, or even leverage browser exploits to get deeper control of the system. Ultimately, the end goal is often to steal data or monetize the access, for example, by draining cryptocurrency wallets or exfiltrating personal information."

### Attacks Misusing Velociraptor on the Rise

The development comes as Huntress said it [observed](https://www.huntress.com/blog/velociraptor-misuse-part-one-wsus-up) a "significant uptick" in attacks weaponizing the legitimate [Velociraptor](https://thehackernews.com/2025/10/hackers-turn-velociraptor-dfir-tool.html) digital forensics and incident response (DFIR) tool over the past three months.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

On November 12, 2025, the cybersecurity vendor said threat actors deployed Velociraptor after obtaining initial access through exploitation of a flaw in Windows Server Update Services ([CVE-2025-59287](https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html), CVSS score: 9.8), which was patched by Microsoft late last month.

Subsequently, the attackers are said to have launched discovery queries with the goal of conducting reconnaissance and gathering details about users, running services, and configurations. The attack was contained before it could progress further, Huntress added.

The discovery shows that threat actors are not just [using](https://thehackern...