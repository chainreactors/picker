---
title: 通过二维码实现命令与控制操作的新方法
url: https://www.freebuf.com/news/417227.html
source: FreeBuf网络安全行业门户
date: 2024-12-10
fetch_date: 2025-10-06T19:39:33.470993
---

# 通过二维码实现命令与控制操作的新方法

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

新型攻击技术曝光：通过二维码实现命令与控制操作

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型攻击技术曝光：通过二维码实现命令与控制操作

2024-12-09 14:34:59

所属地 上海

Mandiant技术公司最近发现了一种新型攻击手段，该手段能够绕过浏览器隔离技术，并通过二维码实现命令与控制（C2）操作。

![](https://image.3001.net/images/20241213/1734077850_675bed9a47958086c10cd.png!small)

浏览器隔离是一种日益受到青睐的安全技术，它通过将所有本地Web浏览器请求重定向到云环境或虚拟机中托管的远程Web浏览器来执行。这样，访问的网页上的所有脚本或内容都在远程浏览器上执行，而不是在本地浏览器上。然后，页面的渲染像素流被发送回请求的本地浏览器，仅显示页面的外观，从而保护本地设备不受任何恶意代码的影响。

许多C2服务器通过HTTP进行通信，而远程浏览器隔离能够过滤恶意流量，使得这些通信模式失效。Mandiant公司发现的新技术试图绕过这些限制，尽管存在一些实际限制，但它揭示了浏览器中现有的安全保护措施并非完美，需要采取“防御性多层次”策略，并结合其他措施。

C2通道允许攻击者与受损系统之间进行恶意通信，使远程黑客能够控制被侵入的设备，执行命令、泄露数据等。由于浏览器本质上需要不断地与外部服务器交互，因此在安全关键环境中会启用隔离措施，以防止攻击者访问底层系统上的敏感数据。这是通过在云端、本地虚拟机或本地环境中运行浏览器的独立沙箱环境来实现的。

当隔离处于激活状态时，隔离的浏览器处理传入的HTTP请求，仅将页面的可视内容流式传输到本地浏览器，这意味着HTTP响应中的脚本或命令永远不会到达目标设备。这阻止了攻击者直接访问HTTP响应或将恶意命令注入浏览器，使得秘密的C2通信变得更加困难。

![](https://image.3001.net/images/20241213/1734077871_675bedaf91737fc8fc7b6.png!small)

攻击者不是将命令嵌入HTTP响应中，而是将它们编码到网页上可视地显示的二维码中。由于在浏览器隔离请求期间不会删除网页的可视渲染，因此二维码能够返回到发起请求的客户端。

在Mandiant的研究中，"受害者"的本地浏览器是由之前感染了设备的恶意软件控制的无头客户端，它会捕获检索到的二维码并对其进行解码以获取指示。

![](https://image.3001.net/images/20241213/1734077903_675bedcfe5616c301a201.png!small)

尽管概念验证表明这种攻击是可行的，但这种技术并不完美，尤其是考虑到实际应用性。首先，数据流的最大限制是2189字节，大约为二维码可以携带的最大数据的74%，如果在恶意软件解释器上读取二维码时存在问题，则数据包的大小还需要进一步减少。其次，需要考虑延迟问题，每个请求需要大约5秒。这将限制数据传输速率约为438字节/秒，因此这种技术不适合发送大容量荷载或支持SOCKS代理。最后，Mandiant表示其研究未考虑领域声誉、URL扫描、数据丢失预防和请求启发式等其他安全措施，这些措施可能会在某些情况下阻止此攻击或使其无效。

尽管Mandiant基于二维码的C2技术是低带宽的，但如果未经阻止仍然可能带来危险。因此，建议在关键环境中的管理员监测异常流量和以自动化模式运行的浏览器。

参考来源：<https://www.bleepingcomputer.com/news/security/qr-codes-bypass-browser-isolation-for-malicious-c2-communication/>

# 数据安全

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