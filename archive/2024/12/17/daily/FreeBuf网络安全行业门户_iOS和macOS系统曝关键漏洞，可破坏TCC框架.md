---
title: iOS和macOS系统曝关键漏洞，可破坏TCC框架
url: https://www.freebuf.com/news/417772.html
source: FreeBuf网络安全行业门户
date: 2024-12-17
fetch_date: 2025-10-06T19:39:52.705690
---

# iOS和macOS系统曝关键漏洞，可破坏TCC框架

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

iOS和macOS系统曝关键漏洞，可破坏TCC框架

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

iOS和macOS系统曝关键漏洞，可破坏TCC框架

2024-12-16 10:41:53

所属地 上海

近日，苹果iOS和macOS系统中被曝光一个关键的安全漏洞，若被成功利用，可能会绕过透明度、同意和控制（TCC）框架，导致用户敏感信息被未经授权访问。漏洞编号CVE-2024-44131，存在于文件提供组件中，苹果通过在iOS 18、iPadOS 18和macOS Sequoia 15中增强符号链接的验证来修复此问题。

![](https://image.3001.net/images/20241216/1734317119_675f943f3240af7fc3158.png!small)

TCC作为苹果设备上的一项关键安全功能，允许用户对应用程序访问敏感数据的请求进行授权或拒绝，如GPS位置、联系人和照片等。

Jamf Threat Labs发现并报告该漏洞，该公司指出，“这种TCC绕过允许未经授权地访问文件和文件夹、健康数据、麦克风或摄像头等，而不会通知用户，这削弱了用户对iOS设备安全性的信任，并使个人数据面临风险。”

漏洞允许恶意应用在后台运行时，拦截用户在文件应用中复制或移动文件的操作，并将它们重定向到其控制的位置。这种劫持行为利用了fileproviderd的高权限，这是一个处理与iCloud和其他第三方云文件管理器相关的文件操作的守护进程，它移动文件后可以将它们上传到远程服务器。

Jamf进一步解释：“具体来说，当用户在后台运行恶意应用可访问的目录内使用Files.app移动或复制文件或目录时，攻击者可以操纵符号链接欺骗文件应用。新的符号链接攻击方法是，首先复制一个正常的文件，为恶意进程复制已开始的可检测信号。然后在复制过程已经开始后插入一个符号链接，有效地绕过符号链接检查。”

因此，攻击者可以利用这种方法复制、移动甚至删除路径“/var/mobile/Library/Mobile Documents/”下的各个文件和目录，以访问与第一方和第三方应用相关的iCloud备份数据，并将它们窃取。这个漏洞的严重之处在于它完全破坏了TCC框架，并且不会向用户触发任何提示。尽管如此，可以访问的数据类型取决于执行文件操作的系统进程。

Jamf表示：“这些漏洞的严重性取决于目标进程的权限，这揭示了对某些数据类型的访问控制执行存在差距，由于这种竞态条件，并非所有数据都可以在不发出警报的情况下提取。例如，由随机分配的UUID保护的文件夹中的数据，以及通过特定API检索的数据不受这种类型的攻击影响。”

与此同时，苹果发布了软件更新，以修复包括WebKit中的四个漏洞在内的多个问题，这些漏洞可能导致内存损坏或进程崩溃，以及音频中的一个逻辑漏洞（CVE-2024-54529），该漏洞可能允许应用程序执行具有内核权限的任意代码。

iPhone制造商还修复了Safari中的一个漏洞（CVE-2024-44246），该漏洞可能允许网站在启用私人中继的设备上将其添加到阅读列表时获取原始IP地址。苹果表示，它通过“改进Safari发起请求的路由”来解决这个问题。

参考来源：<https://thehackernews.com/2024/12/researchers-uncover-symlink-exploit.html>

# 漏洞 # 安全漏洞

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