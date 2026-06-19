---
title: PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM
url: https://www.trendmicro.com/en_us/research/26/f/PeopleTools.html
source: Trend Micro Research, News and Perspectives
date: 2026-06-18
fetch_date: 2026-06-19T07:09:13.273636
---

# PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM

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

[Looking for consumer solutions?](/en_us/forHome.html)

[Under Attack?](https://resources.trendmicro.com/GLB-Under-Attack-Form.html)

3 Alerts

Back

Unread

All

* [Webinar: The AI Threat Landscape — Why Now](https://trendmicro.zoom.us/webinar/register/6917533633873/WN_aVeYZcQPTNyUFAJDibiD3A)
  close

  [Save your spot >](https://trendmicro.zoom.us/webinar/register/6917533633873/WN_aVeYZcQPTNyUFAJDibiD3A)
* [Pwn2Own returns to Berlin with expanded AI categories and more than $1M in prizes.](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026)
  close

  [Learn more >](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026)
* [Webinar: Rethink VulnOps](https://resources.trendmicro.com/mythos-webinar.html)
  close

  [Mythos is accelerating vulnerability exploitation. Act faster >](https://resources.trendmicro.com/mythos-webinar.html)

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

Cyber Threats

# PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM

A pre-authentication remote code execution (RCE) chain in Oracle PeopleSoft PeopleTools abuses the Integration Broker's PSIGW gateway to execute code inside the application server's Java virtual machine (JVM), evading behavioral and network sensors.

By: Jacob Santos
Jun 18, 2026
Read time:  ( words)

[![Share](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg)](https://www.addtoany.com/share)
![Print](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

---

## Key takeaways

* A pre-authentication remote code execution (RCE) chain in Oracle PeopleSoft PeopleTools reaches an internal-only management servlet through a server-side request forgery (SSRF) in the PSIGW gateway, then gains code execution through Java XMLDecoder deserialization. Oracle assigned [CVE-2026-35273](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html) (CVSS 9.8) and released an out-of-band patch on June 10, 2026.
* The chain affects PeopleTools 8.61, and 8.62, including installations that were fully patched before the out-of-band advisory, because Oracle’s prior serialization-filter hardening does not cover this XMLDecoder code path.
* The chain is **behaviorally quiet**: Its final step executes inside the WebLogic JVM on a web-tier restart, with no spawned child process and no required outbound beacon. Detection logic that watches for “Java spawns a shell” or for an on-the-wire exploit signature will, in the common case, see nothing.
* TrendAI™ protections address this threat across the network and endpoint layers, including TrendAI™ Deep Discovery rules and TrendAI™ TippingPoint, TrendAI Vision One™ Server and Workload Protection (SWP), and TrendAI™ Deep Security filters. More guidance may be found in this entry’s recommendations section.

Enterprise resource planning systems handle some of the most sensitive data an organization holds, but they are also deeply connected to internal infrastructure. When a pre-authentication remote code execution (RCE) chain surfaces in one of the most widely deployed ERP platforms and is already being exploited in the wild, it warrants close attention. In this blog entry, TrendAI™ Research details a technical analysis of an active pre-auth...