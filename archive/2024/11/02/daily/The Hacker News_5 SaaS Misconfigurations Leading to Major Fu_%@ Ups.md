---
title: 5 SaaS Misconfigurations Leading to Major Fu*%@ Ups
url: https://thehackernews.com/2024/11/5-saas-misconfigurations-leading-to.html
source: The Hacker News
date: 2024-11-02
fetch_date: 2025-10-06T19:20:51.558937
---

# 5 SaaS Misconfigurations Leading to Major Fu*%@ Ups

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

# [5 SaaS Misconfigurations Leading to Major Fu\*%@ Ups](https://thehackernews.com/2024/11/5-saas-misconfigurations-leading-to.html)

**Nov 01, 2024**The Hacker NewsSaaS Security / Insider Threat

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtX0fw-CFGiZ192kA2-C5lOeDuSS7GZ5WLs-VZz9FPdrQB1zsdGF1KVucbehYCmUtkky1Ea44WG774Dq7mt-xB6Lk17AIBm7GyPudOhMq2bj3xcyeGF1ZM0Qdg9VecIyo4GrIDu6cLAgkkfbyV0708VgIv3wWxmqNOO3VxOcwbSoVutWIy7hCZo2Qwpaw/s790-rw-e365/wing.png)

With so many SaaS applications, a range of configuration options, API capabilities, endless integrations, and app-to-app connections, the SaaS risk possibilities are endless. Critical organizational assets and data are at risk from malicious actors, data breaches, and insider threats, which pose many challenges for security teams.

*Misconfigurations are silent killers, leading to major vulnerabilities.*

So, how can CISOs reduce the noise? What misconfiguration should security teams focus on first? Here are five major SaaS configuration mistakes that can lead to security breaches.

## **#1 Misconfiguration: HelpDesk Admins Have Excessive Privileges**

* **Risk:** Help desk teams have access to sensitive account management functions making them prime targets for attackers. Attackers can exploit this by convincing help desk personnel to reset MFA for privileged users, gaining unauthorized access to critical systems.
* **Impact:** Compromised help desk accounts can lead to unauthorized changes to admin-level features enabling the attackers to gain access to critical data and business systems.
* **Action:** Restrict help desk privileges to basic user management tasks and limit changes to admin-level settings.

[Use Case: The MGM Resort Cyberattack](https://wing.security/blog/saas-security/a-saas-misconfiguration-case-study/?utm_campaign=2024-11-Misconfigurations&utm_source=The%20Hacker%20News&utm_medium=Article&utm_term=Blog%20THN%20Misconfiguration&utm_content=Misconfiguration) -> In September 2023, MGM Resorts International became the target of a sophisticated cyberattack. The attackers, allegedly part of a cybercriminal gang known as Scattered Spider (also referred to as Roasted 0ktapus or UNC3944), used social engineering tactics to penetrate MGM's defenses.

## **#2 Misconfiguration: MFA Not Enabled for All Super Admins**

* **Risk:** Super admin accounts without MFA are high-value targets for attackers due to their elevated access privileges. If MFA is not enforced, attackers can easily exploit weak or stolen credentials to compromise these critical accounts.
* **Impact:** A successful breach of a super admin account can lead to the attacker getting full control over the entire organization's SaaS environment, resulting in potential data breaches and business and reputational damage.
* **Action:** Enforce MFA for all active super admins to add an extra layer of security, and safeguard these high-privilege accounts.

## **#3 Misconfiguration: Legacy Authentication Not Blocked by Conditional Access**

* **Risk:** Legacy protocols like POP, IMAP, and SMTP are still commonly used in Microsoft 365 environments, yet they don't support MFA. These outdated protocols create significant vulnerabilities and without Conditional Access enforcement, attackers can bypass security measures and infiltrate sensitive systems.
* **Impact:** These outdated protocols make accounts more vulnerable to credential-based attacks, such as brute-force or phishing attacks, making it easier for attackers to gain access.
* **Action**: Enable Conditional Access to block legacy authentication and enforce modern, more secure authentication methods.

## **#4 Misconfiguration: Super Admin Count Not Within Recommended Limits**

* **Risk:** Super admins manage critical system settings and mainly have unrestricted access to various workspaces. Too many or too few super admins increase the risk by overexposing sensitive controls or the operational risk of losing access and being locked out of critical business systems.
* **Impact:** Unrestricted access to critical system settings can lead to catastrophic changes or loss of control over security configurations resulting in security breaches.
* **Action:** Maintain a balance of 2-4 super admins (excluding "break-glass" accounts), for both security and continuity, as per [CISA's SCuBA recommendations.](https://www.cisa.gov/resources-tools/services/gws-commoncontrols#GWSCOMMONCONTROLS62v02)

## **#5 Misconfiguration: Google Groups (Join / View / Post) View Settings**

* **Risk:** Misconfigured Google Group settings can expose sensitive data shared via Google Workspace to unauthorized users. This exposure increases insider risks, where a legitimate user could intentionally or unintentionally leak or misuse the data.
* **Impact:** Confidential information, such as legal documents, could be accessed by anyone in the organization or external parties, increasing the risk of insider misuse or data leaks.
* **Action:** ensure that only authorized users can view and access group content to prevent accidental exposure and mitigate insider risk.

Proactively identifying and fixing SaaS misconfigurations saves organizations from catastrophic events impacting business continuity and reputation, but it's not a one-time project. Identifying and fixing these SaaS misconfigurations needs to be continuous because of the constantly changing nature of SaaS applications. SaaS security platforms like [Wing Security](https://wing.security/lp-misconfigurations/?utm_campaign=2024-11-Misconfigurations&utm_source=The%20Hacker%20News&utm_medium=Article&utm_term=LP%20THN%20Misconfiguration&utm_content=Misconfiguration), quickly identify, prioritize, and help you fix potential risks continuously.

Wing's configuration center, based on CISA's SCuBA framework, cuts through the noise and highlights the most critical misconfigurations, offering clear, actionable steps to resolve them. With real-time monitoring, compliance tracking, and an audit trail, it ens...