---
title: Fodcha Is Coming Back, Raising A Wave of Ransom  DDoS
url: https://blog.netlab.360.com/fodcha-is-coming-back-with-rddos/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2022-11-01
fetch_date: 2025-10-03T21:26:24.243749
---

# Fodcha Is Coming Back, Raising A Wave of Ransom  DDoS

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

[![360 Netlab Blog - Network Security Research Lab at 360 icon](/content/images/size/w30/2019/02/netlab_xs-2.png)
360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com)

—

Fodcha Is Coming Back, Raising A Wave of Ransom DDoS

Share this

[Botnet](/tag/botnet/)

# Fodcha Is Coming Back, Raising A Wave of Ransom DDoS

* [![Alex.Turing](/content/images/2019/06/turing.PNG)](/author/alex/)
* [![Hui Wang](/content/images/2017/05/WechatIMG1.jpeg)](/author/huiwang/)
* [![YANG XU](/content/images/2019/04/head.jpg)](/author/xuy1202/)

#### [Alex.Turing](/author/alex/), [Hui Wang](/author/huiwang/), [YANG XU](/author/xuy1202/)

Oct 31, 2022
• 16 min read

# Background

On April 13, 2022, 360Netlab first disclosed the `Fodcha` botnet. After our article was published, Fodcha suffered a crackdown from the relevant authorities, and its authors quickly responded by leaving `"Netlab pls leave me alone I surrender"` in an updated sample.No surprise, Fodcha's authors didn't really stop updating after the fraudulent surrender, and soon a new version was released.

In the new version, the authors of Fodcha redesigned the communication protocol and started to use `xxtea` and `chacha20` algorithms to encrypt sensitive resources and network communications to avoid detection at the file & traffic level; at the same time, a dual-C2 scheme with `OpenNIC domain` as the primary C2 and `ICANN domain` as the backup C2 was adopted.

Relying on the strong N-day vulnerability integration capabilities, the comeback of Focha is just as strong as the previous ones. In our data view, in terms of scale, Fodcha has once again developed into a massive botnet with more than `60K` daily active bots and `40+ C2 IPs`, we also observed it can easily launch more than 1Tbps DDos traffic; in terms of attacks, Fodcha has an average of `100+` daily attack targets and more than `20,000` cumulative attacks, on October 11, Fodcha hit its record and attacked `1,396` unique targets in that single day.

While Fodcha was busy attacking various targets, it has not forgot to mess with us, we saw it using `N3t1@bG@Y` in one of it scan payload.

# Timeline

Backed by our `BotMon` systems, we have kept good track of Fodcha's sample evolution and DDoS attack instructions, and below are the sample evolution and some important DDoS attack events we have seen. (Note: The Fodcha sample itself does not have a specific flag to indicate its version, this is the version number we use internally for tracking purposes)

* On January 12, 2022, the first Fodcha botnet sample was captured.
* April 13, 2022, Disclosure of the [Fodcha](https://blog.netlab.360.com/fodcha-a-new-ddos-botnet/) botnet, containing versions V1, V2.
* April 19, 2022, captured version V2.x, using `OpenNIC's TLDs` style C2
* April 24, 2022, version V3, using xxtea algorithm to encrypt configuration information, adding `ICANN's TLDs` style C2, adding `anti-sandbox` & `anti-debugging` mechanism.
* June 5, 2022, version V4, using structured configuration information, `anti-sandboxing` & `anti-debugging` mechanism were removed.
* July 7, 2022, version V4.x with an additional set of `ICANN C2`.
* On September 21, 2022, a well-known cloud service provider was attacked with traffic exceeding `1Tbps`.

# Botnet Size

In April, we confirmed that the number of Fodcha's global daily live bots was about `60,000` [(refer to our other article)](https://blog.netlab.360.com/fodcha-a-new-ddos-botnet/). We don’t have accurate number of the current size, but suspect that the number of current active bots has not dropped, maybe more than `60,000` now.

There is a positive relationship between the size of a botnet and the number of C2 IPs, and the most parsimonious view is that "the larger the botnet, the more C2 infrastructure it requires. In April, there were `10 c2s` to control the `60,000` bots; After that, we observed that the IPs corresponding to its C2 domains continued to increase. Using a simple dig command to query the latest C2 domain name `yellowchinks.dyn`, we can see it resolves to `44 IPs`.

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2infras.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2infras.png)

One likely reason for this is that their botnet is so large that they need to invest more IP resources in order to have a reasonable ratio between Bots and C2s to achieve load balancing.

# DDoS Statistics

More C2 IPs cost more money, and it seems that the business is good as it has been very active launching ddos attacks.We have excerpted the data from June 29, 2022 to the present, and the attack trends and target area distribution are as follows.

[![](https://blog.netlab.360.com/content/images/2022/10/image.min-1.png)](https://blog.netlab.360.com/content/images/2022/10/image--1-.png)

We can see that the ddos attacks has been non-stop, and China and US have the most targets.

The time distribution of the attack instructions within 7 days is shown below, which shows that Fodcha launched DDoS attacks throughout 7 \* 24 hours, without any obvious working time zone.

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_instimezone.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_instimezone.png)

# Sample Analysis

We have divided the captured samples into four major versions, of which V1and `V2` have been analyzed in the previous blog, here we select the latest `V4` series samples as the main object of analysis, their basic information is shown below.

```
MD5: ea7945724837f019507fd613ba3e1da9
ELF 32-bit LSB executable, ARM, version 1, dynamically linked (uses shared libs), stripped
LIB: uclibc
PACKER: None
version: V4

MD5: 899047ddf6f62f07150837aef0c1ebfb
ELF 32-bit LSB executable, ARM, version 1 (SYSV), statically linked, stripped
Lib: uclibc
Packer: None
Version: V4.X
```

When Fodcha's Bot executes, it will first check `the operating parameters`, `network connectivity`, `whether the "LD_PRELOAD" environment variable is set`, and `whether it is debugged`. These checks can be seen as a simple countermeasure to the typical emulator & sandbox.

When the requirements are met, it first decrypts the configuration information and print “snow slide” on the Console, then there are some common host behaviors, such as single instance, process name masquerading, manipulating watchdog, terminating specific port processes, reporting specific process information, etc. The following will focus on the decryption of configuration information, network communication, DDoS attacks and other aspects of Fodcha.

## Decrypting configuration information (Config)

Fodcha uses a side-by-side Config organization in `V2.X` and `V3`, and a structured Config organization in `V4` and `V4.X`. The following figure clearly shows the difference.

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_disconfig.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_disconfig.png)

Although the organization of Config is different, their encryption methods are the same. As we can see by the constants referenced in the code snippet below, they use the xxtea algorithm with the key `PJbiNbbeasddDfsc`.

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_xxtea.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_xxtea.png)

After inversion, we wrote the following `IDAPYTHON` script to decrypt the configuration information.

```
# md5: ea7945724837f019507fd613ba3e1da9
# requirement: pip install xxtea-py
# test: i...