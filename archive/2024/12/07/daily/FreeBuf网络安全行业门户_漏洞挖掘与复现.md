---
title: 漏洞挖掘与复现
url: https://www.freebuf.com/articles/web/414845.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:30.666969
---

# 漏洞挖掘与复现

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

漏洞挖掘与复现

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

漏洞挖掘与复现

2024-12-06 12:03:12

所属地 广东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

大家好，我是一个在IT行业十余年的小菜鸟，今天与大家聊一聊漏洞的挖掘与复现。

## 一 漏洞复现。

### 1.NetScaler ADC

例如我对CVE-2023-3519漏洞进行了分析，该漏洞是Citrix ADC 和 Citrix Gateway 中存在未经身份验证的远程代码执行漏洞。

由于不同版本会导致网上公开的poc无法正常使用。

根据不同的版本需要修改三处地方。
⦁ bytes\_to\_encode = b'\x00\x30\x90\x2b\x20'。
部分shellcode字节通过url编码传输的过程有问题，需要编码处理。
⦁ shellcode += b'\x48\x83\xC4\x40'。
0x40字节，不同版本可能存在差异。
⦁ return\_address = b'\x8d\x2b\xfe\xff\xff\x7f\x00\x00'。
通过缓冲区的起始地址0x00007FFFFFFE2B50加上0x3D得到0x00007FFFFFFE2B8D即为需要的return\_address。

而上面所说的东西，我在调试时并未找到相关资料，都是通过调试发现。

### 2.sharepoint

列入CVE-2023-29357该漏洞我进行了详细的分析，并且进行了复现，不过该漏洞在网上可以搜寻到详细的复现信息以及漏洞原理，我觉得这个对大家来说并没有太大的难度。

### 3.winrar

CVE-2023-38831：该漏洞是由于压缩包内存在同名文件导致漏洞触发，该漏洞我进行了免杀处理，我发现在将rar逆向并让文件出现异常时，可以绕过defender等杀毒软件针对该漏洞的检测，从而做到免杀。在24年10月，我再一次测试，发现仍然可以绕过当时最新的defeder等杀软的检测。

CVE-2023-40477：据说该漏洞可以实现远程代码执行，不过我在测试时发现，仅能使目标机器崩溃，并没有做到远程代码执行。可能有更好的方法是我没有发现的。

### 4.Weblogic

CVE-2023-21839和CVE-2023-21931等漏洞我都进行了原理分析以及漏洞的复现，但是我发现weblogic漏洞在使用时其实存在很大的问题，就是jdk8u192之后的漏洞利用，存在很大的问题，通常需要进行本地反序列化，而目标机，很多并不存在可以本地反序列化的插件，导致漏洞利用在高版本存在困难。

### 5.word

以CVE-2023-21716为列，由于各大杀软更新很快，word漏洞在刚出来后就很快被抓住特征，并且word版本在联网情况下可以更新，所以使用起来价值并不是很大。免杀这一块也没有过多研究。

### 6.exchenge

从CVE-2020-0688以及最新的Exchange漏洞我都进行了研究，我发现从Exchange2013之后的漏洞大都围绕两个模块，一个是登录模块，大部分都是在生成对应的handler下针对url处理异常导致的漏洞。

![1731060245_672de2158c88d6c843ba2.png!small?1731060246306](https://image.3001.net/images/20241108/1731060245_672de2158c88d6c843ba2.png!small?1731060246306)

一个是远程代码执行模块，大都是在反序列化过程中，对数据处理不当导致的异常。

![](https://image.3001.net/images/20241111/1731287871_67315b3f81343dea87b51.png!small)

## 二 漏洞挖掘。

### 1.Exchange

Exchange最新版本也存在远程代码执行漏洞，在Exchange2013，Exchange2016，Exchange2019都可以使用。以下给大家展示下最新漏洞复现过程，不过由于漏洞未提交也不打算提交，所以就不公布细节了。

<https://wiki.freebuf.com/societyDetail/articleDetail?society_id=0&article_id=104329>

录屏挺清晰的，但是上传后感觉太模糊了，我重新装了个Exchange2019进行测试，上传后稍微清晰一些吧！

https://wiki.freebuf.com/societyDetail/articleDetail?society\_id=0&article\_id=115908

### 2.moodles

moodles最新版本同样存在远程加载漏洞，可以加载远程文件，从而弹窗以及获取用户cookie等敏感信息，感觉用处不是很大。

# 漏洞 # 渗透测试 # 网络安全 # 系统安全 # 漏洞分析

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

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

一 漏洞复现。

* 1.NetScaler ADC
* 2.sharepoint
* 3.winrar
* 4.Weblogic
* 5.word
* 6.exchenge

二 漏洞挖掘。

* 1.Exchange
* 2.moodles

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