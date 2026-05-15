---
title: ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories
url: https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html
source: The Hacker News
date: 2026-05-14
fetch_date: 2026-05-15T05:53:27.778733
---

# ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories](https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html)

**Ravie Lakshmanan**May 14, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjImYNT-qC7frGzEXeok3KDX_JNMKote6V1FVXIpkAoSEER2z1YyT8dpFq5RtRhBQ0cweEPbBIuioDWFf5rw_Mf-0V6rXR2ZrMh2ISDa7X7NlV9zIGsoLSAnyd_86eVkrR4wU24yxbuCYaAmyGFwlF77YCjvgU3n43P-yFT-pzjsmQ35Oaut1klg62bs_-i/s1700-e365/threatsday-2.jpg)

Everything is still on fire.

This week feels dumb in the worst way — bad links, weak checks, fake help desks, shady forum posts, and people turning supply chain attacks into some cursed little game for clout and cash. Half of it feels new. Half of it feels like crap we should have fixed years ago.

The mess keeps getting louder: users get tricked, boxes get popped, tools meant for normal work get used for bad stuff, and nobody seems shocked anymore. Great. Love that for us.

Anyway. Let’s get into it.

1. Exploited PAN-OS RCE

   [Palo Alto Networks Releases Fixes for Exploited Flaw](https://thehackernews.com/2026/05/pan-os-rce-exploit-under-active-use.html)

   Palo Alto Networks has [released](https://thehackernews.com/2026/05/pan-os-rce-exploit-under-active-use.html) the first round of fixes to address [CVE-2026-0300](https://thehackernews.com/2026/05/pan-os-rce-exploit-under-active-use.html), a critical buffer overflow vulnerability in the User-ID Authentication Portal service of PAN-OS software that could allow an unauthenticated attacker to execute arbitrary code with root privileges by sending specially crafted packets. The company said it has observed the flaw being exploited in limited attacks since at least last month, with unknown threat actors leveraging it to drop payloads like EarthWorm and ReverseSocks5.
2. Private AI chats

   [Meta Announces Incognito Chat](https://about.fb.com/news/2026/05/incognito-chat-whatsapp-meta-ai/)

   Meta has [announced](https://about.fb.com/news/2026/05/incognito-chat-whatsapp-meta-ai/) Incognito Chat with Meta AI in its namesake app and WhatsApp. Incognito Chat is "a completely private way to interact with AI, similar to how end-to-end encryption means no one can read your conversations, even Meta or WhatsApp," CEO Mark Zuckerberg said. "Incognito Chat handles all AI inference in a Trusted Execution Environment that ensures your messages are not accessible to us. The conversations on your phone also disappear when you exit the session." The feature is powered by [Private Processing](https://thehackernews.com/2025/04/whatsapp-launches-private-processing-to.html), which already underlies its message summarization and composition tools.
3. Zero-auth data leak

   [Defense Company Exposes Sensitive Data](https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup)

   A defense technology company with Department of Defense contracts exposed user records and military training materials through API endpoints that lacked meaningful authorization checks. The issue affected Schemata, an AI-powered virtual training platform used in military and defense settings. According to [Strix](https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup), an ordinary low-privilege account was able to access data across multiple tenants, including user listings, organization records, course information, training metadata, and direct links to documents hosted on Schemata’s Amazon Web Services instances. In a statement posted on the company’s website, Schemata [said](https://schemata.com/blog/security-disclosure-notice-and-response) it did not have "evidence that any third party exploited the vulnerability to access customer data."
4. Router update reprieve

   [FCC Softens Foreign Router Ban](https://www.fcc.gov/document/oet-announces-extension-and-expansion-waivers)

   The U.S. Federal Communications Commission (FCC) has [extended](https://thehackernews.com/2026/03/fcc-bans-new-foreign-made-routers-over.html) the deadline for owners of banned internet routers to provide security updates to U.S.-based users by two years. In March 2026, the FCC banned the import and sale of all "consumer-grade" internet routers produced in a foreign country, citing unacceptable national security risks. In a new public notice published last week, the Commission's Office of Engineering and Technology (OET) said it is extending this deadline until "at least" January 1, 2029. That said, the extension only applies to software and firmware updates so as to ensure the continued safety of already deployed routers in the U.S. and mitigate potential harm. "These include all software and firmware updates to ensure the continued functionality of the devices, such as those that patch vulnerabilities and facilitate compatibility with different operating systems," per the [FCC](https://www.fcc.gov/document/oet-announces-extension-and-expansion-waivers).
5. APT phishing campaign

   [Operation GriefLure Targets Vietnam and the Philippines](https://www.seqrite.com/blog/operation-grieflure-dissecting-an-apt-campaign-targeting-vietnams-military-telecom-philippine-healthcare/)

   A new state-sponsored threat cluster dubbed Operation GriefLure has been [observed](https://www.seqrite.com/blog/operation-grieflure-dissecting-an-apt-campaign-targeting-vietnams-military-telecom-philippine-healthcare/) targeting Vietnam's telecom and the Philippines' healthcare sectors with a RAR archive distributed via spear-phishing emails to deploy a remote access trojan on compromised hosts, while leveraging credible decoy documents to give them a veneer of legitimacy and trust. The malware is capable of process enumeration, screenshot capture, file and directory listing, credential harvesting, and file execution capabilities.
6. JPEG PowerShell lure

   [Operation SilentCanvas Drops ScreenConnect for Remote Access](https://www.cyfirma.com/research/op...