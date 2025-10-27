---
title: RaccoonO365 Phishing Network Dismantled as Microsoft, Cloudflare Take Down 338 Domains
url: https://thehackernews.com/2025/09/raccoono365-phishing-network-shut-down.html
source: The Hacker News
date: 2025-09-18
fetch_date: 2025-10-02T20:20:07.022125
---

# RaccoonO365 Phishing Network Dismantled as Microsoft, Cloudflare Take Down 338 Domains

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

# [RaccoonO365 Phishing Network Dismantled as Microsoft, Cloudflare Take Down 338 Domains](https://thehackernews.com/2025/09/raccoono365-phishing-network-shut-down.html)

**Sep 17, 2025**Ravie LakshmananCybercrime / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPJ89hVCM5hxCqwxfOA086CpjwRDKWFcmTsqG8RQOa7xzhyphenhyphenWLCMBkeGChxaopcCCjqoXyGFe2HLBEgYXbl3_vWD7Hb2h3oXB2NmCQNCRvJDF_ZTolNAT-9SlL-sQZT81iBiwiqQfqAh7RLsuAimGF7ebfm5m2_GfYvIX1siyzTDRcKM3PB9AyhExRQYMiI/s2600/ms.jpg)

Microsoft's Digital Crimes Unit said it teamed up with Cloudflare to coordinate the seizure of 338 domains used by **RaccoonO365**, a financially motivated threat group that was behind a phishing-as-a-service (Phaas) toolkit used to steal more than 5,000 Microsoft 365 credentials from 94 countries since July 2024.

"Using a court order granted by the Southern District of New York, the DCU seized 338 websites associated with the popular service, disrupting the operation's technical infrastructure and cutting off criminals' access to victims," Steven Masada, assistant general counsel at DCU, [said](https://blogs.microsoft.com/on-the-issues/2025/09/16/microsoft-seizes-338-websites-to-disrupt-rapidly-growing-raccoono365-phishing-service/).

"This case shows that cybercriminals don't need to be sophisticated to cause widespread harm – simple tools like RaccoonO365 make cybercrime accessible to virtually anyone, putting millions of users at risk."

The initial phase of the Cloudflare takedown [commenced](https://www.cloudflare.com/en-in/threat-intelligence/research/report/cloudflare-participates-in-global-operation-to-disrupt-raccoono365/) on September 2, 2025, with additional actions occurring on September 3 and September 4. This included banning all identified domains, placing interstitial "phish warning" pages in front of them, terminating the associated Workers scripts, and suspending the user accounts. The efforts were completed on September 8.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Tracked by the Windows maker under the name Storm-2246, RaccoonO365 is [marketed](https://www.morado.io/blog-posts/understanding-raccoono365-phishing-as-a-service) to other cybercriminals under a subscription model, allowing them to mount [phishing and credential harvesting attacks](https://levelblue.com/blogs/security-essentials/explore-compelling-narratives-from-the-soc) at scale with little to no technical expertise. A 30-day plan costs $355, and a 90-day plan is priced at $999.

The operators also claim that the tool is hosted on bulletproof virtual private servers with no hidden backdoors (unlike, say, [BulletProofLink](https://thehackernews.com/2023/11/major-phishing-as-service-syndicate.html)), and that it's "built for serious players only – no low-budget freeloaders."

According to [Morado](https://www.morado.io/blog-posts/raccoono365-an-active-campaign-and-new-features), campaigns using RaccoonO365 have been active since September 2024. These attacks typically mimic trusted brands like Microsoft, DocuSign, SharePoint, Adobe, and Maersk in fraudulent emails, tricking them into clicking on lookalike pages that are designed to capture victims' Microsoft 365 usernames and passwords. The phishing emails are often a precursor to malware and ransomware.

The most troubling aspect, from a defender's standpoint, is the use of legitimate tools like Cloudflare Turnstile as a CAPTCHA, as well as implementing bot and automation detection using a Cloudflare Workers script to protect their phishing pages, thereby making sure that only intended targets of the attack can access and interact with them.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGQKffiNKDsUTpKaWnnF2uqFZGraS2HTq6-uU8gu2BkQwWFQ8mol0Q_-Iy3SPvAlcKBAvka_eNRXvncDWPOBq3adoSqko8Gv32j5Cd8tDOCOjNTxMhhHAC8d5UboOYrWhYYALk1EEUbrNkw4LJ7FB9qOPDwPf0lDAiEh2KyDERL99qy3_uDrXgFxh-8zrM/s2600/telegram.jpg)

Earlier this April, the Redmond-based company [warned](https://thehackernews.com/2025/04/microsoft-warns-of-tax-themed-email.html) of several phishing campaigns leveraging tax-related themes to deploy malware such as Latrodectus, AHKBot, GuLoader, and BruteRatel C4 (BRc4). The phishing pages, it added, were delivered via RaccoonO365, with one such campaign attributed to an initial access broker called Storm-0249.

The phishing campaigns have targeted over 2,300 organizations in the United States, including at least 20 U.S. healthcare entities.

"Using RaccoonO365's services, customers can input up to 9,000 target email addresses per day and employ sophisticated techniques to circumvent multi-factor authentication protections to steal user credentials and gain persistent access to victims' systems," Microsoft said.

"Most recently, the group started advertising a new AI-powered service, RaccoonO365 AI-MailCheck, designed to scale operations and increase the sophistication – and effectiveness – of attacks."

The mastermind behind RaccoonO365 is assessed to be [Joshua Ogundipe](https://noticeofpleadings.com/RaccoonO365/), an individual based in Nigeria, who, along with his associates, has advertised the tool on an 850-member strong Telegram channel, receiving no less than $100,000 in cryptocurrency payments. The e-crime group is believed to have sold about 100-200 subscriptions, although Microsoft cautioned it's likely an underestimate.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The tech giant said it was able to make the attribution courtesy of an operational security lapse that inadvertently exposed a secret cryptocurrency wallet. Ogundipe and four other co-conspirators currently remain at large, but Microsoft noted that a criminal referral for Ogundipe has been sent to international law enforcement.

Cloudflare, in its own analysis of the PhaaS service, said the takedown of hundreds of domains and Worker accounts is aimed at incre...