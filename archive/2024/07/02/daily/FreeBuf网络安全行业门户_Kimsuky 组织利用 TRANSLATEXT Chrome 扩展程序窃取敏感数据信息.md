---
title: Kimsuky 组织利用 TRANSLATEXT Chrome 扩展程序窃取敏感数据信息
url: https://www.freebuf.com/news/404872.html
source: FreeBuf网络安全行业门户
date: 2024-07-02
fetch_date: 2025-10-06T17:45:09.725832
---

# Kimsuky 组织利用 TRANSLATEXT Chrome 扩展程序窃取敏感数据信息

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

Kimsuky 组织利用 TRANSLATEXT Chrome 扩展程序窃取敏感数据信息

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Kimsuky 组织利用 TRANSLATEXT Chrome 扩展程序窃取敏感数据信息

2024-07-01 10:53:13

所属地 上海

日前，一个名为 Kimsuky 的威胁攻击组织正在使用新型恶意谷歌 Chrome 浏览器扩展程序，窃取大量敏感信息。![1719822417_668268517ef5b4dc533a4.png!small](https://image.3001.net/images/20240701/1719822417_668268517ef5b4dc533a4.png!small)

> Kimsuky 是一个臭名昭著的朝鲜黑客组织，至少从 2012 年起就开始活动，主要策划针对韩国实体的网络间谍和金融攻击，曾以 APT43、ARCHIPELAGO、Black Banshee、Emerald Sleet、Springtail 和 Velvet Chollima 等名称被躲过的执法人员追踪。

2024 年 3 月，Zscaler ThreatLabz 观察到 Kimsuky 网络攻击活动，将扩展程序编号为 TRANSLATEXT，并强调了其收集电子邮件地址、用户名、密码、cookie 和浏览器截图的能力。据悉，威胁攻击者的攻击目标主要针对韩国学术界，特别是一些关注朝鲜政治事务的学术界人员。

最近几周，Kimsuky 威胁组织利用微软 Office 的一个已知安全漏洞 CVE-2017-11882，分发键盘记录程序，并在针对航空航天和国防部门的攻击中使用工作主题诱饵，其目的是投放一个具有数据收集和二次有效载荷执行功能的间谍工具。

网络安全公司 CyberArmor 指出，该恶意程序后门似乎此前从未公开记录过，允许威胁攻击者执行基本侦察，并投放额外的有效载荷来接管或远程控制机器。目前，尚不清楚与新发现活动相关的初始访问的确切模式，但是，研究人员已经获悉该组织利用鱼叉式网络钓鱼和社交工程攻击来激活感染链。
据悉，攻击活动的起于一个 ZIP 压缩包（关于韩国军事历史），其中包含两个文件， 一个是韩文文字处理器文档和一个可执行文件。一旦受害者启动该可执行文件后，威胁攻击者控制的服务器就会立刻检索到一个 PowerShell 脚本，该脚本随即将被威胁攻击者导出到 GitHub 存储库，并通过 Windows 快捷方式 (LNK) 文件下载额外的 PowerShell 代码。

Zscaler 表示，研究人员发现创建于 2024 年 2 月 13 日的 GitHub 账户以 "GoogleTranslate.crx "为名短暂托管了 TRANSLATEXT 扩展，但其传输方式目前尚不清楚。安全研究员 Seongsu Park 也指出，这些文件于 2024 年 3 月 7 日出现在资源库中，但第二天就被删除了，此举意味着 Kimsuky 威胁组织试图尽量减少曝光率。

值得一提的是，伪装成谷歌翻译的 TRANSLATEXT 主要包含 JavaScript 代码，可以绕过谷歌、Kakao 和Naver 等服务的安全措施，从而轻松窃取电子邮件地址、凭证和 cookie，捕获浏览器截图，以及盗取敏感数据信息。

不仅如此，TRANSLATEXT Chrome 扩展程序还被威胁攻击者精心设计，用于从博客 Blogspot URL 获取命令，以便对新打开的标签页进行截图，删除浏览器中的所有 cookies 等。最后，完全专家强调，Kimsuky 威胁组织的主要目标之一是对韩国学术界和政府人员进行监视，以收集有价值的情报。

**参考文章：**

> https://thehackernews.com/2024/06/kimsuky-using-translatext-chrome.html

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