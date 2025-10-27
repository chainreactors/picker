---
title: 恶意软件 Stealc “横空出世”，窃密能力一流
url: https://www.freebuf.com/news/358256.html
source: FreeBuf网络安全行业门户
date: 2023-02-22
fetch_date: 2025-10-04T07:43:20.579138
---

# 恶意软件 Stealc “横空出世”，窃密能力一流

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

恶意软件 Stealc “横空出世”，窃密能力一流

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

恶意软件 Stealc “横空出世”，窃密能力一流

2023-02-21 15:52:11

所属地 上海

Bleeping Computer 网站披露，暗网市场出现了一个名为 Stealc 的新恶意软件，由于大肆宣传窃取信息的能力，以及与 Vidar、Raccoon、Mars 和 Redline 等同类恶意软件具有相似性，获得行业内广泛关注。![1676966141_63f478fd8b363085b9d98.png!small?1676966144087](https://image.3001.net/images/20230221/1676966141_63f478fd8b363085b9d98.png!small?1676966144087)

据悉，2023 年 1 月，网络威胁情报公司 SEKOIA 安全研究人员首次发现了 Stealc ，一个月后，观察到该恶意软件开始进行恶意活动。

## ****Stealc**** ****恶意软件在暗网上大肆推广****

最早，一位名叫 Plymouth 的用户在黑客论坛上发布了大量有关 Stealc 的“广告”，宣称其是一种具有广泛数据窃取能力以及具有易使用管理面板的恶意软件。![1676966159_63f4790f8b3796d4edf67.png!small?1676966161306](https://image.3001.net/images/20230221/1676966159_63f4790f8b3796d4edf67.png!small?1676966161306)

暗网上宣传 Stealc 的帖子 (SEKOIA)

从“广告”内容来看，Stealc 除了能针对网络浏览器数据、扩展程序和加密货币钱包等典型目标外，还有一个可定制化的文件抓取器，能够人为设置想要窃取的任意文件类型。

发布最初的“宣传广告”后，Plymouth 陆续在其它黑客论坛上大肆推广 Stealc 恶意软件，以期向潜在客户提供测试样本，达成交易。

此外，Plymouth 还特地建立一个 Telegram 频道，专门发布 Stealc 新版本的更新日志（最新版本为 V1.3.0，于 2023 年 2 月 11 日发布），需要警惕的是，该恶意软件正在疯狂迭代中，几乎每周都会推出更新版本。

某些帖子中，Plymouth 指出 Stealc 恶意软件并非从零开发，而是基于 Vidar、Raccoon、Mars 和 Redline 等恶意软件优化而来。研究人员对 Stealc 深入分析后发现，该恶意软件和 Vidar、Raccoon 和 Mars 等确实有相似之处，几者都是通过下载合法的第三方 DLL（如sqlite3.dll、nss3.dll），来窃取受害者敏感数据。

## ****Stealc 的功能****

今年 1 月首次发布以来，Stealc 更新了许多功能，其中包括随机化 C2  URL 的系统、更好的日志（被盗文件）搜索和排序系统，以及乌克兰受害者自动排除系统。![1676966171_63f4791baea8ce1c4e0d4.png!small?1676966173376](https://image.3001.net/images/20230221/1676966171_63f4791baea8ce1c4e0d4.png!small?1676966173376)

恶意软件开发时间线（SEKOIA）

SEKOIA 通过分析捕获的样本，发现 Stealc 的部分特征如下。

> 轻量级构建：只有 80KB
>
> 使用合法的第三方 DLLs
>
> 用 C 语言编写，滥用 Windows API 函数
>
> 大多数字符串用 RC4 和 base64 进行混淆
>
> 能够自动渗出被盗数据
>
> 攻击目标：22 个网络浏览器、75 个插件和 25 个桌面钱包。

部署过程中，Stealc 恶意软件会对自身字符串进行解密，并执行反分析检查，以确保其不会在虚拟环境或沙盒中运行。之后，立刻动态加载 WinAPI 函数并启动与 C2 服务器的通信，在第一条信息中发送受害者的硬件标识符和构建名称，并接收响应配置。![1676966190_63f4792eb118095477cc0.png!small?1676966191667](https://image.3001.net/images/20230221/1676966190_63f4792eb118095477cc0.png!small?1676966191667)

目标浏览器的配置指令（SEKOIA）

接下来，Stealc 开始从目标浏览器、扩展程序和应用程序中收集数据，如果处于激活状态，会执行其自定义文件抓取器，最后将所有内容导出到 C2。值得一提的是，窃密活动结束后，Stealc 会把自身和下载的DLL 文件从被感染的主机上删除，以清除入侵痕迹。

研究人员观察到 Stealc 其中之一的传播方式是通过 YouTube，这些视频描述如何安装破解软件并链接到下载网站。![1676966199_63f47937e65cb530a1d74.png!small?1676966201724](https://image.3001.net/images/20230221/1676966199_63f47937e65cb530a1d74.png!small?1676966201724)

最后，研究人员指出，这些下载的软件中嵌入了 Stealc 恶意软件，一旦用户安装程序，恶意软件就开始了“常规”工作，并迅速与其服务器进行通信。因此建议用户不要安装盗版软件，从官方网站下载产品。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/new-stealc-malware-emerges-with-a-wide-set-of-stealing-capabilities/

# 恶意软件

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

Stealc 恶意软件在暗网上大肆推广

Stealc 的功能

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