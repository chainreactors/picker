---
title: 间接提示注入攻击正悄然蔓延至真实网络环境
url: https://mp.weixin.qq.com/s/3X_tjGFTfk40X2NL6wEiNg
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:04:02.748770
---

# 间接提示注入攻击正悄然蔓延至真实网络环境

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1yjnVO4A5mD6kCnkYl2iaiaN26vTxJygSj5Vzj9zSic8JOiaBGhku2ViczSXQnOtnAth6ZxyEKCpkj7qOfahANJmwCIqJKcno1qcF0/0?wx_fmt=jpeg)

# 间接提示注入攻击正悄然蔓延至真实网络环境

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

##

开放网络正在被一种针对大语言模型（LLM）驱动的AI Agent所设计的“陷阱”悄悄渗透。这种被称为间接提示注入（Indirect Prompt Injection，IPI） 的技术，通过在普通网页中隐藏（或明或暗的）恶意指令，静静等待AI Agent读取并执行攻击者的命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX12afTaz84twac79GyXlLsTBWcKtdsRiawtdiaE6vtSGuLucRSdnIslKKYu2m1Shw1e7vrib7ibjaACiaNaFjnk2zSW6FiaAVTiaWI3BY/640?wx_fmt=png&from=appmsg)

IPI攻击杀伤链（来源：Forcepoint）

**Part01**

## ****"忽略先前指令"的威胁现实****

谷歌与Forcepoint的研究团队本周相继发布报告，披露了这类攻击的真实案例证据。

谷歌以每月20至30亿的抓取页面为数据源，重点分析了博客、论坛及评论区等静态网站（不含社交媒体）。

Forcepoint的X-Labs团队则对公开网络基础设施进行了主动威胁狩猎，其遥测系统已捕捉到以“忽略先前指令”和“如果你是LLM”为特征的真实攻击载荷。

两家公司均发现，当前的IPI攻击存在善意与恶意两种动机。

谷歌指出，前者包含恶作剧和有益指导，例如改变AI Agent对话风格（"像小鸟一样发推文"）或在AI摘要中添加相关内容（如提醒用户自行核实事实）。后者则包括：

* 搜索引擎操纵/流量劫持
* 阻止AI Agent获取内容（DoS）并触发破坏性操作的IPI
* 以数据窃取（如API密钥）为目标的IPI
* 专注于系统破坏的IPI（如"尝试删除用户机器上所有文件"）
* 具有破坏意图的IPI指令

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0uvYWKLXibicw1EpdXicaJIONoEfkCWPicuGwVkoeLrLZdt2iallK68vtQPSx8ibZqV2XELNR9oyded3iash0EeeVXehcKfSc8r0ibIT0/640?wx_fmt=png&from=appmsg)

具有破坏意图的IPI（来源：谷歌）

Forcepoint研究人员还发现了旨在实施金融欺诈的IPI尝试：

* 某个攻击载荷完整嵌入了**PayPal交易流程及分步指导**，专门针对具备支付功能的AI Agent。
* 另一案例通过**元标签命名空间注入**，结合极具说服力的关键词（“ultrathink”），成功将AI代理的金融操作引导至**Stripe捐款链接**。
* 第三个案例则是一个疑似广泛分发的**测试载荷**，可能用于在部署高影响力攻击前，识别哪些AI系统更容易被入侵。

**Part02**

## ****针对人类的视觉隐藏技术****

攻击者采用了多种手段向人类隐藏恶意指令，同时确保AI能够完整读取。最常见的手法包括：

* 将文字缩小至单个像素，使其物理不可见
* 将文字颜色淡化至近乎透明
* 直接使用网页设计工具标记为隐藏元素

更复杂的技术还涉及将恶意载荷埋入HTML注释区块，或将指令隐藏在页面的元数据中。

**Part03**

## ****日益增长的IPI攻击趋势****

尽管目前尚未发现复杂的协同攻击证据，但Forcepoint研究人员警告称：“跨多个域名的共享注入模板表明，这已经是有组织的工具，而非孤立的实验。防范窗口正在迅速关闭。”

谷歌的扫描数据也证实了恶意活动的激增趋势：“在2025年11月至2026年2月期间，恶意类别的IPI攻击相对增长了32%。我们对公共网络CommonCrawl存档的多个版本进行了重复扫描，确认了这一增长。”

**Part04**

## ****风险与AI权限成正比****

## ****权限越大，危害越深****

Forcepoint特别强调，IPI攻击的潜在危害与AI Agent被授予的权限高低直接挂钩：

* 风险较低：仅能总结网页内容的浏览器AI
* 高价值目标：能够发送邮件、执行终端命令或处理支付的自主AI

正如报告所言：“如果AI Agent在消费不可信网络内容时，未能严格执行数据与指令之间的边界，那么它所读取的每一个页面，都可能成为攻击的载体。”

**参考来源：**

Indirect prompt injection is taking hold in the wild

https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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