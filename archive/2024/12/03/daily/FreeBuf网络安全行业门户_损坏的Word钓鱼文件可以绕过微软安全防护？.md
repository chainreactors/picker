---
title: 损坏的Word钓鱼文件可以绕过微软安全防护？
url: https://www.freebuf.com/news/416610.html
source: FreeBuf网络安全行业门户
date: 2024-12-03
fetch_date: 2025-10-06T19:39:23.829732
---

# 损坏的Word钓鱼文件可以绕过微软安全防护？

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

损坏的Word钓鱼文件可以绕过微软安全防护？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

损坏的Word钓鱼文件可以绕过微软安全防护？

2024-12-02 10:26:53

所属地 上海

一种新型的网络钓鱼攻击利用了微软Word文件恢复功能，通过发送损坏的Word文档作为电子邮件附件，使它们能够因为损坏状态而绕过安全软件，但仍然可以被应用程序恢复。

威胁行为者不断寻找新的方法来绕过电子邮件安全软件，将他们的网络钓鱼邮件送达到目标收件箱。由恶意软件狩猎公司Any.Run发现的一个新的网络钓鱼活动，使用故意损坏的Word文档作为电子邮件附件，这些邮件伪装成来自工资单和人力资源部门。

![](https://image.3001.net/images/20241202/1733106293_674d1a756c0e3230f0abd.png!small)

这些附件使用了一系列主题，都围绕着员工福利和奖金，包括：

Annual\_Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx
Annual\_Q4\_Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin
Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin
Due\_&\_Payment\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin
Q4\_Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin
这些文档中都包含了Base64编码的字符串"IyNURVhUTlVNUkFORE9NNDUjIw," 解码后为"##TEXTNUMRANDOM45##"。

当打开附件时，Word会检测到文件已损坏，并提示文件中“发现无法读取的内容”，询问是否要恢复它。

![](https://image.3001.net/images/20241202/1733106316_674d1a8c741081fe04b3e.png!small)

这些网络钓鱼文档损坏的方式使得它们很容易被恢复，显示一个文档告诉目标扫描一个二维码以检索文档。如下所示，这些文档被标记为目标公司的徽标，例如下面展示的针对Daily Mail的活动。![](https://image.3001.net/images/20241202/1733106331_674d1a9b19c600ff8487c.png!small)

扫描二维码将用户带到一个网络钓鱼网站，该网站伪装成微软登录页面，试图窃取用户的凭证。

![](https://image.3001.net/images/20241202/1733106358_674d1ab675cfb1b79ef1b.png!small)

虽然这次网络钓鱼攻击的最终目标并不新鲜，但其使用损坏的Word文档是一种新颖的规避检测手段。

"尽管这些文件在操作系统中运行成功，但由于未能为它们的文件类型应用适当的程序，它们仍然未被大多数安全解决方案检测到，"Any.Run解释道。

“它们被上传到VirusTotal，但所有防病毒解决方案都返回了'clean'或'Item Not Found'，因为它们无法正确分析文件。”

这些附件在实现目标方面相当成功。从与BleepingComputer分享的附件和在这次活动中使用的附件来看，几乎所有的在VirusTotal上的检测结果都是零[1, 2, 3, 4]，只有一些[1]被2个供应商检测到。

同时，这也可能是因为文档中没有添加恶意代码，它们只是显示了一个二维码。保护自己不受这种网络钓鱼攻击的一般规则仍然适用。如果你收到了一个未知发件人的电子邮件，特别是如果它包含附件，应立即删除或在打开前与网络管理员确认。

参考来源：<https://www.bleepingcomputer.com/news/security/novel-phising-campaign-uses-corrupted-word-documents-to-evade-security/>

# 系统安全 # 数据安全

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