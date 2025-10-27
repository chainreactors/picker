---
title: 5 Ways Identity-based Attacks Are Breaching Retail
url: https://thehackernews.com/2025/07/5-ways-identity-based-attacks-are.html
source: The Hacker News
date: 2025-07-09
fetch_date: 2025-10-07T00:03:34.283898
---

# 5 Ways Identity-based Attacks Are Breaching Retail

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

# [5 Ways Identity-based Attacks Are Breaching Retail](https://thehackernews.com/2025/07/5-ways-identity-based-attacks-are.html)

**Jul 08, 2025**The Hacker NewsSaaS Security / Cyber Threat

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgihGob_Vhyzb1HAlJ-ib9yBajKfhHoCtxRmB5FcK8z7cKNKU_VpTvRXSdSl3-ENS-gYKoCT11aBl3iFvsDRvMt4DAAIgL33SEbo675uCuuabb-PGFX8ngM03tX1pTduXTS3YTxh40Gqrt_P9iCjjJZ4Y9HxWeXjSOf95wAOmLmAlNcN_d2AABpJ5m3bVk/s790-rw-e365/wing.jpg)

From overprivileged admin roles to long-forgotten vendor tokens, these attackers are slipping through the cracks of trust and access. Here's how five retail breaches unfolded, and what they reveal about...

In recent months, major retailers like Adidas, The North Face, Dior, Victoria's Secret, Cartier, Marks & Spencer, and Co‑op have all been breached. These attacks weren't sophisticated malware or zero-day exploits. They were identity-driven, exploiting overprivileged access and unmonitored service accounts, and used the human layer through tactics like social engineering.

Attackers didn't need to break in. They logged in. They moved through SaaS apps unnoticed, often using real credentials and legitimate sessions.

And while most retailers didn't share all the technical details, the patterns are clear and recurring.

Here's a breakdown of the five recent high-profile breaches in retail:

## **1. Adidas: Exploiting third-party trust**

Adidas [confirmed](https://www.adidas-group.com/en/data-security-information) a data breach caused by an attack on a third-party customer service provider. The company said customer data was exposed, including names, email addresses, and order details. No malware. No breach on their side. Just the blast radius of a vendor they trusted.

### **How these attacks unfold in SaaS identities:**

SaaS tokens and service accounts granted to vendors often don't require MFA, don't expire, and fly under the radar. Once access is no longer needed but never revoked, they become silent entry points, perfect for supply chain compromises that map to tactics like T1195.002, giving attackers a way in without setting off alarms.

### **Security takeaway:**

You're not just securing your users. You're securing the access that vendors leave behind, too. SaaS integrations stick around longer than the actual contracts, and attackers know exactly where to look.

## **2. The North Face: From password reuse to privilege abuse**

The North Face confirmed a credential stuffing [attack](https://www.forbes.com/sites/daveywinder/2025/06/03/password-attack---the-north-face-confirms-data-breach/) (MITRE T1110.004) where threat actors used leaked credentials (usernames and passwords) to access customer accounts. No malware, no phishing, just weak identity hygiene and no MFA. Once inside, they exfiltrated personal data, exposing a major gap in basic identity controls.

### **How these attacks unfold in SaaS identities:**

SaaS logins without MFA are still everywhere. Once attackers get valid credentials, they can access accounts directly and quietly, no need triggering endpoint protections or raising alerts.

### **Security takeaway:**

Credential stuffing is nothing new. It was the fourth credential-based breach for The North Face since 2020. Each one is a reminder that password reuse without MFA is a wide-open door. And while plenty of orgs enforce MFA for employees, service accounts, and privileged roles, many times they go unprotected. Attackers know it, and they go where the gaps are.

![SaaS Identity Security Guide](data:image/png;base64...)

**Want to go deeper?** Download the [**'SaaS Identity Security Guide**](https://wing.security/resources/the-ultimate-guide-to-saas-identity-security-in-2025/?utm_campaign=126888169-2025-06-Hacker%20News-5-Retail-Breaches&utm_source=The%20Hacker%20News&utm_medium=Article&utm_content=Retail-Breaches-Guide)**'** to learn how to proactively secure every identity, human or non-human, across your SaaS stack.

## **3. M&S & Co-op: Breached by borrowed trust**

UK retailers Marks & Spencer and Co-op were reportedly targeted by the threat group Scattered Spider, known for identity-based attacks. According to [reports](https://thehackernews.com/2025/06/scattered-spider-behind-cyberattacks-on.html), they used SIM swapping and social engineering to impersonate employees and trick IT help desks into resetting passwords and MFA, effectively bypassing MFA, all without malware or phishing.

### **How these attacks unfold in SaaS identities:**

Once attackers bypass MFA, they target overprivileged SaaS roles or dormant service accounts to move laterally within the organization's systems, harvesting sensitive data or disrupting operations along the way. Their actions blend in with legitimate user behavior (T1078), and with password resets driven by help desk impersonation (T1556.003), they quietly gain persistence and control without raising any alarms.

### **Security takeaway:**

There's a reason identity-first attacks are spreading. They exploit what's already trusted, and often leave no malware footprint. To reduce risk, track SaaS identity behavior, including both human and non-human activity, and limit help desk privileges through isolation and escalation policies. Targeted training for support staff can also block social engineering before it happens.

## **4. Victoria's Secret: When SaaS admins go unchecked**

Victoria's Secret delayed its earnings release after a cyber [incident](https://apnews.com/article/victorias-secret-earnings-delayed-cyberattack-1fda0fe1da3699177f2ab0c6ee75873e) disrupted both e-commerce and in-store systems. While few details were disclosed, the impact aligns with scenarios involving internal disruption through SaaS systems that manage retail operations, like inventory, order processing, or analytics tools.

### **How these attacks unfold in SaaS identities:**

The real risk isn't just compromised credentials. It's the unchecked power of overprivileged SaaS roles. When a misconfigur...