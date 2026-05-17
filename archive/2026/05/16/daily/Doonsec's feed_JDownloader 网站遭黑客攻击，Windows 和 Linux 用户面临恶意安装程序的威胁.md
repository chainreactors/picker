---
title: JDownloader 网站遭黑客攻击，Windows 和 Linux 用户面临恶意安装程序的威胁
url: https://mp.weixin.qq.com/s/wPfdL_WOy2q524P4fkF-vg
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:33.195216
---

# JDownloader 网站遭黑客攻击，Windows 和 Linux 用户面临恶意安装程序的威胁

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb0uZRlUVTfXGAW55pBTS2v07QVrcJCInO6A9rzicIGYcdCDb0uUcQuVoLKzB1Y2thD7CycGuic2PuoPZg7lLmPTmlhITtIJgqC6o/0?wx_fmt=jpeg)

# JDownloader 网站遭黑客攻击，Windows 和 Linux 用户面临恶意安装程序的威胁

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一款深受数百万用户信赖的热门开源下载管理器，在攻击者入侵其官方网站后，突然变成了恶意软件传播平台。攻击者用针对 Windows 和 Linux 用户的木马版本替换了合法的安装程序。

JDownloader 开发人员证实，该事件发生在 2026 年 5 月 6 日至 7 日之间，当时威胁行为者未经授权访问了该项目的网络基础设施。在这个短暂但关键的窗口期内，攻击者修改了下载链接，以分发嵌入了远程访问功能的恶意安装程序。

JDownloader 被广泛用于管理从文件托管服务和流媒体平台下载的文件，它成为了软件供应链攻击的最新案例。

根据安全报告和 Reddit 社区的发现，用户开始注意到异常行为，包括防病毒警报和可疑的开发者签名，例如“Zipline LLC”和“The Water Team”。

具体影响到：

* Windows“替代安装程序”下载
* Linux shell 安装脚本

其他分发渠道，包括 macOS 版本、JAR 包、Flatpak、Snap 和 Winget 安装，均未受到影响。

经查，该恶意Windows安装程序会部署 基于Python的远程访问木马（RAT），使攻击者能够持续访问受感染的系统。此类恶意软件通常允许攻击者执行命令、窃取数据并部署其他有效载荷。

初步调查显示，攻击者利用了 JDownloader 网站上一个未修补的 CMS 漏洞。该漏洞允许未经授权修改访问控制列表 (ACL)，使攻击者能够在未经身份验证的情况下篡改下载链接。

攻击者一旦入侵系统，就会将合法的安装程序二进制文件替换为植入木马的版本，同时保持正常的下载过程。据 Malwarebytes 报告，这种策略显著提高了感染成功的可能性，因为用户会信任官方来源。

对许多用户而言，最初的入侵迹象来自微软Defender和其他杀毒引擎，它们将下载的可执行文件标记为恶意或未签名。在某些情况下，安装程序缺少正确的品牌标识和有效的数字签名，这更令人怀疑。

* 2026年5月6日至7日：网站遭到入侵，恶意安装程序被分发
* 2026年5月7日：开发商确认网站遭到入侵，并关闭了网站。
* 2026年5月8日至9日：网站恢复，提供干净且经过验证的下载资源
* 事件后：实施了安全加固和补丁措施

开发人员表示，通过应用程序本身安装更新的用户不受影响，因为此次攻击仅限于网站托管的安装程序。

此次事件凸显了可信软件分发渠道被恶意利用的日益严重的威胁。即使是短暂的入侵也可能使成千上万的用户面临恶意软件感染的风险。

典型的感染场景是，用户在入侵窗口期内从官方网站下载安装程序，执行安装程序，并在不知情的情况下安装后门，使攻击者能够远程控制系统。

## **缓解措施和建议**

强烈建议在受影响期间下载过 JDownloader 的用户：

* 请使用官方来源验证安装程序哈希值
* 使用更新的防病毒或EDR工具扫描系统
* 删除可疑文件并从可信来源重新安装
* 监控异常系统行为或未经授权的访问

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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