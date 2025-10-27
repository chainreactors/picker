---
title: 谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码
url: https://www.freebuf.com/news/416908.html
source: FreeBuf网络安全行业门户
date: 2024-12-06
fetch_date: 2025-10-06T19:38:29.916562
---

# 谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码

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

谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码

2024-12-05 11:29:27

所属地 上海

据Cyber Security News消息，最近，独立研究人员在谷歌Chrome 的 V8 JavaScript 引擎中发现了一个严重性较高的类型混淆漏洞。

![](https://image.3001.net/images/20241205/1733369423_67511e4f50258033a7e83.png!small)

该漏洞被追踪为 CVE-2024-12053，当程序为一种数据类型分配内存，却错误地将其视为另一种数据类型时，就会出现类型混淆漏洞。 攻击者可能利用此漏洞在受影响的系统上执行远程代码，从而导致系统受损和数据盗窃。

谷歌已在其最新的 Chrome 更新中迅速解决了该问题，包括适用于 Windows 和 Mac 的 131.0.6778.108/.109版本 ，以及适用于 Linux 的 131.0.6778.108版本。这些更新将在未来几天至几周内推出。

虽然谷歌没有提供利用这一漏洞进行攻击的具体细节，但该公司通常会限制此类信息，直到大多数用户更新了浏览器以降低潜在风险。

Chrome 浏览器的安全团队强调了他们正在进行的内部安全工作的重要性，通过审计、模糊处理和其他措施，他们已经修复了各种问题。

而该漏洞的发现者“gal1ium”和“chluo”因此获得了8000美元奖金，他们于2024 年 11 月 14 日对这一问题进行了报告。根据今年谷歌新发布的Chrome 漏洞赏金计划，新的奖励机制将发现重大漏洞的最高奖金提高到了25万美元，相比之前最高4万美元有了大幅提升。

## 谷歌Chrome 今年已修复了10个零日漏洞

截至今年8月26日，谷歌Chrome 已经修复了今年的第10个零日漏洞。这些漏洞包括：

* **CVE-2024-0519：**Chrome 浏览器 V8 JavaScript 引擎存在一个严重的越界内存访问漏洞，允许远程攻击者通过特制的 HTML 页面利用堆破坏，导致未经授权访问敏感信息。
* **CVE-2024-2887：**WebAssembly (Wasm) 标准中的高严重性类型混乱漏洞。该漏洞可导致利用伪造的 HTML 页面进行远程代码执行 (RCE) 的漏洞。
* **CVE-2024-2886：**网络应用程序用于编码和解码音频和视频的 WebCodecs API 存在使用后即释放漏洞。
* **CVE-2024-4671：**在处理浏览器中内容的呈现和显示的 Visuals 组件中存在一个高严重性的 use-after-free 缺陷。
* **CVE-2024-3159：**Chrome V8 JavaScript 引擎中的越界读取导致的高严重性漏洞。
* **CVE-2024-4761：**Chrome 浏览器的 V8 JavaScript 引擎中存在越界写入问题，该引擎负责在应用程序中执行 JS 代码。
* **CVE-2024-4947：**Chrome V8 JavaScript 引擎中的类型混乱，可安装任意代码。
* **CVE-2024-5274：**Chrome 浏览器 V8 JavaScript 引擎的一种混乱，可能导致崩溃、数据损坏或任意代码执行。
* **CVE-2024-7965：**Chrome  V8 JavaScript 引擎中的一个不恰当实现，可让远程攻击者通过制作 HTML 页面造成堆内存损坏。
* **CVE-2024-7971：**Chrome  V8 JavaScript 引擎中存在类型混乱，可让远程攻击者通过制作 HTML 页面造成堆内存损坏。

**参考来源：**

> [Google Chrome Type Confusion Vulnerability Let Attackers Execute Remote Code](https://cybersecuritynews.com/google-chrome-type-confusion-vulnerability/#google_vignette)

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

谷歌Chrome 今年已修复了10个零日漏洞

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