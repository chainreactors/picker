---
title: 【安全圈】Notepad++ 插件悄然安装恶意软件
url: https://mp.weixin.qq.com/s/MYmmH6mr90BGPHAJv_BK2Q
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:39:38.705957
---

# 【安全圈】Notepad++ 插件悄然安装恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFPHrpVPniaFPzWWqFzL3TzXib5ia2upLq8h6vSAyicHyeodvh4Oy3XLsGxDQeJsFI6TFXlzPcialk5ich61kaNeAzCJP0iaxiciaDL4MfU/0?wx_fmt=jpeg)

# 【安全圈】Notepad++ 插件悄然安装恶意软件

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

乌克兰 CERT 发现了一系列攻击，这些攻击分发了一个包含合法 Notepad++ 应用程序和名为 LunchPoke 的恶意工具（伪装成插件以建立持久性）的压缩包。

该活动被归因于一个跟踪为 UAC-0099 的威胁集群，该集群主要针对乌克兰的组织，此前曾被认为为 APT44（也称为 Sandworm）发起的攻击提供初始访问权限。

攻击者并未利用任何漏洞或影响该流行软件的供应链入侵。

CERT-UA 观察到 UAC-0099 最近改变了其作案手法，现在分发一个包含伪装成 PDF 文档的 VBS 脚本的 ZIP 压缩包。启动后，该 PDF 会检索另一个名为 Evernote.zip 的压缩文件。

第二个压缩包包含合法编辑器 Notepad++ 8.8.3 版本的完整副本、一个恶意插件（NppExport.dll）、一个受密码保护的压缩包（updater.rar）以及合法的 WinRAR 可执行文件。

VBS 脚本将软件包安装到一个随机命名的目录中，启动 Notepad++，然后通过应用程序正常的插件加载机制加载恶意的 NppExport.dll。

CERT-UA 解释说，这个 DLL 就是 LunchPoke，一个在 Windows 上创建计划任务并解压 RAR 文件内容的工具，包含 RemoteLibUpdater.exe 和 InitTest.dll。

RAR 文件中的可执行文件是 BurnyBear，它是 DLL 文件（即 MatchBoil V2 恶意软件加载器）的加载器。

BurnyBear 还具有一个后备机制，以防启动 RemoteLibUpdater.exe 失败，从而触发针对主机 RAM 和 CPU 的资源耗尽攻击。

后者会创建另一个计划任务，更新其配置和命令与控制（C2）地址，然后使用 WinRAR 解压下载的程序。

CERT-UA 未提及在观察到的攻击中交付的最终 payload、该活动的目的或目标组织。

研究人员提到了 CVE-2025-56383，这是 Notepad++ v8.8.3（这些攻击中使用的确切版本）中的一个 DLL 劫持漏洞，但指出 Notepad++ 团队对此问题提出了异议，声称插件加载是标准功能。

CERT-UA 建议系统管理员将 Notepad++ 更新到 8.9.7 版本、7-Zip 更新到 26.02 版本、WinRAR 更新到 7.23 版本，以防止黑客利用现有产品中的已知漏洞并实现隐蔽攻击。

***END***

阅读推荐

[【安全圈】马斯克为了安全，要把"X"完全开源？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077986&idx=1&sn=c72b731dda33c8916f4096cf332615db&scene=21#wechat_redirect)

[【安全圈】每单收超千元服务费，上海警方抓获 3 名外挂代拍违法犯罪人员](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077986&idx=2&sn=11aa39242de4b5b0197f8676b1c497ea&scene=21#wechat_redirect)

[【安全圈】新型 Dolphin X 恶意软件利用 AI 对高价值目标进行评分排名](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077986&idx=3&sn=7212e4b798829226046df566ed3e65d8&scene=21#wechat_redirect)

[【安全圈】数百万辆车可被远程熄火！这个漏洞比你想的更恐怖](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077973&idx=1&sn=c5a357c37a1b18979e6b3c93d7117066&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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