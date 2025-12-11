---
title: Three PCIe Encryption Weaknesses Expose PCIe 5.0+ Systems to Faulty Data Handling
url: https://thehackernews.com/2025/12/three-pcie-encryption-weaknesses-expose.html
source: The Hacker News
date: 2025-12-10
fetch_date: 2025-12-11T03:25:11.114316
---

# Three PCIe Encryption Weaknesses Expose PCIe 5.0+ Systems to Faulty Data Handling

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Three PCIe Encryption Weaknesses Expose PCIe 5.0+ Systems to Faulty Data Handling](https://thehackernews.com/2025/12/three-pcie-encryption-weaknesses-expose.html)

**Dec 10, 2025**Ravie LakshmananHardware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhy3f-oOC7MmSz2Ku0x9-ljdPbuoYceSrPAAqvibbB1WV5spRUhQDjoXmn5mL8TzgQj7GP6CzMRtG0Tm8OJW1qhylFL1uafxAMcmJG3n9n3kgC00yhRIsdmJYXWKco6SyOdONzvEb29HzxOOPtsNTH7aBVL0YgKFCX73q7_pn_UQ3x7b6hWibuoJb5EVYF1/s790-rw-e365/encryption.jpg)

Three security vulnerabilities have been disclosed in the Peripheral Component Interconnect Express (PCIe) Integrity and Data Encryption ([IDE](https://pcisig.com/PCI%20Express/ECN/Base/IntegrityandDataEncryption_A)) protocol specification that could expose a local attacker to serious risks.

The flaws impact PCIe Base Specification Revision 5.0 and onwards in the protocol mechanism introduced by the IDE Engineering Change Notice (ECN), according to the PCI Special Interest Group ([PCI-SIG](https://en.wikipedia.org/wiki/PCI-SIG)).

"This could potentially result in security exposure, including but not limited to, one or more of the following with the affected PCIe component(s), depending on the implementation: (i) information disclosure, (ii) escalation of privilege, or (iii) denial of service," the consortium [noted](https://pcisig.com/PCIeIDEStandardVulnerabilities).

PCIe is a widely used high-speed standard to connect hardware peripherals and components, including graphics cards, sound cards, Wi-Fi and Ethernet adapters, and storage devices, inside computers and servers. Introduced in PCIe 6.0, PCIe IDE is designed to secure data transfers through encryption and integrity protections.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

The [three IDE vulnerabilities](https://kb.cert.org/vuls/id/404544), discovered by Intel employees Arie Aharon, Makaram Raghunandan, Scott Constable, and Shalini Sharma, are listed below -

* **[CVE-2025-9612](https://nvd.nist.gov/vuln/detail/CVE-2025-9612)** (Forbidden IDE Reordering) – A missing integrity check on a receiving port may allow re-ordering of PCIe traffic, leading the receiver to process stale data.
* **[CVE-2025-9613](https://nvd.nist.gov/vuln/detail/CVE-2025-9613)** (Completion Timeout Redirection) – Incomplete flushing of a completion timeout may allow a receiver to accept incorrect data when an attacker injects a packet with a matching tag.
* **[CVE-2025-9614](https://nvd.nist.gov/vuln/detail/CVE-2025-9614)** (Delayed Posted Redirection) – Incomplete flushing or re-keying of an IDE stream may result in the receiver consuming stale, incorrect data packets.

PCI-SIG said that successful exploitation of the aforementioned vulnerabilities could undermine the confidentiality, integrity, and security objectives of IDE. However, the attacks hinge on obtaining physical or low-level access to the targeted computer's PCIe IDE interface, making them low-severity bugs (CVSS v3.1 score: 3.0/CVSS v4 score: 1.8).

"All three vulnerabilities potentially expose systems implementing IDE and Trusted Domain Interface Security Protocol (TDISP) to an adversary that can breach isolation between trusted execution environments," it said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

In an advisory released Tuesday, the CERT Coordination Center (CERT/CC) urged manufacturers to follow the updated PCIe 6.0 standard and apply the Erratum #1 guidance to their IDE implementations. [Intel](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01409.html) and [AMD](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7056.html) have published their own alerts, stating the issues impact the following products -

* Intel Xeon 6 Processors with P-cores
* Intel Xeon 6700P-B/6500P-B series SoC with P-Cores.
* AMD EPYC 9005 Series Processors
* AMD EPYC Embedded 9005 Series Processors

"End users should apply firmware updates provided by their system or component suppliers, especially in environments that rely on IDE to protect sensitive data," CERT/CC said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Integrity](https://thehackernews.com/search/label/Data%20Integrity)[encryption](https://thehackernews.com/search/label/encryption)[firmware](https://thehackernews.com/search/label/firmware)[hardware security](https://thehackernews.com/search/label/hardware%20security)[Trusted Computing](https://thehackernews.com/search/label/Trusted%20Computing)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![ThreatsDay Bulletin: Wi-Fi Hack, npm Worm, DeFi Theft, Phishing Blasts — and 15 More Stories](data:image/svg+xml;base64... "ThreatsDay Bulletin: Wi-Fi Hack, npm Worm, DeFi Theft, Phishing Blasts — and 15 More Stories")

ThreatsDay Bulletin: Wi-Fi Hack, npm Worm, DeFi Theft, Phishing Blasts — and 15 More Stories](https://thehackernews.com/2025/12/threatsday-bulletin-wi-fi-hack-npm-worm.html)

[![⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](data:...