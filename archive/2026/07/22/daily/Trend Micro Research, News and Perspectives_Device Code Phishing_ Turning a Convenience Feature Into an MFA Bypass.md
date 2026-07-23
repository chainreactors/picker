---
title: Device Code Phishing: Turning a Convenience Feature Into an MFA Bypass
url: https://www.trendmicro.com/en_us/research/26/g/device-code-phishing.html
source: Trend Micro Research, News and Perspectives
date: 2026-07-22
fetch_date: 2026-07-23T05:11:45.081766
---

# Device Code Phishing: Turning a Convenience Feature Into an MFA Bypass

[![Trend Micro logo](/content/dam/trendmicro/global/en/core/images/logos/tm-logo-red-white-t.svg)](/en_us/business.html)

search
close
[ ]

* About

  + [Mission and Culture](/en_us/about/why-trend-micro.html)

    - Mission and Culture

      As a leader in the AI-driven shift, we are committed to helping organizations navigate and thrive through a focused portfolio of cybersecurity businesses

      [Learn more](/en_us/about/why-trend-micro.html)
  + [Leadership Team](/en_us/about/leaders.html)

    - Leadership Team

      The executive leadership shaping strategy, innovation, and global direction

      [Learn more](/en_us/about/leaders.html)
  + [Company History](/en_us/about/history-vision-values.html)

    - Company History

      Key milestones and evolution across decades of innovation

      [Learn more](/en_us/about/history-vision-values.html)
  + [Corporate Social Responsibility](/en_us/about/corporate-social-responsibility.html)

    - Corporate Social Responsibility

      Programs and initiatives supporting sustainability, ethics, and global impact

      [Learn more](/en_us/about/corporate-social-responsibility.html)
  + [Careers](/en_us/about/careers.html)

    - Careers

      Opportunities to build your career and shape the future of cybersecurity

      [Learn more](/en_us/about/careers.html)
  + [Office Locations](/en_us/contact.html)

    - Office Locations

      Global offices and presence across regions and markets

      [Learn more](/en_us/contact.html)
