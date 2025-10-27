---
title: 审计发现 FBI 的数据存储管理存在重大漏洞
url: https://www.freebuf.com/articles/409453.html
source: FreeBuf网络安全行业门户
date: 2024-08-27
fetch_date: 2025-10-06T18:06:06.094101
---

# 审计发现 FBI 的数据存储管理存在重大漏洞

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

审计发现 FBI 的数据存储管理存在重大漏洞

* ![]()
* 关注

审计发现 FBI 的数据存储管理存在重大漏洞

2024-08-26 14:40:52

所属地 上海

据The Hacker News消息，美国司法部监察长办公室 （OIG） 的一项审计发现， FBI 在库存管理和处置涉及机密数据的电子存储媒体方面存在“重大漏洞”。

OIG 的审计显示，FBI 对包含敏感但未分类 （SBU） 、存储机密国家安全信息 （NSI） 的电子介质库存管理存在三大主要问题：

* 一旦电子存储介质（例如内部硬盘驱动器和 U 盘）从较大的设备中提取出来，FBI 就无法充分进行追踪，增加了这些介质丢失或被盗的风险。
* FBI 未能始终如一地使用适当的保密级别（例如，机密、最高机密）标记电子存储介质，可能导致敏感信息处理不当或未经授权的访问。
* 销毁文件的设施物理安全性不足，包括内部访问控制不足、等待销毁的媒体存储不安全以及监控摄像头无法正常工作，所有这些都增加了机密信息泄露的风险。

![](https://image.3001.net/images/20240826/1724654491_66cc239b34351574f471a.jpg!small)FBI 设施中暴露的存储设备托盘

FBI 已经承认了这些问题，表示正在制定一项名为“机密和敏感电子设备的物理控制和销毁以及材料政策指令”的新指令，并根据 OIG 的建议实施纠正措施，包括：

* 修订程序以确保所有包含敏感或机密信息的电子存储介质（包括从预定销毁的计算机中提取的硬盘驱动器）都得到适当的说明、跟踪、及时清理和销毁。
* 根据适用的政策和指南，实施控制措施，确保其电子存储介质标有适当的 NSI 分类级别标记。
* 加强对设施中电子存储介质的物理安全的控制和实践，以防止丢失或被盗。

此外，FBI表示正在安装一种保护性“笼子”，用作文件的存储点，这些文件将被视频监控全方位覆盖。

![](https://image.3001.net/images/20240826/1724654551_66cc23d7efffc7a4fb2d3.png!small)FBI 存储设施中使用的保护性铁笼

OIG 希望 FBI 在 90 天内落实相应的整改。

**参考来源：**

> [Audit finds notable security gaps in FBI's storage media management](https://www.bleepingcomputer.com/news/security/audit-finds-notable-security-gaps-in-fbis-storage-media-management/)

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