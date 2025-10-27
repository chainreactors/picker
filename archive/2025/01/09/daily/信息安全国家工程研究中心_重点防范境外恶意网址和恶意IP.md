---
title: 重点防范境外恶意网址和恶意IP
url: https://mp.weixin.qq.com/s?__biz=MzU5OTQ0NzY3Ng==&mid=2247498716&idx=1&sn=24772d9c2334bee074a868f83af9241b&chksm=feb67acfc9c1f3d9811525b69c0fbaf966a633627e675b238da881dcd6f093540b58cc9e54e3&scene=58&subscene=0#rd
source: 信息安全国家工程研究中心
date: 2025-01-09
fetch_date: 2025-10-06T20:11:26.657209
---

# 重点防范境外恶意网址和恶意IP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jmN6xCKMlqjWRebJ49PATnSRtpMianMWulsB6uZ7FcsdQYh5joMQcaE9nf87OcMUWXNT0hx2JGjlQ2qnEbjBaQg/0?wx_fmt=jpeg)

# 重点防范境外恶意网址和恶意IP

NERCIS

信息安全国家工程研究中心

![](https://mmbiz.qpic.cn/mmbiz_gif/jmN6xCKMlqjWRebJ49PATnSRtpMianMWuJN7mOsHBVG8bibDso4a1ARIQGSxLebBR9RderHdngibZHoowpKTHsP3w/640?wx_fmt=gif&from=appmsg)

中国国家网络与信息安全信息通报中心发现一批境外恶意网址和恶意IP，境外黑客组织利用这些网址和IP持续对中国和其他国家发起网络攻击。这些恶意网址和IP都与特定木马程序或木马程序控制端密切关联，网络攻击类型包括建立僵尸网络、网络钓鱼、窃取商业秘密和知识产权、侵犯公民个人信息等，对中国国内联网单位和互联网用户构成重大威胁，部分活动已涉嫌刑事犯罪。相关恶意网址和恶意IP归属地主要涉及：美国、荷兰、新加坡、土耳其、墨西哥、越南等。主要情况如下：

**一、恶意地址信息**

**（一）恶意地址：**gael2024.kozow.com

**关联IP地址：**149.28.98.229

**归属地：**美国/佛罗里达州/迈阿密

**威胁类型：**后门

**病毒家族：**AsyncRAT

**描述：**该恶意地址关联多个AsyncRAT病毒家族样本，部分样本的MD5值为50860f067b266d6a370379e8bcd601ba。相关后门程序采用C#语言编写，主要功能包括屏幕监控、键盘记录、密码获取、文件窃取、进程管理、开关摄像头、交互式shell，以及访问特定URL等。这些病毒可通过移动存储介质、网络钓鱼邮件等方式进行传播，现已发现多个关联变种，部分变种主要针对中国境内民生领域的重要联网系统。

**（二）恶意地址：**185.174.101.218

**归属地：**美国/加利福尼亚州/洛杉矶

**威胁类型：**后门

**病毒家族：**RemCos

**描述：**该恶意地址关联到多个RemCos病毒家族样本，部分样本的MD5值为56f94f8aed310e90b5f513b1eb999c69。RemCos是一款远程管理工具，自2016年起就已存在。攻击者可以利用受感染系统的后门访问权限收集敏感信息并远程控制系统。最新版本的RemCos可以执行各种恶意活动，包括键盘记录、截取屏幕截图和窃取密码。

**（三）恶意地址：**

counterstrike2-cheats.com

**关联IP地址：**45.137.198.211

**归属地：**荷兰/北荷兰省/阿姆斯特丹

**威胁类型：**僵尸网络

**病毒家族：**mirai

**描述：**这是一种Linux僵尸网络病毒，通过网络下载、漏洞利用、Telnet和SSH暴力破解等方式进行扩散，入侵成功后可对目标网络系统发起分布式拒绝服务（DDoS）攻击。

**（四）恶意地址：**bot.merisprivate.net

**关联IP地址：**194.120.230.54

**归属地：**荷兰/北荷兰省/阿姆斯特丹

**威胁类型：**僵尸网络

**病毒家族：**mirai

**描述：**这是一种Linux僵尸网络病毒，通过网络下载、漏洞利用、Telnet和SSH暴力破解等方式进行扩散，入侵成功后可对目标网络系统发起分布式拒绝服务（DDoS）攻击。

**（五）恶意地址：**localvpn.anondns.net

**关联IP地址：**37.120.141.162

**归属地：**荷兰/北荷兰省/阿姆斯特丹

**威胁类型：**后门

**病毒家族：**Nanocore

**描述：**该恶意地址关联到Nanocore病毒家族样本，部分样本的MD5值为954866a242963b6a2caadf0c5b7df5e1，Nanocore是一种远程访问木马，被用于间谍活动和系统远程控制。攻击者获得感染病毒的主机访问权限，能够录制音频和视频、键盘记录、收集凭据和个人信息、操作文件和注册表、下载和执行其它恶意软件负载等。Nanocore还支持插件，能够扩展实现各种恶意功能，比如挖掘加密货币，勒索软件攻击等。

**（六）恶意地址：**

bueenotgay.duckdns.org

**关联IP地址：**217.15.161.176

**归属地：**新加坡

**威胁类型：**僵尸网络

**病毒家族：**MooBot

**描述：**这是一种Mirai僵尸网络的变种，常借助各种IoT设备漏洞例如CVE-2015-2051、CVE-2018-6530、CVE-2022-26258、CVE-2022-28958等实施入侵，攻击成功后，受害设备将下载并执行MooBot的二进制文件，进而组建僵尸网络并可能发起DDoS(分布式拒绝服务)攻击。

**（七）恶意地址：**sidiaisi168.com

**关联IP地址：**154.211.96.238

**归属地：**新加坡

**威胁类型：**后门

**病毒家族：**Farfli

**描述：**该恶意地址关联到多个Farfli病毒家族样本，部分样本的MD5值为b860f4174f47f3622d7175f1e66b49c2。Farfli是一种远控木马，能够通过网络下载、软件捆绑、网络钓鱼等多种方式传播。其允许远程攻击者执行多种远控操作，比如监控电脑屏幕、键盘记录、下载安装任意文件、窃取隐私信息，甚至还可以控制感染的计算机发起DDoS攻击。

**（八）恶意地址：**94.122.78.238

**归属地：**土耳其/伊斯坦布尔省/伊斯坦布尔

**威胁类型：**僵尸网络

**病毒家族：**gafgyt

**描述：**这是一种基于因特网中继聊天（IRC）协议的物联网僵尸网络病毒，主要通过漏洞利用和内置的用户名、密码字典进行Telnet和SSH暴力破解等方式进行扩散传播。可对网络设备进行扫描，攻击网络摄像机、路由器等IoT设备，攻击成功后，利用僵尸程序形成僵尸网络，对目标网络系统发起分布式拒绝服务（DDoS）攻击，可能造成大面积网络瘫痪。

**（九）恶意地址：**

windowwork.duckdns.org

**关联IP地址：**103.88.234.204

**归属地：**墨西哥/墨西哥联邦区/墨西哥城

**威胁类型：**后门

**病毒家族：**RemCos

**描述：**该恶意地址关联到多个RemCos病毒家族样本，部分样本的MD5值为6dfbc8b366bd1f4ebd33695b8f8fa521。RemCos是一款远程管理工具，自2016年起就已存在。攻击者可以利用受感染系统的后门访问权限收集敏感信息并远程控制系统。最新版本的RemCos可以执行各种恶意活动，包括键盘记录、截取屏幕截图和窃取密码。

**（十）恶意地址：**cnc.loctajima.website

**关联IP地址：**103.28.35.146

**归属地：**越南/胡志明市

**威胁类型：**僵尸网络

**病毒家族：**MooBot

**描述：**这是一种Mirai僵尸网络的变种，常借助各种IoT设备漏洞例如CVE-2015-2051、CVE-2018-6530、CVE-2022-26258、CVE-2022-28958等实施入侵，攻击成功后，受害设备将下载并执行MooBot的二进制文件，进而组建僵尸网络并可能发起DDoS(分布式拒绝服务)攻击。

**二、排查方法**

（一）详细查看分析浏览器记录以及网络设备中近期流量和DNS请求记录，查看是否有以上恶意地址连接记录，如有条件可提取源IP、设备信息、连接时间等信息进行深入分析。

（二）在本单位应用系统中部署网络流量检测设备进行流量数据分析，追踪与上述网络和IP发起通信的设备网上活动痕迹。

（三）如果能够成功定位到遭受攻击的联网设备，可主动对这些设备进行勘验取证，进而组织技术分析。

**三、处置建议**

（一）对所有通过社交平台或电子邮件渠道接收的文件和链接保持高度警惕，重点关注其中来源未知或不可信的情况，不要轻易信任或打开相关文件。

（二）及时在威胁情报产品或网络出口防护设备中更新规则，坚决拦截以上恶意网址和恶意IP的访问。

（三）向有关部门及时报告，配合开展现场调查和技术溯源。

*来源：国家网络安全通报中心*

![](https://mmbiz.qpic.cn/mmbiz_gif/jmN6xCKMlqjWRebJ49PATnSRtpMianMWueIlgdmnv17vKcLlMFj75O4QiahNdiby8keE0OeHLfaNP1flvu4N2gJNQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/jmN6xCKMlqjWRebJ49PATnSRtpMianMWuqS51sGPdb7q73R9UE0g4EHny8E2WUIicEHYVpEI1F1Lpoe6u5aOnxicg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/jmN6xCKMlqjWRebJ49PATnSRtpMianMWu4rWjeIdNpXHQZkdhmrLPYRicYM3RZBwcY0A5JePdYTCvzERhNiaBEicZg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jmN6xCKMlqjCRdC7jEXBMClMBDDiasXssFGzhaIl9lIOBpndo18RBgqsCcs8KicRza1e3niaia6AP37WXdryR3roNg/0?wx_fmt=png)

信息安全国家工程研究中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jmN6xCKMlqjCRdC7jEXBMClMBDDiasXssFGzhaIl9lIOBpndo18RBgqsCcs8KicRza1e3niaia6AP37WXdryR3roNg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过