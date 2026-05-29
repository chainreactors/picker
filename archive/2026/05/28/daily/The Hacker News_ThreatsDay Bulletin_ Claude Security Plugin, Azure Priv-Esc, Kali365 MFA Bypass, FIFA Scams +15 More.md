---
title: ThreatsDay Bulletin: Claude Security Plugin, Azure Priv-Esc, Kali365 MFA Bypass, FIFA Scams +15 More
url: https://thehackernews.com/2026/05/threatsday-bulletin-claude-security.html
source: The Hacker News
date: 2026-05-28
fetch_date: 2026-05-29T06:06:36.810541
---

# ThreatsDay Bulletin: Claude Security Plugin, Azure Priv-Esc, Kali365 MFA Bypass, FIFA Scams +15 More

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [ThreatsDay Bulletin: Claude Security Plugin, Azure Priv-Esc, Kali365 MFA Bypass, FIFA Scams +15 More](https://thehackernews.com/2026/05/threatsday-bulletin-claude-security.html)

**Ravie Lakshmanan**May 28, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBnLTRREuP8t8AoMRlakMDVRNoOYCA18IuBTWxA_nms12GdQaSfaU1kgpLSrgUvFFH1goJ_-NOIerDAnZxlD86Oafg_b6QdecLrT4UJdb3_qfmgtxdjrhF8GioeuEZbyZBTVL4cXUcpWqZujpLoI4zBm9y7XvFUjYR5cjF0GmmU_TXlmX0W7zsxlcvV9mW/s1700-e365/tbb.jpg)

Every time you think the industry has finally stopped doing some reckless, low-effort crap, somebody spins up a fresh box full of sketchy loaders, fake installers, recycled social-engineering bait, and enough exposed infrastructure to make you wonder if prod is just a public beta now - meanwhile some researcher casually drops a technique that turns a "minor" foothold into total account compromise because apparently six digits and blind trust were all that stood between your vault and getting absolutely pwned. Cool. Great. Love that for us.

Then there's the supply chain mess... signed binaries, poisoned updates, legit tooling getting hijacked like it's still 2017, plus a few reports this week that feel less like advanced tradecraft and more like watching skiddies discover low-hanging fruit with enterprise branding slapped on top. The weird part isn't that it works. The weird part is how damn easy it still is.

Anyway. Grab caffeine. Let's get into it.

1. Massive regional C2 footprint

   [More than 1.3K C2 Servers Discovered in the Middle East](https://hunt.io/blog/middle-east-malicious-infrastructure-report)

   Hunt.io said it identified more than 1,350 command-and-control (C2) servers across 98 Middle East infrastructure providers over the past three months, between February 1 and May 1, 2026. "C2 infrastructure dominates malicious activity (~96.8%), far exceeding phishing infrastructure (~0.5%) and publicly reported IOCs (~0.5%), while malicious open directories account for the remaining ~2.2% of observed artifacts," it [said](https://hunt.io/blog/middle-east-malicious-infrastructure-report). "Saudi Arabia's STC (Saudi Telecom Company) hosts 981 C2 servers, representing 72.4% of all detected C2 infrastructure in the region. IoT-focused botnets (Hajime, Mozi, and Mirai) combined with offensive frameworks (Tactical RMM, Cobalt Strike, Sliver) represent the dominant malware families operating across Middle Eastern infrastructure."
2. AKS privilege escalation flaw

   [Microsoft Patches Azure Backup for AKS Privilege Escalation Bug](https://olearysec.com/research/azure-backup-aks-silent-patch/)

   Microsoft is said to have silently fixed a privilege escalation flaw in Azure Backup for AKS that allowed a user with only the "Backup Contributor" Azure role (zero Kubernetes permissions) to gain cluster-admin on any AKS cluster, per [security researcher Justin O'Leary](https://olearysec.com/research/azure-backup-aks-silent-patch/). The vulnerability, which does not have a CVE, carries a CVSS score of 9.9. While Microsoft rejected the vulnerability report as "AI-generated content," it appears to have been patched since, and additional validation checks were enforced that did not exist in March 2026.
3. Cybercrime operator jailed

   [Romanian National Sentenced to Prison for U.S. Cyber Attacks](https://www.justice.gov/opa/pr/romanian-national-sentenced-selling-access-networks-oregon-state-government-office-and-other)

   A 46-year-old Romanian national found guilty of breaking into an Oregon state government office in 2021 and other cyber attacks across the U.S. has been sentenced to 56 months in prison. Catalin Dragomir [pleaded guilty](https://www.justice.gov/opa/pr/romanian-national-pleads-guilty-selling-access-networks-oregon-state-government-office-and) to one count of aggravated identity theft and one count of obtaining information from a protected computer in February. Dragomir was arrested in Romania in November 2024 and extradited to the U.S. in January 2025 to face charges. Dragomir "sold access to a computer on the network of an Oregon state government office after obtaining unauthorized access to it in June of 2021," the Justice Department [said](https://www.justice.gov/opa/pr/romanian-national-sentenced-selling-access-networks-oregon-state-government-office-and-other). "During the sale, Dragomir provided the prospective buyer with samples of personal identifying information from the computer. He also sold access to the computer networks of numerous other victims in the United States, causing losses of at least $250,000."
4. DAEMON Tools added to KEV

   [CISA Adds DAEMON Tools Supply Chain Incident to KEV Catalog](https://www.cisa.gov/news-events/alerts/2026/05/27/cisa-adds-three-known-exploited-vulnerabilities-catalog)

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [added](https://www.cisa.gov/news-events/alerts/2026/05/27/cisa-adds-three-known-exploited-vulnerabilities-catalog) the [supply chain attack targeting DAEMON Tools software](https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html) to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply necessary fixes by May 30, 2026. The incident is now being tracked under the identifier [CVE-2026-8398](https://www.cve.org/CVERecord?id=CVE-2026-8398) (CVSS v4 score: 9.3). "Attackers gained unauthorized access to the vendor's (AVB Disc Soft) build or distribution infrastructure and trojanized three binaries: DTHelper.exe, DiscSoftBusServiceLite.exe, and DTShellHlp.exe," according to the description of the CVE. "These files were digitally signed with the legitimate AVB Disc Soft code-signing certificate, allowing the malicious installers to appear trustworthy and bypass signature-based detection."
5. Apple unveils PQC code

   [Apple Open-Sourc...