---
title: Bug bounties are broken – the story of “i915” bug, ChromeOS + Intel bounty programs, and beyond
url: https://buaq.net/go-163813.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:28.527769
---

# Bug bounties are broken – the story of “i915” bug, ChromeOS + Intel bounty programs, and beyond

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

![]()

Bug bounties are broken – the story of “i915” bug, ChromeOS + Intel bounty programs, and beyond

At first, I didn’t plan to write an article about t
*2023-5-17 23:16:55
Author: [blog.pi3.com.pl(查看原文)](/jump-163813.htm)
阅读量:39
收藏*

---

At first, I didn’t plan to write an article about the problems with bug bounty programs. This was supposed to be a standard technical blogpost describing an interesting bug in the Linux Kernel i915 driver allowing for a linear Out-Of-Bound read and write access ([CVE-2023-28410](https://nvd.nist.gov/vuln/detail/CVE-2023-28410)). Moreover, I’m not even into bug bounty programs, mostly because I don’t need to, since I consider myself lucky enough to have a satisfying, stable and well-paid job. That being said, in my spare time, apart from developing and maintaining the [Linux Kernel Runtime Guard (LKRG)](https://lkrg.org) project, I still like doing vulnerability research and exploit development not only for my employer, and from time to time it’s good to update your resume with new CVE numbers. Before I started to have a stable income, bug bounties didn’t exist and most of the quality vulnerability research outcome was paying the bills via brokers (let’s leave aside the moral questions arising from this). However, nowadays we have bug bounty programs…

For the last decade (a bit longer), bug bounty programs gained a lot of deserved traction. There are security researchers who rely on bug bounties as their primary(!) source of income. Such cases are an irrefutable proof of the success of the bug bounty programs. However, before the industry ended up where it is now, it went through a long and interesting route.

## **A little bit of history:**

On November 5, 1993, Scott Chasin created the bugtraq mailing list in response to the problems with CERT, where security researchers could publish vulnerabilities, regardless of vendor response, as part of the full disclosure movement of vulnerability disclosure. On July 9, 2002, Len Rose created Full Disclosure – a “lightly moderated” security mailing list because many people felt that the bugtraq mailing list had “changed for the worse”.

Coordinated (responsible) vulnerability disclosure is a policy under which researchers agree to report vulnerabilities to a coordinating authority, which then reports it to the vendor, tracks the fixes and mitigations, and coordinates the disclosure of information with stakeholders including the public. In some cases, the coordinating authority is the vendor.
However, some researchers started to raise concerns about how vendors handle the reported vulnerabilities (and treat the researchers as enemies) while others started to have expectations of compensation for their reports (bug bounty-like programs).

## **“No more free bugs”**

In March 2009 at CanSecWest conference, Alex Sotirov, Dino Dai Zovi and Charlie Miller announced the “No More Free Bugs” campaign spreading the word that, in most cases, they would no longer be providing vendors with free vulnerability notices. Regardless of how effective it was (not really: <https://twitter.com/0xcharlie/status/1480593646756024323>), it certainly made industry news and opened a broader debate about the problem. It is worth mentioning that in the old days, when security researchers got a free t-shirt for their work, they could consider themselves lucky 😉 The real rewards came in fame and job offers from third parties (if at all).

The reason I’m mentioning all these “past problems” is because they are the basis of how and why we have bug bounty programs today in some form or other. Moreover, certainly we would NOT want to find the industry in a similar shape as in the old days.

## **Bug bounty programs – A new wonderful world!**

Let’s ask ChatGPT the following question:

> * “What is the history of bug bounty programs?”
> * “Bug bounty programs have their origins in the early days of the internet, with companies such as Netscape and Mozilla offering rewards for the discovery and reporting of security vulnerabilities in their software. The concept of a “bug bounty” was formalized by the United States Department of Defense in the early 2000s with the launch of the Vulnerability Reward Program (VRP). Since then, many technology companies and organizations have implemented similar programs, offering rewards to security researchers for finding and reporting vulnerabilities in their systems. These programs have become an important tool in the fight against cybercrime, as they incentivize individuals to find and report vulnerabilities before they can be exploited by malicious actors.”

Pretty accurate 😉 While the market for vulnerabilities has developed, vulnerability commercialization (or “bug bounties”) remains an important tool allowing the developers to discover and resolve bugs before the general public becomes aware of them, preventing incidents of widespread abuse and data breaches.

However, some people might ask *“Why do companies bother creating a bug bounty program?”*. It’s a fair question, what’s the point (from the companies’ perspective) of paying money to “random” people for finding bugs in their products? Bug bounties benefit not only the researchers. In fact, if company’s security is mature enough and their products development is security oriented (which is usually not the case) they can actually bring a lot of benefits, including:

* Cost-effective vulnerability management – bug bounties can be more cost-effective than hiring a third-party security firm to conduct penetration testing or vulnerability assessments, which can be expensive (especially for very complicated and mature products). Additionally, with a bug bounty program, companies can expand their testing and vulnerability research coverage, as they can have many security researchers with different levels of expertise, experience, and skills testing their products and systems. This can help the company to find vulnerabilities that might have been missed by their internal team.
* Brand reputation – by having a bug bounty program, companies can show that they care about security and are willing to invest in it. It can also help to improve the company’s reputation in the security industry.
* “Protect” the brand – by opening a bug bounty program, companies can encourage researchers to report vulnerabilities directly to them, rather than publicizing them or selling them to malicious actors. This can help to mitigate various security risks.
* “Advertisement” to the potential customers – bug bounty are showing that they take security seriously and are actively working to identify and address vulnerabilities. Companies can build trust with their customers, partners, and other stakeholders.

Nevertheless, it should be noted that having a bug bounty program does not replace the need for secure SDLC, regular security testing and vulnerability management practices, and more. It’s an additional layer of security that can complement the existing security measures in place.

## **“Bug bounties are broken”**

As we can see, bug bounties are very successful because both parties – researchers and companies – benefit from them. However, that being said, in recent years more and more security researchers started to loudly complain about some specific bounty programs. A few years ago, given the success of the bug bounties, such unfavorable opinions were marginal. Of course, they have always been there but certainly they were not as visible. Whenever a new company joined the revolution of opening a bug bounty, they were praised (especially by the media) for being mature and understanding the imp...