---
title: 假冒的7-Zip官网暗藏代理木马传播恶意安装包
url: https://www.4hou.com/posts/W1Zn
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-24
fetch_date: 2026-02-25T04:13:40.867909
---

# 假冒的7-Zip官网暗藏代理木马传播恶意安装包

假冒的7-Zip官网暗藏代理木马传播恶意安装包 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 假冒的7-Zip官网暗藏代理木马传播恶意安装包

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)11070

收藏

导语：此次攻击活动并非仅伪装7-Zip，还通过篡改HolaVPN、TikTok、WhatsApp、Wire VPN等软件的安装包传播。

安全研究人员发现，一个伪造的7-Zip网站正在分发被植入木马的压缩工具安装包，该恶意程序会将用户电脑变为住宅代理节点。

住宅代理网络利用家庭用户设备转发流量，以此绕过访问限制，并实施凭证填充、网络钓鱼、恶意软件分发等各类恶意活动。

这一新型攻击活动因用户举报引发广泛关注：该用户在观看YouTube上的电脑装机教程后，依照教程指引，从一个冒充7-Zip官方的网站下载了恶意安装包。

攻击者注册了7zip.com域名，极易误导用户以为访问的是官方工具站点。此外，攻击者还完整复制了7-Zip官方网站（7-zip.org）的文字内容与页面结构。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770792777743702.png "1770792777743702.png")

传播木马化 7-Zip 安装包的恶意网站

研究人员对该安装包进行分析后发现，其使用一张已被吊销的数字证书签名，证书原颁发给Jozeal Network Technology Co.，Limited。

该恶意安装包内同样包含正常的7-Zip程序，可提供工具的完整功能，但会在安装过程中释放三个恶意文件：

**·**Uphero.exe——服务管理与更新加载程序

**·**hero.exe——代理核心载荷

**·**hero.dll——支持库

这些文件会被释放至C:\Windows\SysWOW64\hero\目录，程序还会以SYSTEM权限创建Windows自启动服务，确保恶意程序持久运行。同时，攻击者通过netsh命令修改防火墙规则，允许恶意程序发起内外网连接。

最终，恶意程序会通过Windows管理规范（WMI）与Windows应用程序接口采集主机硬件、内存、CPU、磁盘及网络配置信息，并将数据上报至iplogger.org。

研究人员在分析该恶意程序目的时表示：“尽管初步迹象显示其具备后门类功能，但进一步分析证实，该恶意软件的核心用途为代理程序。受感染主机会被纳入住宅代理网络，允许第三方通过受害者IP地址转发流量。”

分析显示，hero.exe会从轮换的smshero系列C2域名获取配置，并在1000、1002等非常规端口开启外连代理通道，控制指令则通过轻量级XOR算法进行混淆加密。

此次攻击活动并非仅伪装7-Zip，还通过篡改HolaVPN、TikTok、WhatsApp、Wire VPN等软件的安装包传播。

该恶意软件使用以hero/smshero为主题的轮换式命令控制基础设施，流量经Cloudflare并采用TLS加密的HTTPS协议传输；同时通过谷歌解析器使用HTTPS加密DNS（DoH），降低防守方对常规DNS流量监控的可见性。

程序还会检测VMware、VirtualBox、QEMU、Parallels等虚拟化环境及调试器，以此识别自身是否处于分析环境中。

安全专家建议用户，不要直接点击YouTube视频中的链接或搜索引擎推广结果，应为常用软件的官方下载页面添加书签，从正规渠道获取软件。

文章来源自：https://www.bleepingcomputer.com/news/security/malicious-7-zip-site-distributes-installer-laced-with-proxy-tool/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mCzCEock)

#### 你可能感兴趣的

* [![]()

  恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)
* [![]()

  Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)
* [![]()

  新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)
* [![]()

  假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)
* [![]()

  新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)
* [![]()

  AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)
  2026-02-25 12:00:00
* [Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)
  2026-02-25 11:59:00
* [新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)
  2026-02-24 12:00:00
* [假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)
  2026-02-24 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)

  胡金鱼
* [Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)

  胡金鱼
* [新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)

  胡金鱼
* [假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)

  胡金鱼
* [新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)

  胡金鱼
* [AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)

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