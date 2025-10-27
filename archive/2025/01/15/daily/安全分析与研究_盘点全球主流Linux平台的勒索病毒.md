---
title: 盘点全球主流Linux平台的勒索病毒
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489981&idx=1&sn=f92b58bb6a06cfb2d3596dee93f226ab&chksm=902fb695a7583f834b08a2fe2ada4911c36f0915057d542505372673f82224ea3483bf5bdbc0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-01-15
fetch_date: 2025-10-06T20:10:54.892728
---

# 盘点全球主流Linux平台的勒索病毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpwiccNF0e7AniajRvWMWYYibLk9NvSkf6X0GmGmTnBfibvVbVsCRic65waAg/0?wx_fmt=jpeg)

# 盘点全球主流Linux平台的勒索病毒

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言

美国网络信息安全公司CrowdStrike在2021年的攻击数据报告中，总结与2020年度相比，2021年度针对Linux系统的恶意软件增加了35%，其实最近几年针对Linux平台下的恶意软件数据一直在不断的增加，这些恶意软件主要包含僵尸网络、挖矿病毒、勒索病毒、远控木马等，随着云计算平台的发展，针对Linux平台进行攻击的恶意软件家族会越来越多。

几年前Sodinokibi(REvil)勒索病毒黑客组织的14名主要成员被俄罗斯政府联邦安全局(FSB)逮捕，突袭执法行动，当局扣押了数量可观的赃款赃物，包括超过4.26亿卢布（包含加密货币，约合3550万元人民币）、60万美元和50万欧元现金，20辆豪华汽车，并查封了作案所使用的电脑设备以及加密货币电子钱包。

虽然Sodinokibi(REvil)部分成员被捕了，这款勒索病毒己经消亡了，就像此前的GandCrab一样，但是勒索攻击仍然会继续，马上会有新的勒索病毒家族代替Sodinokibi勒索病毒，勒索病毒黑客组织会持续开发新的勒索病毒，发起新的攻击，未来几年勒索攻击仍然将是全球最大的网络安全威胁之一。

笔者给大家盘点了针对Linux平台的勒索病毒家族，这些都是全球主流的勒索病毒家族，每一款勒索病毒家族后面可能都是一个技术相对成熟的黑客组织，未来这些勒索病毒黑客组织还会持续针对Linux平台发起攻击活动，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpaab1VRPqzJNgWRQicPia5pGzrKoUwaX4jJTiaytFfcXYvECkUTIV8nbAA/640?wx_fmt=png)

勒索病毒

**eCh0raix勒索病毒**

eCh0raix勒索病毒是一款专门针对NSA装置而设计的勒索病毒，采用Go/Golang语言编写，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpj0CXlPCLs7Bwzc5dFj5Wc5leD3SDW5tS6ib3ialWzTRVasK8ENbQplzg/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpIxDEDQ3v3xA43rTv2echz2k2E6Jibkv7fb8giaJ8BxJr87317OY1FTLw/640?wx_fmt=png)

**Babuk勒索病毒**

Babuk勒索病毒，也被称为Babyk，该勒索病毒被用于针对企业进行双重勒索攻击活动，不仅加密企业的数据，而且还会窃取企业的核心数据，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpe9r8HFpNttYDln03Sc9TM3MphYelUupygMJKdOktL0ItibrDmNroib5w/640?wx_fmt=png)

**TellYouThePass勒索病毒**

TellYouThePass勒索病毒，曾经利用永恒之蓝漏洞和Apache Log4j CVE-2021-44228漏洞发起攻击，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpEHxSuBVZrrHHLe9ibJAiadbWRtT5vkqgVu0GBQHc2ehWbfe9rY65I1Og/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpMeB1LzcDsXjJOibBCLuwn5LLKeuU3jLdD1Fepy6lxR6cvQRxbPwvPTg/640?wx_fmt=png)

**BlackCat勒索病毒**

BlackCat勒索病毒采用了Rust语言编写，通过命令行调用，可灵活配置绝大部分参数，同时采用RSA+AES/ChaCha20的方式加密磁盘文件，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpSTafX6gEgwQBGYibl1lHRIPpiaicSXOhS7T6TeibQOlf7UcgILutopQ4tA/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUp3XiceyvoFoudOhZYpk8n0iaqEbaVNS9K5Fg2r9Elkib7M7kgXNWUf7HWw/640?wx_fmt=png)

**HelloKitty勒索病毒**

HelloKitty勒索病毒，曾针对SonicWall设备发起攻击，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpLcXsJ2gD40xL6v4hXibkSibvh6lx2SDyqswYJgAoYThUdXVTQnbTliaicg/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpYSHVnFQkoNh4LPGAgouSkzXoodEtGbs89RWLxFDWP27QzLKXaSgChQ/640?wx_fmt=png)

**DarkSide勒索病毒**

DarkSide勒索病毒曾对美国燃油管道系统Colonial Pipeline发起勒索攻击，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpGUkJIXrhQ505tObibRSyNu9Zem0nWDYhYZiakdYc7XInsbD05FAzcOuA/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpuqfRJWCZ0CrX6ebEWGicqc47UbxibYSSCXrEVEOVW9O1gTmljy6octzg/640?wx_fmt=png)

**Sodinokibi(REvil)勒索病毒**

