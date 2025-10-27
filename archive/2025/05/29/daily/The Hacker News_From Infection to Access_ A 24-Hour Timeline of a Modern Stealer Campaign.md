---
title: From Infection to Access: A 24-Hour Timeline of a Modern Stealer Campaign
url: https://thehackernews.com/2025/05/from-infection-to-access-24-hour.html
source: The Hacker News
date: 2025-05-29
fetch_date: 2025-10-06T22:32:05.145382
---

# From Infection to Access: A 24-Hour Timeline of a Modern Stealer Campaign

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

# [From Infection to Access: A 24-Hour Timeline of a Modern Stealer Campaign](https://thehackernews.com/2025/05/from-infection-to-access-24-hour.html)

**May 28, 2025**The Hacker NewsIdentity Theft / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEFtXXnSpjQSi-Py5BVLP2a6oumjBZcCx5zbVufCrvuRt0i-p7wlT37xc-OP0p0_dZVEwluIuTOcDKD5zGPUBQdr4qiDxX0jkuzEyIbOawWjVOOaLelCx_6PoWrrTMIN1aAaVyYYtGESJHgMUQcvOFhqEux0YvLimb9-aZH_mHcOnfxoC6lqVnH2rReHg/s790-rw-e365/flare.png)

Stealer malware no longer just steals passwords. In 2025, it steals live sessions—and attackers are moving faster and more efficiently than ever.

While many associate account takeovers with personal services, the real threat is unfolding in the enterprise. Flare's latest research, [The Account and Session Takeover Economy](https://flare.io/learn/resources/the-account-and-session-takeover-economy?utm_campaign=11744626-2025%20-%20ASTP&utm_source=Media&utm_medium=HackerNews&utm_content=From%20Infection%20to%20Access%3A%20A%2024-Hour%20Timeline%20of%20a%20Modern%20Stealer%20Campaign), analyzed over **20 million stealer logs** and tracked attacker activity across Telegram channels and dark web marketplaces. The findings expose how cybercriminals weaponize infected employee endpoints to hijack enterprise sessions—often in less than 24 hours.

Here's the real timeline of a modern session hijacking attack.

### **Infection and Data Theft in Under an Hour**

Once a victim runs a malicious payload—typically disguised as cracked software, fake updates, or phishing attachments—commodity stealers like Redline (44% of logs), Raccoon (25%), and LummaC2 (18%) take over.

These malware kits:

* Extract browser cookies, saved credentials, session tokens, and crypto wallets
* Automatically exfiltrate data to Telegram bots or command-and-control servers within minutes
* Feed over 16 million logs into just 10 Telegram channels alone, sorted by session type, location, and app

### **Session Tokens: The New Currency**

Within hours, cybercriminals sift through stolen data, focusing on high-value session tokens:

* 44% of logs contain Microsoft session data
* 20% include Google sessions
* Over 5% expose tokens from AWS, Azure, or GCP cloud services

Using Telegram bot commands, attackers filter logs by geography, application, and privilege level. Marketplace listings include browser fingerprint data and ready-made login scripts that bypass MFA.

Pricing for stolen sessions varies widely, with consumer accounts typically selling for $5 to $20, while enterprise-level AWS or Microsoft sessions can fetch $1,200 or more.

### **Full Account Access Within Hours**

Once session tokens are purchased, attackers import them into anti-detect browsers, gaining seamless access to business-critical platforms without triggering MFA or login alerts.

This isn't about personal accounts being misused. It's about attackers infiltrating corporate environments, where they quickly:

* Access business email like Microsoft 365 or Gmail
* Enter internal tools such as Slack, Confluence, or admin dashboards
* Exfiltrate sensitive data from cloud platforms
* Deploy ransomware or move laterally across systems

Flare analyzed a single stealer log that included live, ready-to-use access to Gmail, Slack, Microsoft 365, Dropbox, AWS, and PayPal—all tied to a single infected machine. In the wrong hands, this level of session access can escalate into a serious breach within hours.

### **Why This Matters: The Scale of the Threat**

This is no outlier. It is a **massive, industrialized underground market** enabling ransomware gangs, fraudsters, and espionage groups:

* Millions of valid sessions are stolen and sold weekly
* Tokens remain active for days, allowing persistent access
* Session hijacking bypasses MFA, leaving many organizations blind to breaches

These attacks don't result from breaches at Microsoft, Google, AWS, or other service providers. Instead, they stem from individual users getting infected by stealer malware, which silently exfiltrates their credentials and live session tokens. Attackers then exploit this user-level access to impersonate employees, steal data, and escalate privileges.

According to [Verizon's 2025 DBIR](https://www.verizon.com/business/resources/reports/2025-dbir-data-breach-investigations-report.pdf), 88% of breaches involved stolen credentials, highlighting just how central identity-based attacks have become.

If you're only watching for stolen passwords or failed login attempts, you're missing the biggest attack vector.

### **How to Defend Your Organization**

Session tokens are as critical as passwords and require a new defense mindset:

* Revoke all active sessions immediately after endpoint compromise; password resets alone don't stop attackers
* Monitor network traffic for Telegram domains, a key exfiltration channel
* Use browser fingerprinting and anomaly detection to flag suspicious session use from unknown devices or locations

Adapting defenses to this new reality is essential for stopping fast-moving threat actors.

### **Dive Deeper with Flare**

Our full report covers:

* The most common malware families used in attacks
* Detailed token pricing by access type
* Screenshots of Telegram bots and marketplace listings
* Actionable recommendations for detection and response

Explore our extensive dataset yourself by starting a **free trial**. Search millions of stealer logs, identify exposed sessions, and get ahead of attackers.

[Read the full report](https://flare.io/learn/resources/the-account-and-session-takeover-economy?utm_campaign=11744626-2025%20-%20ASTP&utm_source=Media&utm_medium=HackerNews&utm_content=From%20Infection%20to%20Access%3A%20A%2024-Hour%20Timeline%20of%20a%20Modern%20Stealer%20Campaign) | [Start your free trial](https://try.flare.io/intro/?utm_campaign=11744626-2025%20-%20ASTP&utm_source=Media&utm_medium=HackerNews&utm_content=From%20Infection%20to%20Access%3A%20A%2024-Hour%20Timeline%20of%20a%20M...