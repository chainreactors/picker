---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 3
url: https://buaq.net/go-146345.html
source: unSafe.sh - 不安全
date: 2023-01-21
fetch_date: 2025-10-04T04:27:12.857401
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 3

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

![](https://8aqnet.cdn.bcebos.com/8bef46d9ed854daf59a7f28e72673c2b.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 3

The GoodThe U.S. Department of Justice this week arrested and charged Anatoly Legkodymov, a 40-yea
*2023-1-20 22:0:42
Author: [www.sentinelone.com(查看原文)](/jump-146345.htm)
阅读量:25
收藏*

---

## The Good

The U.S. Department of Justice this week [arrested](https://www.justice.gov/usao-edny/pr/founder-and-majority-owner-bitzlato-cryptocurrency-exchange-charged-unlicensed-money) and charged Anatoly Legkodymov, a 40-year old Russian national, with offenses related to processing more than $700 million of illicit funds, including ransomware proceeds.

Legkodymov, who also went by the online names of ‘Gandalf’ and ‘Tolik’, was a senior executive and majority shareholder of [Bitzlato](https://bitzlato.com/), a cryptocurrency exchange that authorities say knowingly aided [ransomware actors](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) and other cybercriminals to process illicit funds.

![Legkodymov bitzlato](https://www.sentinelone.com/wp-content/uploads/2023/01/GBU2023_wk3_2.jpg)

According to court documents, Bitzlato marketed itself as requiring minimal identification from users, specifying that “neither selfies nor passports [are] required” and knowingly fostered the perception that it was a safe haven for funds used for and resulting from criminal activities.

Bitzlato was heavily involved with cryptocurrency transactions through the notorious darknet market [Hydra](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-15-3/), which was taken down by cops in April 2022. It’s alleged that Bitzlato received more than $15 million in ransomware proceeds and transacted over $700 million in cryptocurrency with Hydra. The U.S. government [says](https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering) that after Hydra’s shuttering, Bitzlato continued to facilitate transactions for Russia-connected darknet markets such as BlackSprut, OMG!OMG!, and Mega.

Legkodymov, who was arrested in Miami on Tuesday, faces up to 5 years jail time if convicted of operating an illegal money transmitting business. As for Bitzlato, European authorities have conducted a separate operation to seize and dismantle its digital infrastructure, taking the service out of the cybercriminal ecosystem once and for all.

## The Bad

Git users are being [urged](https://about.gitlab.com/releases/2023/01/17/critical-security-release-gitlab-15-7-5-released/#critical-security-issues-in-git) to update to the latest release following news of two critical remote code execution bugs this week. The RCEs could allow attackers to exploit heap-based buffer overflow flaws and execute arbitrary code.

[CVE-2022-41903](https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq) and [CVE-2022-23521](https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89) were patched on Wednesday, but a third Windows-specific vulnerability in the Git GUI tool, [CVE-2022-41953](https://github.com/git-for-windows/git/security/advisories/GHSA-v4px-mx59-w99c), is still awaiting a fix. Users are being recommended not to use the tool until an update becomes available.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/GBU2023_wk3_3.jpg)

Mitigations for the two patched vulnerabilities for those that cannot immediately update are:

* Disable ‘git archive’ in untrusted repositories or avoid running the command on untrusted repos
* If ‘git archive’ is exposed via ‘git daemon,’ disable it when working with untrusted repositories by running the `git config --global daemon.uploadArch false` command

Git is used widely in enterprises to manage development projects. The researchers that discovered the flaws in a sponsored audit [pointed out](https://x41-dsec.de/security/research/news/2023/01/17/git-security-audit-ostif/) that vulnerabilities in Git could allow attackers to compromise source code repositories or developer systems and potentially result in security breaches on a large scale.

The researchers went on to say that the sheer size of the Git codebase made it challenging to address all potential instances of the issues they discovered, and they made a number of recommendations to Git’s maintainers to improve code security.

In a separate blog post, GitHub [says](https://github.blog/2023-01-17-git-security-vulnerabilities-announced-2/) that it scanned all repositories on GitHub.com to confirm that no evidence existed that GitHub had been used as a vector to exploit any of the discovered vulnerabilities.

## The Ugly

It’s another tough week for password managers as the recent troubles faced by [LastPass](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-49-4/) have been followed by [news](https://techcrunch.com/2023/01/15/norton-lifelock-password-manager-data/?guccounter=1) of breaches of Norton Lifelock customer accounts.

Norton’s parent company, Gen Digital, has [advised](https://web.archive.org/web/20230113191952/ago.vermont.gov/blog/2023/01/09/nortonlifelock-gen-digital-data-breach-notice-to-consumers/) customers that a likely [credential stuffing attack](https://www.sentinelone.com/blog/7-ways-hackers-steal-your-passwords/) was used to compromise thousands of customer accounts in December. Customers that use the same password for different sites and services are susceptible to credential stuffing attacks if a reused password is exposed or leaked from a breach of one of those sites.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/GBU2023_wk3_1.jpg)

Suspicious activity began around December 1st and was followed by a large number of failed login attempts on December 12th. On January 9th, Gen Digital sent notices to around 6,500 customers of its password manager advising customers that “an unauthorized party likely has knowledge of the email and password you have been using with your Norton account…and your Norton Password Manager”. The advisory went on to recommend customers change their passwords with Norton Lifelock and elsewhere immediately.

The company says that intruders used a list of usernames and passwords obtained from another source such as the [darknet](https://www.sentinelone.com/blog/20-years-in-the-dark-the-dark-web-turns-twenty-what-does-this-mean-for-a-ciso/) to attempt to log into Norton customer accounts. Gen Digital insist that Norton Lifelock’s own systems were not compromised

Despite the bad news, password managers remain an effective first line of defense against account takeovers and compromises so long as users follow recommended procedures. These include using unique passwords for every site, ensuring master passwords are not [easily guessable](https://www.sentinelone.com/blog/7-signs-weak-password/), and employing [2FA authentication](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/) wherever possible.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-3-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)