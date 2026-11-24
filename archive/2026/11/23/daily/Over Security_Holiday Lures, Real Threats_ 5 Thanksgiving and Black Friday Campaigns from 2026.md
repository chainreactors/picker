---
title: Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026
url: https://any.run/cybersecurity-blog/thanksgiving-black-friday-cyber-threats-2026/
source: Over Security
date: 2026-11-23
fetch_date: 2026-11-24T11:49:02.642768
---

# Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/thanksgiving_2026-scaled.png)

[Threat Landscape](https://any.run/cybersecurity-blog/category/threat-landscape/)

# Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026

November 23, 2026

[Add comment](#comments-24466)
4006 views
14 min read

[Home](https://any.run/cybersecurity-blog/)[Threat Landscape](https://any.run/cybersecurity-blog/category/threat-landscape/)

Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/financial-fraud-1024x497.png)

  #### LATAM’s Financial Fraud Ecosystem: Key Threats and Strategies for Business Protection

  46
  0](https://any.run/cybersecurity-blog/latams-financial-fraud/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/thanksgiving_2026-1024x497.png)

  #### Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026

  4006
  0](https://any.run/cybersecurity-blog/thanksgiving-black-friday-cyber-threats-2026/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/Budget_Planning_2027_cover-1024x497.png)

  #### Smarter SOC Spending in 2027: Reduce Costs, Recover Capacity, Strengthen Detection

  12741
  0](https://any.run/cybersecurity-blog/soc-budget-planning-2027/)

[Home](https://any.run/cybersecurity-blog/)[Threat Landscape](https://any.run/cybersecurity-blog/category/threat-landscape/)

Holiday Lures, Real Threats: 5 Thanksgiving and Black Friday Campaigns from 2026

The holiday season brings a surge of invitations, promotional offers, and shared documents — all familiar ways for cybercriminals to disguise malicious activity.

During the 2026 Thanksgiving and Black Friday season, [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=thanksgiving-black-friday-cyber-threats-2026&utm_term=231126&utm_content=linktolanding) analysts investigated five cases involving fake corporate invitations, e-cards, healthcare surveys, promotional newsletters, and discount coupons. The campaigns aimed to steal credentials, collect personal data, deploy scripts, or gain remote access.

Some relied on multi-stage redirects and browser fingerprinting; others abused legitimate services and software rather than traditional malware.

These cases show why email inspection alone isn’t enough. SOC and MSSP analysts need to understand what happens after a user clicks a link or opens a file.

Let’s look at how each attack worked, the indicators it left behind, and the lessons for defenders.

## Thanksgiving: When Holiday Invitations Become Corporate Security Threats

Thanksgiving-themed campaigns in the 2026 dataset primarily used invitations and familiar workplace communications rather than shopping offers.

Two cases involved threats against corporate employees, while the third used a seasonal survey to collect personal information and solicit payments.

### 1. Thanksgiving Potluck Invitation Leads to a Fake Google Workspace Login

**Threat type:** Credential phishing, browser fingerprinting

**Observed:** November 4-5, 2026

**Target:** Employees of a US real estate agency network

A Thanksgiving potluck invitation sent from an organization’s own office mailbox can easily look like an ordinary workplace announcement.

[View the campaign analysis in ANY.RUN Interactive Sandbox](https://app.any.run/tasks/f86629fe-0ad6-4d9d-a527-8388a2ccdc66/?utm_source=anyrunblog&utm_medium=article&utm_campaign=thanksgiving-black-friday-cyber-threats-2026&utm_term=231126&utm_content=linktoservice)

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/thanksgiving01-1024x517.jpeg)

*A Thanksgiving Potluck Invitation phishing campaign observed in ANY.RUN’s Sandbox*

In this case, [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=thanksgiving-black-friday-cyber-threats-2026&utm_term=231126&utm_content=linktolanding) researchers investigated an email sent from the front desk mailbox of a franchise office belonging to a large US real estate agency network. An employee from another office forwarded the message, flagging it as suspicious.

The subject was “RSVP to Thanksgiving Potluck.” The email contained a festive invitation reading “Thanksgiving Potluck — you’re invited!” and asked recipients to RSVP before November 16.

The message imitated a familiar event invitation format, making it particularly convincing in a corporate environment.

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/thanksgiving02-1-1024x584.jpeg)

*The lure email in the Thanksgiving Potluck Invitation phishing campaign*

Clicking the “View & RSVP” button redirected the recipient to **trident-ww[.]com/ok/**, where the phishing chain began.

The page displayed a fake security verification step featuring a Gmail logo and the message “Security Check — I’m not a robot.”

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/thanksgiving03-1024x569.png)

*Fake Google security check page*

After displaying “Verification successful,” it presented a Google Workspace sign-in page.

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/thanksgiving04-1024x576.png)

*Fake Google sign in page*

The login form was loaded inside an iframe from a separate domain, **om[.]anthonnyfry[.]com**. Interestingly, opening the form directly caused a ...