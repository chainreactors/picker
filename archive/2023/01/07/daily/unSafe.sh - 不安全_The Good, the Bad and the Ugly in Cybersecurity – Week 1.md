---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 1
url: https://buaq.net/go-144498.html
source: unSafe.sh - 不安全
date: 2023-01-07
fetch_date: 2025-10-04T03:13:34.880681
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 1

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c1e42d8f9ab858722993e6d7d2b43df9.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 1

The GoodIt’s been a busy start to the new year for privacy regulators, who have hit both Meta (aka
*2023-1-6 22:0:57
Author: [www.sentinelone.com(查看原文)](/jump-144498.htm)
阅读量:29
收藏*

---

## The Good

It’s been a busy start to the new year for privacy regulators, who have hit both Meta (*aka* Facebook) and Apple with new fines.

Apple has been given an $8 million penalty by France’s [CNIL](https://www.cnil.fr/fr/identifiant-publicitaire-sanction-de-8-millions-deuros-lencontre-de-apple-distribution-international) for failing to obtain consent from iOS 14.6 users relating to identifiers used to present targeted ads. Meta, which had just received a fine of $170 million from the CNIL [a few weeks ago](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-52-3/), now faces a further whopping $410 million (€390 million) fine from Ireland’s Data Protection Commission ([DPC](https://www.dataprotection.ie/en/news-media/data-protection-commission-announces-conclusion-two-inquiries-meta-ireland)).

![](https://www.sentinelone.com/wp-content/uploads/2023/01/meta-scaled.jpg)

The DPC fined Meta Ireland €210 million for breaches of the [GDPR](https://www.sentinelone.com/blog/gdpr-turns-two-has-anything-really-changed/) relating to its Facebook service and €180 million for breaches in relation to Instagram. Both relate to complaints that users were forced to consent to personalized ads in order to use the offered services.

In better news for Meta and users of the company’s WhatsApp instant messaging service, this week saw WhatsApp roll out [support for proxy servers](https://faq.whatsapp.com/520504143274092/?cms_platform=web). This allows users to connect to each other and maintain end-to-end encrypted chats even if authorities block WhatsApp’s own servers, as Iranian authorities did back in September in the wake of civil unrest.

## The Bad

No sooner had we noted that supply chain attacks via public code repositories were likely to be an increasingly common feature of the [2023 threat landscape](https://www.sentinelone.com/blog/sentinelones-cybersecurity-predictions-2023-whats-next/) than a threat actor ran a dependency confusion attack against the PyTorch package on PyPI.

Dependency confusion attacks are different from the more common typosquatting attacks that we’ve seen used against shared repos recently like [CrateDepression](https://www.sentinelone.com/labs/cratedepression-rust-supply-chain-attack-infects-cloud-ci-pipelines-with-go-malware/) and [pymafka](https://www.sentinelone.com/labs/use-of-obfuscated-beacons-in-pymafka-supply-chain-attack-signals-a-new-trend-in-macos-attack-ttps/). The technique takes advantage of the fact that some packages have dependencies that are hosted on private servers. However, by default, package managers that handle a client’s request for dependencies search the public code registry first for instances of the dependency. That means if the dependency package’s name is available on the public registry, an attacker can upload a malicious package to the registry and essentially intercept the dependency request from the client when users build it on their local machines.

An individual, who subsequently [claimed](https://twitter.com/Ax_Sharma/status/1609586774204116994?s=20&t=y0MmgN8hOxarnusTx6uf3A) to be a ‘researcher’, uploaded a [malicious public version](https://medium.com/checkmarx-security/py-torch-a-leading-ml-framework-was-poisoned-with-malicious-dependency-e30f88242964) of the privately-hosted torchtriton package used by PyTorch. Users that built PyTorch between December 25th and December 30th received the fake torchtriton dependency. The malware was almost identical to the legitimate torchtriton save for the addition of a malicious binary at `./triton/runtime/triton`  and code to ensure that it was executed. The triton executable collects and exfiltrates a variety of sensitive data from the victim’s machine to a remote URL including:

* Nameservers from `/etc/resolv.conf`
* Hostname from `gethostname()`
* Current username
* Current working directory
* Environment variables
* `/etc/hosts`
* `/etc/passwd`
* First 1,000 files in `$HOME`
* `$HOME/.gitconfig`
* `$HOME/.ssh/`

The malicious package has since been removed and replaced with a stub to prevent further attempts at exploiting the same trick. However, dependency confusion attacks are possible wherever private packages do not claim the same namespace in the public repository. Aside from PyPI, packages hosted on NPM and YARL are also known to be vulnerable to dependency confusion attacks.

![PyTorch supply chain attack](https://www.sentinelone.com/wp-content/uploads/2023/01/image.png)[Source](https://www.bleepingcomputer.com/news/security/pytorch-discloses-malicious-dependency-chain-compromise-over-holidays/)

It’s estimated that there were around 2300 malicious downloads during the time the malware was hosted on PyPI and PyTorch users are urged to uninstall and download the latest version if they think they might be affected. It is also recommended that credentials or keys stored in any of the locations noted above be rotated or reset.

## The Ugly

In a different kind of dependency attack, DLL sideloading reared its ugly head again this week with [news](https://www.bleepingcomputer.com/news/security/hackers-abuse-windows-error-reporting-tool-to-deploy-malware/) that threat actors are abusing Microsoft’s Windows Problem Reporting tool, `WerFault.exe`, to deploy [Pupy RAT](https://github.com/n1nj4sec/pupy).

Victims receive an email with a malicious attachment. When double-clicked, the attachment mounts an ISO file containing a legitimate copy of `WerFault.exe` and a malicious version of a dependency, `faultrep.dll`. When users click the [shortcut LNK file](https://www.sentinelone.com/labs/who-needs-macros-threat-actors-pivot-to-abusing-explorer-and-other-lolbins-via-windows-shortcuts/) “recent inventory& our specialties.lnk” located in the mounted drive, it launches `WerFault.exe`, which in turn looks for and loads the DLL dependency located in the same directory.

The doctored DLL presents the user with a decoy XLS spreadsheet while in the background it loads an encrypted Pupy RAT payload into memory.

![WerFault Pupy RAT](https://www.sentinelone.com/wp-content/uploads/2023/01/Screenshot-2023-01-06-at-11.55.05-AM.jpg)[Source](https://labs.k7computing.com/index.php/pupy-rat-hiding-under-werfaults-cover/)

Pupy is an open-source, cross-platform attack framework with payloads that work on Windows, Linux, Android and [macOS](https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/). Its capabilities include the ability to open a backdoor, execute arbitrary code and execute further payloads.

It is not immediately clear who is behind the campaign, but based on the XLS lure targets appear to be Chinese-speaking users. Sideloading DLLs via legitimate Microsoft software continues to be an issue defenders need to take seriously: Last year, Microsoft security tool [Windows Defende](https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool/)r was found being used to sideload Cobalt Strike during LockBit ransomware incidents.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-1-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* adm...