---
title: Telegram协议设计致命缺陷：可以实现无视代理追踪
url: https://mp.weixin.qq.com/s/LEQH9U4Bs8kqM6w2p8hQAg
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T06:00:31.180987
---

# Telegram协议设计致命缺陷：可以实现无视代理追踪

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P2WmIhO0yR7RXyYtT7I97s3Pvxqmf5W1YHcyHlboJvOZbMfuq8mOMowmSwrhE9W8siafTLVLyAsTAmemRb51l5yULpLTH3ej2Q/0?wx_fmt=jpeg)

# Telegram协议设计致命缺陷：可以实现无视代理追踪

原创

A译
A译

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Nfy04C0rQr3wOibQzSguYsqbT0atxCb9OpMMjuwZ5GVHszAshOicquPVKM2sFDmD4KfsXCT0tGzINtG6BHHzuYXHJ3enw4LKGBM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617500&idx=1&sn=73c0634d23ef9a5a7ca009cf0e3b1929&scene=21#wechat_redirect)

> **导语**：VPN换了、IP变了、应用重启了——你以为Telegram的连接记录就此断开了？错了。独立安全机构Symbolic Software（符号软件）最新技术审查证实，Telegram的MTProto协议存在一项根本性设计缺陷：它在网络层明文暴露一个与用户设备强绑定的长期标识符，任何网络路径上的被动观察者都能用它追踪你。更换IP、启用VPN、切换网络，对这个标识符毫无影响。这是"匿名通信"承诺的彻底崩塌。

---

## 一、技术剖析：auth\_key\_id是什么

MTProto（Mobile Protocol，移动协议）是Telegram自研的通信协议，其消息结构在设计上就在每一帧数据的\*\*外部头部（external header）\*\*最前端预置了一个64比特的`auth_key_id`。这个字段是用户2048位授权密钥（authorization key）SHA-1哈希值的低64位，而授权密钥在账户注册时生成，永久存储于用户设备，从不经过网络传输。

理论上这个设计用于服务端快速定位解密密钥——但问题恰好出在这里：**这个标识符本身是明文传输的**。

符号软件的技术审查（编号GNMX-01）测试了所有主流Telegram客户端，结果触目惊心：

**Android客户端**：MTProto运行在纯TCP之上，只覆盖了一层简单的XOR混淆层。Telegram自己的文档明确说这套混淆仅用于对抗"幼稚的协议检测"，不提供任何加密保护。去混淆在计算上微不足道——`auth_key_id`在每个MTProto消息的外部头部以明文形式赫然在列。

**桌面客户端（macOS/Windows/Linux）**：Telegram桌面版连接目标为443端口（HTTPS标准端口），但流量根本不是HTTPS。审查团队用了四种独立技术交叉验证：TLS指纹分析（从未观察到ClientHello）、证书验证（全程无TLS握手）、数据包结构分析（MTProto外部头部紧接TCP报头，中间无TLS记录层）、选择性流量屏蔽（在防火墙中屏蔽Telegram IP段的HTTPS出站流量，仅允许纯TCP 443通过，客户端一切正常）。这证实Telegram桌面版使用443端口的唯一目的是穿透那些"放行HTTPS、屏蔽非标准端口"的简单防火墙规则——它根本不是TLS加密。

![Telegram MTProto协议头部结构与auth_key_id暴露示意](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N8QLVeST0c1Q4BXyZp4iaHw2omkU0aj158NWM4lsSIoqgR0HcHfm884iaUqScKCcPdvdQZOibaiaJ6hK58PlfphXWZ5E8hadAUC7U/640?wx_fmt=png "Telegram MTProto协议头部结构与auth_key_id暴露示意")

---

## 二、追踪实验：VPN和IP变更全部无效

符号软件进行了系统性的追踪持续性测试，结果令人警醒：

| 测试条件 | 正常情况下应能对抗的追踪手段 | auth\_key\_id状态 |
| --- | --- | --- |
| 应用重启 | 会话级标识符、内存状态 | **不变** |
| IP地址变更（DHCP续期） | IP地址追踪 | **不变** |
| WiFi网络切换 | 网络级指纹、IP归属 | **不变** |
| WiFi与蜂窝网络切换 | IP归属及网络介质指纹 | **不变** |
| 启用VPN | IP追踪、地理位置、网络归属 | **不变** |
| 流量经由Tor | 来源IP、路径观察 | **不变** |
| 切换至同一数据中心内另一Telegram服务器IP | 服务器端点锁定 | **不变** |
| 连续数日至数周持续观察 | 短期或会话轮换标识符 | **不变** |

结论只有一个：**auth\_key\_id是一个跨越一切网络条件变化的持久化设备指纹**。

---

## 三、前向保密（PFS）为何也无济于事

Telegram支持完美前向保密（Perfect Forward Secrecy），理论上应能限制密钥泄露后的损失。但符号软件明确指出：**PFS解决的是"事后解密"问题，而非"实时流量分析"和"设备追踪"问题**。

启用PFS后，可见标识符会切换为临时密钥对应的`auth_key_id`，而非永久密钥。但临时密钥本身有效期通常为24小时，在此期间临时`auth_key_id`和永久的一样可观察、可追踪。更关键的是：**新旧密钥之间的绑定步骤本身就是网络可见事件**。旧临时`auth_key_id`用于协商和授权新临时密钥，两者相继出现在同一流量流中，来自同一客户端，通常还来自同一IP地址。攻击者只需维护一个"密钥旋转事件"的记录数据库，就能将任意次数的密钥轮换串联成完整的设备轨迹。

