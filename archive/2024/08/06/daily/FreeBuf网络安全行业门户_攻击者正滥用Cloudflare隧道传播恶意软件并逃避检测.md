---
title: 攻击者正滥用Cloudflare隧道传播恶意软件并逃避检测
url: https://www.freebuf.com/news/407793.html
source: FreeBuf网络安全行业门户
date: 2024-08-06
fetch_date: 2025-10-06T18:04:39.717270
---

# 攻击者正滥用Cloudflare隧道传播恶意软件并逃避检测

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

攻击者正滥用Cloudflare隧道传播恶意软件并逃避检测

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

攻击者正滥用Cloudflare隧道传播恶意软件并逃避检测

2024-08-05 11:00:53

所属地 上海

网络安全公司eSentire 和 Proofpoint 发现，滥用 Clouflare 的 TryCloudflare 免费服务进行恶意软件传播的情况有所增加，涉及多个恶意软件系列。![](https://image.3001.net/images/20240805/1722829262_66b049ceca3c3c7cd4cf8.jpg!small)

该攻击方式需要使用 TryCloudflare 创建一个速率限制隧道，该隧道充当管道，通过 Cloudflare 的基础设施将流量从攻击者控制的服务器中继到本地机器。

据观察，利用这种技术的攻击链可传播一系列恶意软件，如 AsyncRAT、GuLoader、PureLogs Stealer、Remcos RAT、Venom RAT 和 XWorm。

攻击的最初载体是一封包含 ZIP 压缩文件的网络钓鱼电子邮件，该压缩文件包含一个 URL 快捷方式文件，可将收件人引向一个的WebDAV 服务器上的 Windows 快捷方式文件，该服务器由 TryCloudflare 托管代理。快捷方式文件会执行下一阶段的批处理脚本，这些脚本负责检索和执行额外的 Python 有效载荷，同时显示托管在同一 WebDAV 服务器上的诱饵 PDF 文档。

eSentire 指出，这些脚本执行的操作包括启动诱饵 PDF、下载额外的恶意有效载荷以及更改文件属性以避免被检测。

据 Proofpoint 称，这些网络钓鱼邮件以英语、法语、西班牙语和德语编写，电子邮件数量从数百到数万不等，目标是世界各地的组织机构。 这些邮件主题涵盖了发票、文件请求、包裹递送和税收等。 虽然该活动被归因于一个相关活动集群，但并未与特定的攻击者或团体联系起来。据电子邮件安全厂商评估，该活动是出于经济动机。

去年，Sysdig首次记录了利用TryCloudflare进行恶意攻击的情况，一个被称为LABRAT的加密劫持和代理劫持活动通过GitLab中一个现已打补丁的关键漏洞，利用Cloudflare隧道渗透目标并掩盖其命令与控制（C2）服务器。
此外，由于使用WebDAV和服务器消息块（SMB）进行有效载荷的部署，企业必须将外部文件共享服务的访问权限限制在已知的、允许列表的服务器上。“使用Cloudflare隧道为攻击者提供了一种使用临时基础设施来扩展其攻击的方法，并为及时构建和关闭攻击提供了灵活性，”Proofpoint研究人员Joe Wise和Selena Larson表示。

临时 Cloudflare 实例允许攻击者以一种低成本的方法使用辅助脚本进行攻击，同时限制了检测和删除工作的风险。因为攻击者利用其服务来掩盖恶意行为并通过所谓的“依赖信任的服务”（LoTS） 来增强其运营安全性，Spamhaus 项目呼吁 Cloudflare 审查其反滥用政策。

**参考来源：**

> [Cybercriminals Abusing Cloudflare Tunnels to Evade Detection and Spread Malware](https://thehackernews.com/2024/08/cybercriminals-abusing-cloudflare.html)

# 恶意软件

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