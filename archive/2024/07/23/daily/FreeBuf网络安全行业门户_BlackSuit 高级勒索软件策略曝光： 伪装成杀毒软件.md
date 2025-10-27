---
title: BlackSuit 高级勒索软件策略曝光： 伪装成杀毒软件
url: https://www.freebuf.com/news/406645.html
source: FreeBuf网络安全行业门户
date: 2024-07-23
fetch_date: 2025-10-06T17:43:12.396319
---

# BlackSuit 高级勒索软件策略曝光： 伪装成杀毒软件

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

BlackSuit 高级勒索软件策略曝光： 伪装成杀毒软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

BlackSuit 高级勒索软件策略曝光： 伪装成杀毒软件

2024-07-22 11:29:22

所属地 上海

在最近发生的一系列中断主要业务的事件中，KADOKAWA 公司经历了延伸到多个网站的服务中断。最初看似技术故障的事件很快升级为由臭名昭著的 BlackSuit 勒索软件组织策划的全面勒索软件攻击。五周前，BlackSuit 声称对此次攻击负责，并发出最后通牒：要么满足他们的赎金要求，要么在 7 月 1 日公开发布被盗信息。

Deep Instinct 威胁实验室的深入分析显示，BlackSuit 的战术和技术发生了巨大演变。该勒索软件现在采用的是先进的混淆方法，包括将其有效载荷伪装成奇虎 360 杀毒软件的合法组件。与早期版本相比，最新的 BlackSuit 样本的检测率要低得多，这表明威胁行为者在刻意规避安全措施。

![](https://image.3001.net/images/20240722/1721618638_669dd0ce377c7d2e39175.png!small)VirusTotal 检测率

最新的样本包含编码字符串和导入 DLL ，旨在阻止分析工作。强制性 ID 参数绕过了自动仿真，提高了规避能力。最有影响的变化之一是将勒索软件伪装成知名免费杀毒软件奇虎 360 的合法组成部分，这包括虚假水印，大大降低了检测率。伪装文件虽然没有签名，但与奇虎真正的 QHAccount.exe 文件非常相似，从而有效地规避了安全软件。

BlackSuit 还集成了一些高级功能，如用于加密的非对称密钥交换、删除影子副本以禁止轻松恢复，以及禁用安全模式和关闭系统的功能。加密后的文件会添加 .blacksuit 扩展名，并附带赎金说明（通常名为 readme.blacksuit.txt）。

BlackSuit 勒索软件采用了多种初始攻击载体，包括使用窃取凭证的 RDP、VPN 和防火墙漏洞、带宏的 Office 电子邮件附件、torrent 网站、恶意广告和第三方木马。攻击者还利用 CobaltStrike、WinRAR、PUTTY、Rclone、Advanced IP Scanner、Mimikatz 和 GMER 等工具。这种多样化的载体使 BlackSuit 的目标更为广泛，危及大量数据。

![](https://image.3001.net/images/20240722/1721618903_669dd1d7a9ab493fcd6bf.png!small)BlackSuit 泄密网站上的受害者资料示例

另外，BlackSuit 在暗网上运营着一个新闻和泄密网站，一旦过了赎金的截止日期，他们就会在网站上公布受害者的外泄数据。这些资料包括受影响组织的关键信息，如行业、员工人数、收入和联系方式等。、

**参考来源：**

https://securityonline.info/blacksuits-advanced-ransomware-tactics-exposed-masquerades-as-antivirus/

# 泄密 # 绕过 # 勒索软件

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