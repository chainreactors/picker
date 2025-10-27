---
title: 攻击者正滥用Gophish传播远程访问木马程序
url: https://www.freebuf.com/news/413485.html
source: FreeBuf网络安全行业门户
date: 2024-10-24
fetch_date: 2025-10-06T18:51:48.461832
---

# 攻击者正滥用Gophish传播远程访问木马程序

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

攻击者正滥用Gophish传播远程访问木马程序

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

攻击者正滥用Gophish传播远程访问木马程序

2024-10-23 10:39:38

所属地 上海

据The Hacker News消息，名为Gophish 的开源网络钓鱼工具包正被攻击者用来制作DarkCrystal RAT（又名 DCRat）和PowerRAT 远程访问木马，目标针对俄国用户。

Gophish 允许组织通过利用简易的模板来测试其网络钓鱼防御措施，并启动基于电子邮件的跟踪活动。但攻击者利用Gophish制作网络钓鱼邮件，并伪装成Yandex Disk 链接（“disk-yandex[.]ru“），以及伪装成 VK 的 HTML 网页，VK 是俄罗斯最主要使用的社交网络。

![](https://image.3001.net/images/20241023/1729651285_671862552f1cce910c79d.jpeg!small)感染链

据观察，攻击者根据所使用的初始访问载体推送包含DCRat 或 PowerRAT恶意木马的Microsoft Word 文档或嵌入 JavaScript 的 HTML。当受害者打开 maldoc 并启用宏时，就会执行一个恶意 Visual Basic (VB) 来提取 HTML 应用程序 (HTA) 文件（"UserCache.ini.hta"）和 PowerShell 加载器（"UserCache.ini"）。该宏负责配置 Windows 注册表项，以便每次用户在设备上登录其帐户时都会自动启动 HTA 文件。

HTA 会删除一个负责执行 PowerShell 加载程序的 JavaScript 文件（“UserCacheHelper.lnk.js”）。JavaScript 使用名为“cscript.exe”的合法 Windows 二进制文件执行。

研究人员称，伪装成 INI 文件的 PowerShell 加载程序脚本包含PowerRAT 的 base64 编码数据块有效载荷 ，该数据块在受害者的机器内存中解码和执行。

除了执行系统侦察外，该恶意软件还会收集驱动器序列号并连接到位于俄罗斯的远程服务器以接收进一步的指示。如果未从服务器收到响应，PowerRAT 将配备解码和执行嵌入式 PowerShell 脚本的功能。到目前为止，分析的样本中没有一个包含 Base64 编码的字符串，表明该恶意软件正在积极开发中。

与此类似，采用嵌入恶意 JavaScript 的 HTML 文件的替代感染链会触发一个多步骤过程，从而导致部署 DCRat 恶意软件。

DCRat 是一种模块化的恶意软件 ，可以窃取敏感数据、捕获屏幕截图和击键，提供对受感染系统的远程控制访问，并导致其他文件的下载和执行。

除了俄罗斯，在临近的乌克兰、白俄罗斯、哈萨克斯坦、乌兹别克斯坦和阿塞拜疆也监测到了恶意活动，显示整个俄语片区使用者都是攻击者的针对目标。

**参考来源：**

> [Gophish Framework Used in Phishing Campaigns to Deploy Remote Access Trojans](https://thehackernews.com/2024/10/gophish-framework-used-in-phishing.html)

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