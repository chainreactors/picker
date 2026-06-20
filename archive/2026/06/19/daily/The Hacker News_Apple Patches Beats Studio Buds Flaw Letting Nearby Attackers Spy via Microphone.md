---
title: Apple Patches Beats Studio Buds Flaw Letting Nearby Attackers Spy via Microphone
url: https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html
source: The Hacker News
date: 2026-06-19
fetch_date: 2026-06-20T06:14:43.499709
---

# Apple Patches Beats Studio Buds Flaw Letting Nearby Attackers Spy via Microphone

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Apple Patches Beats Studio Buds Flaw Letting Nearby Attackers Spy via Microphone](https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html)

**Ravie Lakshmanan**Jun 19, 2026Mobile Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvlr0i44MWKmuHJKLS1V3uKSMse7tVsRFBTpyD1VGLaRZy24qq4bIb6K3Db1s0eKtuh3TkLCYFWn6eJ-uEkVnkO9CbPHHUlD3j8Z-SEFFr9A1X6ndd-fQd6UKTAyXO0DhUI2ZTe1sc4Eq7NLoGUyjQUkKmhHp99QGz3WTcFAnucAnfiioLDFiGaTbI8Wvx/s1700-e365/apple.jpg)

Apple has updated its Beats Studio Buds wireless earbuds to patch a high-severity vulnerability that could be exploited by nearby hackers to eavesdrop on users.

The vulnerability, tracked as **[CVE-2025-20701](https://support.apple.com/en-us/127557)** (CVSS score: 8.8), refers to a case of incorrect authorization impacting the Airoha Bluetooth audio SDK that makes it possible to pair a Bluetooth audio device without user consent.

[Successful exploitation](https://www.sentinelone.com/vulnerability-database/cve-2025-20701/) of the flaw could lead to remote escalation of privilege without requiring any additional execution privileges or user interaction. The issue has been addressed in Beats Firmware Update 1B211.

"An attacker within Bluetooth range may be able to listen through the microphone of a device which is not yet paired and actively seeking pair requests," Apple said in an advisory released this week.

Details of the vulnerability [first emerged](https://thehackernews.com/2025/06/weekly-recap-airline-hacks-citrix-0-day.html#:~:text=Vulnerabilities%20in%20Airoha%20SoCs) in June 2025 when ERNW GmbH researchers Dennis Heinze and Frieder Steinmetz [flagged it alongside two other flaws](https://www.airoha.com/product-security-bulletin/2025) in Airoha SoCs (CVE-2025-20700 and CVE-2025-20702) at the TROOPERS security conference in Germany. Similar patches were [released](https://www.jabra.com/support/release-notes/release-note-jabra-link-390#2.5.0) by Jabra in December 2025.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"In most cases, these vulnerabilities allow attackers to fully take over the headphones via Bluetooth. No authentication or pairing is required," the researchers noted at the time. "The vulnerabilities can be triggered via Bluetooth BR/EDR or Bluetooth Low Energy (BLE). Being in Bluetooth range is the only precondition. It is possible to read and write the device’s RAM and flash."

"These capabilities also allow attackers to hijack established trust relationships with other devices, such as the phone paired to the headphones. These capabilities allow for multiple attack scenarios."

### New Unpatchable Exploit Discovered in Apple's A12 and A13 Chips

The disclosure comes as Paradigm Shift disclosed a novel iPhone [SecureROM](https://theapplewiki.com/wiki/Bootrom) (aka BootROM) vulnerability impacting Apple's A12 and A13 chips, in addition to a proof-of-concept (PoC) exploit codenamed [usbliter8](https://github.com/prdgmshift/usbliter8).

"The exploit leverages both a hardware bug in the USB controller and a specific configuration flaw present in the device firmware," the European cybersecurity company [said](https://ps.tc/pages/blog-usbliter8.html). "As these vulnerabilities reside in immutable code, affected users should be aware that migrating to newer hardware remains the most effective mitigation."

At a high level, the exploit works by leveraging a flaw in the USB controller built into Apple SoCs. The controller uses a memory buffer to store SETUP and OUT packets transmitted at the start of data transfer. The research found that it's possible to trigger a [buffer underflow primitive](https://cwe.mitre.org/data/definitions/124.html) by taking advantage of the fact that the controller also accepts smaller packets, effectively allowing for malicious code injection and execution under certain conditions.

The problem, Paradigm Shift noted, is likely rooted in the USB controller hardware itself, not in Apple's software. The A11 chip is not susceptible to the vulnerability, while A12 and A13 are confirmed to be susceptible.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"The difference is that the A11 USB driver manually resets the DMA address to its initial value after receiving each packet," the company said. "On A12 and A13, USB DART is configured in bypass mode, allowing us to overwrite SRAM data freely. In contrast, A14 and later generations appear to configure the DART correctly in SecureROM, making the vulnerability unexploitable."

The usbliter8 exploit is comparable to [checkm8](https://thehackernews.com/2020/05/iphone-ios-jailbreak-tools.html), the publicly known BootROM exploit of this kind that impacted all iOS devices ranging from iPhone 4s (A5 chip) to iPhone 8 and iPhone X (A11 chip).

"The usbliter8 exploit demonstrates that even on more recent SecureROM generations, including those protected by [Pointer Authentication](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication), subtle hardware bugs can still be leveraged to achieve full code execution and break the chain of trust," Paradigm Shift said.

"The security of the BootROM is critical: vulnerabilities at this level can compromise the integrity of the entire device. Although usbliter8 doesn't affect SEP itself, it opens up wider attack vectors to compromise the Secure Enclave."

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
[**Share on ...