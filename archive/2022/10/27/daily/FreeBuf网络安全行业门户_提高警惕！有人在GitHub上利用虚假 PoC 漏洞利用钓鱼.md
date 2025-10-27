---
title: 提高警惕！有人在GitHub上利用虚假 PoC 漏洞利用钓鱼
url: https://www.freebuf.com/news/347905.html
source: FreeBuf网络安全行业门户
date: 2022-10-27
fetch_date: 2025-10-03T21:01:00.486111
---

# 提高警惕！有人在GitHub上利用虚假 PoC 漏洞利用钓鱼

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

提高警惕！有人在GitHub上利用虚假 PoC 漏洞钓鱼

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

提高警惕！有人在GitHub上利用虚假 PoC 漏洞钓鱼

2022-10-26 15:34:13

所属地 上海

莱顿高级计算机科学研究所的研究人员在GitHub上发现了数以千计存在问题的存储库，这些存储库为各种漏洞提供虚假的概念验证（PoC），并借此隐藏传播恶意软件。

GitHub是最大的代码托管平台之一，研究人员用它来发布PoC漏洞，以帮助安全社区验证漏洞的修复或确定一个漏洞的影响和范围。

据莱顿高级计算机科学研究所的研究人员称，如果不包括被证实的恶作剧软件，以虚假PoC进行掩饰，实际上恶意软件的可能性约高达10.3%。![](https://image.3001.net/images/20221026/1666756688_6358b050b47a09c651418.png!small)

****数据收集和分析****

研究人员使用以下三种机制分析了47300多个储存库，包含2017年至2021年期间披露的漏洞：

* IP地址分析：将PoC的发布者IP与公共封锁名单以及VT和AbuseIPDB进行比较。
* 二进制分析：对提供的可执行文件及其哈希值运行VirusTotal检查。
* 十六进制和Base64分析：在执行二进制和IP检查之前对混淆的文件进行解码。

![](https://image.3001.net/images/20221026/1666756824_6358b0d8547c6925d9e8e.jpg!small)在提取的150734个独特的IP中，有2864个与封锁名单条目相匹配，1522个在Virus Total的反病毒扫描中被检测为恶意的，其中1069个存在于AbuseIPDB数据库中。二进制分析检查了一组6160个可执行文件，发现共有2164个恶意样本托管在1398个存储库中。

![](https://image.3001.net/images/20221026/1666756879_6358b10f4feea1cfc6b47.jpg!small)

总的来说，在测试的47313个软件库中，有4893个软件库被认为是恶意的，其中大部分涉及到2020年的漏洞。报告中包含了一小部分带有虚假PoC的软件库，这些软件库正在传播恶意软件。研究人至少分享了60个案例，然而这些例子仍然是存活的，并且正在被GitHub取缔。

****PoC中的恶意软件****

通过仔细研究其中一些案例，研究人员发现了大量不同的恶意软件和有害脚本，从远程访问木马到Cobalt Strike。

一个有趣的案例是CVE-2019-0708的PoC，通常被称为 "BlueKeep"，它包含一个base64混淆的Python脚本，从Pastebin获取一个VBScript。该脚本是Houdini RAT，一个基于JavaScript的老式木马，支持通过Windows CMD执行远程命令。

![](https://image.3001.net/images/20221026/1666756966_6358b1666dc5d1fbfe4f7.jpg!small)

在另一个案例中，研究人员发现了一个假的PoC，这是一个收集系统信息、IP地址和用户代理的信息窃取器。这是另一个研究人员之前创建的安全实验，所以用自动工具找到它是对研究人员的确认，他们的方法是有效的。

还有一些没有在技术报告中体现的例子，例如：

PowerShell PoC包含一个用base64编码的二进制文件，在Virus Total中被标记为恶意的。

Python PoC包含一个单行代码，用于解码在Virus Total中被标记为恶意的base64编码的有效载荷。

伪造的BlueKeep漏洞包含一个被大多数反病毒引擎标记为恶意的可执行文件，并被识别为Cobalt Strike。一个隐藏在假PoC中的脚本，其中有不活跃的恶意组件，但如果其作者愿意，依旧可以造成损害。

![](https://image.3001.net/images/20221026/1666757047_6358b1b7edfff5fe9e59e.jpg!small)

****如何保持安全****

盲目相信GitHub上未经验证的仓库是不可取的，因为其内容没有经过审核，所以用户在使用前要对其进行审查。建议软件测试人员仔细检查他们下载的PoC，并在执行之前尽可能多地进行检查。

专家认为，所有测试人员都应该遵循这三个步骤。

1. 认真审核即将在网络上运行的代码。
2. 如果代码太模糊，需要太多的时间来手动分析，就在一个环境中（例如一个隔离的虚拟机）进行沙盒测试，并检查你的网络是否有可疑的流量。
3. 使用开源的情报工具，如VirusTotal来分析二进制文件。

目前，研究人员已经将他们发现的所有恶意软件库报告给GitHub，但在所有这些软件库被审查和删除之前，还需要一些时间，所以许多软件库仍然对公众开放。

> 参考来源：<https://www.bleepingcomputer.com/news/security/thousands-of-github-repositories-deliver-fake-poc-exploits-with-malware/>

# 漏洞 # 网络安全 # 数据安全

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