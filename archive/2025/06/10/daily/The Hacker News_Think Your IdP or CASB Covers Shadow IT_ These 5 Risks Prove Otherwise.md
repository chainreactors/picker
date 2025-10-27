---
title: Think Your IdP or CASB Covers Shadow IT? These 5 Risks Prove Otherwise
url: https://thehackernews.com/2025/06/think-your-idp-or-casb-covers-shadow-it.html
source: The Hacker News
date: 2025-06-10
fetch_date: 2025-10-06T22:57:40.005370
---

# Think Your IdP or CASB Covers Shadow IT? These 5 Risks Prove Otherwise

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

# [Think Your IdP or CASB Covers Shadow IT? These 5 Risks Prove Otherwise](https://thehackernews.com/2025/06/think-your-idp-or-casb-covers-shadow-it.html)

**Jun 09, 2025**The Hacker News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZcHGLAQOp9rjB0VZcOLQvMbsQuEynw-4He57SyuMCJWEU4ohr2VBjFTTCu71nlSrwFKiuDqRjxoBUrwJGqlF9Yv1VzagiFy25A27VkwqUrnwEn6xcwghntC3nzDHmQ0yHB7-L1O72u6_xW7-0RXY9JIqxZIuI7j5E-czee3B2ACVWEmDzEnEfPIa11GU/s790-rw-e365/main.png)

You don’t need a rogue employee to suffer a breach.

All it takes is a free trial that someone forgot to cancel. An AI-powered note-taker quietly syncing with your Google Drive. A personal Gmail account tied to a business-critical tool. That’s shadow IT. And today, it’s not just about unsanctioned apps, but also dormant accounts, unmanaged identities, over-permissioned SaaS tools, and orphaned access. Most of it slips past even the most mature security solutions.

**Think your CASB or IdP covers this? It doesn’t.**

They weren’t built to catch what's happening inside SaaS: OAuth sprawl, shadow admins, GenAI access, or apps created directly in platforms like Google Workspace or Slack. **Shadow IT is no longer a visibility issue - it’s a full-blown attack surface.**

[Wing Security](https://wing.security/?utm_source=The_Hacker_News&utm_medium=Article_Top&utm_campaign=114039033-2025-06-Hacker%20News-5-ShadowIT-Risks) helps security teams uncover these risks before they become incidents.

Here are 5 real-world examples of shadow IT that could be quietly bleeding your data.

### **1. Dormant access you can’t see, that attackers love to exploit**

* **The risk**: Employees sign up for tools using just a username and password, without SSO or centralized visibility. Over time, they stop using the apps, but access stays, and worse, it is unmanaged.
* **The impact**: These zombie accounts become invisible entry points into your environment. You can’t enforce MFA, monitor usage, or revoke access during offboarding.
* **Example:** CISA and global cyber agencies issued a joint advisory warning in 2024 that Russian state-sponsored group APT29 (part of the SVR) actively targets dormant accounts to gain access to enterprise and government systems. These accounts often serve as ideal footholds since they go unnoticed, lack MFA, and remain accessible long after they're no longer in use.

### **2. Generative AI quietly reading your emails, files, and strategy**

* **The risk**: SaaS apps powered by Generative AI usually request broad OAuth permissions with full access to read inboxes, files, calendars, and chats.
* **The impact**: These SaaS apps often grant more access than required, exfiltrate sensitive data to third parties with unclear data retention and model training policies. Once access is granted, there’s no way to monitor how your data is stored, who has access internally, or what happens if the vendor is breached or misconfigures access.
* **Example**: In 2024, DeepSeek accidentally [exposed internal LLM training files](https://www.cm-alliance.com/cybersecurity-blog/deepseek-cyber-attack-timeline-impact-and-lessons-learned) containing sensitive data due to a misconfigured storage bucket, highlighting the risk of giving third-party GenAI tools broad access without oversight around data security.

### **3. Former employees still hold admin access, months after leaving**

* **The risk**: When employees onboard new SaaS tools (especially outside your IdP), they often are the sole admin. Even after they leave the company, their access remains.
* **The impact**: These accounts can have persistent, privileged access to company tools, files, or environments, posing a long-term insider risk.
* **Real-life example**: A contractor set up a time-tracking app and linked it to the company’s HR system. Months after their contract ended, they still had admin access to employee logs.

[See what Wing uncovers in your SaaS environment.](https://wing.security/request-a-demo/?utm_source=The_Hacker_News&utm_medium=Article_Mid&utm_campaign=114039033-2025-06-Hacker%20News-5-ShadowIT-Risks) Talk with a security expert and get a demo.

### **4. Business-critical apps tied to personal accounts you don’t control**

* **The risk**: Employees sometimes use their personal Gmail, Apple ID, or other unmanaged accounts to sign up for business apps like Figma, Notion, or even Google Drive.
* **The impact**: These accounts exist entirely outside of IT visibility. If they get compromised, you can’t revoke access or enforce security policies.
* **Example**: In the [2023 Okta customer support breach](https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/), hackers exploited a service account without MFA that had access to Okta’s support system. The account was active, unmonitored, and not tied to a specific person. Even companies with mature identity systems can miss these blind spots.

### **5. Shadow SaaS with app-to-app connectivity to your crown jewels**

* **The risk**: Employees connect unsanctioned SaaS apps directly to trusted platforms like Google Workspace, Salesforce, or Slack—without IT involvement or review. These app-to-app connections often request broad API access and stay active long after use.
* **The impact**: These integrations create hidden pathways into critical systems. If compromised, they can enable lateral movement, allowing attackers to pivot across apps, exfiltrate data, or maintain persistence without triggering traditional alerts.
* **Example**: A product manager connected a roadmap tool to Jira and Google Drive. The integration requested broad access but was forgotten after the project ended. When the vendor was later breached, attackers used the lingering connection to pull files from Drive and pivot into Jira, accessing internal credentials and escalation paths. This type of lateral movement was seen in the [2024 Microsoft breach](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-...