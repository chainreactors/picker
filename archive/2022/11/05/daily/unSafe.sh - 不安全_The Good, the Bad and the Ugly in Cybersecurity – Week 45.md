---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 45
url: https://buaq.net/go-134230.html
source: unSafe.sh - 不安全
date: 2022-11-05
fetch_date: 2025-10-03T21:42:41.126819
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 45

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

![](https://8aqnet.cdn.bcebos.com/9d60827c2d4cd5d8ea86d781888fe8a8.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 45

The GoodSoftware supply chain attacks aren’t just creeping into the threat landscape anymore – the
*2022-11-4 21:0:0
Author: [www.sentinelone.com(查看原文)](/jump-134230.htm)
阅读量:29
收藏*

---

## The Good

[Software supply chain attacks](https://www.sentinelone.com/blog/defending-the-enterprise-against-digital-supply-chain-risk-in-2022/) aren’t just creeping into the threat landscape anymore – they have been fully on the rise over recent years. After multiple high-profile attacks, including those on [SolarWinds](https://www.sentinelone.com/blog/stopping-solarwinds-breach-with-jared-phipps-from-sentinelone/) and [Kaseya](https://www.sentinelone.com/blog/revils-grand-coup-abusing-kaseya-managed-services-software-for-massive-profits/), nation states and organizations alike have all worked to share lessons learned and raise their awareness on supply chain attacks.

This week, the NSA, CISA, and the Office of the Director of National Intelligence (ODNI) released a new set of [guidelines](https://media.defense.gov/2022/Oct/31/2003105368/-1/-1/0/SECURING_THE_SOFTWARE_SUPPLY_CHAIN_SUPPLIERS.PDF) for securing software supply chain operations. The guidelines were created in coordination with public-private cross-sector, [Enduring Security Framework (ESF)](https://www.nsa.gov/About/Cybersecurity-Collaboration-Center/Cybersecurity-Partnerships/ESF/), to provide suppliers with best practices for planning, prevention, and response processes.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/GBU-Wk-45_chain.jpg)

While the document lays out comprehensive instructions to help suppliers define criteria for security checks and respond to [vulnerabilities](https://www.sentinelone.com/blog/how-to-modernize-vulnerability-management-in-todays-evolving-threat-landscape/), it more importantly articulates the notion of establishing shared responsibility.

“Prevention is often seen as the responsibility of the software developer, as they are required to securely develop and deliver code, verify third party components, and harden the build environment. But the supplier also holds a critical responsibility in ensuring the security and integrity of our software,” the NSA noted in their [press release](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3204427/esf-partners-nsa-and-cisa-release-software-supply-chain-guidance-for-suppliers/).

[Software supply chain attacks](https://www.sentinelone.com/blog/hiding-among-friends-how-to-beat-the-new-breed-of-supply-chain-attacks/) have remained at the forefront of discussion by U.S. officials with a new federal [strategy](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf) to adopt a [zero-trust model](https://www.sentinelone.com/blog/moving-to-a-zero-trust-security-model/) announced in January of this year followed in May by [NIST Special Publication 800-191](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1.pdf) addressing supply chain risk management. The ESF is set to release another set of guidelines, focusing next on customers in the software supply chain lifecycle. This week’s release is preceded by the first in the series, a guideline created to support [developers](https://media.defense.gov/2022/Sep/01/2003068942/-1/-1/0/ESF_SECURING_THE_SOFTWARE_SUPPLY_CHAIN_DEVELOPERS.PDF) specifically.

## The Bad

Popular file-hosting service, Dropbox, disclosed this week that they suffered a breach after a phishing campaign targeted employees. In their [blog post](https://dropbox.tech/security/a-recent-phishing-campaign-targeting-dropbox), the California-based company explained that attackers accessed 130 of their code repositories in GitHub, but the breach did not include unauthorized access to user accounts, content, passwords, or payment information. Code for its core apps and infrastructure were also not contained in the compromised repositories.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/GBU-Wk-45_fish.jpg)

This [phishing campaign](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) on Dropbox shares its roots with a campaign that targeted [GitHub](https://github.blog/2022-09-21-security-alert-new-phishing-campaign-targets-github-users/) just a few months ago. In both cases, the threat actor impersonated CircleCI, a continuous integration software, to harvest user credentials and [MFA](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/) codes. Attackers were able to breach Dropbox’s defenses by using legitimate-looking phishing emails that directed employees to enter their [credentials](https://www.sentinelone.com/blog/credentials-harvesting-from-domain-shares/) and hardware authentication key to pass a one-time password (OTP) to a fake CircleCI site.

Dropbox revealed that the code accessed by the threat actor contained some credentials, mainly API keys used by the company’s developers, and also “a few thousand names and email addresses” belonging to employees, sales leads, third-party vendors, as well as current and past customers.

Though the company has underscored that no customer data was stolen, the need for large companies to harden their authentication protocols is clear. In this case, over 700 million registered users rely on Dropbox for folder sharing, cloud storage, file backup, task management, and document signing services.

[Identity-based protection](https://www.sentinelone.com/blog/rise-in-identity-based-attacks-drives-demand-for-a-new-security-approach/) has long needed more attention with even the U.S. government [mandating](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf) this year that all federal agencies are to implement both [zero-trust architecture](https://www.sentinelone.com/blog/cisa-zero-trust-identity/) and phishing-resistant MFA. Dropbox’s blog confirmed that the company has accelerated an upgrade to their authentication tools and will soon use biometric factors or hardware tokens across its environment.

## The Ugly

The RomCom RAT has come out to play again, and this time it’s using rogue versions of SolarWinds Network Performance Monitor (NPM), KeePass password manager, and PDF Reader Pro. RomCom also has been known to use trojanized variants of [Advanced IP Scanner and pdfFiller](https://thehackernews.com/2022/10/romcom-hackers-circulating-malicious.html).

[Researchers](https://blogs.blackberry.com/en/2022/11/romcom-spoofing-solarwinds-keepass) found RomCom actors leveraging customer trust in well-known software brands to create typo-squat lookalike download sites, effectively disguising their malware as legitimate products. This is done by scraping the HTML code from the company’s legitimate site, registering a new, similar domain, and deploying targeted [phishing](https://www.sentinelone.com/blog/phishing-revealing-vulnerable-targets/) emails or social media posts to lure in specific users.

The spoofed websites host and deploy the RomCom RAT ([remote access trojan](https://www.sentinelone.com/blog/ciso-essentials-how-remote-access-trojans-affect-the-enterprise/)), which is capable of taking screenshots and collecting sensitive information, before exporting them back to the threat actor’s server.

RomCom seems to be expanding on this tactic now that fake Veeam Backup Recovery installers have been identified, too.

> We're observing that ROMCOM RAT is now being packaged as an installer for Veeam Backup and Recovery software. This is in addition to the KeePass Password...