* Portfolio

  + [TrendAI™](https://www.trendaisecurity.com)

    - TrendAI™

      The global AI security leader empowering organizations with full visibility and consolidated protection that inspires confidence, drives innovation, and eliminates risk

      [Learn more](https://www.trendaisecurity.com)
  + [TrendLife™](https://www.trendlife.com/)

    - TrendLife™

      Enabling peace of mind across your family in the AI era

      [Learn more](https://www.trendlife.com/)
  + [Magna™](https://magnaai.com/)

    - Magna™

      Provides advisory, build, integration, and operations for secure AI infrastructure, applications, and services

      [Learn more](https://magnaai.com/)
  + [VicOne](https://vicone.com/)

    - VicOne

      Security for the connected car ecosystem and modern mobility systems

      [Learn more](https://vicone.com/)
  + [TXOne Networks](https://www.txone.com/)

    - TXOne Networks

      Zero trust security for industrial systems and critical infrastructure

      [TXOne Networks](https://www.txone.com/)
* Investors

  + [Financial Reports and Data](/en_us/about/investor-relations.html)

    - Financial Reports and Data

      Quarterly and annual reports, financial statements, and key metrics

      [Learn more](/en_us/about/investor-relations.html)
  + [Earnings Conference](/en_us/about/investor-relations/conference-calendar.html)

    - Earnings Conference

      Earnings calls, presentations, and investor communications

      [Learn more](/en_us/about/investor-relations/conference-calendar.html)
* News and Media

  + [Newsroom](https://newsroom.trendmicro.com/)

    - Newsroom

      News, insights, and announcements from across our portfolio shaping the future of cybersecurity

      [Learn more](https://newsroom.trendmicro.com/)

Back

Back

Back

Back

* [Contact Us](https://www.trendaisecurity.com/en-us/contact)

[Looking for home security solutions?](/en_us/forHome.html)

[Under Attack?](https://resources.trendmicro.com/GLB-Under-Attack-Form.html)

1 Alerts

Back

Unread

All

* [The TrendAI™ 2026 Cyber Risk Report is here.](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/trendai-2026-cyber-risk-report)
  close

  [See the data >](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/trendai-2026-cyber-risk-report)

Support

* [Business Solutions](https://success.trendmicro.com/en-US/)
* [Consumer Solutions](https://helpcenter.trendmicro.com/en-us/)
* [Education and Certification](/en_us/business/services/support-services/education.html)
* [Contact Support](https://success.trendmicro.com/en-US/contactus/)
* [Find a Support Partner](https://partner.trendmicro.com/partner-locator-home/)

Resources

* [AI Innovation](/en_us/business/ai/innovation.html)
* [Trend Micro vs. Competition](/en_us/about/compare.html)
* [Cybersecurity Terms Library](/en_us/what-is.html)
* [Threat Encyclopedia](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/)
* [Glossary of Terms](https://www.trendmicro.com/vinfo/us/security/definition/a)
* [Webinars](/en_us/about/events.html)

Log In

* [Trend Vision One](https://signin.v1.trendmicro.com/)
* [Support](https://success.trendmicro.com/en-US/)
* [Partner Portal](https://partner.trendmicro.com/)
* [Cloud One](https://cloudone.trendmicro.com/)
* [Product Activation and Management](https://tm.login.trendmicro.com/simplesaml/saml2/idp/SSOService.php)
* [Referral Affiliate](https://signup.cj.com/member/signup/publisher/?cid=1867119#/branded?_k=xaeu3t)

Back

arrow\_back

search

|  |
| --- |
|  |

close

Content has been added to your Folio

Go to Folio (0)
close

Phishing

# Device Code Phishing: Turning a Convenience Feature Into an MFA Bypass

Device code phishing abuses a legitimate authentication feature designed for devices with limited input capabilities. This article breaks down how the technique works, examines a recent observed case, and outlines the layered security measures organizations can implement.

By: Ahmed Elsayed, Ahmed Hussein, Ahmed Kamal, Mahmoud Soheem
Jul 22, 2026
Read time:  ( words)

[![Share](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg)](https://www.addtoany.com/share)
![Print](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

---

**Key takeaways**

* Device code phishing involves the abuse of the OAuth 2.0 device authorization grant, a feature built for devices that cannot display a normal login page.
* The victim signs in and approves on the genuine Microsoft page, so no password is stolen, and MFA is satisfied for real. The session is simply issued to the attacker instead of to the user.
* When the attacker targets the Microsoft Authentication Broker, a single approval can be turned into registered rogue devices and long-lived refresh tokens, which means durable access rather than a one-off login.
* The best defenses are heightening user awareness, blocking the device-code flow where it is not needed, and using a detection solution that catches the behavior and keeps watch on the underlying events.

**Introduction**

For years, the advice to users was simple: turn on multi-factor authentication (MFA), and most account takeovers can be prevented. That advice still holds, and MFA still blocks most [password-based attacks](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/from-stealers-to-systems-the-new-model-of-credential-theft). The problem is that attackers adapt, and the more an organization relies on a single control, the more attention that control attracts.

The first big shift was adversary-in-the-middle [phishing](https://www.trendmicro.com/en_us/what-is/phishing.html), where a proxy site sits between the user and Microsoft and relays the login in real time to capture the session cookie. Device code [phishing](https://www.trendmicro.com/vinfo/us/security/news/threat-landscape/email-threat-landscape-report-evolving-threats-in-email-based-attacks) is the next step, and in some ways, it is cleaner for the attacker. There is no fake login site to build or to get blocked, and there is nothing visually wrong for the user to notice, because the page they enter their password on really is Microsoft. The only unusual thing is a short code and a plausible reason to enter it.

**How device code authentication is meant to work**

The device authorization grant exists for a s...