---
title: 溯源专题 | 通过PDF文件信息进行攻击溯源
url: https://www.freebuf.com/articles/network/351431.html
source: FreeBuf网络安全行业门户
date: 2022-12-13
fetch_date: 2025-10-04T01:18:58.965201
---

# 溯源专题 | 通过PDF文件信息进行攻击溯源

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

溯源专题 | 通过PDF文件信息进行攻击溯源

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

溯源专题 | 通过PDF文件信息进行攻击溯源

2022-12-12 10:57:36

所属地 广东省

## 正文

“PDF是Portable Document Format的简称，意为“可携带文档格式”，是由Adobe Systems用于与应用程序、操作系统、硬件无关的方式进行文件交换所发展出的文件格式。PDF文件以PostScript语言图象模型为基础，无论在哪种打印机上都可保证精确的颜色和准确的打印效果，即PDF会忠实地再现原稿的每一个字符、颜色以及图象。” — — WIKI

近期作者发现有很多黑客组织在攻击时，喜欢额外放一个PDF作为诱饵文档，用来迷惑用户降低用户的警惕性，殊不知，PDF中也存在着多个字段可以协助我们进行溯源。

首先，我们先来认识一下PDF文件，PDF结构分为四个部分，分别是：

1.  \_header\_，提供PDF版本号

2.  \_body\_ ，包含页面，图形内容和大部分辅助信息的主体，全部编码为一系列对象。

3.  \_xref Table\_，交叉引用表，列出文件中每个对象的位置便于随机访问。

4.  \_Trailer\_，trailer包括trailer字典，它有助于找到文件的每个部分， 并列出可以在不处理整个文件的情况下读取的各种元数据。

![1669967944_6389b048512f8fbc15777.png!small](https://image.3001.net/images/20221202/1669967944_6389b048512f8fbc15777.png!small)

我们可以测试一下，就使用Word来生成一个PDF吧，首先打开Word，点击文件。

![1669967951_6389b04fdaff56229500c.png!small](https://image.3001.net/images/20221202/1669967951_6389b04fdaff56229500c.png!small)

选择另存为，点击浏览，选择保存类型为PDF。

![1669967958_6389b0569cb0ba1afbd16.png!small](https://image.3001.net/images/20221202/1669967958_6389b0569cb0ba1afbd16.png!small)

这样我们就生成了一个PDF文件，如下图

![1669967966_6389b05e08327e4c9347a.png!small](https://image.3001.net/images/20221202/1669967966_6389b05e08327e4c9347a.png!small)

接着，我们使用010Editor 打开PDF（首次打开会提示安装一个PDF模板），我们选择点击“安装”模板。

![1669967973_6389b06518dd83cf780a7.png!small](https://image.3001.net/images/20221202/1669967973_6389b06518dd83cf780a7.png!small)

点击同意。

![1669967981_6389b06daa55c5ed42a5c.png!small](https://image.3001.net/images/20221202/1669967981_6389b06daa55c5ed42a5c.png!small)

此时我们便使用010Editor解析了PDF文件。

我们先简单看一下文件结构，我们展开“struct PDFHeader sPDFHeader”可以看到这个PDF文件遵守的是PDF1.7的规范。

![1669967988_6389b074e02bc0133d610.png!small](https://image.3001.net/images/20221202/1669967988_6389b074e02bc0133d610.png!small)

我们接着向下看，找到”PDFObj”中的”Author”对象，可以看到有一部分乱码了，我们定位到到编辑界面去查看。

![1669967996_6389b07cdbe9d6f0d0acd.png!small](https://image.3001.net/images/20221202/1669967996_6389b07cdbe9d6f0d0acd.png!small)

依次点击“Author”对象所在的”PDFObj\[8\]”->”Data\[200\]”，可以看到上面部分的编辑框已经定位到字段位置。

![1669968003_6389b083e44b01e953faf.png!small](https://image.3001.net/images/20221202/1669968003_6389b083e44b01e953faf.png!small)

我们可以通过编辑窗看到作者名字是“PC”，使用了“Microsoft Word LTSC”创建了该PDF。

创建的时间是“2022年12月01日11点12分21秒”，时区是“+08:00”。

![1669968010_6389b08abe90b549042f1.png!small](https://image.3001.net/images/20221202/1669968010_6389b08abe90b549042f1.png!small)

我们接着往下看，发现还有一个“XML”对象。

![1669968017_6389b091f21733500d4d5.png!small](https://image.3001.net/images/20221202/1669968017_6389b091f21733500d4d5.png!small)

我们依旧在编辑器中定位过去，并将其复制出来。

![1669968024_6389b0987fd9ee243217a.png!small](https://image.3001.net/images/20221202/1669968024_6389b0987fd9ee243217a.png!small)

发现我们依旧可以在该字段看到用户、时间、时区、生成软件等信息。

![1669968031_6389b09f55f0411f4539e.png!small](https://image.3001.net/images/20221202/1669968031_6389b09f55f0411f4539e.png!small)

在我们日常的工作中，便可以通过上述方法，对黑客使用的诱饵文档进行分析，并提取其中的关键信息，像是时区、用户名、使用软件等等进行攻击溯源。

PS：补充一点，使用不同软件生成的PDF是会有细微不同的，例如Chrome生成的PDF会附带“UA”信息，其他软件生成PDF也是类似原理。

PPS：作者曾在前些年使用了该方法，溯源到了某黑客团队的，最后，希望大家也能有所收获！

# 技术分享 # 攻击溯源

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

正文

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