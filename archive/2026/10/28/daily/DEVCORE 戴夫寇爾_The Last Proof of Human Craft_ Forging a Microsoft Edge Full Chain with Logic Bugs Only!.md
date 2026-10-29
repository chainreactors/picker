---
title: The Last Proof of Human Craft: Forging a Microsoft Edge Full Chain with Logic Bugs Only!
url: https://devco.re/blog/2026/10/28/the-last-proof-of-human-craft-forging-a-microsoft-edge-full-chain-with-logic-bugs-only-en/
source: DEVCORE 戴夫寇爾
date: 2026-10-28
fetch_date: 2026-10-29T07:51:55.803594
---

# The Last Proof of Human Craft: Forging a Microsoft Edge Full Chain with Logic Bugs Only!

[![](/images/logo.svg)](/en/)

* Services

  [## Red Team Assessment

  Simulation of real-world attacks to identify vulnerabilities and achieve objectives without disrupting business operations.](/en/services/red-team/)
  [## Offensive Product Security Research

  Assess high-risk vulnerabilities across hardware, firmware, and software from an attacker’s perspective—strengthening secure coding and hardening products against advanced threats.](/en/services/opsr/)
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
  [## Offensive Product Security Research](/en/services/opsr/)
  [## Penetration Testing](/en/services/penetration-test/)
  [## Security Consulting](/en/services/security-consulting/)
  [## Security Training](/en/services/security-training/)
  [## OffSec Advanced Training](https://training.devco.re/)
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

[#Pwn2Own](/en/blog/tag/Pwn2Own/) [#Microsoft Edge](/en/blog/tag/Microsoft%20Edge/) [#UXSS](/en/blog/tag/UXSS/) [#RCE](/en/blog/tag/RCE/) [#Vulnerability](/en/blog/tag/Vulnerability/) [#Windows](/en/blog/tag/Windows/)

# The Last Proof of Human Craft: Forging a Microsoft Edge Full Chain with Logic Bugs Only!

[Orange Tsai](/en/blog/author/orange)
2026-10-28

![](https://devco.re/assets/img/blog/20261028/cover.jpg)

---

I think I should still dump some of my work once in a while, even though it feels like fewer and fewer people actually sit down and read articles these days (or maybe now they all leave it to their agents XD). Anyway, this is what I built for Pwn2Own Berlin 2026 — a completely handmade, logic-only Microsoft Edge Full Chain, with no memory corruption, and no AI at all! 🔥

> Confirmed! Orange Tsai (@orange\_8361) of DEVCORE Research Team (@d3vc0r3) chained 4 logic bugs to achieve a sandbox escape on Microsoft Edge, earning $175,000 and 17.5 Master of Pwn points. Full win! #Pwn2Own #P2OBerlin https://t.co/vJaIpGG4cD
>
> — TrendAI Zero Day Initiative (@thezdi) [May 14, 2026](https://x.com/thezdi/status/2054868495888777266?ref_src=twsrc%5Etfw)

The whole chain is made up of five bugs and two Windows features. I have also shared the whole bug-hunting and chaining process at this year’s HITCON and Hexacon, plus some fun stories along the way. You can check [the slides here](https://github.com/orangetw/My-Presentation-Slides/blob/main/data/2026-The-Last-Proof-of-Human-Craft-en.pdf)!

Also, maybe everyone thinks LLMs can already pwn everything in the AI era, so something made entirely by hand somehow feels a bit more precious. That might also be why this chain was nominated for this year’s Pwnie Awards and won the Epic Achievement award. 🎉

![pwnie-award-2026](/assets/img/blog/20261028/cover.jpg)

## Let’s Navigate!

So where do we start with a logic-only full chain? Well, since it’s a “browser,” let’s start by looking at how “browsing” (or what Chromium calls “navigation”) works. I won’t go into too much detail in this post, because I think in this era, you can just ask your agents to fill in the details :)

But I’d still recommend reading “[Life of a Navigation](https://docs.google.com/presentation/d/1YVqDmbXI0cllpfXD7TuewiexDNZYfwk6fRdmoXJbBlM/edit)” from Chrome University if you want to get the full picture.

### The Forgotten Navigation Throttles

While I was walking through the Chromium Navigation flow, something called “Navigation Throttles” caught my attention. They live in the Browser Process, and intercept all navigation requests initiated by either the Browser or the Renderer. Maybe it’s easy to say this in hindsight, but out of the 3,000+ CVEs Google Chrome has fixed over the past five years, there are only fewer than 20 related to them. So I guess this is also a corner not too many people pay attention to.

Anyway, I started digging into the Navigation Throttles, and checked how Google Chrome and Microsoft Edge implemented them. And while going through the code, I found that Edge has a throttle called `EdgeCAGuidanceNavigationThrottle` for its enterprise Entra ID feature (the `CA` here stands for [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)). The purpose of this throttle is to guide users to the right User Profile when Edge detects them signing in with ...