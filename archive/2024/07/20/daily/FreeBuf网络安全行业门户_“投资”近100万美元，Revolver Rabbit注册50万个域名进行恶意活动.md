---
title: “投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动
url: https://www.freebuf.com/news/406477.html
source: FreeBuf网络安全行业门户
date: 2024-07-20
fetch_date: 2025-10-06T17:42:52.565637
---

# “投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动

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

“投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

“投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动

2024-07-19 11:18:22

所属地 上海

近日，专注于 DNS 的安全厂商 Infoblox 的研究人员发现，一个名为 Revolver Rabbit 的网络犯罪团伙注册了 50 多万个域名，通过散布一种叫 XLoader（Formbook 的后继者）的信息窃取恶意软件，收集 Windows 和 macOS 系统的敏感信息或对其执行恶意代码。

![](https://image.3001.net/images/20240719/1721358942_6699da5eca4e07884b4ce.png!small)为了以如此大的规模开展行动，该威胁行为者依赖于注册域名生成算法（RDGAs），这是一种可以在瞬间注册多个域名的自动化方法。RDGAs 类似于恶意软件中的域名注册算法 (DGAs)，网络犯罪分子利用这种算法创建潜在的指挥与控制 (C2) 通信目的地列表。

两者之间的一个区别是，DGAs 嵌入在恶意软件中，只有部分生成的域名会被注册，而 RDGAs 则保留在威胁行为者手中，所有域名都会被注册。

研究人员可以通过分析 DGAs 并对其进行逆向工程，以了解潜在的 C2 域名，但 RDGAs 是保密的，这就让找到生成要注册域名的模式变得更具挑战性。

Infoblox 称，Revolver Rabbit 控制着 50 多万个 .BOND 顶级域名，这些域名被用来为恶意软件创建诱饵和实时 C2 服务器。考虑到一个 .BOND 域名的价格约为 2 美元，Revolver Rabbit 在其 XLoader 业务上的 “投资 ”接近 100 万美元，这还不包括过去在其他顶级域名上购买的域名。

Infoblox 表示："这种威胁行为者最常用的 RDGAs 模式是一系列一个或多个字典单词，后面跟着一个五位数的数字，每个单词或数字之间用破折号隔开。”

这些域名通常很容易阅读，似乎专注一个特定的主题或地区，显示出广泛的多样性，示例如下：

* usa-online-degree-29o[.]bond
* bra-portable-air-conditioner-9o[.]bond
* uk-river-cruises-8n[.]bond
* ai-courses-17621[.]bond
* app-software-development-training-52686[.]bond
* assisted-living-11607[.]bond
* online-jobs-42681[.]bond
* perfumes-76753[.]bond
* security-surveillance-cameras-42345[.]bond
* yoga-classes-35904[.]bond

研究人员说，“最近几个月的跟踪，他们发现 Revolver Rabbit RDGAs 和一些已知的恶意软件有联系，这凸显了 RDGAs 作为威胁行为者工具箱中的一种技术的重要性”。

Infoblox 追踪 Revolver Rabbit 已近一年，但直到最近才弄清楚他们的真实面目。虽然过去也观察到过类似的活动，但没有意识到它们背后有这么大的操作。

参考来源：https://www.bleepingcomputer.com/news/security/revolver-rabbit-gang-registers-500-000-domains-for-malware-campaigns/

# 恶意代码 # 域名 # 信息窃取 # 域名安全

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