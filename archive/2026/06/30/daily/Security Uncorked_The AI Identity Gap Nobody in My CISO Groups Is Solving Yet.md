---
title: The AI Identity Gap Nobody in My CISO Groups Is Solving Yet
url: https://securityuncorked.com/2026/06/the-ai-identity-gap-nobody-in-my-ciso-groups-is-solving-yet/
source: Security Uncorked
date: 2026-06-30
fetch_date: 2026-07-01T06:23:21.643806
---

# The AI Identity Gap Nobody in My CISO Groups Is Solving Yet

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)* ···

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)* ···

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)

![](https://securityuncorked.com/wordpress/wp-content/uploads/2026/06/2026-06-SU-Blog-AI-Identity-GapSPIFFE-1500x350.png)

[Next
FortiBleed: What Security Teams Need to Know (and Why This Story Is Bigger Than Fortinet)](https://securityuncorked.com/2026/06/fortibleed-what-security-teams-need-to-know-and-why-this-story-is-bigger-than-fortinet/)

[AI](https://securityuncorked.com/category/ai/), [Identity](https://securityuncorked.com/category/identity/)

# The AI Identity Gap Nobody in My CISO Groups Is Solving Yet

12 hours ago

8 min read

[Add comment](https://securityuncorked.com/2026/06/the-ai-identity-gap-nobody-in-my-ciso-groups-is-solving-yet/#respond) Watch LaterRemove Cinema Mode

Machine identities now outnumber human identities in the enterprise 109 to 1. That was one in a long list of surprising things I recently learned. Here we look at machine IDs, the secret zero conundrum, SPIFFE, and more.

Machine identities now outnumber human identities in the enterprise 109 to 1. That was one in a long list of surprising things I recently learned, and something almost all enterprises are struggling with. The rest of them have the same problem, they just lack enough visibility (or self-awareness) to know it’s a problem.

I’m in several CISO chat and message groups on various platforms. They’re ad-hoc, just friends swapping war stories, trading tricks, and sharing both wins and frustrations of CISO-ing in today’s climate.

***Wrangling shadow AI and AI agent identity in general has been at the top of most discussions of late***, so I paid extra attention when I had the opportunity to sit down with [Uzi Ailon](https://www.linkedin.com/in/uzi-ailon-329588/). He’s the VP of Machine Identity Solutions at CyberArk, now part of Palo Alto Networks, and he’s been eyeballs deep in solving the challenges of machine and non-human identities for years.

I know next to nothing about the identity space of cybersecurity, at least compared to Uzi. So I’m sharing a few interesting things I learned talking to him, and a few related alarming stats out of the [Verizon 2026 DBIR](https://www.verizon.com/business/resources/reports/dbir) and CybarArk/Palo Alto Networks [2026 Identity Security Landscape Report](https://www.paloaltonetworks.com/idira/identity-security-landscape-report?utm_source=google-panw_inhouse-discovery-amer-idnt-idira&utm_medium=paid_search&utm_campaign=google-idnt-idira-amer-multi-discovery-en-nonbrand-phr-t1-Threat_Intel&utm_content=701Ki000000p3xZ&utm_term=cyber%20threat%20landscape%20report&cq_plac=&cq_net=g&gclsrc=aw.ds&gad_source=1&gad_campaignid=23835726465&gbraid=0AAAAADHVeKnHG8KssZ1cW0AQnb1cgsmoN&gclid=CjwKCAjwt7XQBhBkEiwAtStpp5PzawXlDcgSF2FPvq9fuLuZBMJoWBJjcLcjqcWHps-7U97L22_xrxoCQTgQAvD_BwE).

## What “Machine Identity” Encompasses

When we say “machine identity”, we mean ***anything that isn’t a human that needs access to systems, data, or other resources.*** That includes:

* **Service accounts** — the workhorses of enterprise IT, often shared, rarely rotated, and almost never deprovisioned, because no one knows what they’re for, who added them, or when
* **API keys** — the credentials that let applications talk to each other, frequently hardcoded into source code (although they shouldn’t be)
* **OAuth tokens** — short-lived (in theory) authorization tokens; in practice, often long-lived and forgotten
* **Certificates** — TLS/SSL and client certs that authenticate systems and services
* **Workload identities** — containers, microservices, and cloud functions that spin up, do a job, and spin down
* **CI/CD pipeline credentials** — the secrets baked into your build and deployment automation
* **AI agents** — autonomous or semi-autonomous software that reasons, makes decisions, and takes actions on behalf of users or other systems; every agent is its own identity
* **Bots and RPA** (robotic process automation) — scripted automation that logs in and acts like a user, but isn’t one
* **IoT and OT devices** — sensors, controllers, and operational technology endpoints that authenticate to networks and management systems
* **SaaS integration tokens** — the credentials connecting your third-party apps to each other (think: Slack to Salesforce, Klue to Salesforce…)
* **SSH keys —** often generated by developers, rarely tracked, almost never audited

## Secret Zero

***I am extremely embarrassed*** to say this phrase was new to me. It describes the complication of giving a machine/workload/AI agent its first credential… which itself requires that credential ‘live’ somewhere.

***Secret zero is the original boot...