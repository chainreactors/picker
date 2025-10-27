---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 5
url: https://buaq.net/go-147868.html
source: unSafe.sh - 不安全
date: 2023-02-04
fetch_date: 2025-10-04T05:39:43.968981
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 5

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

![](https://8aqnet.cdn.bcebos.com/eecedd07ba26fd22362846a778b55772.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 5

The GoodThe FTC this week has handed out a $1.5 million penalty to a U.S. healthcare company that
*2023-2-3 22:0:46
Author: [www.sentinelone.com(查看原文)](/jump-147868.htm)
阅读量:32
收藏*

---

## The Good

The FTC this week has handed out a $1.5 million penalty to a U.S. healthcare company that promised its customers it would “never share personal health information with advertisers or third parties” and then allegedly did [precisely that](https://www.scmagazine.com/analysis/breach/ftc-slaps-goodrx-with-1-5m-fine-for-sharing-health-data-with-facebook-others).

The Department of Justice filed an enforcement action on behalf of the FTC against GoodRx under its new Health Breach Notification rule. The complaint against the company accused it of failing to notify customers about unauthorized disclosure of health PII (personally identifiable information). According to the FTC, GoodRx repeatedly shared individually identifiable health information over a four year period with Facebook, Google, Twilio, Branch, and Criteo.

> FTC enforcement action to bar GoodRx from sharing consumers’ sensitive health info for advertising: <https://t.co/ag4TCYS2Ii> /1
>
> &mdash; FTC (@FTC) [February 1, 2023](https://twitter.com/FTC/status/1620827827833638912?ref_src=twsrc%5Etfw)

The FTC went on to complain that GoodRx had uploaded contact details of its own customers to Facebook along with advertising IDs, and that it used privileged information about those customers’ previous medication purchases to target their profiles with health-related ads. In doing so, the company exposed their information to Facebook, which itself is facing multiple ongoing lawsuits related to scraping data from hospital websites for use in targeted ads.

FTC director Samuel Levine said of the action that “Digital health companies and mobile apps should not cash in on consumer’s extremely sensitive and personally identifiable health information” and that the FTC would continue to use its legal authority to protect American consumers.

## The Bad

SIM swapping attacks, where a threat actor impersonates a customer of a mobile phone carrier and requests a transfer of the customer’s number to a new device, have been utilized to pull off some [high profile hacks](https://www.sentinelone.com/blog/lapsus-data-breach/) recently. This week, it’s bad news for Google Fi customers, who have been targeted by hackers that gained access to technical SIM data after breaching a Google Fi network provider.

Google’s U.S. telecommunications and mobile internet service, Google Fi, informed customers this week that personal data had been exposed after a breach of one of its network providers. Google notified customers that the incident had exposed their phone numbers, SIM card serial numbers, and other details. However, the company emphasized that there was no access to Google’s systems or any systems overseen by Google.

Users on social media, however, soon began reporting notifications from Google Fi that described SIM swapping attacks.

![Google Fi hack SIM Swap](https://www.sentinelone.com/wp-content/uploads/2023/02/Google-Fi.jpg)

SIM swapping attacks allow the attacker to receive both phone calls and SMS text messages intended for the legitimate user and, among other things, allow attacks to intercept text-based [2FA authentication](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/) messages.

Google says its incident response team investigated the breach and implemented measures to secure data on the provider’s system and notified everyone potentially impacted. The SIM swapping attacks were temporary and Google Fi has since restored service to all customers’ registered SIM cards.

## The Ugly

Threat actors have been creating malicious OAuth applications as part of a phishing campaign aimed at breaching Microsoft cloud services, it was revealed this week.

According to [MSRC](https://msrc-blog.microsoft.com/2023/01/31/threat-actor-consent-phishing-campaign-abusing-the-verified-publisher-process/), threat actors ran a consent phishing campaign after impersonating companies enrolling in MCPP/MPN (Microsoft Cloud Partner Program, *aka* Microsoft Partner Network). Consent phishing works by tricking users into granting permissions to malicious cloud applications that can then be weaponized to compromise legitimate cloud services and access sensitive data.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/open.jpg)

Once victims granted access to the malicious OAuth apps, threat actors used them to exfiltrate email mailboxes, likely with the further objective to use the stolen data in email [Reply Chain attacks](https://www.sentinelone.com/blog/email-reply-chain-attacks-what-are-they-how-can-you-stay-safe/), [Business Email Compromises](https://www.sentinelone.com/cybersecurity-101/business-email-compromise-bec/) (BEC), and [spear phishing](https://www.sentinelone.com/blog/phishing-revealing-vulnerable-targets/) attacks.

The campaign, which primarily targeted MCPP customers in the UK and Ireland, was first spotted on December 15th last year, with the actors using fraudulent partner accounts to register OAuth applications in Azure AD that appeared to be from [verified publishers](https://learn.microsoft.com/en-us/azure/active-directory/develop/publisher-verification-overview).

The Redwood tech giant says that all identified fraudulent applications have now been disabled and affected customers informed. Even so, it comes amid [turbulent times](https://www.scmagazine.com/analysis/application-security/after-a-year-of-exchange-exploits-microsoft-presses-customers-to-patch-on-prem-servers) for the company. Despite announcing security sales of over [$20 billion in 2022](https://www.govinfosecurity.com/microsoft-security-sales-hit-20b-as-consolidation-increases-a-21015), the company’s products across endpoint and cloud remain notorious for multiple high-impact [vulnerabilities](https://www.sentinelone.com/blog/why-your-operating-system-isnt-your-cybersecurity-friend/) and cloud-based [attack vectors](https://www.darkreading.com/cloud/microsoft-azure-kerberos-attacks-open-cloud-accounts).

Attacks using bogus OAuth apps have targeted Microsoft’s cloud services before, with separate threat activities seen in January 2022 and September 2022, according to [reports](https://thehackernews.com/2023/02/hackers-abused-microsofts-verified.html).

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-5-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)