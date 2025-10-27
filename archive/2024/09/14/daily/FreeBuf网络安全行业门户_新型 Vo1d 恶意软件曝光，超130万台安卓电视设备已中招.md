---
title: 新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招
url: https://www.freebuf.com/news/410913.html
source: FreeBuf网络安全行业门户
date: 2024-09-14
fetch_date: 2025-10-06T18:27:13.557744
---

# 新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招

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

新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招

2024-09-13 09:29:01

所属地 上海

![1726190813_66e394dd73d685bd35c97.png!small](https://image.3001.net/images/20240913/1726190813_66e394dd73d685bd35c97.png!small)

近日，有攻击者使用一种新的 Vo1d 后门恶意软件感染了 130 余万台安卓电视流媒体盒，使得攻击者能够完全控制这些设备。

Android TV是谷歌针对智能电视和流媒体设备推出的操作系统，为电视和远程导航提供了优化的用户界面，集成了谷歌助手，内置Chromecast，支持电视直播，并能安装应用程序。

该操作系统为包括 TCL、海信和 Vizio 电视在内的众多制造商提供智能电视功能。它还是英伟达 Shield 等独立电视流媒体设备的操作系统。

在 Dr.Web 的最新报告中，研究人员发现有 200 多个国家的 130 万台设备都感染了 Vo1 d 恶意软件，其中在巴西、摩洛哥、巴基斯坦、沙特阿拉伯、俄罗斯、阿根廷、厄瓜多尔、突尼斯、马来西亚、阿尔及利亚和印度尼西亚检测到的数量最多。

![1726190871_66e39517f411a101591ed.png!small](https://image.3001.net/images/20240913/1726190871_66e39517f411a101591ed.png!small)

受 Vo1d 感染电视盒的地理分布，图源：Dr.Web

在此次恶意软件活动中，被视为目标的安卓电视固件包括：

* 安卓 7.1.2；R4 版本/NHG47K
* 安卓 12.1；电视盒版本/NHG47K
* 安卓 10.1；KJ-SMART4KVIP Build/NHG47K

根据安装的 Vo1d 恶意软件版本，该活动将修改或替换操作系统文件，所有这些文件都是 Android TV 中常见的启动脚本。`install-recovery.sh``daemonsu``debuggerd`

![1726190893_66e3952d7dcbb875c5a56.png!small](https://image.3001.net/images/20240913/1726190893_66e3952d7dcbb875c5a56.png!small)

修改后的 install-recovery.sh 文件，图源：Dr.Web

该恶意软件活动利用这些脚本实现持久性，并在启动时激活Vo1d恶意软件。 Vo1d恶意软件本身位于文件中，这些文件的名称就是以该恶意软件命名的。Dr.Web解释称，Android.Vo1d的主要功能隐藏在其vo1d（Android.Vo1d.1）和wd（Android.Vo1d.3）组件中，这两个组件协同工作。

Android.Vo1d.1模块负责启动Android.Vo1d.3并控制其活动，必要时重启其进程。此外，它还可以在C&C服务器的指令下下载并运行可执行文件。

Android.Vo1d.3 模块负责安装并启动加密并存储在其体内的 Android.Vo1d.5 守护进程。该模块还可以下载并运行可执行文件。此外，它监控指定的目录，并安装在其中找到的 APK 文件。

尽管 Dr.Web 尚不清楚 Android 电视流媒体设备是如何被入侵的，但研究人员认为，这些设备之所以成为攻击目标，是因为它们通常运行着带有漏洞的过时软件。

Dr.Web 认为，其中最有可能的感染途径或许是中间恶意软件的攻击，该软件利用操作系统漏洞来获取 root 权限。另一个可能的途径可能是使用内置 root 访问权限的非官方固件版本。

为了防止这种恶意软件的感染，建议 Android 电视用户检查并安装新固件更新。同时确保在它们通过暴露的服务被远程利用的情况下，将这些设备从互联网上移除。

此外，用户也应避免在 Android 电视上从第三方网站安装 APK 形式的 Android 应用程序，因为它们是恶意软件的常见来源。

> 参考来源：[New Vo1d malware infects 1.3 million Android TV streaming boxes (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/new-vo1d-malware-infects-13-million-android-tv-streaming-boxes/)

# 安卓安全 # 安卓恶意软件

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