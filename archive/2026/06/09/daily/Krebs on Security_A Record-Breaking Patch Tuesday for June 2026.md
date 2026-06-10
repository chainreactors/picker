---
title: A Record-Breaking Patch Tuesday for June 2026
url: https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/
source: Krebs on Security
date: 2026-06-09
fetch_date: 2026-06-10T06:17:30.873090
---

# A Record-Breaking Patch Tuesday for June 2026

Advertisement

[![](/b-knowbe4/52.jpg)](https://www.knowbe4.com/secure-humans-and-agents?utm_source=krebs&utm_medium=display&utm_campaign=brand-ai-campaign-26&utm_content=static-human-ready)

Advertisement

[![](/b-knowbe4/53.jpg)](https://www.knowbe4.com/secure-humans-and-agents?utm_source=krebs&utm_medium=display&utm_campaign=brand-ai-campaign-26&utm_content=static-human-ready)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# A Record-Breaking Patch Tuesday for June 2026

June 9, 2026

[2 Comments](https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/#comments)

**Microsoft** today released software updates to plug nearly 200 security holes across its **Windows** operating systems and supported software, a record number of fixes for the company’s monthly Patch Tuesday cycle. Nearly three dozen of those bugs earned Microsoft’s most dire “critical” rating, and exploit code for at least three of the weaknesses is now publicly available.

The software giant said in [a blog post](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday) last month that both its engineers and the security community are increasing using artificial intelligence tools to find bugs, meaning this month’s heavy Patch Tuesday may start to become the norm, said **Satnam Narang**, senior staff research engineer at **Tenable**.

“Some surveys put AI usage among security professionals generally at 90%, so it’s unsurprising that this volume of patches may be the norm,” Narang said. “Pandora’s proverbial box has been opened, and as more advanced AI models become available, we expect the norm to continue upward across the board, not just for Patch Tuesday.”

June’s zero-day bugs include [CVE-2026-49160](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-49160), a denial of service vulnerability affecting a range of web servers, including Microsoft **Internet Information Services** (IIS). Microsoft says the flaw was reported by OpenAI’s Codex.

Two of the zero-days addressed this month appear to stem from recent vulnerability disclosures by **Nightmare Eclipse**, the nickname chosen by a security researcher who has been dropping exploits for various Windows flaws. One of those, dubbed “GreenPlasma,” leverages an elevation of privilege weakness in the Windows Collaborative Translation Framework, the same framework patched today in [CVE-2026-45586](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-45586).

Nightmare Eclipse also last month released “YellowKey,” an exploit for a Windows BitLocker vulnerability that allows an attacker with physical access to view encrypted data, and [CVE-2026-50507](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-50507) is a patch for an elevation of privilege bug in BitLocker.

Microsoft received heavily blowback on social media last month after it said in [a blog post](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure) that it was considering taking legal action against the security researcher. The company later clarified on Twitter/X that while it has no intention of pursuing legal actions against researchers, it would report them to authorities if they break the law. The advisories for CVE-2026-49160 and CVE-2026-50507 do not credit any researchers in the acknowledgement section, saying only that “Microsoft recognizes the efforts of those in the security community who help us protect customers through coordinated vulnerability disclosure.”

**Nightmare Eclipse** claims to be [a former employee](https://infosec.exchange/%40briankrebs/116661298779426573) of Microsoft, although Microsoft has not responded to questions about this claim. **Rapid7** notes that a recent blog post by Nightmare Eclipse included an image of Albert Vesker, a character from the Resident Evil video game series who formerly worked as a researcher for a technology company before going rogue.

Nightmare Eclipse has pledged to release even more zero-day exploits for Windows in what they called a “bone shattering” drop planned for July 14 (the same day as next month’s Patch Tuesday). Immediately following the release of Microsoft patches today, the researcher [published an exploit](https://deadeclipse666.blogspot.com/2026/06/its-patch-tuesday.html) for what they claimed was a zero-day bug in Windows Defender.

While 200 vulnerabilities may be a record for Patch Tuesday, the actual number of security flaws Microsoft addressed this month is far higher, said Rapid7’s **Adam Barnett**.

“So far this month, Microsoft has provided patches to address 360 browser vulnerabilities, which is an order of magnitude more than has been typical in any given month over the past few years,” Barnett wrote. “As usual, browser [flaws] are not included in the Patch Tuesday count above. Indeed, the vast, and presumably sustained, uptick in the number of browser vulnerabilities has led to Microsoft no longer enumerating Chromium CVEs in the Security Update Guide.”

Microsoft also patched a zero-day vulnerability in **Visual Studio Code** that allows attackers to steal GitHub tokens with a single click. The company was forced to push a stopgap fix for the flaw on June 3, after a researcher [published instructions](https://blog.ammaraskar.com/github-token-stealing/) showing how to exploit it. The researcher said they opted not to work with Microsoft because of a recent experience wherein Redmond silently patched a flaw they reported without offering credit or recognition.

Microsoft battled its own internal zero-day emergencies last week, after at least 72 of the company’s public code repositories were infected with [a variant of the Shai-Hulud worm](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents). Researchers found that all of the affected packages were connected to Microsoft official Azure Durable Task SDK, which got [hit by the same Shai-Hulud worm](https://opensourcemalware.com/blog/miasma-reaches-azure) in May.

Other major software makers are also shipping outsized update bundles this month. **Adobe** has released updates to fix a massive number of critical vulnerabilities [across a range of products](https://helpx.adobe.com/security/security-bulletin.html), including **Adobe Experience Manager**, **Acrobat Reader** and **Cold Fusion**. On June 3, **Google** resolved [a whopping 429 vulnerabilities](https://securityboulevard.com/2026/06/google-patches-429-chrome-vulnerabilities-in-major-browser-update/) in its latest **Chrome** browser update (Chrome automatically downloads updates but installing them usually requires a complete restart of the browser).

As ever, please consider backing up your data before applying operating system updates, and drop a note in the comments if you run into any problems with this month’s patches.

Further reading:

[Microsoft’s Security Update Guide](https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun)

[Action1’s Patch Tuesday breakdown](https://www.action1.com/patch-tuesday/patch-tuesday-june-2026/?vyi)

[SANS Internet Storm Center notes on Patch Tuesday](https://isc.sans.edu/diary/Microsoft%20June%202026%20Patch%20Tuesday/33064)

*This entry was posted on Tuesday 9th of June 2026 06:07 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patche...