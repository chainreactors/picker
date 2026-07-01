---
title: 传Claude Code内置隐藏后门，专门检测中国用户
url: https://mp.weixin.qq.com/s/bT-jN4uTjianx_qNsywhtw
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:59.156165
---

# 传Claude Code内置隐藏后门，专门检测中国用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1hDbIkvTAx5IVwvb48ZxgcmA1wr20iaViabzhicpCNVVibXpiaOWKKSjzAL5icEOV9EWjjU9reFoYPbyrarZnFx94icLInNYvbV7ROia8/0?wx_fmt=jpeg)

# 传Claude Code内置隐藏后门，专门检测中国用户

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX06ADqRFplvdej5HJX1vQiactichuibjlnz3C2MnlpKqShwZbwib1ZIlIQHPng8mpyyMNic4aWyNfeF4mtcxoiaCdWs630EewylSiagRM/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3fZWnt1upGC48Ncr6wZJSoXf03XHxKqvTa0WEQDykzHuUmibNUyvdaTUTSpAY5LL4Pp0MuBsLvIeOZloMwBQOOMmeX3des7OoQ/640?wx_fmt=png&from=appmsg)

近期有消息称Anthropic针对性封禁浙江、杭州IP访问Claude，背后或和此前指控阿里大规模蒸馏模型数据相关。

官方称4月22日至6月5日间，超2.5万个账号累计交互2880万次，涉嫌批量爬取模型数据。有用户反馈封禁通知邮件暗藏追踪工具，打开便会定位使用者，提交申诉也无法解除限制，前往杭州出差的从业者需注意规避使用该工具，目前相关争议暂无完整官方定论。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0uia2J8MJqP5lOzI3YfcIX9JMbhibre5MsMdphVsql3JJSeiaSxoaOsVYPl91z1QXO3tzQnX2sF13XbY68YwefrsTfxWncpmJduo/640?wx_fmt=jpeg&from=appmsg)

早在 2026 年 4 月 2 日发布的2.1.91版本，Anthropic 就已经在 Claude Code 中埋下检测机制：程序会自动识别用户是否开启代理。一旦检测到代理，它不会明文上传数据，而是偷偷改动系统提示词里不易察觉的字符，以此隐秘传递三类关键信息：用户是否身处国内、代理跳转地址是否为国内域名、使用者是否隶属于国内 AI 实验室。

有开发者本地搭建了私人Claude Code环境，平时依靠代理打通GPT与 Claude双模型，以此实现精细化的上下文统筹管理。

更新至2.1.196版本后，软件新增限制：只要开启代理，Anthropic 就会直接关停远程控制功能。开发者逆向拆解程序代码，想要解除这项限制时，意外挖出一段疑点重重的底层逻辑。

Part01

 代码监测逻辑

这套检测逻辑内嵌在Claude Code的程序二进制文件中，从 2.1.91 版本上线后就从未改动，完整检测流程如下：

一旦检测到用户开启代理工具，程序会依次执行两项校验：

* 读取本机系统时区，判断是否为上海时区Asia/Shanghai或乌鲁木齐时区Asia/Urumqi；
* 解析当前代理访问地址，比对内置域名黑名单，判断该链接是否属于国内域名、或是关联国内人工智能实验室。

Anthropic会根据这两项校验结果，悄悄篡改系统提示词内的日期字段，以此暗地传递用户环境信息。

只要系统时区识别为中国时区，提示词里的日期格式就会发生变更：标准格式2026-06-30会被替换成斜杠分隔的2026/06/30。除此之外，句子「Today's date is」里的撇号字符，也会根据代理地址类型替换成不同 Unicode 符号，用作区分标记，三种对应规则如下：

* 代理为国内域名、匹配内置域名清单，但不属于国内 AI 实验室：替换为右单引号 \u2019，符号样式：'
* 代理不属于国内域名、不在清单内，但指向国内 AI 实验室：替换为修饰符撇号 \u02BC，符号样式：ʼ
* 代理既是国内域名、匹配清单，同时归属国内 AI 实验室：替换为修饰符撇号 \u02B9，符号样式：ʹ

用户可以自行在 Claude Code 源码里验证这套机制。在2.1.196 版本中，实现该功能的相关函数名为 Crt ()、Rrt (e)、e0t ()、Zup ()、edp 以及 Vla。要说明的是，这些都是代码压缩混淆后的简写函数名，每次版本更新都会更换。不过用户可以让 Claude Code 或者 Codex 逆向解析程序、检索这段检测逻辑，基本能轻松定位到对应代码。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX079c7Rib8vNiatibdkiagRUIHiaXEb8XrJfCJ5hQ7sSu5ZYVib9o1IYwAfdUuaibvzu7bRCu7HiaicLBMibIxJB1ttd86JRWCM4m9xOibH38/640?wx_fmt=png&from=appmsg)

Part02

 Anthropic真实意图

不难看出，Anthropic 上线这套检测机制，初衷是筛查国内未经授权倒卖 Claude 接口、国内 AI 实验室蒸馏模型的行为。但让人不安的是，官方刻意在二进制程序中对这段代码做了加密混淆处理。大量代码采用密钥 91 进行异或加密，目的就是防止他人通过文本提取工具直接抓取到这段监测逻辑。除此之外，2.1.91 版本的更新日志里，完全没有提及新增这项检测功能。

官方利用隐写技术在系统提示词中隐藏数据的操作，也彻底暴露了他们的真实意图：只改动细微字符，普通用户甚至大模型本身都很难察觉，但 Anthropic 后台却能轻易识别、解码我们的环境信息。

Part03

严重透支用户信任

即便厂商想要管控非法倒卖、模型蒸馏的出发点尚可理解，但 Anthropic 在用户不知情、未获得许可的前提下，暗中上传设备系统信息与代理配置，本质上是彻底辜负了开发者的信任。

仅仅依靠时区标签就对全体相关用户开展监控，本身就属于过度收集用户信息。而这套监测机制的存在，还引申出更严峻的安全隐患：如果 Anthropic 仅仅因为用户身处国内，就敢偷偷上传本机隐私数据，谁能保证他们不会暗中操控模型输出带有偏向性的内容？此前旗下产品 Fable 就出现过类似问题，直到研究人员公开曝光，官方才做出调整。更极端一点，厂商甚至有可能恶意干预模型行为。

开发者通常会授予 Claude Code 完整的文件读写权限、大量终端操作权限，方便工具完成代码开发工作。可这也意味着，厂商完全有能力借助这些权限，在本地设备执行任意远程代码。今天他们只是偷偷读取时区信息，明天就有可能暗中破坏本地文件、批量窃取设备内全部数据。

开发者们对 Claude Code 抱有极高的使用信任，因此强烈要求 Anthropic 提升产品透明度。维护自身知识产权无可厚非，但不该以在所有开发者设备中植入等同于间谍程序的监测模块为代价。

另外还有一点客观事实：这类检测手段，一方面损害了合规使用者的隐私，另一方面技术门槛极低，稍有基础的技术人员就能轻松绕过。一边侵犯正常用户隐私，一边又很难真正遏制非法倒卖、模型蒸馏行为，这套机制的实际作用其实要打上一个大大的问号。

参考来源：

Anthropic embedded spyware in Claude Code — and attempted to hide it from you

https://www.reddit.com/r/ClaudeAI/comments/1ujila1/anthropic\_embedded\_spyware\_in\_claude\_code\_and/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

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