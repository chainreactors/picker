---
title: China-Aligned Hackers Hijack Sogou Input Method DNS Requests to Deploy DarkVigil Backdoor
url: https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:13.209544
---

# China-Aligned Hackers Hijack Sogou Input Method DNS Requests to Deploy DarkVigil Backdoor

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [China-Aligned Hackers Hijack Sogou Input Method DNS Requests to Deploy DarkVigil Backdoor](https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html)

**Ravie Lakshmanan**Nov 04, 2026Vulnerability / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMawvNNOvRYRm-k7ii9yDdw214v4kwQ7h5fAfOaUVkvMetNwArral8qumlObtaftjOcBsibL9vkqM1UT0-9l9jYPjj3M3C9NcPfg5pdIuENUfdKlK7lyseCS30AVhgLLs6a-2fdXlSDymSVeyIziO7IC13HFCaOf1v4sjbgmkeKfewWNsbTJCJ0WR2zLBZ/s1700-nu-rw-lo-l85-e365/key.jpg)

A China-aligned threat actor known as **SlippyNunchucks** has been attributed to a Domain Name System (DNS) hijacking operation abusing insecure HTTP communications in Windows versions of Sogou Input Method as part of a surveillance campaign designed to deploy an implant called DarkVigil (aka FDMTP).

The campaign, observed starting July 1, 2026, is assessed to have targeted organizations and Chinese-speaking individuals in Hong Kong, Thailand, Japan, Vietnam, Oman, and Sri Lanka, according to ESET.

"DarkVigil implants are typically deployed through popular Chinese applications," ESET researcher Anh Ho [said](https://www.welivesecurity.com/en/eset-research/slippynunchucks-hijacks-sogou-input-methods-brand-promotion-mechanism-to-distribute-malware/) in a report shared with The Hacker News. "By abusing these applications, the SlippyNunchucks threat actor has been able to reach Chinese-speaking users across Asia and Europe."

Some of the applications abused by the adversary include Sogou Input Method, QuickFox, QingTalk, MiYunChat, SoftCam, and tawk.to.

Active since at least September 15, 2023, SlippyNunchucks is known for targeting organizations and Chinese-speaking individuals across South and East Asia. These attacks lead to the deployment of a modular .NET framework that includes DarkVigil and a set of over 20 plugins.

Although the use of the backdoor has been [previously linked to Mustang Panda](https://thehackernews.com/2024/09/mustang-panda-deploys-advanced-malware.html), ESET said it found no tactical overlaps between the threat actor and DarkVigil-related activity in its telemetry, prompting it to classify it as a distinct intrusion set.

Earlier this August, Fortinet's FortiGuard Incident Response Team [detailed](https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html) the threat actor's supply chain compromise of the QuickFox VPN and network acceleration tool to deliver DarkVigil.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

According to the Slovakian cybersecurity company, the adversary shifted to exploiting Sogou Input Method, a popular Chinese-language input method editor developed by Tencent, as a delivery vector three days after QuickFox released a clean version of its program.

Specifically, the attack involves hijacking the app's branded vocabulary promotion mechanism to serve a malicious configuration, which ultimately paves the way for the deployment of the malware via SGTool.exe, a legitimate Sogou Input Method component that functions as a multi-purpose task dispatcher.

In a clean environment, the executable sends an HTTP request to the "config.pinyin.sogou[.]com/api/brandScd/getBrandScd.php" endpoint to fetch a configuration. But in the attack discovered by ESET, the DNS resolution of the domain is tampered with to resolve it to one of the two staging servers -

* [47.239.250[.]102](https://www.virustotal.com/gui/ip-address/47.239.250.102/) (sogou-cdn[.]com)
* [47.237.122[.]175](https://www.virustotal.com/gui/ip-address/47.237.122.175/) (dev.soft-png-cdn.com)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijtfAuyTeWjxnqp8DhpquRGRnmlGSrGVwuscP8Yqt16QynD8tcG90zmKM3On-KLzCbyB_9uYYIQ98-QC8HKUDwKW0NvsLWlIN-_FhxtPrtdGWfX6eUDsl11rYOwZLVEc5O4wfC4Gqi6JA9DgtAVu9eeABf5l0oLFQ9Guzai_dUFBDtlY3bFiM5HHPetlAF/s1700-nu-rw-lo-l85-e365/so.png)

The consequence of this DNS hijacking was that HTTP requests to the "getBrandScd.php" endpoint were routed to one of the staging servers, which then responded with a malicious configuration. The configuration, for its part, instructs the binary to download two additional payloads from "sogou-cdn[.]com" and launch the malware via DLL sideloading -

* A legitimate Adobe executable ("biz\_helper.exe")
* A rogue DLL ("libcef.dll") containing DarkVigil

DarkVigil is notable for its use of Duplex Message Transport Protocol (DMTP) for command-and-control (C2), allowing the client to execute and orchestrate plugins received from an attacker-controlled server to facilitate persistence or data collection.

Following responsible disclosure, Tencent addressed the vulnerability (CVE-2026-120422) in version 16.10, released on October 29, 2026, by migrating the affected HTTP requests to HTTPS.

SlippyNunchucks is suspected to operate keeping the interests of the Chinese government in mind, with ESET describing it as a nation-state surveillance effort.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"Although SlippyNunchucks targets organizations and individuals across multiple sectors, we discovered significant surveillance activity against an organization operating Chinese-language online betting platforms in Sri Lanka, Hong Kong, and the Philippines," ESET said.

"The targeting of this organization is notable given China's restrictions on gambling, including criminal penalties for operating gambling businesses and organizing Chinese citizens to gamble abroad."

This is not the first time China-nexus threat actors have [weaponized](https://thehackernews.com/2023/08/encryption-flaws-in-popular-chinese.html) the Sogou Input Method as an entry point for malware distribution. In September 2026, Gen Digital said a [now-patched vulnerability](https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou) in the input method editor (CVE-2026-51990) was exploited by [UNC35...