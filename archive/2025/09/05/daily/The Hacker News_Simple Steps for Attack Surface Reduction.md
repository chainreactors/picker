---
title: Simple Steps for Attack Surface Reduction
url: https://thehackernews.com/2025/08/simple-steps-for-attack-surface.html
source: The Hacker News
date: 2025-09-05
fetch_date: 2025-10-02T19:42:44.881332
---

# Simple Steps for Attack Surface Reduction

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

# [Simple Steps for Attack Surface Reduction](https://thehackernews.com/2025/08/simple-steps-for-attack-surface.html)

**Sep 04, 2025**The Hacker NewsEndpoint Security / Application Security

[![Attack Surface Reduction](data:image/png;base64... "Attack Surface Reduction")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiT7Mcp1XC9bIhaFPW66sVpaNPIvFQDNSGzon1KrrTWu64Cra_ZJaxjblD4WnJGqlCzFPOyG61RvcUXvmQz_ay2onExNP3SFMRfCwpjBnARFo0NpUm2VeQZB2xyUIeF0er71HnTv15OKWP6jbJKfnrf42GfKOwVbcRwCY-hb-_7Jn2afXZkKT2rh6QxfPI/s790-rw-e365/TL-MAIN.jpg)

Story teaser text: Cybersecurity leaders face mounting pressure to stop attacks before they start, and the best defense may come down to the settings you choose on day one. In this piece, Yuriy Tsibere explores how default policies like deny-by-default, MFA enforcement, and application Ringfencing ™ can eliminate entire categories of risk. From disabling Office macros to blocking outbound server traffic, these simple but strategic moves create a hardened environment that attackers can't easily penetrate. Whether you're securing endpoints or overseeing policy rollouts, adopting a security-by-default mindset can reduce complexity, shrink your attack surface, and help you stay ahead of evolving threats.

Cybersecurity has changed dramatically since the days of the "Love Bug" virus in 2001. What was once an annoyance is now a profit-driven criminal enterprise worth billions. This shift demands proactive defense strategies that don't just respond to threats—they prevent them from ever reaching your network. [CISOs, IT admins, and MSPs need solutions that block attacks by default](https://www.threatlocker.com/book-a-threatlocker-demo?utm_source=hacker_news&utm_medium=sponsor&utm_campaign=yuriy_1_q3_25&utm_content=yuriy_1&utm_term=article), not just detect them after the fact. Industry frameworks like NIST, ISO, CIS, and HIPAA provide guidance, but they often lack the clear, actionable steps needed to implement effective security.

For anyone starting a new security leadership role, the mission is clear: Stop as many attacks as possible, frustrate threat actors, and do it without alienating the IT team. That's where a security-by-default mindset comes in—configuring systems to block risks out of the gate. As I've often said, the attackers only have to be right once. We have to be right 100% of the time.

Here's how setting the right defaults can eliminate entire categories of risk.

## Require multi-factor authentication (MFA) on all remote accounts

Enabling MFA across all remote services—including SaaS platforms like Office 365 and G Suite, as well as domain registrars and remote access tools—is a foundational security default. Even if a password is compromised, MFA can prevent unauthorized access. Try to avoid using text messages for MFA as it can be intercepted.

While it may introduce some friction, the security benefits far outweigh the risk of data theft or financial loss.

## Deny-by-default

[One of the most effective security measures nowadays is application whitelisting or allowlisting. This approach blocks everything by default and only allows known, approved software to run.](https://www.threatlocker.com/platform/application-allowlisting?utm_source=hacker_news&utm_medium=sponsor&utm_campaign=yuriy_1_q3_25&utm_content=yuriy_1&utm_term=article) The result: Ransomware and other malicious applications are stopped before they can execute. It also blocks legitimate-but-unauthorized remote tools like AnyDesk or similar, which attackers often try to sneak in through social engineering.

Users can still access what they need via a pre-approved store of safe applications, and visibility tools make it easy to track everything that runs—including portable apps.

## Quick wins through secure configuration

Small changes to default settings can close major security gaps on Windows and other platforms:

* Turn off Office macros: It takes five minutes and blocks one of the most common attack vectors for ransomware.
* Use password-protected screensavers: Auto-lock your screen after a short break to stop anyone from snooping around.
* Disable SMBv1: This old-school protocol is outdated and has been used in big attacks like WannaCry. Most systems don't need it anymore.
* Turn off the Windows keylogger: It's rarely useful and could be a security risk if left on.

## Control network and application behavior for organizations

* Remove local admin rights: Most malware doesn't need admin access to run, but taking it away stops users from messing with security settings or even installing malicious software.
* Block unused ports and limit outbound traffic:
  + Shut down SMB and RDP ports unless absolutely necessary—and only allow trusted sources.
  + Stop servers from reaching the internet unless they need to. This helps avoid attacks like SolarWinds.
* [Control application behaviors: Tools like ThreatLocker Ringfencing ™ can stop apps from doing sketchy things](https://www.threatlocker.com/platform/ringfencing?utm_source=hacker_news&utm_medium=sponsor&utm_campaign=yuriy_1_q3_25&utm_content=yuriy_1&utm_term=article)—like Word launching PowerShell (yes, that's a real attack method).
* Secure your VPN: If you don't need it, turn it off. If you do, limit access to specific IPs and restrict what users can access.

## Strengthen data and web controls

* Block USB drives by default: They're a common way for malware to spread. Only allow secure managed, encrypted ones if needed.
* Limit file access: Apps shouldn't be able to poke around in user files unless they really need to.
* Filter out unapproved tools: Block random SaaS or cloud apps that haven't been vetted. Let users request access if they need something.
* Track file activity: Keep an eye on who's doing what with files—both on devices and in the cloud. It's key for spotting shady behavior.

## Go beyond defaults with monitoring and patching

Strong defaults are just the beginning. Ongoing vigilance is critical:

* Regular patching: Most attacks use know...