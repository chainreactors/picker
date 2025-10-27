---
title: Emotet 恶意软件冒充美国税务局进行网络钓鱼
url: https://www.freebuf.com/news/361692.html
source: FreeBuf网络安全行业门户
date: 2023-03-28
fetch_date: 2025-10-04T10:53:03.466753
---

# Emotet 恶意软件冒充美国税务局进行网络钓鱼

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

Emotet 恶意软件冒充美国税务局进行网络钓鱼

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Emotet 恶意软件冒充美国税务局进行网络钓鱼

2023-03-27 14:16:10

所属地 海外

Bleeping Computer 网站披露，Emotet 恶意软件以美国纳税人为目标，冒充美国国税局向受害者发送 W-9 纳税申报表，进行钓鱼活动。![1679898304_642136c007f36d7dea206.png!small?1679898304631](https://image.3001.net/images/20230327/1679898304_642136c007f36d7dea206.png!small?1679898304631)

Emotet 作为一款臭名昭著的恶意软件，主要通过网络钓鱼电子邮件传播，这些电子邮件包含带有恶意宏的 Microsoft Word 和 Excel 文档。在微软默认阻止下载的 Office 文档中存在宏后，Emotet 转而使用带有嵌入式脚本的 Microsoft OneNote 文件来安装 Emotet 恶意软件。

据悉，一旦安装了 Emotet，该恶意软件便会窃取受害者的电子邮件，用于未来的回复链攻击，发送更多的垃圾邮件，并安装其它恶意软件，为勒索软件团伙等其它威胁郭建者提供初始访问权限。

## ****Emotet 为美国税收********做好了“********准备********”****

Emotet 恶意软件通常使用“主题式”钓鱼活动，以搭上假期和年度商业活动的便车，例如当前的美国纳税季。在 Malwarebytes 和 Palo Alto Networks Unit42 安全研究人员观察到的新网络钓鱼活动中，Emotet 恶意软件以纳税人为目标，发送附有虚假 W-9 纳税表附件的电子邮件。

Malwarebytes 研究人员发现，威胁攻击者冒充美国国税局的“检查员”，发送标题为“美国国税局纳税申报表 W-9”的电子邮件。

在这些钓鱼电子邮件中有一个名为“W-9 form.ZIP”的 ZIP 存档，其中包含了一个恶意的 Word 文档。此Word 文档已“膨胀”到 500MB 以上，使安全软件更难检测到它是恶意的。![1679898324_642136d4f0731340b681a.png!small?1679898326090](https://image.3001.net/images/20230327/1679898324_642136d4f0731340b681a.png!small?1679898326090)

冒充国税局的 Emotet 电子邮件（来源： Malwarebytes）

目前，微软默认阻止宏，用户不太可能遇到启用宏的麻烦，也不太可能使用恶意 Word 文档感染宏。![1679898353_642136f1ae4b3beb9c6d6.png!small?1679898354422](https://image.3001.net/images/20230327/1679898353_642136f1ae4b3beb9c6d6.png!small?1679898354422)

Emotet Word 文档（来源： BleepingComputer）

在 Unit42 Brad Duncan 观察到的 Emotet 网络钓鱼活动中，攻击者通过使用带有嵌入 VBScript 文件的Microsoft OneNote 文档来绕过这些限制，这些文件安装了 Emotet 恶意软件。

此外，网络钓鱼活动使用回复链电子邮件，其中包含假装来自向用户发送 W-9 表格的业务合作伙伴的电子邮件，如下所示：![1679898364_642136fc29514b8849974.png!small?1679898364976](https://image.3001.net/images/20230327/1679898364_642136fc29514b8849974.png!small?1679898364976)

带有恶意的微软 OneNote 附件的 Emotet 回复链电子邮件（来源：Unit42）

所附的 OneNote 文件将假装受到保护，要求用户双击 "查看 "按钮，查看文件。但是，隐藏在 "查看 "按钮下面的是一个 VBScript 文档，它将被同步启动。![1679898375_642137076ae12e1d6755e.png!small?1679898376362](https://image.3001.net/images/20230327/1679898375_642137076ae12e1d6755e.png!small?1679898376362)

冒充 W-9 表格的恶意微软 OneNote 文件（资料来源：BleepingComputer：）

在启动嵌入式 VBScript 文件时，微软 OneNote 会警告用户该文件可能是恶意的。不幸的是，“历史经验”告诉我们，许多用户无视这些警告，只是让文件运行。

一旦执行，VBScript 将下载 Emotet DLL 并使用 regsvr32.exe 运行它。此后，该恶意软件现在将悄悄地在后台运行，窃取电子邮件、联系人，并等待进一步的有效载荷安装到设备上。

最后提醒用户，如果收到任何声称是 W-9 或其他税表的电子邮件，首先应使用本地杀毒软件扫描这些文件。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/emotet-malware-distributed-as-fake-w-9-tax-forms-from-the-irs/

# 网络钓鱼 # 系统安全

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

Emotet 为美国税收做好了“准备”

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