---
title: New PHP-based Ducktail infostealer is now after crypto wallets
url: https://buaq.net/go-131921.html
source: unSafe.sh - 不安全
date: 2022-10-21
fetch_date: 2025-10-03T20:27:02.563271
---

# New PHP-based Ducktail infostealer is now after crypto wallets

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

New PHP-based Ducktail infostealer is now after crypto wallets

A phishing campaign known to specifically target employees with access
*2022-10-20 20:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-131921.htm)
阅读量:12
收藏*

---

A phishing campaign known to specifically target employees with access to their company's Facebook Business and Ads accounts has significantly widened its net and begun using a first-of-its-kind information-stealing malware to go after crypto wallets.

The Ducktail *(Woo-ooh!)* campaign was [first made public](https://www.bleepingcomputer.com/news/security/linkedin-phishing-target-employees-managing-facebook-ad-accounts/) three months ago in July, but it's thought to have been active [since 2018](https://labs.withsecure.com/publications/ducktail). The cybercriminal behind the campaign is thought to be from Vietnam.

## Ducktail 101

Social engineering attacks and malware form the core of Ducktail's *modus operandi*. In previous campaigns, it used a .NET Core malware that specifically steals Facebook Business and Ads accounts and saved browser credentials. All stolen data was then exfiltrated to its [command & control (C2)](https://www.malwarebytes.com/glossary/cc) server, a private Telegram channel.

In this latest campaign, the cybercriminals replaced .NET Core with malware written in PHP. Not only does Ducktail continue to steal Facebook credentials and browser data, but it also steals cryptocurrency wallets, too. These are then stored on a [command & control (C2)](https://www.malwarebytes.com/glossary/cc) website in [JSON (JavaScript Object Notation)](https://www.w3schools.com/whatis/whatis_json.asp) format, wherein texts are easy to understand.

Note that Ducktail also broadened its target to include all Facebook users.

The attacker lures their target into downloading and installing a malicious installer (usually compressed in a ZIP file) by making them believe it's a video game, subtitle, adult video, or cracked MS application file (among others). This ZIP is hosted on popular file-sharing platforms.

Once the file is opened, the malware shows a fake "Checking Application Compatibility" pop-up to distract users while it installs in the background. The malware then executes two processes: The first is for establishing persistence on the affected system, meaning the malicious script is scheduled to run daily and regularly; The second is for data stealing tasks.

Zscaler researchers [broke down the kinds of data](https://www.zscaler.com/blogs/security-research/new-php-variant-ducktail-infostealer-targeting-facebook-business-accounts) this PHP malware steals:

* Browser information (machine ID, browser version, user profiles). In particular, this malicious script is after sensitive data stored in Chrome browsers.
* Information stored in browser cookies
* Crypto account information from the *wallet.dat* file
* Data from various Facebook pages, such as API graph, Ads Manager, and Business, which are not limited to:
  + Accounts and their status
  + Ads payment cycle
  + Currency details
  + Funding source
  + Payment method
  + PayPal payment method (email address tied to PayPal accounts)
  + Verification status

Data stored on the C2 website is retrieved and used to conduct further information theft within the affected system. Additional stolen information is fed back to the C2 server.

## Stay safe from the Ducktail infostealer

As Ducktail uses clever social engineering tactics as the precursor to infection and information theft, it is more important than ever for Facebook users, especially those responsible for their business's Facebook accounts, to be wary of this information stealer's risks. Prevention is key.

* Never download files not relevant to your work, especially if you're using company-provided computers and mobile devices.
* Be wary of downloading files from popular file-sharing sites. Malware is usually shared there, too.
* If something seems too good to be true, it probably is. You'd be better off avoiding it.

If you suspect you've been infected by Ducktail malware and you're a Facebook Business administrator, check if any new users have been added to *Business Manager > Settings > People.* Revoke access to any unknown users with admin access.

Lastly, it is essential to have [security software you can count on](https://www.malwarebytes.com/) installed on your computer to protect against risky files that may still end up on the computer, regardless of one's vigilance. Remember that some malware campaigns don't need human intervention to infect systems. You have to watch out for those, too.

Stay safe!

文章来源: https://www.malwarebytes.com/blog/news/2022/10/this-new-php-based-ducktail-infostealer-is-now-after-crypto-wallets
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)