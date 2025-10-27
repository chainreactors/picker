---
title: 新型 Linux 恶意软件 “sedexp ”利用 Udev 规则隐藏信用卡盗刷器
url: https://www.freebuf.com/news/409427.html
source: FreeBuf网络安全行业门户
date: 2024-08-27
fetch_date: 2025-10-06T18:06:07.441767
---

# 新型 Linux 恶意软件 “sedexp ”利用 Udev 规则隐藏信用卡盗刷器

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

新型 Linux 恶意软件 “sedexp ”利用 Udev 规则隐藏信用卡盗刷器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型 Linux 恶意软件 “sedexp ”利用 Udev 规则隐藏信用卡盗刷器

2024-08-26 11:56:49

所属地 上海

网络安全研究人员发现了一种新的隐秘 Linux 恶意软件，它利用一种非常规技术在受感染系统上实现持久性，并隐藏信用卡盗刷代码。

Aon 的 Stroz Friedberg 事件响应服务团队将这款恶意软件命名为 sedexp，认为它是一个有经济动机的威胁行为者所为。

研究人员 Zachary Reichert、Daniel Stein 和 Joshua Pivirotto 表示："这种高级威胁自 2022 年开始活跃，它隐藏在众目睽睽之下，同时为攻击者提供反向 shell 功能和高级隐藏战术。

恶意行为者不断改进和完善他们的技术，并转而使用新技术来逃避检测，这并不奇怪。

sedexp 之所以值得关注，是因为它使用了 udev 规则来保持持久性。Udev 是设备文件系统（Device File System）的替代品，它提供了一种机制，可根据设备属性识别设备，并配置规则，以便在设备状态发生变化（即设备被插入或移除）时做出响应。

udev 规则文件中的每一行都至少有一个键值对，因此可以通过名称匹配设备，并在检测到各种设备事件时触发特定操作（例如，在连接外部硬盘时触发自动备份）。

SUSE Linux 在其文档中指出："匹配规则可以指定设备节点的名称，添加指向该节点的符号链接，或运行指定程序作为事件处理的一部分。如果找不到匹配规则，则使用默认设备节点名称创建设备节点。“

sedexp的udev规则——ACTION=="add", ENV{MAJOR}=="1", ENV{MINOR}=="8", RUN+="asedexpb run:+"——是这样设置的：每当/dev/random（对应设备次要编号8）加载时，就会运行恶意软件，这通常发生在每次重启时。

sedexp 的 udev 规则--ACTION==“add”, ENV{MAJOR}==“1”, ENV{MINOR}==“8”, RUN+=“asedexpb run:+” --设置为每当加载 /dev/random（对应设备次要序号 8）时运行恶意软件，这通常发生在每次重启时。

换句话说，每次系统重启后都会执行 RUN 参数中指定的程序。

该恶意软件具有启动反向 shell 的功能，以方便远程访问被入侵的主机，还能修改内存，从 ls 或 find 等命令中隐藏任何包含 “sedexp ”字符串的文件。

Stroz Friedberg 表示，在它调查的案例中，该功能被用来隐藏 web shell 、更改 Apache 配置文件和 udev 规则本身。

研究人员说："该恶意软件被用于在网络服务器上隐藏信用卡刮取代码，这表明该恶意软件的重点是经济收益。“sedexp 的发现表明，除了勒索软件之外，出于经济动机的威胁行为者的复杂性也在不断发展。

参考来源：

<https://thehackernews.com/2024/08/new-linux-malware-sedexp-hides-credit.html>

# webshell # 恶意软件 # 信用卡盗刷

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