---
title: 360实锤银狐木马新套路！合法远控工具成“帮凶”
url: https://mp.weixin.qq.com/s/s9O15olMRl4WUZRYYTdGMw
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:16:06.123366
---

# 360实锤银狐木马新套路！合法远控工具成“帮凶”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zfoRGB81MxNp1ZG0rMUVpeT6icb3WmCcxNibYp1ltLH7cVYMZRtd6giajJicrAWLcER2ia23LjvqvURN9lTskic7LhCF477ScniaCQTC9d3hbSwxfc/0?wx_fmt=jpeg)

# 360实锤银狐木马新套路！合法远控工具成“帮凶”

360数字安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

近期，部分东南亚国家进入一年一度的报税与薪资审查期，银狐木马组织也趁机活跃起来，开始发送鱼叉式网络钓鱼邮件，展开针对性攻击。

据360数字安全集团近期监测，这些邮件通常会伪装成财务相关的诱饵文件，主题多涉及财税、薪资调整等关键词，容易让公司职员放松警惕。正因如此，不少用户在不明所以的情况下，便打开了附件中的恶意文件，或点击了邮件正文里的恶意链接。

**以360捕获到的具体案例为例，邮件附件中的恶意文件带有数字签名：SyncFutureTec Company Limited。实际上，这一签名对应的软件是南京某科技公司开发的合法商业远程控制产品，本用于正规用途，如今却被银狐木马组织恶意利用。一旦用户被诱导执行了该恶意软件，其计算机便会立即落入攻击者手中，被远程控制。**

**后果包括敏感数据被窃取、用户活动被实时监控；更为严重的是，受害设备还可能被进一步用作跳板，向用户所在公司的网络发起渗透，从而使攻击的威胁范围不断扩大。**

360通过深入分析捕获到的攻击事件发现，受害用户收到的钓鱼邮件中附带了一个名为“Tax Assessment Letter.zip”的压缩包，里面是一个被恶意利用的远程控制工具。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxNbCg3QLxg4ufH17bTEwPs99MLjuiaGmibPAoficB7B1QAWrIZsEBRqmJSYe4LfJPQl291gLw8MmMticAXy1A4FFJZ0eIwcTnvrF3s/640?wx_fmt=png&from=appmsg)

该工具本身是一款合法的终端安全管理平台，数字签名为“SyncFutureTec Company Limited”，支持远程监控、多机远程协助、双屏会话等功能。由于该签名是真实的，部分安全厂商会对其直接放行，这恰恰被攻击者利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxO6icKn6ZV8gm0XBQWaa1sBD940IiaoM1Y3PyuX79dtBX6rzkwmBta3cWGmo7NKwiaJbSUZAlt8BRSC5lHVesLYCP8pvnDibgpU20g/640?wx_fmt=png&from=appmsg)

攻击者通过将安装包命名为 [IPv4]Clientsetup.exe，其中 [IPv4] 直接充当C2地址，利用该工具配置处理上的缺陷，在安装过程中自动配置远程C2地址，无需修改文件内容，从而避免签名失效。

安装后，该工具在 C:\Windows\SysWOW64\msres 释放文件并设为只读和系统隐藏，配置文件 YTSysConfig.ytf 中保存上线C2地址，C:\log 下生成日志文件记录服务启动、驱动加载等执行信息。攻击者借助这一合法框架，可长期窃取数据、精细控制受害环境、实时监控用户活动并维持持久化访问。

针对本轮银狐木马威胁，最有效的防御策略，不仅在于强化对钓鱼信息的识别能力、严守安全操作规范，更在于构建体系化、智能化的纵深防御体系。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zfoRGB81MxPbpK2ALcCCpKdt9n2fIxAsWLchviaFCwibz6LZhIPhBGickgVL3azrdSt0okUn5bXAcWwxIfibicxnX1XoJduEnSY0aBKlEzibZb3cs/640?wx_fmt=jpeg&from=appmsg)

**作为国内兼具数字安全和人工智能双重能力的企业，360在自研安全大模型的赋能下，将安全专家的能力和经验进行固化，并结合过去20年积累的海量样本数据、情报能力以及终端安全上1200余项能力点，打造出终端安全智能体蜂群。**

为有效应对银狐木马威胁，360依托终端安全智能蜂群体赋能的云安全立体防护体系，构建起涵盖传播拦截、行为监测、深度清理的银狐木马全周期防御矩阵。

**在木马传播的初始阶段**

该体系中的下载安全防护模块已实现对主流通讯软件的全链路覆盖，可对通过钉钉、微信、QQ等渠道传播的恶意文件进行实时检测，在木马落地前即完成自动查杀。

**针对攻击者精心设计的对抗手段**

比如遭遇掺杂大量干扰文件的多文件攻击，抑或是面对超大文件规避检测的传统伎俩，以及针对加密压缩包和“配置型白利用”等新型攻击方式，该体系皆可依托终端安全智能体蜂群赋能的智能分析系统，将安全专家的分析经验汇集于模型之中，快速从各类扫描数据中找出符合以上攻击特性的样本，从而实现自动阻断拦截。此外，还会对无法识别的可疑文件进行标记，并持续监测其后续行为。

**对于传输过程中的漏网之鱼**

360主动防御系统会对用户电脑提供强力保护。近期，银狐木马常用的攻击包括PoolParty注入、模拟用户点击、WFP断网、安全软件驱动利用、Windows Defender策略滥用等，360主动防御对这些攻击均能进行有效防御，并对发现的漏网之鱼进行清剿。

**在终端处置环节**

360云安全立体防护体系中的远控·勒索急救模式展现强大应急响应能力。该模式可一键切断攻击者控制通道，为深度清理争取宝贵时间窗口。此外，该体系不仅支持对各类驱动级木马的清理、对被篡改的系统配置进行修复，也支持对被银狐木马利用的合法管理软件的智能检测与卸载。

**据360终端安全智能体蜂群监测，近两年被滥用于攻击的合法软件已达数十款，常见包括IPGUARD、阳途、固信、安在等，360终端安全智能体蜂群已支持对此类软件的全面检测与一键清理。**

目前，360云安全立体防护体系已经实现对该新型银狐木马病毒的全面查杀，即便政企机构不幸感染该远控木马，仅需依据安全扫描结果执行清理与修复操作，重启系统即可恢复运行，建议广大政企机构尽快部署。

**如需咨询相关服务**

**请联系电话**

**400-0309-360**

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● 2026两会观察 | 周鸿祎为智能体人才培养献策，360先行落地 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585196&idx=1&sn=411d31527985da5cfb73f1beb83c429b&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ●  360龙虾卫士重磅上线：九大能力专治OpenClaw“裸奔” | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585414&idx=1&sn=eda1a5e0a9282e83255dfe33c7de4ab7&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● IDC双报告首推：360以绝对实力护航每只“龙虾”安全 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585375&idx=1&sn=e70a863eb3baac335080bdc9c4d0143a&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 360安全龙虾「养虾速成课」正式上线ISC.AI学苑！ | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585434&idx=2&sn=9e145e933928722c36df13f6cdbd53dd&scene=21#wechat_redirect) | |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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