Sodinokibi(REvil)勒索病毒黑客组织曾利用0day漏洞，通过Kaseya VSA发起大规模供应链攻击行动，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpgnZlWAd3xr0vegUH60z3rCBiaCRGJRWpCdgKPkPib0F6ZFhZ0N5dddkA/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpE1FluevgJIUIWBMWNquAKIoOKDicXlBO4Y2da5zz6UpOoPB1vterJaw/640?wx_fmt=png)

**DarkRadiation勒索病毒**

DarkRadiation勒索病毒是一款针Linux系统平台的新型勒索病毒，此次攻击的大部分组件主要针对 Red Hat 和 CentOS Linux 发行版，但是在某些脚本中也包含基于 Debian 的 Linux 发行版，同时还会对Docker应用进行相关的攻击，该勒索病毒样本主要采用Bash编写，生成的勒索提示信息，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpjK3sTcT9zUianxDZ5XQ0VC78tn5t6YReLnk37RJ3FC5svsDEcoBNjsw/640?wx_fmt=png)

**Hive勒索病毒**

Hive勒索病毒采用GO语言编写，加密算法使用AES+RSA，同时这款勒索病毒也采用了“双重”勒索的模式，通过在暗网上公布受害者数据，来逼迫受害者交纳赎金，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUp5BuKwJicnTiawdZdKzziccKBlV9huvZqJTH7dNRMCcNbXuOJMw2ibXicGEA/640?wx_fmt=png)

生成的勒索提示信息文件，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpEOeg2L6ZaNbsXDJNibJ2Fqd8B0UWMGcQyu3y5DsVZlfv4gfmUngUdvw/640?wx_fmt=png)

**AvosLocker勒索病毒**

AvosLocker勒索病毒在2021年6月底被发现，全球各地都有企业遭受攻击，赎金要求从5万美元到7.5万美元不等，加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUp1kXm9FgMxcC9tO6AXq5ALcErQYiaJMy1YB180xvch3Fl1qEIicV5Y9UQ/640?wx_fmt=png)

生成的勒索提示信息，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpWOmEFWd2bCtSBvnmsTMK1pBQt0Cpz7RYpXqLkdOjd0Uz1nYkvmO0BQ/640?wx_fmt=png)

**SFile勒索病毒**

SFile勒索病毒又称Escal，最早出现于2020年,近期发现了它的Linux版，加密后的文件后缀名为：nuctech-gj0okyci，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpAYqhQfdpJocsouZybe3Nuic7QyxWCornibDLs7qSgcz9e9PdLibI7VL3w/640?wx_fmt=png)

之前比较流行的Satan勒索病毒、XBash勒索病毒、Lucky勒索病毒等，有大部分以前主要都是针对Windows平台的，后面慢慢发展到了Linux平台，通过这些针对Linux平台的勒索病毒家族可以预见，未来会有越来越多的勒索病毒黑客组织开始针对Windows和Linux两个平台同时发起勒索攻击。

总结

一些人不太了解恶意软件，总是会觉得现在恶意软件很少了，而且一些人还会认为说Linux、Mac平台没有病毒了，其实不管是Windows、Linux平台，还是Mac平台，恶意软件已经无处不在，只是目前Windows平台仍然占据全球大部分的市场份额，攻击Windows产台能给黑客带来更多的收益，所以针对Windows平台的恶意软件会更多。

**随着云计算或物联网的发展，当某个平台逐渐成为主流之后，这个平台就会成为黑客攻击的重点，针对这个平台的恶意软件就会增多，所以不管哪个平台，其实都是一样的，没有说哪个平台更安全这种说法，只是黑客还没有针对这个平台发起攻击吧了，当全球大部分的黑客将目标全对准一个平台的时候，这个平台就将成为全球黑客攻击的“耙子”，就不存在说某个平台安不安全的问题了。**

未来随着云计算的发展，5G以及物联网平台的普及，针对Linux平台的恶意软件未来肯定会越来越多，而且**随着Mac个人市场的不断增加，针对Mac平台攻击的恶意软件也会不断增多**，目前大家看到的针对Linux平台的恶意软件大多数以挖矿、僵尸网络病毒为主，其实还有很多针对Linux平台的恶意软件，包含勒索病毒、远控木马类等。

笔者深度跟踪和研究过上百种主流的勒索病毒黑客组织，现在勒索病毒攻击手法多种多样，并且通过之前跟踪的一些大型的勒索病毒黑客组织的攻击活动，可以发现勒索病毒黑客组织APT式定向化勒索攻击的技术手段越来越高，APT式定向勒索攻击会成为未来针对企业进行勒索攻击的主流方式，同时针对个人的勒索攻击也在逐步流行，勒索病毒黑客组织无时无刻不在寻找着新的攻击目标，可以预测，勒索病毒攻击在未来几年仍然将是全球最大的网络威胁，不管是个人还是企业，一定要提高安全意识。

[《勒索病毒专题报道》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247486870&idx=1&sn=353edf9d6c8d67154b719a075b02b41e&scene=21#wechat_redirect)

如果对勒索病毒研究感兴趣的，可以加入笔者的勒索病毒知识星球，里面全部都是笔者最近几年收集整理的各种勒索病毒相关知识，包含全球主流的勒索病毒家族的分析报告、威胁情报、攻击技巧等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUr7QMa5TJW2FMZ8MEJwVUpXz0AybYBCZwjWwsNRWZicJStnLvFcTNsk8zqsPXfQbJASKrMtGAvAPw/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAMNWnNxuKxOiazwV340ZWLNabkxDjrOKQTRyphGJxKHGwlLlEy3vCicyg/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过