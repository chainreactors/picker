---
title: SparkCat恶意活动利用OCR技术窃取加密货币钱包恢复短语
url: https://www.freebuf.com/articles/421113.html
source: FreeBuf网络安全行业门户
date: 2025-02-06
fetch_date: 2025-10-06T20:35:39.177879
---

# SparkCat恶意活动利用OCR技术窃取加密货币钱包恢复短语

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

SparkCat恶意活动利用OCR技术窃取加密货币钱包恢复短语

* ![]()
* 关注

SparkCat恶意活动利用OCR技术窃取加密货币钱包恢复短语

2025-02-05 12:53:43

所属地 上海

![](https://image.3001.net/images/20250205/1738764185589440_544bd207f7af4e5693670921aee359ec.png!small)

## SparkCat恶意活动概述

2024年底，卡巴斯基的专家发现了一场名为SparkCat的恶意活动，该活动通过传播恶意软件来针对加密货币钱包。早在2023年3月，ESET就发现了一些经过修改的即时通讯应用版本中嵌入了恶意软件，这些软件利用光学字符识别（OCR）技术扫描受害者设备中的图片，寻找恢复加密货币钱包访问权限的短语。

卡巴斯基在2024年底发现的SparkCat活动采用了类似的策略，但这次攻击同时针对Android和iOS用户。专家指出，这些带有恶意软件的应用程序甚至通过官方应用商店进行分发。

## 恶意软件的技术细节

专家发现，Android和iOS应用程序中嵌入了恶意的SDK/框架，用于窃取加密货币钱包的恢复短语。这些恶意应用在Google Play上的下载量已超过24.2万次。卡巴斯基表示，这是首次在App Store中发现此类窃取程序。

![image](https://image.3001.net/images/20250205/1738764187177898_c37745fd53dd47a485ea6f74e6e3e711.png!small)

卡巴斯基发布的报告指出：“Android恶意软件模块解密并启动了一个基于Google ML Kit库的OCR插件，用于识别设备图库中图片中的文本。通过从C2服务器接收的关键词，木马程序将这些图片发送到命令服务器。iOS恶意软件模块的设计类似，同样使用了Google ML Kit库进行OCR处理。”报告还提到：“我们将其命名为SparkCat的恶意软件使用了一种未公开的协议与C2服务器通信，该协议是用Rust语言实现的，这在移动应用中较为罕见。”

## 恶意SDK的工作原理

恶意SDK伪装成分析模块，在Android上使用名为“Spark”的Java组件，在iOS上使用名为“Gzip”、“googleappsdk”或“stat”的Rust组件。该组件与C2服务器通信，并从加密的GitLab文件中执行命令。

研究人员通过分析时间戳和GitLab仓库中配置文件的创建日期，确定SparkCat自2024年3月以来一直活跃。

该模块使用Google ML Kit OCR从图片中提取文本，搜索多种语言的加密货币钱包恢复短语。恶意软件根据受害者的语言加载不同的OCR模型，以区分图片中的拉丁字母、韩文、中文和日文字符。

报告进一步解释：“SDK随后将设备信息上传到命令服务器的/api/e/d/u路径，并接收一个对象来调节恶意软件的进一步操作。”报告还提到：“我们自问：攻击者对哪些图片感兴趣？为此，我们独立从命令服务器请求了OCR搜索的关键词列表。每次请求，我们都收到了中文、日文、韩文、英文、捷克语、法语、意大利语、波兰语和葡萄牙语的关键词。所有这些关键词都指向攻击者的财务动机：他们对恢复加密货币钱包访问权限的短语（即助记词）感兴趣。”

## 攻击范围和影响

此次攻击主要针对欧洲和亚洲的Android和iOS用户，使用了本地化的关键词和支持多个国家的应用程序，包括阿联酋、哈萨克斯坦、中国、印度尼西亚、津巴布韦等。

报告总结道：“不幸的是，尽管官方平台有严格的审核机制，以及众所周知的利用OCR窃取加密货币钱包的套路，受感染的应用程序仍然出现在Google Play和App Store中。”报告还指出：“这种木马程序尤其危险，因为应用程序内部的恶意植入物没有任何明显的迹象：它请求的权限可以用于应用程序的主要功能，或者乍一看似乎无害，而且恶意软件运行得非常隐秘。这一案例再次打破了‘Android恶意应用程序的威胁与iOS无关’的神话。”

报告还包含了攻击的指标（IoCs）。

**参考来源：**

> [SparkCat campaign target crypto wallets using OCR to steal recovery phrases](https://securityaffairs.com/173873/malware/sparkcat-campaign-target-crypto-wallets.html)

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