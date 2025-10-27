---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 13
url: https://buaq.net/go-156336.html
source: unSafe.sh - 不安全
date: 2023-04-01
fetch_date: 2025-10-04T11:19:27.319968
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 13

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

![](https://8aqnet.cdn.bcebos.com/522c76a4987b24be61fb38abca7ec00b.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 13

The GoodThe Biden administration signed a new executive order this week; the latest in an effort t
*2023-3-31 21:0:8
Author: [www.sentinelone.com(查看原文)](/jump-156336.htm)
阅读量:25
收藏*

---

## The Good

The Biden administration signed a new [executive order](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/03/27/executive-order-on-prohibition-on-use-by-the-united-states-government-of-commercial-spyware-that-poses-risks-to-national-security/) this week; the latest in an effort to prohibit U.S. government agencies from buying and using commercial [spyware](https://www.sentinelone.com/cybersecurity-101/what-is-spyware/) operationally. Targeting spyware’s increasing threat to national security and its implication in human rights abuse, the President [called](https://www.whitehouse.gov/briefing-room/statements-releases/2023/03/27/fact-sheet-president-biden-signs-executive-order-to-prohibit-u-s-government-use-of-commercial-spyware-that-poses-risks-to-national-security/) for an international coalition focused on combating spyware as a whole.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/commercial_spyware_biden_ban-scaled.jpg)

Governments across the globe have been known to collect troves of sensitive data for law enforcement and intelligence purposes. As use of spyware grew to meet these needs, the tools have inevitably been made available to opposing entities who have used them to meet their goals of abuse and oppression.

Spyware has long been marked as a high-level issue. The order emphasized that commercial spyware poses counterintelligence and security risks to the U.S. government if used by foreign governments or persons to gain access to U.S. computers and its data without authorization. Further, spyware is often used to collect information on [political figures, dissents, activists,](https://www.sentinelone.com/labs/modifiedelephant-apt-and-a-decade-of-fabricating-evidence/) academics, [journalists](https://www.sentinelone.com/labs/egomaniac-an-unscrupulous-turkish-nexus-threat-actor/), or members of marginalized communities for the purpose of intimidation.

While President Biden’s executive order does allow some exceptional use cases, it represents a clear step towards the clamp down on using commercial spyware for non-testing purposes. The impact of modern-day technology on government systems and human rights continues to grow and it is likely that more issues will arise from these intersections and highlight the continued need to regulate, oversee, and audit new advancements in technology.

## The Bad

A new comprehensive toolset is being sold to threat actors through private Telegram channels, SentinelLabs researchers [reported](https://www.sentinelone.com/labs/dissecting-alienfox-the-cloud-spammers-swiss-army-knife/) this week. Dubbed ‘AlienFox’, this toolset [enables](https://assets.sentinelone.com/sentinellabs22/s1_-sentinellabs_dis#page=1) actors to perform scans for misconfigured servers and extract API keys and secrets from AWS, Google, and Microsoft.

Analyzing three versions of AlienFox, researchers noted that the malware is being used to enumerate misconfigured hosts through security scanning services such as LeakIX and SecurityTrails. The AlienFox operators search for vulnerable services that are associated with widely-used frameworks such as Laravel, Drupal, Joomla, Magento, Opencart, Prestashop, and WordPress. Finally, the operators leverage various scripts provided in the toolset to [harvest credentials](https://www.sentinelone.com/cybersecurity-101/the-ultimate-guide-to-preventing-account-takeover-attacks/) and sensitive data from configuration files that are exposed on compromised servers of cloud-based email platforms.

Currently, the most recent version of the toolset has been able to establish persistence on a compromised Amazon Web Services (AWS) account, escalate privileges, and automate a spam campaign. This version also has added an account-checking capability along with an automated cryptocurrency wallet seed cracker for Ethereum and Bitcoin.

![Wallet seed generation in ETH.py](https://www.sentinelone.com/wp-content/uploads/2023/03/alienfox_3.jpg)

Wallet seed generation in *ETH.py*

The cyber defense community continues to see a rise in attacks on cloud services, particularly for the purpose of expanding subsequent threat campaigns. This is reflected in AlienFox’s highly modular nature, which is observed to be accommodating new features and improvements to attract new buyers and secure renewals from existing ones. Organizations can defend themselves from AlienFox tools by establishing strict configuration management and least privilege practices. Leveraging a [Cloud Workload Protection Platform (CWPP)](https://www.sentinelone.com/cybersecurity-101/cloud-security/) on virtual machines and containers is also key in detecting suspicious activity with the OS before full compromise can occur.

## The Ugly

An ongoing cyberattack has occupied the emergency response of international VoIP software developer, 3CX, for the past week as threat actors leverage a trojanized version of their 3CX DesktopApp. The full impact of the continuing attack is unknown so far, though 3CX’s suite of products service over 12 million users in 190 countries with big names like the UK’s [National Health Service](https://digital.nhs.uk/cyber-alerts/2023/cc-4291), Ikea, and American Express as part of their clientele.

A [report](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/) published by SentinelLabs researchers explains that use of the trojanized 3CX DesktopApp is just the first stage in the multi-stage supply chain attack currently tracked under the campaign name, SmoothOperator.

Infection begins with an MSI installer being downloaded from the official 3CX website or a user pushes an update to an already-installed desktop application. Following initial infection, the actors behind SmoothOperator take advantage of a DLL side-loading technique designed to pull icon file (ICO) payloads appended with Base64 data from GitHub. The malware uses these Base64 strings to download the final payload which then steals credentials and sensitive data housed in popular browsers.

3CX has since released a [security alert](https://www.3cx.com/community/threads/3cx-desktopapp-security-alert.119951/) announcing the imminent release of a new build. In the meantime, the company advises its users to uninstall the desktop app or switch over to the [PWA agent](https://www.3cx.com/blog/releases/web-client-pwa/) in the meantime. In a [blog post](https://www.3cx.com/blog/news/desktopapp-security-alert/) by 3CX posted the same day, the company divulged that the issue was seemingly associated with one of the bundled libraries compiled into the Electron Windows App via GIT.

The SmoothOperator supply chain campaign is a developing story and more details may come to light in coming days. SentinelOne customers are protected against SmoothOperator with [no additional action](https://www.youtube.com/watch?v=V8Eq3w0vRvQ) required.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-13-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)