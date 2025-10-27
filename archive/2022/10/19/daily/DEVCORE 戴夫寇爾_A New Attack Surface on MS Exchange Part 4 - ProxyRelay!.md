---
title: A New Attack Surface on MS Exchange Part 4 - ProxyRelay!
url: https://devco.re/blog/2022/10/19/a-new-attack-surface-on-MS-exchange-part-4-ProxyRelay/
source: DEVCORE 戴夫寇爾
date: 2022-10-19
fetch_date: 2025-10-03T20:16:03.598628
---

# A New Attack Surface on MS Exchange Part 4 - ProxyRelay!

[![](/images/logo.svg)](/en/)

* Services

  [## Red Team Assessment

  Simulation of real-world attacks to identify vulnerabilities and achieve objectives without disrupting business operations.](/en/services/red-team/)
  [## Penetration Testing

  Infiltration of designated enterprise systems to uncover potential vulnerabilities and assess the risks or damages.](/en/services/penetration-test/)
  [## Security Consulting

  Consultation of resource distribution and long-term defensive strategies from the attacker’s perspective.](/en/services/security-consulting/)
  [## Security Training

  Instruction on defending and preventing incidents with the hacker mindset, also the response procedures and analysis of attacks when incidents happen.](/en/services/security-training/)
  [## OffSec Advanced Training

  Structured in-person (OffSec Live Training) and online training, featuring up-to-date offensive security skills with OffSec certification and resources.](https://training.devco.re/)
* Research

  [## Overview

  Research of updated cybersecurity techniques and trends, assess the security of products, and evolve the red team with broad experience.](/en/research/overview/)
  [## Competitions and Awards

  Awards from international cybersecurity competitions.](/en/research/awards/)
  [## Enterprise Vulnerability Reports

  Research of the risk of enterprise systems, identification of potential weaknesses, and report to vendors.](/en/research/bug-bounty/)
  [## International Conferences

  Sharing vulnerability research and security knowledge at international cybersecurity conferences.](/en/research/talks/)
  [## CVE List

  Discovery of critical vulnerabilities in leading international products and services.](/en/research/cve/)
* Company

  [## Company Overview

  Founded by a world-class white hat hacker team, providing cybersecurity services including Red Team Assessment, Penetration Testing, Security Consulting, and Security Training.](/en/company/about/)
  [## Team Members

  Composed of cybersecurity experts with the hacker mindset, exploring innovative exploitation techniques with high morality and extreme caution.](/en/company/our-team/)
  [## Achievements

  DEVCORE has been invited to leading cybersecurity conferences, has uncovered hundreds of critical product vulnerabilities, and helped enterprises improve their defensive capabilities.](/en/company/history/)
  [## Corporate Social Responsibility

  We provide diverse internship channels and programs to nurture the next generation and promote cybersecurity awareness.](/en/company/csr/)
  [## Job Opportunities

  Join us to secure the world and improve the cybersecurity industry together.](/en/company/jobs/)
  [## DEVCORE CONFERENCE

  DEVCORE’s annual technical conference focused on offensive security research, red team insights, and novel attack vectors from real-world operations.](https://conf.devco.re/)
* News

  [## BLOG

  Latest news](/en/blog/)
  [## Media Resources

  Media Kit, Logo and Usage Guideline](/en/media-kit/)
* [Search](/en/search/)
* [Contact](/en/contact/)

* Services

  [## Red Team Assessment](/en/services/red-team/)
  [## Penetration Testing](/en/services/penetration-test/)
  [## Security Consulting](/en/services/security-consulting/)
  [## Security Training](/en/services/security-training/)
* Research

  [## Overview](/en/research/overview/)
  [## Competitions and Awards](/en/research/awards/)
  [## Enterprise Vulnerability Reports](/en/research/bug-bounty/)
  [## International Conferences](/en/research/talks/)
  [## CVE List](/en/research/cve/)
* Company

  [## Company Overview](/en/company/about/)
  [## Team Members](/en/company/our-team/)
  [## Achievements](/en/company/history/)
  [## Corporate Social Responsibility](/en/company/csr/)
  [## Job Opportunities](/en/company/jobs/)
  [## DEVCORE CONFERENCE](https://conf.devco.re/)
* News

  [## BLOG](/en/blog/)
  [## Media Resources](/en/media-kit/)
* [## Search](/en/search/)
  [## Contact](/en/contact/)
* Language

  [## 中文](/)
  [## English](/en)

# BLOG

* [All Articles](/en/blog/)
* [Tech Editorials](/en/blog/category/Tech%20Editorials/)
* [Media Resources](/en/media-kit/)

[Tech Editorials](/en/blog/category/Tech%20Editorials)

[#Advisory](/en/blog/tag/Advisory/) [#CVE](/en/blog/tag/CVE/) [#RCE](/en/blog/tag/RCE/) [#Exchange](/en/blog/tag/Exchange/) [#Pwn2Own](/en/blog/tag/Pwn2Own/)

# A New Attack Surface on MS Exchange Part 4 - ProxyRelay!

[Orange Tsai](/en/blog/author/orange)
2022-10-19

![](https://devco.re/assets/img/blog/20221019/cover.jpeg)

---

Hi, this is a long-time-pending article. We could have published this article earlier (the original bug was reported to MSRC in June 2021 with a 90-days Public Disclosure Policy). However, during communications with MSRC, they explained that since this is an architectural design issue, lots of code changes and testings are expected and required, so they hope to resolve this problem with a one-time CU (Cumulative Update) instead of the regular Patch Tuesday. We understand their situation and agree to extend the deadline.

Microsoft eventually released [Exchange Server 2019 CU 12](https://support.microsoft.com/en-au/topic/cumulative-update-12-for-exchange-server-2019-kb5011156-6a4e598a-876c-4ff1-9cfa-f7b87246f1d8) and [Exchange Server 2016 CU 23](https://support.microsoft.com/en-us/topic/cumulative-update-23-for-exchange-server-2016-kb5011155-98183ada-e4cd-465f-b201-69d40fb74678) on April 20, 2022. However, **this patch did not enable by default**. Microsoft didn’t release the patch-activating methods until August 09, 2022. So, we originally had the opportunity to demonstrate our attack at [Pwn2Own Vancouver 2021](https://www.zerodayinitiative.com/blog/2022/1/12/pwn2own-vancouver-2022-luanch). However, we dropped the idea quickly because our intention is not to earn bounties. We are here to [secure the world](https://devco.re/en/about/)! You can check the [Timeline](#Timeline) to know the detailed disclosure process.

# Idea

Since Microsoft blocked our Proxy-Related attacks in April 2021, I have been thinking about whether there is a way to bypass the mitigation. During that April patch, Microsoft enhanced the authentication part of CAS Frontend by requiring all HTTP requests that need a Kerberos Ticket to be authenticated first. This enhancement effectively mitigated the attack surface we proposed and stopped unauthenticated HTTP requests accessing the CAS Backend. So Exchange is safe now?

Of course not, and this article is to prove this! Since Microsoft only fixes the problematic code, we proposed several attacks and possible weaknesses in our [POC 2021](https://powerofcommunity.net/2021.htm) and [HITCON 2021](https://hitcon.org/2021/agenda/279d7810-e619-4dc3-9113-b11bad5277ec/) talks.

![](/assets/img/blog/20221019/1.png)

Maybe you have heard that our first prediction has already been made in recent [ProxyNotShell](https://doublepulsar.com/proxynotshell-the-story-of-the-claimed-zero-day-in-microsoft-exchange-5c63d963a9e9). The attack reuses the path confusion of ProxyShell but attaches a pre-known authentication instead. It’s solid but it looks it still needs a valid authentication (not sure, still haven’t time to dig into). However, we hinted there is another way not to fight with the auth-enhancement face-to-face during my talks. Now we can finally disclose it :)

Just in case you don’t know, I am a big fan of [Printer Bug](https://www.thehacker.recipes/ad/movement/mitm-and-coerced-authentications/ms-rprn) (kudos to [Lee Christensen](https://twitter.com/tifkin_), [Will Schroeder](https://twitter.com/harmj0y), and [Matt Nelson](https://twitter.com/enigma0x3) for their amazing talk at [DerbyCon 2018](https://www.slideshare.net/harmj0y/derbycon-the-unintended-risks-of-trusting-active-directory)). PrinterBug allows an attacker to coerce any domain-joined machine to initiate an SMB connection with its own Machine Account to the attacker via [MS-RPRN](https://do...