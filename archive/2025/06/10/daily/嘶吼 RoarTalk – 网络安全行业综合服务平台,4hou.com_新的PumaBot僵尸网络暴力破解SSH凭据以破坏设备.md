---
title: 新的PumaBot僵尸网络暴力破解SSH凭据以破坏设备
url: https://www.4hou.com/posts/jB9l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-10
fetch_date: 2025-10-06T22:50:55.622998
---

# 新的PumaBot僵尸网络暴力破解SSH凭据以破坏设备

新的PumaBot僵尸网络暴力破解SSH凭据以破坏设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 新的PumaBot僵尸网络暴力破解SSH凭据以破坏设备

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-06-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)67802

收藏

导语：泄漏之后，文本文件将从受感染的主机上擦除，以删除恶意活动的任何痕迹。

一种新发现的基于Go的Linux僵尸网络恶意软件名为PumaBot，它通过暴力破解嵌入式物联网设备上的SSH凭证来部署恶意负载。

PumaBot 的针对性也体现在它根据从命令和控制 (C2) 服务器获取的列表针对特定的 IP 地址，而不是对互联网进行广泛的扫描。

**瞄准监控摄像头**

Darktrace在一份报告中记录了PumaBot，该报告概述了僵尸网络的攻击流程、入侵指标（IoCs）和检测规则。恶意软件从其C2 （ssh.ddos-cc.org）接收目标ip列表，并试图在端口22上执行暴力登录尝试以开放SSH访问。在这个过程中，它会检查“Pumatronix”字符串的存在，这可能与供应商的监控和交通摄像头系统的目标相对应。

一旦目标被建立，恶意软件就会接收凭证来针对它们进行测试。如果成功，它运行‘uname -a’来获取环境信息并验证目标设备不是蜜罐。

接下来，它将它的主二进制文件（jierui）写入/lib/redis，并安装一个systemd服务（redis.service），以确保设备重启时的持久性。

最后，它将自己的SSH注入到“authorized\_keys”文件中以保持访问，即使在清除了主要感染的情况下也是如此。

当感染处于活跃状态时，PumaBot可以接收命令，试图窃取数据，引入新的有效载荷，或窃取横向移动中有用的数据。

Darktrace看到的有效负载示例包括自我更新脚本、PAM rootkit（替换合法的“pam\_unix”）。所以'和daemons（二进制文件“1”）。

恶意PAM模块获取本地和远程SSH登录详细信息，并将其存储在一个文本文件（con.txt）中。“监视者”二进制文件(1)不断查找该文本文件，然后将其泄露到C2。

![credentials.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250529/1748503449833155.png "1748499432652321.png")

在文本文件上写入凭据

在泄漏之后，文本文件将从受感染的主机上擦除，以删除恶意活动的任何痕迹。PumaBot的规模和成功概率目前尚不清楚，也没有资料提到目标IP列表有多广泛。

这种新型僵尸网络恶意软件的特别之处在于，它不是直接利用受感染的物联网进行分布式拒绝服务（DoS）攻击或代理网络等低级网络犯罪，而是发起有针对性的攻击，从而为企业网络的深入渗透开辟了道路。

为了防御僵尸网络威胁，建议将物联网升级到最新可用的固件版本，更改默认凭据，将它们置于防火墙之后，并将它们与有价值的系统隔离在单独的网络中。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-pumabot-botnet-brute-forces-ssh-credentials-to-breach-devices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9XTq3Rys)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)