正如安全研究员沃兹尼亚克（Michał "rysiek" Woźniak）此前分析的："客户端IP地址与临时auth\_key\_id同时变化的概率极低。"这不是隐私边界，这是一条网络可见的事件链，连接着旧标识符与新标识符。

---

## 四、谁可以追踪你

这个漏洞的可怕之处在于**不需要任何主动攻击**。符号软件在报告中列举了"在作用域内"的对立方类别：

* 网络路径上的ISP
* 移动通信运营商的深度数据包检测系统
* 企业或机构网络管理员
* 公共WiFi运营商
* 互联网交换点（IXP）或中转网络运营商
* 恶意热点经营者
* 国家 surveillance 项目
* 任何对传输介质有物理或无线访问权限的被动窃听者

没有一个需要中间人攻击，不需要证书伪造，不需要主动协议操控。**只需要简单的流量抓取和公开文档记录的轻微去混淆步骤**，就能从任何Telegram流量中提取持久的设备标识符。

---

## 五、秘密聊天无法防御这一层

Telegram的"秘密聊天"功能提供了端到端加密，但这并不保护`auth_key_id`问题。原因很直接：端到端加密作用于Telegram的应用层内容，而`auth_key_id`存在于**MTProto外部头部**，位于秘密聊天加密层的下方。传输层的事实在应用层加密下依然原封不动——秘密聊天加密的是"说了什么"，而追踪者关心的是"谁在说"。

---

## 六、Telegram官方回应苍白无力

据iStories报道，Telegram曾回应称`auth_key_id`"定期更换，不泄露用户信息"。符号软件用实证测试了这句话——结果截然相反：

> "我们的实证测试表明，auth\_key\_id的轮换虽在理论上可行，但在实践中极少发生——在应用重启、网络变更或延长时段测试中，我们未观察到任何轮换行为。这种持久性，与'频繁轮换'的说法相矛盾，极大加剧了暴露的隐私影响。"

要让"定期轮换"真正对抗追踪，需要满足两个条件同时成立：轮换频率高于对手的相关性分析窗口，且轮换本身对网络不可见。**当前部署的协议两个条件都不满足**。

---

## 七、国内影响：Telegram被用于识别"特定用户"

Telegram在国内拥有大量技术从业者、开发者群体及隐私意识较强的用户群体。这个漏洞对国内用户的影响尤为直接：

* \*\*GFW（国家防火墙）\*\*可被动提取经过跨境节点的Telegram流量中的`auth_key_id`，构建长期用户追踪数据库，即便用户使用VPN出口，Telegram客户端本身的连接特征（去混淆后明文）依然可被识别。
* **宽带/移动运营商**可记录用户设备在数月内的`auth_key_id`出现规律，精确还原用户的通信时间表和行为模式。
* **特定用户识别**：对安全研究人员、记者、活动人士而言，这意味着一旦某次Telegram通信的`auth_key_id`与真实身份产生关联（比如在同一时间访问了已知IP），该标识符就成为跨越一切后续网络变化的"终身标签"。

符号软件报告指出："这一漏洞的影响远不止理论层面。对于使用Telegram的记者、活动人士和其他高风险用户群体，这尤其重要。"而在国内，这些群体恰恰是Telegram的重度用户。

---

## 八、根本问题：设计层面的隐私放弃

符号软件的技术报告给出了最为尖锐的定性：

> "该漏洞并非源于技术失误，而是Telegram通过不采取适当加密措施，对其用户隐私的基本放弃。正确的解决方案是……强制使用传输层加密——这几乎是所有其他主要消息平台的通用做法。技术实现简单，性能影响微乎其微，隐私收益却极为显著。在Telegram实现适当TLS加密之前，它持续让用户暴露于不必要的隐私风险之中。"

讽刺的是，实现这一修复的技术门槛几乎为零。几乎所有主流互联网服务早已默认启用TLS——Telegram的桌面客户端甚至已经"假装"在使用TLS（端口443），却从未真正实现。

**用户怎么办？** 在Telegram修复这个设计缺陷之前，没有有效的客户端侧缓解手段。启用VPN只能更换IP，更换设备会生成新的`auth_key_id`（但旧标识符已记录），使用代理同理。唯一有效的防护是将Telegram通信转移到其他协议——而对于已经将Telegram作为主要工作通信工具的群体，这个迁移本身的成本就是壁垒。

这个漏洞的存在，或许正是某些人希望用户继续留在Telegram上的理由。

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MkQ9uQgrplJ1VM22B3ibaib5I7E66cFThF5gcSHUiblD0nSpyO1aMzhkpCntC7YFupvbo3uySFBYn8fIZbxn75B3DhyvyltPsta8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617065&idx=1&sn=1e30ce488590711587c29414a82b7ab8&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M6kfpWeYytyBgO0DC1jZPRU2TibWlRJC5yPHf8Nh8FJBKLXm3icia8YdibIByciaWbKLkV0QWibwFRriaDzMYEUGKF41FlImbkb4V5G8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617222&idx=2&sn=a600c58c6ac251bf0313134ad70a4fd8&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PhonibtNh9JibUEsbcxjX9iabDfmibaSZSvqdmp4Ey0apM8Ll8zRUgibCARXiaCcJPLMLLrk6Pv8AbVCclDKyy5EqOjFpGNgcDLxPbM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617751&idx=1&sn=f1c1ed68d848029fc1ff726087cac05a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MKE8UsztH3T5yt5F13tk2udcoNmLlyTbAicYiaPrFzulCbOGjcmZRwZIyyKNkCHRpktJz6LwpyyU5jHugpDSTKp1cUyRvm3Nvzo/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617464&idx=1&sn=a447b46bf211ae577eec30f82ed1d089&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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