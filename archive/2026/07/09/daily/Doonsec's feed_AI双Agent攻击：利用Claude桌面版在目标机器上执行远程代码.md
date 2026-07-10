---
title: AI双Agent攻击：利用Claude桌面版在目标机器上执行远程代码
url: https://mp.weixin.qq.com/s/9eoon5kEJF7Hp1EDs3Ehuw
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:29.204547
---

# AI双Agent攻击：利用Claude桌面版在目标机器上执行远程代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1hX4HySJ29gfjc6UmCRHh7VNFgjAyatsbvrVmMRsam3d2ugoFb16oEkf0PEWhmlmAmialia4EWMXzyLsAGBykD0Mmib78W1ADtjg/0?wx_fmt=jpeg)

# AI双Agent攻击：利用Claude桌面版在目标机器上执行远程代码

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2Uwe6m6uV8dxG0wEAEiahByENDAtFeN1t63kfVIeYnAYpiaBJLfWMyOicHFrG6P66mffVD7MoyRzBnLzbSFBA7yfV9tibNsDcib8SY/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0ZIU3Z2ZUuZTuwVIdicFkMRB5ibob3Hnl4h5EJQOgoCWNcBBV8ibO1WMxKj6Xmz4PXqzxQSN9k0jlhFo8PibejKdEElmaz1DialjC4/640?wx_fmt=png)

安全研究人员发现，被入侵的电子邮箱可被武器化，在受害者机器上实现完整的远程代码执行——这种攻击并非通过恶意软件或钓鱼链接，而是将受害者自己的Claude桌面助手变成攻击工具。

Pentera实验室的安全研究人员发现的这种攻击始于通过第三方平台获取客户邮箱访问权限，该权限是通过利用认证流程漏洞获得的。研究团队没有采用传统的密码重置或钓鱼手段，而是利用邮箱访问权限横向渗透至受害者的Claude账户，并将"个人偏好"字段识别为理想的攻击面——这个用户可编辑的提示词会同步到账户关联的所有设备和会话中。

Part01

Claude桌面版远程代码执行漏洞

研究人员通过向这个同步字段注入经过编码的非明显提示词，使得受害者在下次打开应用时，Claude桌面版会静默执行攻击者控制的指令，且不会触发重新认证或可见警告。攻击载荷指示Claude枚举已安装的具备命令执行能力的扩展程序（如Desktop Commander MCP工具），并通过它们执行攻击者提供的命令。

![攻击链（来源：PENTERA）](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2DMhYZDRnXBCT2eKLEG8GIV1YibkRz7BjJwibwkDOFXgtwCarNZ4SmQnZgNwgvKc0icfGMOdyAlPabbn3icGTFApKt5Ho38RqiaxGI/640?wx_fmt=png)

如果已存在具备命令执行能力的扩展程序，Claude会在常规聊天过程中自动执行恶意指令，无需受害者进行任何额外操作。若不存在此类扩展，Claude本身就会成为社会工程攻击媒介：它会显示一个逼真的虚假错误信息，敦促用户安装Desktop Commander，并附带一个看似合法的安装页面。一旦安装完成，受害者发送的下一条普通消息就会触发代码执行，从而将这个受信任的助手变成持久的命令控制通道，能够获取并执行攻击者轮换的命令。

Part02

相关漏洞研究

独立研究揭示了Claude扩展生态系统的相关弱点。LayerX此前披露了一个影响Claude桌面扩展(DXT)的零点击RCE漏洞，可通过恶意构造的日历事件触发，该漏洞获得了CVSS 10分的评分。Koi Security同样在Anthropic自家的Chrome、iMessage和Apple Notes连接器中发现了未净化的命令注入缺陷，这些漏洞被评为CVSS 8.9分，现已被修复。这些发现共同指向一个系统性模式：本地代码执行扩展与自然语言信任相结合，创造了广泛的攻击面。

Part03

厂商回应与安全建议

Pentera于2025年11月向Anthropic报告了其发现。Anthropic承认了这项研究，但拒绝将其归类为安全漏洞，称"个人偏好、skills和MCP连接器"的设计初衷就是通过Claude桌面版执行代码，并将此行为称为"预期功能而非安全漏洞"。该公司表示相关防护措施已列入路线图，并指出现有的会话管理和账户认证控制可作为缓解措施，同时强调该攻击需要事先获得账户访问权限。

安全团队应将AI桌面应用程序视为能够执行代码和访问本地文件的特权软件，监控同步助手设置的未授权更改，并限制可与AI客户端配对的扩展程序。随着AI助手模糊了聊天界面与系统Agent之间的界限，其感知能力与实际能力之间的差距正成为一种独特且目前监控不足的企业风险。

参考来源：

AI Double Agent Attack Turns Claude Desktop to Execute Remote Code on a Target Machine

https://cybersecuritynews.com/claude-desktop-to-execute-remote-code/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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