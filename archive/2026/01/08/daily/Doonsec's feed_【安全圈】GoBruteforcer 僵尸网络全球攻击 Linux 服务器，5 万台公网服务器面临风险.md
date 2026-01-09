---
title: 【安全圈】GoBruteforcer 僵尸网络全球攻击 Linux 服务器，5 万台公网服务器面临风险
url: https://mp.weixin.qq.com/s/NBUe4Dd_wtmcqdx4WBnkJw
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:28:46.529165
---

# 【安全圈】GoBruteforcer 僵尸网络全球攻击 Linux 服务器，5 万台公网服务器面临风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaagd6b1vg9wuP9ibiaVZiaLjrKppLBusKdmoshmxpeG2WQKvKNcxXbib5GYYNTxhoWKgVZDpDEYr3HtQ/0?wx_fmt=jpeg)

# 【安全圈】GoBruteforcer 僵尸网络全球攻击 Linux 服务器，5 万台公网服务器面临风险

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

僵尸网络

 一款名为**GoBruteforcer**的高复杂度 Go 语言僵尸网络，正针对全球范围内的 Linux 服务器发起猛烈攻击，通过暴力破解手段尝试获取 FTP、MySQL、PostgreSQL 及 phpMyAdmin 等公网暴露服务的弱密码。

 Check Point Research近期记录到该恶意软件的 2025 年变种版本，其技术水平较之前版本实现大幅升级，已成功攻陷数万台服务器。

该僵尸网络采用模块化感染链架构，核心组件包含网页后门、下载器、互联网中继聊天（IRC）僵尸程序以及暴力破解模块。

据切克波因特的分析数据显示，全球超**5 万台公网暴露服务器**或面临高布鲁特福瑟攻击风险，目前有近 570 万台 FTP 服务器、223 万台 MySQL 服务器及 56 万台 PostgreSQL 服务器在默认端口上暴露。

#### 人工智能生成服务器配置成攻击推手

本轮GoBruteforcer攻击浪潮的爆发，**主要源于两大关键因素：一是大量运维人员直接复用人工智能生成的服务器部署示例，这类配置模板普遍存在通用用户名与弱默认密码问题；二是 XAMPP 等老旧网站集成环境仍被广泛使用，其搭载的各类服务缺乏基础加固措施。**

研究人员发现，该僵尸网络在暴力破解的凭证列表中，大量使用 “appuser”“myuser” 等通用运维用户名，而这些用户名恰好是大型语言模型在生成数据库配置示例时最常推荐的默认名称。

切克波因特的调查显示，高布鲁特福瑟使用的凭证列表，与一个包含 1000 万条泄露密码的数据库存在约**2.44% 的重合度**。

尽管这一匹配成功率看似较低，但庞大的暴露服务基数，使得暴力破解攻击对威胁行为体而言具备极高的经济效益。谷歌 2024 年《云威胁态势报告》指出，在遭攻陷的云环境中，**47.2% 的初始入侵路径均源于弱密码或缺失身份验证机制**，这也印证了此类攻击手段的可行性。

僵尸网络的命令与控制服务器会下发包含 200 组凭证的列表用于暴力破解任务，且攻击配置文件每周会更新数次。

密码列表的生成逻辑十分固定，仅基于 375-600 个常用弱密码构成基础库，再衍生出 “appuser1234”“operatoroperator” 等基于用户名变体的密码组合。

相较于 2023 年首次被记录的早期版本，2025 年变种版本实现多项重大技术升级：其 IRC 僵尸程序组件已完全基于 Go 语言重构，并使用加布勒混淆工具（Garbler）进行深度代码混淆，彻底取代了原先基于 C 语言的开发架构。

该恶意软件还新增进程伪装技术，通过调用`prctl`系统调用将自身进程名修改为 “init”，并对二进制文件进行覆盖处理，以此躲避安全检测。

研究人员还发现一个以加密货币敛财为目标的攻击活动，威胁行为体在攻陷服务器后，会部署额外的 Go 语言工具集，其中包含针对波场（TRON）及币安智能链的挖矿程序与钱包窃取工具。

在一台被攻陷的服务器上，调查人员提取到一个包含约 2.3 万个波场钱包地址的文件，并通过链上交易数据分析证实，这批攻击已成功实现经济收益。

该僵尸网络通过多重机制保障自身的抗打击能力：内置备用 C2 服务器地址、基于域名的故障恢复路径，以及将已感染主机升级为分发节点或 IRC 中继服务器的功能。

IRC 僵尸程序模块每日可完成两次更新，暴力破解组件则通过与系统架构匹配的 Shell 脚本下载，并在执行前校验文件的 MD5 哈希值，确保恶意程序未被篡改。

#### 攻击兼具广谱性与针对性

GoBruteforcer的攻击活动同时具备**广谱扫射**与**定向行业打击**的双重特征。通用型攻击活动会组合使用通用运维用户名与标准弱密码发起试探；而专项攻击任务则会采用 “cryptouser”“appcrypto” 等加密货币相关用户名，或 “wpuser” 这类针对 WordPress 系统的专属凭证。

该恶意软件还会针对性攻击 XAMPP 集成环境 —— 这一热门开发工具通常默认启用 FTP 服务，并将 FTP 根目录映射到公网可访问的网页路径，存在严重安全隐患。

僵尸网络的架构设计具备高效攻击能力，受感染主机每秒可扫描约 20 个 IP 地址，且在 FTP 攻击任务执行期间，能将带宽消耗控制在较低水平：出站流量约 64 千比特 / 秒，入站流量约 32 千比特 / 秒。

攻击线程池的规模会根据目标服务器的 CPU 架构动态调整：64 位系统上会运行 95 个并发暴力破解线程，32 位系统则会适配为更少的线程数。

该恶意软件还具备智能目标筛选能力，会主动排除私有网络、云服务商网段及美国国防部 IP 地址范围，以此降低被安全监测系统发现的概率。

#### 防护建议

企业可通过以下措施降低GoBruteforcer攻击风险：实施强密码策略、关闭不必要的公网暴露服务、部署多因素身份验证机制，以及持续监测异常登录尝试行为。

***END***

阅读推荐

[【安全圈】美军进攻委内瑞拉前当地电信公司BGP路由发生异常 流量被引导至不安全的路线](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=1&sn=10d365f3aeaa11a32edd4b32ab718cbd&scene=21#wechat_redirect)

[【安全圈】两款Chrome扩展窃取90万用户与ChatGPT的对话记录](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=2&sn=340af758cdc973198fef16ee90d05a49&scene=21#wechat_redirect)

[【安全圈】0Day漏洞Chronomaly可获取Linux内核root权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=3&sn=dea95a9fbe14ba2f6a20a39754e7f77a&scene=21#wechat_redirect)

[【安全圈】D-Link 多款老旧 DSL 网关路由器被曝命令注入 0day，已遭野外利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=4&sn=9c7154506dafe5b5720c6a61411d4662&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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