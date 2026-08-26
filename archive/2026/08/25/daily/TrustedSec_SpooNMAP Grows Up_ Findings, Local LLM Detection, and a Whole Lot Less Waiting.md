---
title: SpooNMAP Grows Up: Findings, Local LLM Detection, and a Whole Lot Less Waiting
url: https://trustedsec.com/blog/spoonmap-grows-up-findings-local-llm-detection-and-a-whole-lot-less-waiting
source: TrustedSec
date: 2026-08-25
fetch_date: 2026-08-26T03:06:50.062830
---

# SpooNMAP Grows Up: Findings, Local LLM Detection, and a Whole Lot Less Waiting

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [SpooNMAP Grows Up: Findings, Local LLM Detection, and a Whole Lot Less Waiting](https://trustedsec.com/blog/spoonmap-grows-up-findings-local-llm-detection-and-a-whole-lot-less-waiting)

August 25, 2026

# SpooNMAP Grows Up: Findings, Local LLM Detection, and a Whole Lot Less Waiting

Written by
Larry Spohn

Penetration Testing
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/SpooNMAPGrowsUp_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1787167934&s=9968f6f847c1074c0aba91922e8143cb)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#fdc28e889f97989e89c0be95989e96d8cfcd928889d8cfcd8995948ed8cfcd9c8f89949e9198d8cfcd9b8f9290d8cfcda98f888e899899ae989ed8cfccdb9c908dc69f929984c0ae8d9292b3b0bcadd8cfcdba8f928a8ed8cfcda88dd8cebcd8cfcdbb94939994939a8ed8cfbed8cfcdb1929e9c91d8cfcdb1b1b0d8cfcdb99889989e89949293d8cfbed8cfcd9c9399d8cfcd9cd8cfcdaa95929198d8cfcdb19289d8cfcdb1988e8ed8cfcdaa9c948994939ad8cebcd8cfcd9589898d8ed8cebcd8cfbbd8cfbb898f888e8998998e989ed39e9290d8cfbb9f91929ad8cfbb8e8d929293909c8dd09a8f928a8ed0888dd09b94939994939a8ed091929e9c91d0919190d0999889989e89949293d09c9399d09cd08a95929198d0919289d091988e8ed08a9c948994939a "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspoonmap-grows-up-findings-local-llm-detection-and-a-whole-lot-less-waiting "Share on Facebook")
* [Share on X](https://twitter.com/share?text=SpooNMAP%20Grows%20Up%3A%20Findings%2C%20Local%20LLM%20Detection%2C%20and%20a%20Whole%20Lot%20Less%20Waiting%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspoonmap-grows-up-findings-local-llm-detection-and-a-whole-lot-less-waiting "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspoonmap-grows-up-findings-local-llm-detection-and-a-whole-lot-less-waiting&mini=true "Share on LinkedIn")

A while back, we released [SpooNMAP](https://trustedsec.com/blog/get-to-hacking-massively-faster-the-release-of-spoonmap). A little wrapper that lets masscan do what masscan does best (find open ports at ludicrous speed) and then hands the results to Nmap for the banner grabbing it does best. The whole point was to get you hacking faster, and it worked. People used it, and it was great. Then vibe coding came along, which prompted a lot of "You know what would make this better?" kinds of ideas to work through.

This release is a big one. SpooNMAP used to stop at "here are your open ports." Now, it keeps going and tells you which of those ports are *actually interesting*, and it does it faster than before!

### **From Port Scanner to Findings Machine**

SpooNMAP now runs context-aware NSE scripts against the services it finds and writes you a real, severity-sorted findings report. Turn on script scanning and you get `findings.txt`, `findings.md`, and `findings.json`, each finding tagged CRITICAL/HIGH/MEDIUM/LOW with a copy-paste command to reproduce it.

Out of the box, it flags anonymous FTP, weak SSH ciphers, SMBv1, NFS exports, exposed MSSQL instances, weak RDP encryption, expired certificates, LDAP without signing or channel binding, anonymous LDAP enumeration, default SNMP community strings, unauthenticated VNC, and a pile of others. Internal and external scans get different script sets, because the things worth checking from the outside aren't the same as the things worth checking once you're on the inside.

We also bundled **15 custom NSE scripts** for stuff the stock library doesn't cover, including RAKP hash capture from IPMI/BMC interfaces (drop it straight into Hashcat mode 7300), DameWare detection (CVE-2019-3980), cups-browsed (CVE-2024-47176), and proper LDAP signing / channel-binding checks.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/SpooNMAPGrowsUp_Larry/Fig01_Larry_SpooNMapGrowsUp.png?w=320&q=90&auto=format&fit=max&dm=1787167869&s=dbfff185fddc64e3c5926bf1d346fbd7)

### **Yes, it Hunts for Exposed Local LLMs**

Everybody and their startup is running a local LLM now, and half of them are sitting wide open on the network with no authentication. SpooNMAP now looks for that. There's a dedicated Local LLM scan category and detection for Ollama, OpenAI-compatible endpoints, Gradio, and KoboldCpp, flagged HIGH externally and MEDIUM internally, complete with a proof-of-concept curl so you can prove it talks back. Free model access is a good finding. Free model access on someone's DMZ is a *great* finding.

### **Pick What You Actually Want to Scan**

Instead of memorizing port lists, you now choose from service categories at the prompt. The new Containers & Debuggers category is one of my favorites: Docker APIs, kubelet, Node.js inspector, Delve, JDWP, and friends. All of the "why is this exposed?" po...