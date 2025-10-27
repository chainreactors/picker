---
title: Bybit被窃15亿美元事件溯源：黑客利用Safe实施供应链攻击
url: https://www.freebuf.com/news/423141.html
source: FreeBuf网络安全行业门户
date: 2025-03-01
fetch_date: 2025-10-06T21:58:42.206548
---

# Bybit被窃15亿美元事件溯源：黑客利用Safe实施供应链攻击

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Bybit被窃15亿美元事件溯源：黑客利用Safe实施供应链攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Bybit被窃15亿美元事件溯源：黑客利用Safe实施供应链攻击

2025-02-28 10:42:22

所属地 上海

美国联邦调查局（FBI）日前正式将 Bybit 遭受创纪录的15 亿美元加密货币被窃事件与朝鲜黑客组织 Lazarus 联系起来。与此同时，Bybit 的首席执行官 Ben Zhou 宣布要对 Lazarus全面”开战“

FBI 表示，朝鲜应对此次加密货币交易所的虚拟资产盗窃事件负责。该事件被归咎于 FBI 追踪的一个特定集群 TraderTraitor，该集群也被称为 Jade Sleet、Slow Pisces 和 UNC4899。

FBI 称：“TraderTraitor 的行为迅速，已将部分被盗资产转换为比特币和其他虚拟资产，并分散在多个区块链上的数千个地址中。预计这些资产将被进一步洗钱，并最终转换为法定货币。”

值得一提的是，TraderTraitor 集群此前曾被日本和美国当局指控参与 2024 年 5 月从加密货币公司 DMM Bitcoin 窃取价值 3.08 亿美元加密货币的事件。

## 朝鲜黑客的常用攻击手法

TraderTraitor 以针对 Web3 行业的公司而闻名，通常诱骗受害者下载带有恶意软件的加密货币应用程序，从而实施盗窃。此外，该集群还被发现会策划以工作为主题的社会工程活动，导致恶意 npm 包的部署。

与此同时，Bybit 已启动赏金计划，以帮助追回被盗资金，同时指责 eXch 拒绝配合调查并协助冻结资产。

Bybit 表示：“被盗资金已被转移到无法追踪或冻结的目的地，例如交易所、混币器或跨链桥，或转换为可以冻结的稳定币。我们需要所有相关方的合作，要么冻结资金，要么提供资金流动的更新，以便我们继续追踪。”

## 攻击背后的技术细节

总部位于迪拜的 Bybit 还分享了由 Sygnia 和 Verichains 进行的两项调查的结论，将此次攻击与 Lazarus 集团联系起来。

Sygnia 表示：“对三个签名者主机的取证调查表明，攻击的根本原因是从 Safe{Wallet} 基础设施中产生的恶意代码。”

![image](https://image.3001.net/images/20250227/1740647076848084_5a983ccbd4724fb5aadb22a6874481dd.jpg!small)

Verichains 指出：“app.safe.global 的良性 JavaScript 文件似乎在 2025 年 2 月 19 日 UTC 时间 15:29:25 被恶意代码替换，专门针对 Bybit 的以太坊多签冷钱包。” 并补充说：“攻击设计为在下一次 Bybit 交易期间激活，该交易发生在 2025 年 2 月 21 日 UTC 时间 14:13:35。” Safe.Global 的 AWS S3 或 CloudFront 账户/API 密钥可能泄露或被攻破，从而为供应链攻击铺平了道路。

在一份单独声明中，多签钱包平台 Safe{Wallet} 表示，此次攻击是通过入侵 Safe{Wallet} 开发人员的机器来实施的，影响了 Bybit 运营的账户。该公司进一步指出，它已实施额外的安全措施来减轻攻击载体。

## Lazarus 集团的历史与手法

Safe{Wallet} 表示：“此次攻击是通过入侵 Safe{Wallet} 开发人员的机器来实现的，导致提交了伪装成恶意的交易。Lazarus 是朝鲜国家支持的黑客组织，以对开发者凭证进行复杂的社会工程攻击而闻名，有时还结合零日漏洞利用。”

目前尚不清楚开发人员的系统是如何被入侵的，尽管 Silent Push 的一项新分析发现，Lazarus 集团在 2025 年 2 月 20 日 22:21:57 注册了域名 bybit-assessment[.]com，该域名在加密货币被盗前几小时注册。

WHOIS 记录显示，该域名是使用电子邮件地址“trevorgreer9312@gmail[.]com”注册的，该地址此前已被确认为 Lazarus 集团用于另一个名为“Contagious Interview”活动的身份。

该公司表示：“Bybit 劫案似乎是由朝鲜威胁行为组织 TraderTraitor 实施的，TraderTraitor 也被称为 Jade Sleet 和 Slow Pisces，而加密货币面试骗局是由朝鲜威胁行为组织 Contagious Interview 领导的，该组织也被称为 Famous Chollima。”

“受害者通常通过 LinkedIn 接触，他们在那里被社会工程学欺骗参与虚假的工作面试。这些面试是目标恶意软件部署、凭证收集以及进一步危害财务和公司资产的切入点。”

据估计，自 2017 年以来，与朝鲜有关的行为者已经窃取了超过 60 亿美元的加密资产。上周窃取的 5 亿美元超过了 2024 年全年从 47 起加密货币劫案中窃取的 34 亿美元。

**参考来源：**

> [Bybit Hack Traced to Safe{Wallet} Supply Chain Attack Exploited by North Korean Hackers](https://thehackernews.com/2025/02/bybit-hack-traced-to-safewallet-supply.html)

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

朝鲜黑客的常用攻击手法

攻击背后的技术细节

Lazarus 集团的历史与手法

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)