---
title: 低成本恶意软件泛滥，能窃取多个浏览器存储的个人数据
url: https://www.freebuf.com/news/412760.html
source: FreeBuf网络安全行业门户
date: 2024-10-15
fetch_date: 2025-10-06T18:51:29.210254
---

# 低成本恶意软件泛滥，能窃取多个浏览器存储的个人数据

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

低成本恶意软件泛滥，能窃取多个浏览器存储的个人数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

低成本恶意软件泛滥，能窃取多个浏览器存储的个人数据

2024-10-14 10:00:51

所属地 上海

网络中存在的各类威胁错综复杂且不断变化，攻击者一直在改进其攻击方法，经常出现一些新的信息窃取恶意软件。据Cyber Security News消息，最近一种名为 PureLogs 的恶意软件以其低廉的价格、不俗的功能受到攻击者青睐。

![](https://image.3001.net/images/20241014/1728873250_670c832247aecf13a84a3.png!small)

PureLogs  是用 C# 构建的 64 位信息窃取程序，并使用 commercial.NET Reactor 打包器将其程序集捆绑到多个阶段， 能够通过 Chrome、Edge、Opera等浏览器获取私人信息，与 Lumma、Vidar 和 Meduza 等少数其他恶意软件具有相同的能力。

2022 年，PureLogs 最初在地下市场上出售，此后在多个地下论坛上进行了推广，并在 clearnet 上保留了一个帐户和专用市场。目前该程序通过将潜在客户引导至特定Telegram机器人以获得支持和销售查询，价格为每月99美元、每季度199美元、每年299美元和终身用户的499美元，是市场上最便宜的信息窃取程序之一。

根据 Flashpoint Intel Team 报告，PureLogs 分三个阶段运行。加载和执行阶段是第一个阶段，第二阶段是在加载最终信息窃取程序集之前进行反沙箱测试和网络配置。到了第三阶段，PureLogs开始实施信息窃取程序代码，并获取以下信息：

* 浏览数据
* Chrome、Edge 和 Opera 扩展
* 加密货币钱包应用程序
* 桌面应用程序
* 受害者计算机信息

文件夹、文件扩展名等都可以被 PureLogs 识别并抓取，并可将相关数据传输到 Telegram。PureLogs 的Telegram 面板可显示受害者的详细信息、被窃数据的数量、捕获的屏幕截图以及可以整个下载的日志文件。

由于该恶意软件非常易于操作、价格低廉且进入门槛低，让低水平攻击者也能成功实施较复杂的攻击操作。

**参考来源：**

> [PureLogs, Low Cost Infostealer Attacking Chrome Browser](https://cybersecuritynews.com/purelogs-chrome-browser/)

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