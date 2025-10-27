---
title: 注意！高级威胁组织APT-C-36正在活跃
url: https://www.freebuf.com/articles/359128.html
source: FreeBuf网络安全行业门户
date: 2023-03-03
fetch_date: 2025-10-04T08:32:21.078368
---

# 注意！高级威胁组织APT-C-36正在活跃

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

注意！高级威胁组织APT-C-36正在活跃

* ![]()
* 关注

注意！高级威胁组织APT-C-36正在活跃

2023-03-02 14:57:14

所属地 上海

近日，据黑莓安全研究与威胁情报团队称，名为Blind Eagle 的APT组织正在活跃，针对哥伦比亚各个关键行业发起持续性网络攻击，包括卫生、金融、执法、移民以及负责哥伦比亚和平谈判在内的机构都是该组织的重点攻击目标。黑莓安全研究与威胁情报团队还发现，该组织正在向厄瓜多尔、智利和西班牙地区扩张。![](https://image.3001.net/images/20230302/1677740169_6400488984d6ae29243d8.png!small)

资料显示，Blind Eagle又被称为APT-C-36，以高活跃度和高危害性出名。2018年4月，研究人员捕获到了第一个针对哥伦比亚政府的定向攻击样本，并在此后近一年时间内，先后捕获了多起针对哥伦比亚政企机构的定向攻击。

基于近段时间APT-C-36高活跃性，知名安全团队Check Point Research发布了该组织的详细调查报告，介绍了其高级工具集和攻击方式，例如通过鱼叉式网络钓鱼电子邮件传送的 Meterpreter 有效载荷。

简单来说，APT-C-36组织会精心设计用于网络钓鱼的电子邮件，其中往往带有一个指向PDF文件的链接，该文件会被托管至 DIAN 网站上，但实际上这是一条恶意链接，用户访问后系统将会感染恶意软件，从而被该组织入侵。

黑莓研究人员进一步指出，“假冒的 DIAN 网站页面包含一个按钮，诱导受害者下载 PDF 文件以查看该网站声称待处理的税务发票。访问后就会从 Discord 内容分发网络 (CDN) 下载恶意文件。”![](https://image.3001.net/images/20230302/1677740226_640048c2ab17431cb0fd7.jpg!small)

被用于攻击的有效载荷是一个混淆的 Visual Basic 脚本 (VBS)，它在打开“PDF”文件时执行，会利用 PowerShell 检索基于 .NET 的 DLL 文件，最终将 AsyncRAT 加载到内存中。而一旦恶意软件被安装在用户的系统上，APT-C-36组织就可以随时连接到受感染的端点，并执行任意操作。

值得一提的是，APT-C-36组织一般会使用DuckDNS 等动态 DNS服务来远程控制受感染的主机。由于在其鱼叉式网络钓鱼电子邮件中使用该语言，APT-C-36被认为是讲西班牙语的组织。

虽然目前无法确定APT-C-36组织基地的具体位置，但安全研究人员根据现有的信息认为其在南美洲，且该组织持续针对哥伦比亚政府、机构，因此被认为具有某个国家/地区的背景。

黑莓安全人员称，“该组织使用的作案手法与之前几乎保持一致，非常简单但是也很有效，这也意味着该组织内部对于，通过网络钓鱼电子邮件发起攻击活动的方式感到满意，并且对使用它们充满信心。”

那么问题来了？

为什么目标用户没有采取针对性的防御措施，APT-C-36组织又是通过什么来保障成功率？毕竟在网络安全领域，“一招鲜吃遍天”是一个低概率的事件。

参考来源：https://thehackernews.com/2023/02/apt-c-36-strikes-again-blind-eagle.html

# 钓鱼攻击 # 网络攻击 # APT组织

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