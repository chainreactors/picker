---
title: 黑客利用 Xeon Sender 发起大规模短信钓鱼攻击
url: https://www.freebuf.com/news/409012.html
source: FreeBuf网络安全行业门户
date: 2024-08-21
fetch_date: 2025-10-06T18:03:50.506347
---

# 黑客利用 Xeon Sender 发起大规模短信钓鱼攻击

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

黑客利用 Xeon Sender 发起大规模短信钓鱼攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客利用 Xeon Sender 发起大规模短信钓鱼攻击

2024-08-20 10:19:35

所属地 上海

![1724121422_66c4014ee91144d5e2359.png!small](https://image.3001.net/images/20240820/1724121422_66c4014ee91144d5e2359.png!small)

恶意行为者正在使用一种名为 Xeon Sender 的云攻击工具，通过滥用合法服务大规模开展短信钓鱼和垃圾邮件活动。

SentinelOne安全研究员亚Alex Delamotte在与《黑客新闻》分享的一份报告中提到：攻击者可以利用Xeon通过多个软件即服务（SaaS）提供商，使用服务提供商的有效凭证发送信息。

据悉，用于大规模分发短信的服务包括亚马逊通知服务（SNS）、Nexmo、Plivo、Proovl、Send99、Telesign、Telnyx、TextBelt 和 Twilio。

值得注意的是，该活动并没有利用这些提供商的任何固有弱点，而是使用合法的 API 进行垃圾短信群发攻击。还引用了 SNS Sender 等工具，这些工具越来越多地成为批量发送钓鱼信息并最终获取目标敏感信息的途径。

其主要是通过 Telegram 和黑客论坛传播，其中一个旧版本归功于一个专门宣传破解黑客工具的 Telegram 频道。最新版本以 ZIP 文件形式提供下载，归功于一个名为 Orion Toolxhub的 Telegram 频道，该频道有 200 名成员。

Orion Toolxhub 创建于 2023 年 2 月 1 日，免费为成员提供可用于暴力破解攻击、IP 地址反向查询的软件，如 WordPress 网站扫描器、PHP web shell、比特币剪切器，以及一个名为 YonixSMS 的程序，该程序声称可提供无限短信发送功能。

Xeon Sender 也被称为 XeonV5 和 SVG Sender。这个基于 Python 的程序的早期版本最早在 2022 年被检测到。

Delamotte 表示：该工具的另一个化身是托管在带有图形用户界面的网络服务器上。这种托管方式消除了潜在的访问障碍，使那些可能不擅长运行 Python 工具并对其依赖关系进行故障排除的技术水平较低的攻击者也能使用。

无论使用哪种变体，Xeon Sender 都为用户提供了一个命令行界面，可用于与所选服务提供商的后台 API 通信，并协调垃圾短信群发攻击。

这也意味着威胁分子已经掌握了访问端点所需的 API 密钥。精心制作的 API 请求还包括发件人 ID、信息内容以及从文本文件中的预定义列表中选择的电话号码之一。

除了短信发送方法外，Xeon Sender还具有验证Nexmo和Twilio账户凭证、为给定的国家代码和地区代码生成电话号码以及检查所提供的电话号码是否有效等功能。

SentinelOne 表示，尽管该工具缺乏精细度，但源代码中充满了单个字母或字母加数字等模棱两可的变量，使调试工作更具挑战性。

Xeon Sender 主要使用供应商特定的 Python 库来制作 API 请求，这给检测带来了更大的挑战。因为每个库都是独一无二的，提供商的日志也是如此，团队可能很难检测到对特定服务的滥用行为。

因此，为了抵御 Xeon Sender 这样的威胁，企业应该监控与评估或修改短信发送权限相关的活动，或对分发列表的异常更改，如大量上传新的收件人电话号码。

> 参考来源：[Xeon Sender Tool Exploits Cloud APIs for Large-Scale SMS Phishing Attacks](https://thehackernews.com/2024/08/xeon-sender-tool-exploits-cloud-apis.html)

# 网络钓鱼 # 钓鱼攻击

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