---
title: 警惕！新型银行木马TCLBANKER曝光
url: https://mp.weixin.qq.com/s/MgQeXdXlSfT1luJHc1EFZw
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:35:57.359285
---

# 警惕！新型银行木马TCLBANKER曝光

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/757fvrbk7oal367ZsMgDseSQVyYzS0fbe1EW7JGkb1WKpibwJpBeiakAUvtyhHKjIOF6dz3kupSOoUMmCbBftEGjibMwe1zub3RiaM9dz3w1OaQ/0?wx_fmt=jpeg)

# 警惕！新型银行木马TCLBANKER曝光

安世加

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**新闻**

*News Today*

近日，Elastic Security Labs披露了一款名为TCLBANKER的新型银行木马。它是旧版Maverick家族的重大升级版本，目前攻击集中在巴西，但安全专家警告其扩散范围预计将持续扩大。

**伪装成Logitech AI工具：带合法签名的陷阱**

TCLBANKER的初始感染手法极具欺骗性：攻击者将其伪装成Logitech AI Prompt Builder工具的安装包。更令人防不胜防的是，这个安装包带有有效的数字签名，让它在初期能够绕过部分安全软件的检测。

一旦用户不慎安装，木马便会在后台静默运行，等待下一步指令。

**瞄准59个金融平台：全屏伪造界面窃取凭证**

进入系统后，TCLBANKER会根据C2（命令与控制）服务器下发的配置，针对59个银行、金融科技和加密货币平台实施攻击。

其核心手法是：当用户访问真实金融网站或应用时，木马会立即展示一个全屏的伪造界面，覆盖在真实页面上。用户在虚假页面输入的账号、密码、甚至一次性验证码，都会被直接发送给攻击者。

这种手法比传统键盘记录更隐蔽——用户以为自己登录的是真实银行，实际上所有信息都交给了黑客。

**最危险的功能：双渠道蠕虫式传播**

TCLBANKER最令人不安的特性，是其双蠕虫传播机制：

* WhatsApp模块

木马会在后台克隆受害者的浏览器会话数据，以受害者本人的身份登录WhatsApp网页版，然后向通讯录中的好友批量发送钓鱼文件或恶意链接。由于消息来自真实好友，接收者很难产生怀疑。

* Outlook模块

木马会接管受害者的Outlook邮箱，从受害者的真实邮件地址向外批量发送钓鱼邮件。这些邮件绕过了大多数标准邮件安全过滤——因为它们确实来自一个合法、可信的发件人地址。

这意味着，一个感染者可能成为攻击者的“跳板”，导致几十甚至上百个联系人相继中招。

**技术特点：C2托管在Cloudflare Workers上**

TCLBANKER的命令与控制（C2）基础设施主要托管在Cloudflare Workers上。这一选择让攻击流量混入了正常的Cloudflare CDN通信中，增加了检测和拦截的难度。

同时，该木马支持实时远程控制，攻击者可以根据受害者设备上的具体情况，动态下发不同指令。

**目前影响与未来风险**

截至报告发布，TCLBANKER的攻击主要集中在巴西的金融用户。但鉴于其通过WhatsApp和邮件进行蠕虫式传播的特性，以及攻击工具包本身可以快速适配其他国家和地区的金融机构，安全机构预计扩散范围将持续扩大。

尤其值得注意的是，由于该木马能够劫持用户真实社交账号进行传播，一旦某个地区的用户中招，其连锁扩散效应将远超传统钓鱼攻击。

本文信息来源： Elastic Security Labs 官方报告

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

安世加为出海企业提供SOC 2、ISO 27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/mmbiz_jpg/757fvrbk7oZJECIxUc7sRxib1HdDZx25byCyN7WOic7GRMHzEw0ZoG8m8lCWLcUwMCbFiaBX2qeDY99YuyFPeGlicQsEuYA9BAT6rk65BE29QHg/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

安世加

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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