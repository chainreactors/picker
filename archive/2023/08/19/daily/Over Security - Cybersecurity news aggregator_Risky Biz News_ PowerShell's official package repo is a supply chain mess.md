---
title: Risky Biz News: PowerShell's official package repo is a supply chain mess
url: https://riskybiznews.substack.com/p/powershell-supply-chain-mess
source: Over Security - Cybersecurity news aggregator
date: 2023-08-19
fetch_date: 2025-10-04T12:02:06.399925
---

# Risky Biz News: PowerShell's official package repo is a supply chain mess

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: PowerShell's official package repo is a supply chain mess

### In other news: LinkedIn hit by wave of account hijacks; the US Chamber of Commerce wants one-year delay for SEC cyber rules; and China passes AI regulation.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Aug 18, 2023

Share

***This newsletter is brought to you by [Thinkst](https://thinkst.com/), the makers of the much-loved [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Apple Podcasts:***

[PowerShell Gallery](https://www.powershellgallery.com/), the official repository for the PowerShell scripting language, contains (*still-unfixed*) design flaws that can be abused by threat actors for typosquatting and impersonation attacks.

Discovered by cloud security firm *[AquaSec](https://blog.aquasec.com/powerhell-active-flaws-in-powershell-gallery-expose-users-to-attacks)*, these issues can be weaponized in supply chain attacks to trick developers into downloading and running malicious PowerShell packages on their systems or inside enterprise applications.

The first issue researchers found was that PSGallery does not come with any kind of protection against typosquatting, allowing threat actors to register packages that mimic the names of more successful PowerShell modules just by adding punctuation inside the name.

This behavior is the exact opposite of what GitHub does on [npm](https://blog.npmjs.org/post/168978377570/new-package-moniker-rules.html), where developers can't register new packages that resemble popular libraries just by adding dots, dashes, and underscores in the names.

Even worse, the PSGallery also allows threat actors to copy the metadata of any PowerShell module, including the highly-coveted "*Author(s)*" and "*Owners*" fields, allowing threat actors to pass malicious packages as coming from legitimate developers and companies.

> A proof-of-concept package showcasing both of these issues can be seen [here](https://www.powershellgallery.com/packages/Az.Table/2.2.2), where a PowerShell module developed by AquaSec named Az.Table perfectly mimics the original AzTable package, including the author field, which lists a Microsoft employee as its creator.

A last bug also allows threat actors to list a user's entire list of packages, including private and unpublished libraries. Such information could be used for more targeted supply chain or dependency confusion scenarios, where knowledge of private packages can help attackers fine-tune their copycat modules.

AquaSec has disclosed its findings this week after reporting the three issues to Microsoft last September. The company says that although Microsoft tried to fix the issues twice, the design flaws are still present on the PSGallery portal and are still reproducible/exploitable. Hmm... I wonder where I've heard [something like this before](https://riskybiznews.substack.com/p/risky-biz-news-microsoft-accused-977).

[![](https://substackcdn.com/image/fetch/$s_!nokK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05aa1600-9558-4a9f-be66-3406673759ff_854x436.png)](https://substackcdn.com/image/fetch/%24s_%21nokK%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/05aa1600-9558-4a9f-be66-3406673759ff_854x436.png)

Knowledge of these issues and the fact that they're still open to exploitation will most likely contribute to a rise in attacks targeting PSGallery.

Right now, npm and PyPI bear the brunt of most typosquatting and supply chain attacks, mostly because of their popularity and ease of attacks.

With PowerShell playing a crucial role in enterprise automation operations, the PSGallery checks all the boxes on an attack vector ripe for exploitation.

---

### **Breaches, hacks, and security incidents**

**LinkedIn account hacks:** Hackers are breaking into LinkedIn accounts and locking users out of their profiles, according to reports on [Reddit](https://old.reddit.com/r/linkedin/comments/15cx1zg/mega_thread_so_your_linkedin_account_got/), [support forums](https://answers.microsoft.com/en-us/windows/forum/all/got-hacked-by-a-ramblerru-account/122aec21-5b89-4996-8a92-c4d51e259d96), and [security firms](https://cyberint.com/blog/research/linkedin-accounts-under-attack-how-to-protect-yourself/). The accounts are allegedly being compromised due to password reuse. Compromised accounts typically have their email address changed to a Rambler[.]ru alternative, suggesting most of the recent hacks are being conducted by the same threat actor. Some users reported receiving ransom demands, with the hackers offering to restore their account access for a small sum of cryptocurrency.

**RocketSwap crypto-heist:** The RocketSwap cryptocurrency platform was hacked for $860,000 worth of assets. The crypto-heist took place after the hackers brute-forced one of the company's servers and stole one of its wallet's private keys.

[![](https://substackcdn.com/image/fetch/$s_!iWqd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f5eef83-7b37-44a2-8ed1-641a1c5cb273_563x483.png)](https://substackcdn.com/image/fetch/%24s_%21iWqd%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/0f5eef83-7b37-44a2-8ed1-641a1c5cb273_563x483.png)

### **General tech and privacy**

**Quantum resilient FIDO2 security key:** Google has [developed](https://security.googleblog.com/2023/08/toward-quantum-resilient-security-keys.html) the first-ever version of a FIDO2 security key that includes protections against quantum computing attacks. The implementation is a new version of OpenSK, an open-source project that provides free firmware for security keys. Google says this new OpenSK firmware version uses a novel ECC/Dilithium hybrid signature schema its engineers co-developed together with academics from ETH Zurich.

**Chrome extensions scan:** Google will show notifications to Chrome users when one or more of their installed extensions are removed from the official Web Store. The notifications will be shown when an extension is marked as malware, the extension is removed for ToS violations, or when the extension is unpublished by its developer. [The new feature](https://developer.chrome.com/blog/extension-safety-hub/) will come in Chrome 117, scheduled for release at the start of September. Chrome 116 users can enable it right now via this Chrome flag:

> ***chrome://flags/#safety-check-extensions***

[![](https://substackcdn.com/image/fetch/$s_!VHyi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe6abe77-c9fd-46a0-91f2-059c8c2be636_1049x604.png)](https://substackcdn.com/image/fetch/%24s_%21VHyi%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/fe6abe77-c9fd-46a0-91f2-059c8c2be636_1049x604.png)

[![](https://substackcdn.com/image/fetch/$s_!4zZI!,w_1456,...