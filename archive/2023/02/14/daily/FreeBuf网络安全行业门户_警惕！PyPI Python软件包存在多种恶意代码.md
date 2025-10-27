---
title: 警惕！PyPI Python软件包存在多种恶意代码
url: https://www.freebuf.com/news/357434.html
source: FreeBuf网络安全行业门户
date: 2023-02-14
fetch_date: 2025-10-04T06:31:58.365502
---

# 警惕！PyPI Python软件包存在多种恶意代码

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

警惕！PyPI Python软件包存在多种恶意代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕！PyPI Python软件包存在多种恶意代码

2023-02-13 15:20:24

所属地 上海

![](https://image.3001.net/images/20230213/1676268824_63e9d5186407ce1764f86.png!small)

近日，研究人员发现Python软件包索引（PyPI）中存在四个不同的流氓软件包，包括投放恶意软件，删除netstat工具以及操纵SSH authorized\_keys文件。

存在问题的软件包分别是是aptx、bingchilling2、httops和tkint3rs，这些软件包在被删除之前总共被下载了约450次。其中aptx是冒充高通公司比较流行的同名音频编、解码器，而httops和tkint3rs则分别是https和tkinter的盗版。不难看出这些软件包的名字都是刻意伪装过的的，目的就是为了迷惑人们。

经过对安装脚本中注入的恶意代码分析显示，存在一个虚假的Meterpreter有效载荷，它被伪装成 "pip"，可以利用它来获得对受感染主机的shell访问。

此外，还采取了一些步骤来删除用于监视网络配置和活动的netstat命令行实用程序，以及修改.ssh/authorized\_keys 文件以设置用于远程访问的 SSH 后门。

![](https://image.3001.net/images/20230213/1676268867_63e9d54315aeed1828364.png!small)

但是有迹象表明，潜入软件存储库的恶意软件是一种反复出现的威胁，Fortinet FortiGuard 实验室发现了五个不同的 Python 包——web3 -essential、3m-promo-gen-api、ai-solver-gen、hypixel-coins、httpxrequesterv2和httpxrequester 旨在收集和泄露敏感信息。

这些威胁是在 ReversingLabs 揭示了一个名为 aabquerys 的恶意 npm 模块时发布的，该模块伪装成合法的 abquery 包，试图诱骗开发人员下载它。

就其本身而言，经过混淆的 JavaScript 代码具有从远程服务器检索第二阶段可执行文件的功能，而远程服务器又包含一个 Avast 代理二进制文件 (wsc\_proxy.exe)，已知该文件容易受到 DLL侧载攻击。

![](https://image.3001.net/images/20230213/1676268894_63e9d55e72b28f7a62119.png!small)

这使攻击者能够调用一个恶意库，该恶意库被设计为从命令和控制（C2）服务器上获取第三阶段的组件Demon.bin。

ReversingLabs研究员Lucija Valentić说："Demon.bin是一个具有典型的RAT（远程访问木马）功能的恶意代理，它是使用一个名为Havoc的开源、后开发、命令和控制框架生成的。

此外，据说aabquerys的作者还发布了另外两个名为aabquery和nvm\_jquery的软件包的多个版本，它们有可能是aabquerys的早期迭代。

Havoc 远非唯一在野外检测到的 C2 利用框架，犯罪分子还在恶意软件活动中利用 Manjusaka、Covenant、Merlin 和 Empire 等自定义套件。

调查结果最后还强调了恶意软件包潜伏在npm 和 PyPi 等开源存储库中的风险越来越大，这可能会对软件供应链产生严重影响。

> 参考链接：https://thehackernews.com/2023/02/researchers-uncover-obfuscated.html

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