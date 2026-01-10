---
title: 微软 Defender 误伤“正版”激活工具，一字母之差引发乌龙
url: https://mp.weixin.qq.com/s/qr92f3n6C1wrsP-j4mRubQ
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:21:40.074872
---

# 微软 Defender 误伤“正版”激活工具，一字母之差引发乌龙

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFlUJHyf6iaDcbFFInfpojZeSAAxQia1niaR0aaZjia4PHH8QHPCGGzPQ91Q/0?wx_fmt=jpeg)

# 微软 Defender 误伤“正版”激活工具，一字母之差引发乌龙

看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

近日，微软安全防护软件 Microsoft Defender 卷入一场颇具争议的“误伤”事件。其本意为打击冒用知名开源工具“微软激活脚本”（MAS）之名的恶意软件，却因过滤规则存在偏差，意外将正版的 MAS 工具也一并拦截，导致许多用户在尝试合法激活时操作失败。

事件源头可从一则典型的 Defender 威胁警报中窥见。警报显示，系统检测到名为“Trojan.PowerShell/FakeMas.DA!MTB”的活跃威胁，并将其归类为“危险程序，执行来自恶意攻击者的命令”。受影响的进程直接关联到 PowerShell 执行环境。而当用户尝试运行正版 MAS 的典型命令（irm https://get.activated.win | iex）时，Defender 会报错并阻止，提示“脚本内容恶意”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFMANa7BianWCibBpBlFZXdHkPPnRJjKebspHXaNQ6HGp9upKiaXEjeXspw/640?wx_fmt=png&from=appmsg)

微软显然意识到了 MAS 工具及其被恶意仿冒的现象。近期出现了大量注册相似域名传播木马的“李鬼”脚本，此事也得到了 MAS 开发团队在社交媒体上的证实。微软 Defender 的主动拦截机制，其初衷正是为了打击这些钓鱼版本。

然而，问题的关键在于一个细微的字符差异。经安全研究人员比对：

-正版 MAS 命令域名为：https://get.activated.win

-已知的恶意仿冒域名为：https://get.activate.win（缺少字母d）

目前迹象表明，微软 Defender 的拦截名单似乎不慎将正版域名也纳入了黑名单。尽管受条件所限，暂时无法验证恶意版本是否被成功拦截，但若最终结果是安全软件“放行了恶意脚本，却挡住了无害的正版”，无疑将构成巨大的安全讽刺。

这一误判带来了现实困扰。由于 Microsoft Defender 在 Windows 系统中默认启用并实时保护，受影响的用户若需使用正版 MAS，当前必须手动暂时关闭 Defender 的实时防护等核心安全功能，待激活完成后再立即重新开启。这个过程本身便带来了短暂的安全窗口期。

资讯来源：securityonline.info

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