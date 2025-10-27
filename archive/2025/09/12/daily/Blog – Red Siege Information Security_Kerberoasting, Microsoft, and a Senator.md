---
title: Kerberoasting, Microsoft, and a Senator
url: https://redsiege.com/blog/2025/09/kerberoasting-microsoft-and-a-senator/
source: Blog – Red Siege Information Security
date: 2025-09-12
fetch_date: 2025-10-02T20:01:37.210102
---

# Kerberoasting, Microsoft, and a Senator

Register Now For On-Demand Training!

[Learn More](https://training.redsiege.com)

[![](https://redsiege.com/wp-content/uploads/2022/01/redsiege-logo-300x73.png)](https://redsiege.com)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

![](https://redsiege.com/wp-content/themes/red-siege-theme/img/icon-phone.svg) +1 234-249-1337

# Kerberoasting, Microsoft, and a Senator

By Tim Medin | September 11, 2025

Table of Contents

Toggle

* [Kerberoasting, Microsoft, and a Senator](#Kerberoasting_Microsoft_and_a_Senator)
  + [The Kerberoasting Vulnerability in Brief](#The_Kerberoasting_Vulnerability_in_Brief)
  + [Senator Ron Wyden](#Senator_Ron_Wyden)
  + [Encryption and Kerberoasting](#Encryption_and_Kerberoasting)
  + [Microsoft’s Response](#Microsofts_Response)
  + [What can you do?](#What_can_you_do)
  + [Immediate Executive Actions](#Immediate_Executive_Actions)
  + [Conclusion](#Conclusion)
  + [Less Brief and not Super Technical Background on Kerberoasting](#Less_Brief_and_not_Super_Technical_Background_on_Kerberoasting)

# Kerberoasting, Microsoft, and a Senator

When I came up with Kerberoasting in 2014, I never thought it would live for more than a year or two. I (erroneously) thought that people would clean up the poor, dated credentials and move to more secure encryption. Here we are 11 years later, and unfortunately it still works more often than it should. In 2024, healthcare giant Ascension was hit by ransomware. On September 10, 2025, a senator wrote a letter to the FTC about Kerberoasting and Microsoft’s deficiencies in protecting Windows. Let’s first very briefly discuss what Kerberos is, then I’ll touch on Microsoft’s response and the senator’s letter to the FTC.

## The Kerberoasting Vulnerability in Brief

All 500 of the Fortune 500 use Active Directory and therefore Kerberos to authenticate to their Windows systems. A user receives a “ticket” to prove who they are to registered services inside Active Directory (for simplicity, I’ll just say server). To protect the ticket, it is encrypted using a derivative (hash) of the server’s password. The server decrypts the ticket and then decides if the user has access, and if so, how much access.

The issue is any valid user (even a compromised one) can request a ticket for any server. This means an attacker can request and save tickets for any and all servers. With those tickets in hand, the attacker then makes a guess as to the server’s password and attempts to decrypt the tickets. Since the attack is offline, an attacker can attack the password as fast as their (often specialized) hardware will let them, up to billions of attempts per second. And with no lockout of the account due to the the attack being offline.

For a little more depth (but not a ton), see the end of this article. For much more in-depth technical details, I have hands-on pay-what-you-can training (down to free, as in beer, as in $0) on the topic available at [training.redsiege.com](https://training.redsiege.com/courses/f7994264-fadd-46b0-b27b-2a17ac279ada).

## Senator Ron Wyden

Sen. Ron Wyden (D–Oregon) sent a [letter](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_microsoft_kerberoasting_ransomwarepdf.pdf) to FTC Chairman Andrew Ferguson in response to the 2024 ransomware breach of the healthcare giant Ascension. Ars Technica wrote an [article](https://arstechnica.com/security/2025/09/senator-blasts-microsoft-for-making-default-windows-vulnerable-to-kerberoasting/) on the topic. The senator called out Microsoft for supporting RC4 encryption on Kerberos tickets, which makes the Kerberoasting attack significantly faster.

Let’s see why RC4 matters.

## Encryption and Kerberoasting

With the Kerberoast attack, attackers are targeting the encryption key (the server’s password), not the underlying encryption protocol. The common encryption protocols for encryption on tickets are RC4, AES128, and AES256. The attackers aren’t fundamentally breaking RC4, but…

The problem with RC4 is that it is significantly faster to crack RC4 Kerberos tickets than it is to crack AES128 or AES256 tickets. Based on a quick benchmark on my laptop’s GPU, AES128 and AES256 are approximately 350 and 700 times slower to crack, respectively (benchmarks by some others show it is even slower). And yes, AES based Kerberos tickets are still susceptible to Kerberoasting, it just takes longer.

The thing is, longer matters. If it takes a day to crack an RC4 ticket, that would take nearly a year to crack the same AES128 ticket, and nearly two years for AES256. If an attacker can’t crack the ticket in a reasonable amount of time, they move onto the next thing. Also, it gives the organization more time to detect an intruder before they elevate or extend their access. Is it perfect, no, but it is better. In security we far too often make perfect the enemy of good (or better).

That said, if the password is really bad, going a thousand times slower isn’t going to have any meaningful benefit.

## Microsoft’s Response

In the Ars Technica article, Microsoft is quoted as:

> RC4 is an old standard, and we discourage its use both in how we engineer our software and in our documentation to customers – which is why it makes up less than .1% of our traffic. However, disabling its use completely would break many customer systems. For this reason, we’re on a path to gradually reduce the extent to which customers can use it, while providing strong warnings against it and advice for using it in the safest ways possible. We have it on our roadmap to ultimately disable its use. We’ve engaged with The Senator’s office on this issue and will continue to listen and answer questions from them or others in government.
>
> In Q1 of 2026 any new installations of Active Directory Domains using Windows Server 2025 will have RC4 disabled by default, meaning any new domain will inherently be protected against attacks relying on RC4 weaknesses. We plan to include additional mitigations for existing in-market deployments with considerations for compatibility and continuity of critical customer services.

Microsoft claims this affects “less than 0.1% of traffic”, but this statistic is misleading. It’s like saying “only 0.1% of our doors are used by burglars” – attackers will simply choose the weak door. Microsoft has prioritized backward compatibility over security, leaving all organizations vulnerable by default.

The truth is, since the protocol is enabled (by default), all an attacker needs to do is request an RC4 ticket. The surrounding traffic (99.9%) is irrelevant. Microsoft has left RC4 enabled because they have chosen to support backward compatibility (as mentioned in the quote), which leads to a faster Kerberoast attack.

The second paragraph is misleading as well. They state that “in Q1 of 2026 any new installations of Active Directory Domains using Windows Server 2025 will have RC4 disabled by default”. The key here is “new”. Existing Active Directory Domains will still maintain their backward compatibility, and RC4, by default. If a new server is installed, and it doesn’t support RC4, that doesn’t prevent the rest of the domain, and the Domain Controllers (the brains of the Domain) from preventing RC4.

On October 11, 2024, Microsoft published a blog post titled [Microsoft’s guidance to help mitigate Kerberoasting](https://www.microsoft.com/en-us/security/blog/2024/10/11/microsofts-guidance-to-help-mitigate-kerberoasting/). In the article Microsoft discusses mitig...