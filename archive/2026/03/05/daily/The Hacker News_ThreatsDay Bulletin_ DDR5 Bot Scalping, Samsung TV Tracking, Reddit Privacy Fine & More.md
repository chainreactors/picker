---
title: ThreatsDay Bulletin: DDR5 Bot Scalping, Samsung TV Tracking, Reddit Privacy Fine & More
url: https://thehackernews.com/2026/03/threatsday-bulletin-redis-rce-ddr5-bot.html
source: The Hacker News
date: 2026-03-05
fetch_date: 2026-03-06T04:04:48.046130
---

# ThreatsDay Bulletin: DDR5 Bot Scalping, Samsung TV Tracking, Reddit Privacy Fine & More

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [ThreatsDay Bulletin: DDR5 Bot Scalping, Samsung TV Tracking, Reddit Privacy Fine & More](https://thehackernews.com/2026/03/threatsday-bulletin-redis-rce-ddr5-bot.html)

**Ravie Lakshmanan**Mar 05, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmX71oTh0PhBoeXrV6BUD7_jQe9VWPqHc60ijUxf4iv8wPE8UeWY8dlDrfbx3-Ut5aNoNQZJ8DH_ADNQGgFL4NbMMcw-IayIe9HXKG3l5EN3-og9LuNqBP452mXpm1HTn3ooWlJ-q4QRqvPJC4gmR0lstJ8KWdQYa2knQ5J69nneIwIRTKKG43fXtcWRXm/s1700-e365/threatsday.jpg)

Some weeks in cybersecurity feel routine. This one doesn’t.

Several new developments surfaced over the past few days, showing how quickly the threat landscape keeps shifting. Researchers uncovered fresh activity, security teams shared new findings, and a few unexpected moves from major tech companies also drew attention.

Together, these updates offer a useful snapshot of what is happening behind the scenes in the cyber world right now. From new tactics and campaigns to security and policy changes that could affect millions of users, there is a lot unfolding at once.

Below is a quick roundup of the most notable stories making headlines this week.

1. Phishing Campaign Deploys Multiple Malware Strains

   [Ukraine Targeted by SHADOWSNIFF, SALATSTEALER, DEAFTICKK Malware](https://cert.gov.ua/article/6287707)

   The Computer Emergency Response Team of Ukraine (CERT-UA) has [warned](https://cert.gov.ua/article/6287707) of a hacking campaign targeting Ukrainian government institutions using phishing emails containing a ZIP archive (or a link to a website vulnerable to cross-site scripting attacks) to distribute SHADOWSNIFF and SALATSTEALER information-stealing malware and a Go backdoor called DEAFTICKK. The agency attributed the activity to a threat actor tracked as UAC-0252. The development comes as a suspected Russian espionage campaign is targeting Ukraine with two previously undocumented malware strains, [BadPaw and MeowMeow](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html), according to ClearSky. While the campaign is likely said to be the work of APT28, the cybersecurity company did not identify the targets of the campaign or say whether the attacks were successful.
2. Fake RMM Service Spreads RAT via Phishing

   [Threat Actor Masquerades as RMM Vendor to Distribute RAT](https://www.proofpoint.com/us/blog/threat-insight/dont-trustconnect-its-a-rat)

   A new malware-as-a-service (MaaS) dubbed TrustConnect ("trustconnectsoftware[.]com") masqueraded as a legitimate remote monitoring and management (RMM) tool for $300 per month. It's assessed that the threat actor behind TrustConnect was also a prominent user of [RedLine Stealer](https://thehackernews.com/2024/04/new-redline-stealer-variant-disguised.html). According to email security firm [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/dont-trustconnect-its-a-rat), multiple threat actors have been observed distributing the malware via phishing emails as of January 27, 2026. The emails claim to be event invites or bid proposals, tricking recipients into clicking on links that lead to the download of bogus executables that install TrustConnect RAT. The RAT backdoors users' machines and gives attackers full mouse and keyboard control, allowing them to record and stream the victim's screen. Some campaigns have also been observed delivering legitimate remote access software like ScreenConnect and LogMeIn Resolve alongside TrustConnect between January 31 and February 3, 2026. Customers who purchase the toolkit are granted access to a dashboard to remotely commandeer infected devices and generate branded installers containing the malware. After Proofpoint took steps to disrupt some of the malware's infrastructure on February 17, 2026, the threat actor resurfaced with a rebranded version of the malware platform called DocConnect. "Disruptions to MaaS operations like RedLine, Lumma Stealer, and Rhadamanthys have created new opportunities for malware creators to fill gaps in the cybercrime market," Proofpoint said. "Although TrustConnect only masqueraded as a legitimate RMM, the lures, attack chains, and follow-on payloads (which include RMMs) show overlap with techniques and delivery methods that are frequently observed in RMM campaigns and used by multiple threat actors." The development comes amid skyrocketing abuse of legitimate RMM software in cyber attacks.
3. Chrome Moves to Two-Week Release Cycle

   [Google Revises Chrome Release Cycle](https://developer.chrome.com/blog/chrome-two-week-release)

   Google has announced that new Chrome iterations will be released every two weeks, moving away from the current four-week release cycle. Since 2021, Google has been shipping major Chrome versions every four weeks, and since 2023, it has been delivering security updates every week for a reduced patch gap and improved quality. "The web platform is constantly advancing, and our goal is to ensure developers and users have immediate access to the latest performance improvements, fixes, and new capabilities," Google [said](https://developer.chrome.com/blog/chrome-two-week-release). The new release cycle will also apply to beta releases, starting with Chrome 153, which will arrive on September 8, 2026.
4. TPMS Signals Allow Covert Vehicle Tracking

   [Vehicle Tire Pressure Sensors Enable Silent Tracking](https://dspace.networks.imdea.org/handle/20.500.12761/2011)

   Researchers at IMDEA Networks Institute have found that Tire Pressure Monitoring System (TPMS) sensors inside each car wheel broadcast unencrypted wireless signals containing persistent identifiers. While the feature is designed for vehicle safety, each sensor transmits a unique ID that does not change, allowing the same car to be recognized again and tracked over time. This, in turn, opens the door to a low-cost monitoring network that uses software-defined radio receivers near roads (at a distance ...