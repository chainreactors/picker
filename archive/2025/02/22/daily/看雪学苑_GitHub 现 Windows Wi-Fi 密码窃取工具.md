---
title: GitHub 现 Windows Wi-Fi 密码窃取工具
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589903&idx=3&sn=a6fea8c3a69296a1f9b47c68422a16d1&chksm=b18c2a4586fba353f45df7ca0d0c6413eb0a1a2e6ad2f8e87b768aff5a3094dc646232b2319c&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-22
fetch_date: 2025-10-06T20:37:26.548649
---

# GitHub 现 Windows Wi-Fi 密码窃取工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ek9ruQx01sxWvO9icMYXOzHb1g1EIjiaIpZN6ZGKE4G7ILiagFDKMaznVySOkibOvwvOnMAKQsp1PTwA/0?wx_fmt=jpeg)

# GitHub 现 Windows Wi-Fi 密码窃取工具

看雪学苑

看雪学苑

近日，一款名为 “Windows-Wi-Fi-Password-Stealer” 的 GitHub 代码库引发广泛关注。该库由某用户创建，内含一个基于 Python 编写的脚本，其功能令人咋舌 —— 竟能从 Windows 系统中提取已保存的 Wi-Fi 登录凭证，并将这些敏感信息存入文本文件。

虽说该代码库对外宣称仅供教育用途，可其一旦被恶意利用，后果不堪设想。据网络地下情报源在社交平台 X 上发布的帖子透露，此库包含几个关键文件。其中，“Password Stealer.py” 作为主脚本，承担执行提取凭证的核心任务；“requirements.txt” 罗列出运行脚本所需的 Python 依赖项；“README.md” 则详细说明了安装与使用步骤。

该工具的运行机制巧妙利用了 Windows 系统的原生功能。它先调用合法的网络命令 “netsh wlan show profile”，获取与系统关联的无线网络名称（SSID）列表。接着，针对每个 SSID，运行 “netsh wlan export profile” 命令，生成包含配置详情的 XML 文件，而 Wi-Fi 密码（PSK）就以明文形式藏身其中。这些 XML 文件会被临时存于系统工作目录，由 Python 脚本解析出密码后立即删除，试图以此躲避检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Ek9ruQx01sxWvO9icMYXOzHfvwSiaHVSuGlqnL0x1H4GKibIkymdyBBeo7KCQ9ImzNTx7PcwqhGTLMw/640?wx_fmt=png&from=appmsg)

因其基于 Python 编写，依赖项少，还能用 PyInstaller 转为独立可执行文件，操作门槛极低。README 里不仅指导用户安装依赖项，还教授如何将脚本变为可执行文件，这无疑让非技术人员也能轻易上手，大大增加了被恶意利用的风险。

此类工具公然现身 GitHub 等平台，无疑为不法分子打开了 “方便之门”。他们能轻易改造代码，窃取登录凭证，非法闯入网络，在受侵环境里肆意横窜。这一事件也为各组织机构敲响警钟，推行 Wi-Fi 多因素认证、定期更换密码迫在眉睫。虽说工具本身并非生来邪恶，但其被滥用却暴露了操作系统在处理敏感凭证时的重大漏洞，网络安全防护之路，任重道远。

资讯来源：cybersecuritynews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibExiboJzOiafqGLvlOkrmU6NIr3qSr7ibpkIo2N5mhCTNXoMl37s2oRSIDw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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