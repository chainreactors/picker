---
title: AI安全观察|湘易办的清晨六点，和 50 美元一次的攻击
url: https://mp.weixin.qq.com/s/_J75gyroqgQCzerLrBsUbQ
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:02:21.658786
---

# AI安全观察|湘易办的清晨六点，和 50 美元一次的攻击

# AI安全观察|湘易办的清晨六点，和 50 美元一次的攻击

原创

小谢AGI
小谢AGI

小谢取证

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AI 安全观察

湘易办的清晨六点，
和 50 美元一次的攻击

一条推送叫醒一个省，一串字母惊动一个行业

一

早上 6 点 06 分

11 月 11 日，周三。湖南很多人的这个早晨，是被一条推送叫醒的。

6 点 06 分，锁屏亮起，一条来自「湘易办」的通知。标题挺正规——《市场准入壁垒清理整治行动问题线索征集公告》。往下看，画风突变：

ARTEX3742 自定义

正文-ARTEX3742PUSH-1794348367

![](https://mmbiz.qpic.cn/mmbiz_jpg/b34oV9VTkcGE8qqwyYibiaeRU8njc1KiazJRyxPOXibG0WKUWMU9DgKwGGPW193eSXzPicNzjk3ltGI3BImXGyiaQESMVnpgtYn19NG7q9ZbVnt2o/640?wx_fmt=jpeg&from=appmsg)

▲ 11 月 11 日 06:06 的锁屏（图：公开流传的网友截图）

这不是个例。接下来将近四个小时，全省用户陆陆续续收到一串同类推送。把网友截图按时间排一排，大概是这个节奏：

**07:42**　ARTEX3928-NEGCTL

**07:44**　ARTEX283CHK、ARTEX-TEST-ALIAS2、ARTEX3855（连发）

**07:45 起**　那份公告开始复读，通知中心里"现在、2 分钟前、3 分钟前……"连刷六遍

**09:50**　还在推

![](https://mmbiz.qpic.cn/mmbiz_jpg/b34oV9VTkcFZbHXOtl2hWxTaHiajturMVA5KHgLUQ5klxUhyoQ1nTlVdfHJALcic9RwIBDiaZbunjz1Jz7Pc0O8eMxZh0Hicia95RT0pbFM0M5Wk/640?wx_fmt=jpeg&from=appmsg)

▲ 网友的通知中心（图：公开流传的网友截图）

名字一个比一个像没写完的草稿。有人在评论区问：运维是不是还在睡觉？

湘易办不是个小 App——湖南省政务服务的总入口，2022 年底上线，全省企业、群众、公务人员掌上办事都靠它。测试味道十足的字符串，就这么走了生产环境的推送通道，落在千万人的锁屏上。

到写稿为止，没有看到官方通报。谁发的、为什么挑早上六点、公告为什么被复读，全都没有说法。

但安全圈已经坐不住了。因为那串字符里，有四个字母太扎眼：**ARTEX**。

二

那四个字母

ARTEX，今年安全圈没人陌生的名字。

一套 7 月 26 日刚开源的 AI 自主渗透框架，作者代号 Autumn-27，ScopeSentry 的作者。它把"一次渗透测试"压缩成了一个表单：描述框里写上目标和意图，比如"测试 example.com 这个站点""拿下后台管理权限、获取敏感密钥权限"，剩下的侦察、漏洞挖掘、利用、提权，planner 拆任务、worker 并行跑，一路推到目标达成。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b34oV9VTkcGAvBhFhavibUXyxbrftMojazyvj9rybytvJCwkwBZE8YatOSYbI9hYMEqqpnLiahVyOVsD8Fhfsv2CUREUST3fMGBib481OlwTjA/640?wx_fmt=jpeg&from=appmsg)

▲ ARTEX 的"新建任务"窗口——填两句话，剩下的交给智能体（图：公开部署教程截图）

它不挑模型。配置页里填个 API Key，OpenAI、Anthropic、DeepSeek、本地 Ollama 都能接。后来 CrowdStrike 复盘韩国那场攻击，攻击者的工具链里就有 DeepSeek、GLM 和 Grok。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b34oV9VTkcFYdU00NoGxumNgictvQYHVscheZialiafG0Xmmk1JZPBAFx5463De4UqAOEHjAWusxmbzwKIcAAJ5ibXpGXqC9dREA73DamQZBMJc/640?wx_fmt=jpeg&from=appmsg)

▲ ARTEX 的模型接入配置，接哪家都行（图：公开部署教程截图）

给它排个时间线，密度相当吓人：

**7 月 26 日**　开源，AGPL-3.0 协议，star 很快过千；

**9 月底—10 月初**　韩国至少 7 家金融机构被同一套工具打穿，6 万多人信息泄露。CrowdStrike 把这事归因给一名说中文的黑客——依据之一，是他留了个没关的开放目录；

**10 月 8 日**　作者宣布闭源、仓库下架。可 fork 早就遍地都是了，删得掉入口，删不掉副本；

**11 月 6 日**　Censys 发博客：全网 800 多个 ARTEX 部署实例直接暴露在公网，打开网页就能进，**不用密码**。里面躺着的攻击数据"远超韩国银行"，还捎带了支付公司和游戏公司。

所以，当一个省级政务 App 的推送通道在清晨六点开始复读"ARTEX3742"，你很难要求安全从业者不产生联想。

当然，也可能纯属巧合——内部系统的代号撞了名。没有官方说法之前，谁也定不了性。

