---
title: New Twitter data dump is a cleaned up version of old Twitter dump
url: https://buaq.net/go-144524.html
source: unSafe.sh - 不安全
date: 2023-01-07
fetch_date: 2025-10-04T03:13:31.279911
---

# New Twitter data dump is a cleaned up version of old Twitter dump

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

New Twitter data dump is a cleaned up version of old Twitter dump

News of data dumps is often scary as the possibilities of identity thef
*2023-1-6 23:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-144524.htm)
阅读量:18
收藏*

---

News of data dumps is often scary as the possibilities of identity theft, account takeovers, user de-anonymization, and other online data-driven threats rear their ugly heads. Reading about the latest reports of a new Twitter dump, however, is like opening up an already-healed wound, as the dump turned out to be the same one back in November 2022 that [affected more than 400 million users](https://www.malwarebytes.com/blog/news/2022/11/twitter-user-data-leaks-continue-to-drip-from-the-faucet). Security researchers from Privacy Affairs [verified](https://www.privacyaffairs.com/200-million-twitter-data-leak/) this to be true. Only this set is a lot cleaner—the file size containing it significantly smaller because the number of affected users has been halved to 200 million after duplicates were removed.

The person responsible, who claims not to have originally collected the user data, has now decided to make the data freely available, offering it up on the site they were earlier trying [to profit from](https://www.bleepingcomputer.com/news/security/200-million-twitter-users-email-addresses-allegedly-leaked-online/). How bad is this? Should Twitter users be concerned?

## From the forums to the public

Privacy Affairs claims data in the set can be used in social engineering attacks and [doxxing](https://www.malwarebytes.com/doxxing). If email addresses and phone numbers are included in the dump, and the option to search for users using any of these pieces of data is enabled, then those entries would appear via [abuse of an API](https://www.zdnet.com/article/twitter-says-an-attacker-used-its-api-to-match-usernames-to-phone-numbers/) in the data harvested. Phone numbers, in particular, could leave someone open to identification or SIM swap attacks on their mobile network provider.

Naturally, this would be the biggest concern for people with phone numbers or other identifying information in any leak. In this case, [things may not be as bad as they sound](https://www.theregister.com/2023/01/05/twitter_leak_200m_accounts/). From the forum post:

> I combined the files, converted to CSV, added a header, changed invalid control characters to "\*", deduplicated (including the 23M that were the same except for different # of followers), made the dates smaller and computer-friendly, and removed spaces that appeared before some emails. I also used very high compression, so the compressed file is just over 4GB. I intentionally didn't sort it, so the curious will have an easier job comparing it to the original.

If you suspect you've been caught up in this leak, you can check on [Haveibeenpwned](https://haveibeenpwned.com/), which has added the data to its system and is currently notifying anyone signed up for the notification service.

## A welcome relief?

The forum poster goes on to say the following:

> NOTE: There are NO PASSWORDS, NO PHONES, NO PHYSICAL ADDRESSES in this file. The original scrape did not contain any of that data.

While the data does include email addresses, the lack of passwords, phone numbers, and physical location is good. What's left behind, other than email addresses, is publicly available information someone could gather up by various means. This includes name, screen name, follow count, account creation date, and others.

Unless your threat model is very specific and hinges on the exposure of your email address, you probably have little to worry about on this occasion. While there could be some form of social engineering risk from this data going public, the majority of it is likely to be data that a casual attacker could harvest from publicly available information very quickly in any case.

Stay safe out there!

---

文章来源: https://www.malwarebytes.com/blog/news/2023/01/new-twitter-data-dump-is-a-cleaned-up-version-of-old-twitter-dump
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)