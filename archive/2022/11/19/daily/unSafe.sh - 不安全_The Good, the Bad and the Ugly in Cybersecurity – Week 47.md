---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 47
url: https://buaq.net/go-136288.html
source: unSafe.sh - 不安全
date: 2022-11-19
fetch_date: 2025-10-03T23:11:23.659073
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 47

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

![](https://8aqnet.cdn.bcebos.com/101cef83c49cc8f2e8fa624a7d4f5fc5.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 47

The GoodU.S. officials have finally arrested and charged long-wanted suspected cyber criminal Vyac
*2022-11-18 22:0:14
Author: [www.sentinelone.com(查看原文)](/jump-136288.htm)
阅读量:23
收藏*

---

## The Good

U.S. officials have finally arrested and charged long-wanted suspected cyber criminal Vyacheslav Penchukov, a Ukrainian national they allege acted as a ringleader of JabberZeus – one of the most notorious cybergangs on record.

According to the [FBI](https://archives.fbi.gov/archives/news/pressrel/press-releases/international-cooperation-disrupts-multi-country-cyber-theft-ring), the JabberZeus gang has stolen upwards of $70 million in both the United States and across Europe in recent years. The crime group leveraged banking trojan Zeus malware and [botnets](https://www.sentinelone.com/cybersecurity-101/botnets/) to collect bank account numbers, PIN numbers, passwords, RSA SecureID tokens, and other personal information. After JabberZeus gained access to victims’ bank accounts and drained their funds, the money was then transferred out of the U.S. through a network of mule accounts. JabberZeus has been known to target small to medium-sized entities including businesses, municipalities, and churches.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/jabberzeus3__1__pdf.png)

This arrest comes as a result of U.S. law enforcement playing out the long game. Having been closely monitored by cybercrime analysts as early as 2009, Penchukov (*aka* “Tank”) was arrested by the Swiss Federal Office of Justice (FOJ) when he eventually travelled to Geneva last month. Penchukov’s extradition to the U.S. was approved this week.

Penchukov has been charged with conspiracy to participate in racketeering activity, bank fraud, conspiracy to commit computer fraud and identity theft, and aggravated identity theft together with [eight](https://archives.fbi.gov/archives/omaha/press-releases/2014/nine-charged-in-conspiracy-to-steal-millions-of-dollars-using-zeus-malware) other suspects. Another alleged member of JabberZeus, [Maksim Yakubets](https://www.fbi.gov/wanted/cyber/maksim-viktorovich-yakubets) (*aka* “Aqua”), currently has a $5 million bounty on his head offered by the FBI as reward for information leading to his arrest and conviction.

## The Bad

This week, security researchers disclosed multiple vulnerabilities and bypass methods found in multi-cloud and application delivery firm F5’s BIG-IP and BIG-IQ devices. The flaws, if successfully leveraged, could compromise affected systems running a customized distribution of CentOS.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/22-11-18-00-06-45-697_deco-scaled.jpg)

[Researchers](https://www.rapid7.com/blog/post/2022/11/16/cve-2022-41622-and-cve-2022-41800-fixed-f5-big-ip-and-icontrol-rest-vulnerabilities-and-exposures/) say the two vulnerabilities could be exploited to achieve remote access. [CVE-2022-41622](https://support.f5.com/csp/article/K94221585) (CVSS 8.8) is assigned to flaws in BIG-IP and BIG-IQ vulnerable to unauthenticated remote code execution via cross-site request forgery (CSRF). [CVE-2022-41800](https://support.f5.com/csp/article/K13325942) (CVSS 8.7) describes a bug in the appliance mode, iControl REST, which makes it vulnerable to authenticated remote code execution (RCE) via RPM spec injection.

Attackers exploiting the flaws could gain persistent root access to a device’s management interface though this would require an administrator to visit a malicious website while in an active session. F5 [explained](https://support.f5.com/csp/article/K05403841) that the vulnerabilities cannot be exploited without an attacker having first moved past existing barriers using unknown mechanisms. Needing such specific criteria to exist, F5 notes that these methods would be very difficult to exploit, but could lead to complete compromise should it occur.

So far, the company is not aware of any incidents involving these vulnerabilities, though a detailed [proof of concept](https://github.com/rbowes-r7/refreshing-soap-exploit) has since been released. Impacted customers have been advised by F5 to request and install the hotfix specific to their product version.

## The Ugly

Concerns over the prevalence of the [Log4Shell](https://www.sentinelone.com/blog/cve-2021-44228-staying-secure-apache-log4j-vulnerability/) RCE vulnerability continue nearly a year after its initial disclosure. CISA and the FBI [reported](https://www.cisa.gov/uscert/ncas/alerts/aa22-320a) this week than an unnamed Iranian-backed APT actor used Log4Shell to compromise a U.S. Federal Civilian Executive Branch (FCEB) organization over a period of months.

A CISA investigation found that as early as February 2022, the threat actor exploited the notorious vulnerability in an unpatched [VMware Horizon](https://www.sentinelone.com/labs/log4j2-in-the-wild-iranian-aligned-threat-actor-tunnelvision-actively-exploiting-vmware-horizon/) server to install [XMRig](https://www.sentinelone.com/blog/is-cryptojacking-going-out-of-fashion-or-making-a-comeback/) crypto mining software. Then, shifting [laterally into the domain controller](https://www.sentinelone.com/blog/top-10-ways-to-protect-your-active-directory/) (DC), they compromised credentials and implanted Ngrok reverse proxies on several hosts to establish persistence in the FCEB agency’s network.

[![](https://www.sentinelone.com/wp-content/uploads/2022/11/Screenshot-2022-11-18-at-10.31.15-AM.jpg)](https://infosec.exchange/%40veronicabp/109363327755278610)

The joint advisory urged all organizations using VMware systems that were not immediately patched or mitigated with workarounds to assume breach and begin [threat hunting](https://www.sentinelone.com/blog/six-steps-to-successful-and-efficient-threat-hunting/) efforts after patching against Log4Shell.

Log4Shell is a [critical vulnerability](https://www.sentinelone.com/lp/log4j-log4shell-cve-2021-44228-staying-secure/) allowing an attacker to run unauthorized code on an affected server, access parts of a network that is not connected to the internet, and [move laterally](https://www.sentinelone.com/cybersecurity-101/lateral-movement/) across a network to access internal systems storing sensitive data. Scoring a 10 on NIST’s severity scale, Log4Shell is as critical as a vulnerability can get and it continues to be abused by various threat actors since it first made global headlines in December 2021.

Late last year, CISA had issued [warnings](https://www.cisa.gov/news/2021/12/11/statement-cisa-director-easterly-log4j-vulnerability) that the vulnerability had the potential to affect an unprecedented number of devices. In June of this year, the Cyber Safety Review Board (CSRB) published a formal [review](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf) of the December Log4j event remarking that the endemic flaw “remains deeply embedded in systems” and that “organizations should be prepared to address Log4j vulnerabilities for years to come”.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-47-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)