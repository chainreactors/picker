---
title: 【安全圈】致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068140&idx=2&sn=62525dfabedac7cf4d4a2e4e17fb2b1f&chksm=f36e756cc419fc7a995ca579f46b6508ac2b8d903b71be90b43fa9a52a4946263f8c2de226f3&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-26
fetch_date: 2025-10-06T20:37:25.724659
---

# 【安全圈】致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh9BoT0kbn2Lib2cmgWN6iakdVVtLVgSAibzQliclpaBJPibhEEtXpicT6SWwL0AyoL8x7UiaQ8oYSGkkNFQ/0?wx_fmt=jpeg)

# 【安全圈】致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络钓鱼

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh9BoT0kbn2Lib2cmgWN6iakdHzxpRqtGL9rPqBpZBm5KDL1uDyd8bFWY072g7ZkxgNa66KvHW8H1VQ/640?wx_fmt=other&from=appmsg)

亚太地区的多家工业组织已成为钓鱼攻击的目标，这些攻击旨在传播一种名为致命RAT（FatalRAT）的已知恶意软件。卡巴斯基工业控制系统应急响应中心在一份周一发布的报告中表示：“攻击者利用合法的中国云内容分发网络（CDN）myqcloud和网易有道云笔记服务作为其攻击基础设施的一部分。”报告还指出：“攻击者采用了一种复杂的多阶段载荷递送框架，以确保逃避检测。”

这次攻击的主要目标是政府机构和工业组织，特别是制造业、建筑业、信息技术、电信、医疗、电力与能源、大规模物流和运输等行业，涉及台湾、马来西亚、中国、日本、泰国、韩国、新加坡、菲律宾、越南和香港等地区。邮件中使用的诱饵附件表明，此次钓鱼攻击主要针对中文用户。

值得注意的是，致命RAT的活动曾利用虚假的谷歌广告作为分发渠道。2023年9月，Proofpoint公司记录到另一起以电子邮件为媒介的钓鱼攻击，传播了多种恶意软件家族，包括致命RAT、Gh0st RAT、紫狐（Purple Fox）和ValleyRAT。这两次入侵活动的有趣之处在于，它们主要针对中文用户和日本组织。其中部分活动被归因于一个名为银狐APT（Silver Fox APT）的威胁组织。

### 攻击链与恶意软件加载

最新攻击链的起点是一封包含中文文件名ZIP压缩包的钓鱼邮件。当用户打开该压缩包后，会启动第一阶段加载程序，随后向有道云笔记发送请求，以获取动态链接库（DLL）文件和致命RAT配置器。配置器模块则从note.youdao[.]com下载另一条笔记的内容，以访问配置信息，同时打开一个诱饵文件以避免引起怀疑。

另一方面，DLL是第二阶段加载程序，负责从配置文件中指定的服务器（“myqcloud[.]com”）下载并安装致命RAT载荷，同时显示一个关于应用程序运行问题的虚假错误信息。此次攻击的一个重要特点是使用了DLL侧加载技术，以推进多阶段感染序列并加载致命RAT恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh9BoT0kbn2Lib2cmgWN6iakdcagxxIDdBsA3HJicn2pZSJxrDWicGLibpibSzxoWCjWGicsBle5zyPZibB0Q/640?wx_fmt=other&from=appmsg)

卡巴斯基表示：“威胁行为者采用了一种黑白结合的方法，利用合法二进制文件的功能，使事件链看起来像正常活动。攻击者还使用了DLL侧加载技术，将恶意软件的持久性隐藏在合法进程内存中。”致命RAT还执行了17项检查，以确定恶意软件是否在虚拟机或沙盒环境中运行。如果其中任何一项检查失败，恶意软件将停止执行。

### 恶意软件功能与幕后黑手

致命RAT在等待命令与控制（C2）服务器的进一步指令之前，会终止所有rundll32.exe进程实例，并收集系统信息和已安装的各种安全解决方案的相关数据。致命RAT是一款功能强大的木马，能够记录键盘输入、损坏主引导记录（MBR）、打开/关闭屏幕、在Google Chrome和Internet Explorer等浏览器中搜索和删除用户数据、下载AnyDesk和UltraViewer等附加软件、执行文件操作、启动/停止代理，以及终止任意进程。

目前尚不清楚是谁在背后操纵使用致命RAT的攻击，但战术和工具与其他活动的重叠表明，“它们都反映了某种程度上相关的不同系列攻击”。卡巴斯基以中等置信度评估，背后可能是一个中文威胁行为者。研究人员表示：“致命RAT的功能为攻击者提供了几乎无限的攻击开发可能性：通过网络传播、安装远程管理工具、操纵设备、窃取和删除机密信息。”

“在攻击的各个阶段持续使用中文服务和界面，以及其他间接证据，表明可能有一个中文威胁行为者参与其中。”

来源：FatalRAT Phishing Attacks Target APAC Industries Using Chinese Cloud Services

***END***

阅读推荐

[【安全圈】拦截钓鱼网址操作失误致Cloudflare服务中断](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068120&idx=1&sn=ae8350bd62f190fd9ab9a30dfe146983&scene=21#wechat_redirect)

[【安全圈】虚假的CS2锦标赛直播被用于盗取加密货币和 Steam 账号](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068120&idx=2&sn=7c1da16297dd1d2f1094b9a648825790&scene=21#wechat_redirect)

[【安全圈】GitHub 上发现 Windows Wi-Fi 密码窃取恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068120&idx=3&sn=a24961da5e35d85056d0ee9b767256d5&scene=21#wechat_redirect)

[【安全圈】CVE-2024-56000（CVSS9.8）：KLEO WordPress 主题中存在的账户接管漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068120&idx=4&sn=d542bcb895565396eeb06f3dd27a9809&scene=21#wechat_redirect)

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

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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