而这，恰恰是这件事里最值得说的部分。

三

最难的不是防，是定性

换个位置想想。假如你是接手这起事件的取证工程师，摆在你面前的是什么？

生产推送通道、测试字符串、早上六点、持续近四小时、真公告被复读 N 遍。

三种可能：外部入侵；内部测试走了错通道；供应商图省事，直接拿生产环境压测。三种定性，对应的法律后果完全不同。

搁以前，这题不难——黑客作案会掩饰，内部测试有报备，看一眼行为特征基本能分。现在不好分了。ARTEX 这类工具把"一次像模像样的攻击"的技术门槛拆到了地板上，于是一次手滑、一次没切环境、一次没改完的配置，产生的流量特征和一次真实攻击**几乎一模一样**。

工具是同一套，流量是同一种，区别只剩动机。而动机，偏偏是取证里最难证明的东西。

往后的现场会越来越多长这样：是入侵还是测试，得靠日志之外的边角证据——谁在几点登录了控制台、任务描述里写了什么、有没有授权文书——一点一点拼出来。

工具越来越聪明，定性这件事，反而越来越依赖笨功夫。

四

黑色十月的账单

把镜头拉远。湘易办这个早晨，放在今年这个被从业者私下叫作"黑色十月"的月份里，甚至排不上号。

看看十月的账单：

**10 月 6 日**　AI 推理服务商 Fireworks 内部凭证泄露，攻击者顺藤摸进 Cursor，一个恶意插件最多波及 5000 家企业；

**10 月 19 日**　路透社披露：一个人，5000 美元的 AI token，用现成的 agent 攻破四个国家 100 多家公司的网站，覆盖 1200 多个电商站点，John Deere、SharkNinja、Cummins 都在名单上。折算下来，**攻破一家公司的成本约 50 美元**；

**10 月 29 日**　币安 20 分钟被盗 63 亿美元，区块链分析公司 Elliptic 称这"几乎可以肯定是已知最大规模的单次盗窃"；

**同一天**　Cursor 扩展市场上架了一个被篡改的 Claude Code 扩展，活了 11 个小时。

前 Facebook 安全负责人、现任 Cognition 首席安全官的 Alex Stamos，用"kill chain 的反转"来解释这一切：以前是武器造好了再打，现在 AI 直接扑向目标，实时找漏洞、实时写利用、实时入侵。微软给 ARTEX 的描述更直白——从侦察到数据外泄，几乎不需要人插手。

Stamos 还说过一句被反复引用的话：很久没见过下载一个开源工具就能攻破数十亿美元公司的事了，"这就像 90 年代"。

顺便一提，微软的"补丁星期二"从每月 150 个补丁，涨到 300、600，最近一次，900 多个。防守方的账单也在涨，而且是几何级地涨。

五

下一个点"创建"的人

回到 11 月 11 日早晨。

不管最后定性是什么，这件事最扎心的地方在于：它看起来已经不像"事故"，而像"日常"。一个省级政务 App 的推送通道在早高峰复读四个小时，评论区点赞最多的话是调侃运维的——大家都默认了，出这种事，不稀奇。

50 美元一次的攻击，900 个补丁的周二，800 个不设密码的控制台。攻击的价格一路跳水，防御的价格一路看涨，夹在中间的定性工作——判断这是犯罪、事故还是测试——正在变成取证人员的日常考题。

那位在凌晨点下"创建"按钮的人，可能真的只想看看推送通道通不通。

但下一个点"创建"的，未必是这个意图。

说明：湘易办事件部分基于公开流传的网友截图，截至目前未见官方通报，文中推断仅供参考；ARTEX 相关信息来自 CrowdStrike、微软、Censys、TechCrunch 等公开报道。本文不代表任何机构立场。

觉得有用，点个赞、在看，转发给还在被新名词绕晕的朋友

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflR6KAuv76jxcDmxfj7lfPGViavaEBnj4AYdBxI4NC7rCe1s9T0s7pogE9GFnibMkpDpv2tPiblwehCEw/640?wx_fmt=png&from=appmsg)

 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflR6KAuv76jxcDmxfj7lfPGVNjUMjm27caIWTkbjyrYbYv5EU19Kibb9tiaOuHta02kQh9tXNKCIFO1w/640?wx_fmt=png&from=appmsg)

敬请各位大佬关注：小谢取证

![图片](https://mmbiz.qpic.cn/mmbiz_png/CibE0jlnugbX5SLGI9312kOrkH7gXIN5NPic75bQ8WbAFMEqvZiaQ0WSk4W9eYUfJJRzlMgibjic8mIGicMvjialoDgmQ/640?wx_fmt=png)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bQS6HX6lflR6KAuv76jxcDmxfj7lfPGV3nr2Qm4NwNoocKykavISZ8YFwZSerGVOJtV1BJJuLZLcDLAXMibicd9Q/640?wx_fmt=jpeg&from=appmsg)

**扫取二维码获取**

**更多精彩**

**小谢取证**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/HficxWTTwt1Bt3mgRlo88wGCQuAJ2kv0pzM18jFmpv4CJEBMNAicGSSvDlWSN6DG5JJ0Q8EI6oEuaZS0QNyAojYw/640?wx_fmt=gif)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflQTn7rbjfcWYyeHhTPSFnLkeCfGa1T5EZFzrZDdkrmq13K3jn4PtK4CqDhWOpUVZeD2X7rpAuq02g/0?wx_fmt=png)

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