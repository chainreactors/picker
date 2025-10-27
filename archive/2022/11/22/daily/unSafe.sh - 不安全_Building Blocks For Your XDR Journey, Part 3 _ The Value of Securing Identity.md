---
title: Building Blocks For Your XDR Journey, Part 3 | The Value of Securing Identity
url: https://buaq.net/go-136638.html
source: unSafe.sh - 不安全
date: 2022-11-22
fetch_date: 2025-10-03T23:22:50.728939
---

# Building Blocks For Your XDR Journey, Part 3 | The Value of Securing Identity

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

![](https://8aqnet.cdn.bcebos.com/0fae2fb77224b21f2da1c735c51e1c61.jpg)

Building Blocks For Your XDR Journey, Part 3 | The Value of Securing Identity

A Guest Post by Mark Harris, former Senior Director Analyst at GartnerThis is Part 3 of our multi-
*2022-11-21 22:0:53
Author: [www.sentinelone.com(查看原文)](/jump-136638.htm)
阅读量:24
收藏*

---

**A Guest Post by Mark Harris, former Senior Director Analyst at Gartner**

This is Part 3 of our multi-part XDR ([eXtended Detection and Response](https://www.sentinelone.com/platform/)) blog series, where we discuss the importance and value of securing identity. If you haven’t read it yet, we recommend checking out [Part 1](https://www.sentinelone.com/blog/building-blocks-for-your-xdr-journey-part-1-extending-beyond-the-endpoint/), which discusses why organizations need to extend protection beyond the endpoint to stay ahead of adversaries, and [Part 2](https://www.sentinelone.com/blog/building-blocks-for-your-xdr-journey-part-2-why-edr-is-the-cornerstone-for-great-xdr/), which discusses why Endpoint Detection and Response (EDR) is a foundation and a cornerstone for any XDR strategy.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Building-Blocks-For-Your-XDR-Journey-Part-3-Extending-To-Identity-Security.jpg)

## Identity, The Missing Piece

Malware authors and attackers continue to evolve the tactics, techniques, and procedures (TTPs) that they use. Vulnerabilities in applications and operating systems are regularly identified, and patching and maintaining systems to prevent those vulnerabilities from being exploited has been a constant challenge for organizations large and small. However, most attackers take a more familiar and less technical route to gain initial access: social engineering to access user credentials and data. Research suggests that nearly 50% of attacks are a result of [stolen credentials](https://www.sentinelone.com/blog/windows-security-essentials-preventing-4-common-methods-of-credentials-exfiltration/). Once an attacker has control of a user’s identity, they have the same privileges and access as the real user.

[Social engineering](https://www.sentinelone.com/cybersecurity-101/spear-phishing/) has been a key element of attacks for many years, whether it be through phishing emails, or clicking on links to exploit a vulnerability. Even the simple warnings seen in Office documents such as Microsoft Word that a document has active content (i.e. Macros) are often ignored and a user will simply enable them. Repeatedly asking users to make cybersecurity decisions will inevitably lead to user fatigue and failure.

## Credentials are Gold to the Attacker

Credentials are the key to the user’s identity, the way systems identify and authenticate who a user is. This identity is based on an [Active Directory](https://www.sentinelone.com/blog/active-directory-security/) (AD). AD effectively defines an organization structure: users are part of groups, groups have different rights and privileges to access systems and therefore data.

[Multi-factor authentication](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/) (MFA) is a critical part of checking that the user is real and who they say they are. However, as with many security controls, a balance must be struck between authenticating a user too often and allowing them to get on with their work. Once authenticated, the user won’t be asked to re-authenticate again for some time.

That’s the upside, but the downside is that if malware is successfully installed on an endpoint, and the user has already authenticated, the malware will now have the same access rights as the user. Credentials also cross traditional boundaries and are used to manage cloud entitlements and directory systems that cover both human and machine identities.

MFA is a critical component of [Identity Access Management](https://www.sentinelone.com/cybersecurity-101/identity-security-what-it-is-why-its-so-important/) (IAM), which controls access to the systems and services within an organization. Privilege Access Management (PAM) is a subset of IAM and controls not only the access but more fine-grained controls over what the user can do. Both focus on allowing access rather than preventing access, so again, if an attacker has taken control of a device, they are effectively authenticated in the same way as the “real” user.

## Managing Identity Risk

Unfortunately, the risks associated with identity don’t stop there. Once you have the credentials for one user, it’s relatively straightforward to gain access to another user’s credentials. There are simple-to-use, free, open-source tools that can escalate privileges from one user to another. [Mimikatz](https://www.sentinelone.com/cybersecurity-101/mimikatz/) is the most widely known. All an attacker needs to do once they have compromised a regular user is download Mimikatz and steal the credentials of another user to gain higher privileged access. This can then be used to connect to another device and move laterally. Access to the active directory can be gained very quickly, and then the attacker can create their own set of credentials and have free reign over the entire organization.

Many malware groups include Mimikatz as part of the malware, or at least their version of it. When combined with scripting tools like [PowerShell](https://www.sentinelone.com/cybersecurity-101/windows-powershell/) (e.g., `Invoke-Mimikatz`), these attacks can be carried out without any further files being written to disk.

Managing AD is notoriously difficult; credential permissions and configurations are constantly changing in most organizations as workers, applications and data morph and evolve. Adapting and responding to business needs means that maintaining security is a constant battle and often leads to protection gaps and accounts being overprivileged.

Gartner estimates that 50% of cloud security failures are due to poor management of identities, access and privileges. This figure is expected to rise to 75% by 2023.

Protecting against these sorts of complex attacks is the focus for Endpoint Detection and Response (EDR) solutions and increasingly Extended Detection and Response (XDR). By correlating and combining information from multiple endpoints, multiple security tools, the tell-tale signs of an attack can be identified. Even so, these solutions on the whole focus on the security of systems rather than users and their identities.

## Identity Threat Detection and Response

A new category has recently begun to appear, [Identity threat detection and response](https://www.sentinelone.com/blog/xdr-meets-itdr/) (ITDR). These solutions focus on detecting identity-based attacks, whilst identity-based attack surface management (ASM) focuses on restricting the ability for the attacker to easily move laterally by identifying misconfigurations and overprivileged accounts.

SentinelOne has introduced both an identity-based attack surface management capability with Ranger AD and ITDR with Singularity Identity.

[Ranger AD](https://www.sentinelone.com/platform/singularity-ranger-ad/) analyses the active directory structure and identifies accounts that are misconfigured or over privileged. This makes it harder for the attacker to gain privileged access, at the very least making it harder for them.

[Singularity Identity](https://www.sentinelone.com/platform/singularity-identity/) not only identifies identity-based attacks but works with Singularity Hologram to create network-based lures and deception to protect assets and trick attackers into revealing t...