---
title: 24,650 Internet-Exposed BMCs Disclose IPMI Password Hashes Before Login
url: https://thehackernews.com/2026/07/24650-internet-exposed-bmcs-disclose.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:26.881138
---

# 24,650 Internet-Exposed BMCs Disclose IPMI Password Hashes Before Login

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [24,650 Internet-Exposed BMCs Disclose IPMI Password Hashes Before Login](https://thehackernews.com/2026/07/24650-internet-exposed-bmcs-disclose.html)

**Ravie Lakshmanan**Jul 28, 2026Vulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIZDJmL5vHIaEgakZEwVC-O1KGBidMz7xrUS6MQmj0Nfqx4_WzGlwmz4amGxIwYa2PEJTKr5UsFwkh8lEOoFkjAVwTm38bgmbc_gDW2-__9MBpP5Z6cWQrIjFTe3tKTMEhD2lX3XyTrIe0T4mQDruecN3nCWqHUpkU5NpW5OIzZFy5la9RQnMCsmGkt-n8/s1700-e365/bmcs.jpg)

Cybersecurity researchers have sounded an alert after finding more than 36,000 Baseboard Management Controller (BMC) management interfaces exposing Intelligent Platform Management Interface (IPMI) protocol to the public internet.

Of the 36,872 internet-exposed server-management interfaces running IPMI, 24,650 have been found to disclose password-derived authentication hashes before login due to a vulnerability with the IPMI v2.0 specification itself, according to a [new report](https://lavahq.io/research/bmc-exposure-alert) Lava shared with The Hacker News. IPMI v2.0 was [introduced](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface#Version_history) in February 2024.

The issue in question is [CVE-2013-4786](https://nvd.nist.gov/vuln/detail/CVE-2013-4786) (CVSS score: 7.5), a high-severity information disclosure flaw that enables remote attackers to obtain password hashes for valid accounts and conduct offline password guessing attacks by obtaining the HMAC from an RMCP+ Authenticated Key-Exchange Protocol (RAKP) message response from a BMC.

Per an [advisory](https://www.dell.com/support/kbdoc/en-us/000222162/data-domain-ipmi-v2-0-password-hash-disclosure) released by Dell, "this is an inherent problem with the specification for IPMI v2.0," with the PC maker noting that there is no patch.

"More than 30% of the returned hashes were associated with passwords that could be recovered using common wordlists and predictable factory chassis-sticker formats," security researcher Michael Katchinskiy said. "The exposure also affected modern Supermicro and HPE servers operated by GPU providers, including systems that were still using factory-issued passwords."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

BMCs are specialized management processors embedded on a server's motherboard that control power, firmware, remote console access, operating system installation, and system recovery. They also act as a crucial component for remote data center automation and uptime to monitor hardware telemetry and facilitate mass deployment of firmware updates and BIOS configurations.

To bridge remote commands to the hardware, the BMC typically communicates using protocols like IPMI and Redfish. As highlighted by firmware security company Eclypsium in [late 2022](https://thehackernews.com/2022/12/new-bmc-supply-chain-vulnerabilities.html) and [early 2023](https://thehackernews.com/2023/02/additional-supply-chain-vulnerabilities.html), the privileged position enjoyed by BMCs can also make them ideal attack targets for bad actors looking to gain remote control and deploy persistent malware.

Because BMCs run completely independently of the host operating system, a mechanism known as Out-of-Band (OOB) management, an attacker who manages to successfully compromise an exposed BMC can sidestep traditional security controls, survive operating system reinstalls, and maintain access.

"In modern AI data centers, where the same bare-metal environment often hosts multiple tenants, a single exposed BMC can potentially place multiple organizations' workloads at risk through shared infrastructure or lateral movement, making this a significant blind spot in the infrastructure underpinning the AI data center boom," the Israeli company said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi30H9bvrCm9GTcnsYS1juCHvIP9GZNueh1kHoPM93UXh9DrPdpmzIzBXK3iHKyeZD3-Vt7sIEJf2CVCeGL5jrsxqD1FL0Y2b_TpWc227MFOCSG4Af8CNKyrCnQNdexDytZU_kMvvRBoFnZ08CJz9AG69xHODcpS2z00sJ6o-z4Fo0mRdkd8yHoEvgVso74/s1700-e365/bmc.png)

At the heart of the research is CVE-2013-4786, a 20-year-old weakness in IPMI 2.0, which an attacker can exploit to recover weak, reused, factory-set, or predictably formatted passwords.

"During the authentication process, the BMC can return a message response containing an HMAC-SHA1 authentication code calculated using the account password and session values known to the requester," Katchinskiy explained. "An unauthenticated remote party that can reach UDP port 623 can request this response and test password guesses offline. Unlike repeated online login attempts, the offline process does not require a new request to the BMC for every password candidate."

As of May 6, 2026, a search of the public internet for IPMI services exposed on UDP port 623 uncovered 36,872 unique hosts, of which more than 14,000 are located in the U.S. The remaining systems are concentrated in Germany, China, the Netherlands, and the U.K.

Further analysis has determined that nearly 25,000 exposed password-derived authentication materials before login, allowing offline credential cracking. Perhaps even more concerningly, a total of 6,240 BMCs returned authentication material for an empty username that matched a weak password candidate and another 2,340 BMCs returned authentication data for a named account such as ADMIN or root that matched a password from publicly available wordlists.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

In tests conducted by Lava, HPE iLO factory passwords were recoverable within a minute using modern GPU hardware, while Supermicro factor...