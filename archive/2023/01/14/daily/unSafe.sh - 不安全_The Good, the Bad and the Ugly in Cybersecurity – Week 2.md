---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 2
url: https://buaq.net/go-145434.html
source: unSafe.sh - 不安全
date: 2023-01-14
fetch_date: 2025-10-04T03:51:03.069247
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 2

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

![](https://8aqnet.cdn.bcebos.com/e79478d9c92e8afd3abf8f7846d582e4.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 2

The GoodThe Federal Communications Commission (FCC) has proposed a number of reforms to breach rep
*2023-1-13 22:0:12
Author: [www.sentinelone.com(查看原文)](/jump-145434.htm)
阅读量:18
收藏*

---

## The Good

The Federal Communications Commission (FCC) has proposed a number of [reforms](https://docs.fcc.gov/public/attachments/FCC-22-102A1.pdf) to breach reporting requirements for U.S. telecoms providers to better protect customers and reduce the impact of security incidents.

With the severity and frequency of data breaches up since the rules were last updated in 2007, the new ones would eliminate the seven-day timeframe for reporting breaches, moving instead to reports filed within a 24 to 72 hour window. Further, providers would need to send data breach reports to agency staff as well as the FBI and Secret Service.

> FCC data breach rules are 15 years old. An update is way overdue. It starts now. <https://t.co/Lzul0Fkfja>
>
> — Jessica Rosenworcel (@JRosenworcel) [January 6, 2023](https://twitter.com/JRosenworcel/status/1611400050654986252?ref_src=twsrc%5Etfw)

The proposed updates follow several cyber intrusions on leading global telecoms providers. In 2022 alone, Australian telecoms giant, Optus, [disclosed](https://www.optus.com.au/about/media-centre/media-releases/2022/09/optus-notifies-customers-of-cyberattack) a data breach in which customer data was stolen, Comcast Xfinity faced their second data breach within a two-year span, and Verizon [notified](https://www.documentcloud.org/documents/23166980-verizon-important-account-information-prepaid-notice) their prepaid customers of account breaches leading to SIM swapping and unauthorized changes on their credit cards. The year before saw [T-Mobile](https://www.t-mobile.com/news/network/cyberattack-against-tmobile-and-our-customers) suffer a major breach that affected 77 million individuals and resulted in more than 100 million private records posted for sale in underground forums.

Telecommunications is an oft-targeted industry by threat actors for its direct access to their clients. Providers are earmarked by nation state-backed actors seeking to conduct espionage on political critics. For cyber criminals, providers hold the keys to customer PII (personally identifiable information) that is not only valuable amongst dark marketplace buyers, but also leveraged in social engineering attacks and [identity theft](https://www.sentinelone.com/blog/rise-in-identity-based-attacks-drives-demand-for-a-new-security-approach/). The FCC’s recent proposals will be a welcome update to U.S. data breach regulations with its next steps focusing on helping telecom carriers enforce stricter data security practices and [combat](https://www.sentinelone.com/blog/dealing-with-cyberattacks-a-survival-guide-for-c-levels-it-owners/) industry-wide vulnerabilities.

## The Bad

More than 1300 domains have been compromised this week in an ongoing threat using AnyDesk’s brand name to distribute Vidar info-stealer malware. The impersonation campaign banks on the popularity of the remote desktop solution, used by IT professionals globally for [remote connectivity](https://www.sentinelone.com/blog/stopping-cyberattacks-on-remote-workers-starts-at-the-endpoint/) and administrative tasks.

In this active campaign, those accessing the compromised domains are led to a fake, cloned AnyDesk site prompting them to download Vidar malware masquerading as a software installation `.zip` file. Then, they are redirected to a Dropbox folder which delivers the info-stealing malware payload – a technique used by the threat actor to evade detection since Dropbox is safelisted by many AV solutions.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/23-01-12-15-42-46-649_deco-scaled.jpg)

News outlets [report](https://www.bleepingcomputer.com/news/security/over-1-300-fake-anydesk-sites-push-vidar-info-stealing-malware/) that many of the domains have since been taken offline and for the sites that remain online, the Dropbox links no longer work. However, given that all 1300 domains lead to the same spoof site, the threat actors can keep the campaign going by simply updating the download URL address.

[Vidar](https://www.sentinelone.com/labs/info-stealers-how-malware-hacks-private-user-data/) malware has been around since 2018, responsible for [stealing credentials](https://www.sentinelone.com/blog/redline-stealer-malware/), saved passwords, crypto wallet and banking information, as well as browser history. Info-stealing malware has grown in popularity with cyber criminals as a dedicated means of prying legitimate credentials and cookies out of users’ hands.

Increasingly, info-stealer source code has been placed [up for sale](https://www.darkowl.com/blog-content/a-review-of-infostealers-sold-on-the-darknet/), bought by ransomware operators for low-cost, quick access and for use in [MFA-fatigue](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/) attacks. Users are best protected from the rise in info-stealing malware by downloading from trusted sites only, using an [endpoint protection security solution](https://www.sentinelone.com/platform/), avoiding browser-based password managers, and regularly clearing their browser cookies.

## The Ugly

This week, the pro-Russian hacktivist group known as [NoName057(16)](https://www.sentinelone.com/labs/noname05716-the-pro-russian-hacktivist-group-targeting-nato/) continues to launch [distributed denial-of-service (DDoS)](https://www.sentinelone.com/cybersecurity-101/what-is-denial-of-service-dos/) attacks against NATO countries and Ukraine.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/23-01-12-15-44-07-358_deco-scaled.jpg)

Linking their attacks tightly to political events, the pro-Russian group has been attributed to attacking the websites of Czech presidential candidates in the country’s 2023 election, the Polish government, and Latvia’s parliament. NoName057(16)’s attacks on Poland line up with the latter’s official recognition of Russia as a state sponsor of terrorism. Lithuania being caught in a dispute with Russia over train and port usage was cause enough for the hacktivists to attack the Lithuanian cargo and shipping sector.

SentinelLabs researchers [report](https://www.sentinelone.com/labs/noname05716-the-pro-russian-hacktivist-group-targeting-nato/) that the group makes instant messaging app, Telegram, their home base for communications and have used GitHub to host their DDoS tool website for free before their accounts were disabled for violating the company’s acceptable use policies.

NoName057(16) employs a collaborator payment program where the group coordinates with volunteers to carry out its attacks on targets. This model is lucrative to those who are compelled to join attacks for financial gain rather than for political reasons. Top DDoS performers are rewarded in [cryptocurrency](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) and followers are encouraged to add skin to the game by contributing more technical resources for the next attack.

Though researchers say that the DDoS attacks from NoName057(16) have little to no wider consequence, volunteer-powered attacks with modelized incentive are a cause for concern as threat actors continue to take advantage of a highly volatile political landscape.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-2-4/
 如有侵权请联系:admin#unsafe.sh

© [unSa...