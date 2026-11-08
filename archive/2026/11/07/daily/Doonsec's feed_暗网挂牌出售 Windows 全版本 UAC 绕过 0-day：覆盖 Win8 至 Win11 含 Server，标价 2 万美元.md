---
title: 暗网挂牌出售 Windows 全版本 UAC 绕过 0-day：覆盖 Win8 至 Win11 含 Server，标价 2 万美元
url: https://mp.weixin.qq.com/s/TS5T9UxEcRisJknbp7bHMg
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:08:59.478711
---

# 暗网挂牌出售 Windows 全版本 UAC 绕过 0-day：覆盖 Win8 至 Win11 含 Server，标价 2 万美元

# 暗网挂牌出售 Windows 全版本 UAC 绕过 0-day：覆盖 Win8 至 Win11 含 Server，标价 2 万美元

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

11 月 6 日，安全情报平台 dbugs（隶属 Positive Technologies）通过其 X 账号 @ptdbugs 发布了一条暗网市场情报：有人正在出售一个针对 Windows 操作系统的 0-day 利用，类型为 UAC 绕过，声称影响从 Windows 8 到 Windows 11 的全部客户端版本以及对应的 Server 版本，标价 2 万美元（约 14 万元人民币）。这条信息本身没有披露任何技术细节；它是一则"售卖帖"，不是漏洞通告。本文把它当作一次威胁情报简报来拆解：公开能确认什么、不能确认什么，这类 0-day 在攻击者手里如何被使用，以及在没有补丁的窗口期企业和个人该怎么防。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Gnth8hrVRwz08xAJ76lMAHS0Ir1MEly8Sqnk6aZNykKxGldR3ySUG2l37bE9gq3CEDITFVJichqM2ibqmKs16ksfQwPnUxRjj6A/640?wx_fmt=jpeg&from=appmsg)

## 一、先看问题：公开信息能确认与不能确认的

能确认的事实只有以下几条：

* **来源与发布时间**

  ：dbugs（PT 旗下漏洞/利用情报平台）在其暗网情报栏目发布，X 发布时间为 2026-11-06 12:42 UTC；dbu.gs 页面标注"Dark Web / Yesterday 15:53"，与 X 时间落在同一天。
* **售卖标的**

  ：一个 Windows 操作系统的 0-day 利用，漏洞类型为 **UAC Bypass（用户账户控制绕过）**。
* **影响范围（卖方声称）**

  ：从 **Windows 8 到 Windows 11**，并包含对应的 Server 版本。这是卖方自述，未经独立验证。
* **价格**

  ：**2 万美元**。
* **页内声明**

  ：dbu.gs 标注"For informational purposes only（仅作信息用途）"。
* **技术细节**

  ：**未公开**。售卖帖不提供绕过的具体载体、触发条件或利用代码。

这里要钉死一个偏差：**"影响 Win8 到 Win11 含 Server"是卖方的宣传口径，不是已验证的漏洞范围**。同样地，"UAC Bypass"在地下市场里有时被泛化使用，可能指从标准用户到高完整性（管理员）的绕过，也可能叠加完整的 SYSTEM 提权；listing 没有说明终点权限，因此 2 万美元的标价更像是"到达管理员/高完整性"的入门价，而非完整内核级 SYSTEM 链；但这只是基于价格的合理推测，公开信息没有证实。

待解问题钉墙：

* 该 0-day 是否已有在野利用：公开渠道未见证据。
* 微软是否已知悉并着手修复：截至本文成稿未见 MSRC 或 Patch Tuesday 相关公告。
* 绕过的具体技术载体：尚未披露。
* 卖方是否真有可用利用、还是"画饼"：无法从 listing 判断。

## 二、UAC 绕过在攻击链里到底站哪一级

要理解为什么一个"只是绕过 UAC"的 0-day 会被标价出售，得先看清它在攻击链里的位置。

UAC（User Account Control，用户账户控制）是 Windows 的一道"半程防线"：即使你用管理员账户登录，日常进程默认也以中等完整性级别运行，只有在你点击"允许"后才会提升为高完整性（管理员）级别。它的设计目标是**减少恶意代码以高权限静默运行的机会**，而不是一道真正的安全边界。微软自己多次把 UAC 定性为"威慑而非防线"。

正因为如此，UAC 绕过从来不是攻击的终点，而是**从低权限到高权限之间的一级跳板**。一个典型的入侵链条会是这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0HdS6leSrdyuxuib6iafhM5ico3DnEjsb8FZ6OkGdXicXa57uOY8WgxLPPnXq9gF4yrW8mALcyRHmCJedfNf4sXoWEA50iaicpyia3t8A/640?wx_fmt=png&from=appmsg)

攻击者先通过钓鱼、漏洞或凭据投送拿到一台机器的**标准用户或中等完整性**立足点，再用 UAC 绕过把自身提到**高完整性/管理员**，之后才能安装持久化组件、dump 凭据、关闭或干扰安全软件、向域内的其他机器横向移动。也就是说，这个 0-day 的价值在于**把"已经进门的低权限进程"快速变成"能搞事的高权限进程"**，它通常和初始访问、凭据窃取、横向移动载荷打包使用。

这就解释了它和"完整提权到 SYSTEM"的区别：如果只是绕过 UAC 到管理员，攻击者还受限于管理员本身的权限边界；若叠加内核漏洞到 SYSTEM，则能关掉 EDR、加载驱动、使其脱离用户态监控。2 万美元的定价，加上"UAC Bypass"的直白标注，更贴近前者。

## 三、把这条售卖帖放进 2026 年的 Windows 0-day 背景里

公开信息没有给出这条 0-day 的技术，但 2026 年本身就是 Windows 提权/绕过类 0-day 异常活跃的一年，可以用已披露的案例说明"为什么这类挂牌值得重视"：注意，下面这些是**别的、已公开或已修补的漏洞**，不是本条售卖帖：

* **CVE-2026-68820**

  ：Windows afd.sys 驱动中的释放后使用漏洞，被朝鲜关联的 Lazarus 组织用于内核级提权到 SYSTEM，并部署 FudModule rootkit 干扰 EDR 与 Smart App Control，微软在 2026 年 8 月补丁中修复。
* **CVE-2026-21510**

  ：Windows Shell（MOTW / Mark of the Web）绕过，攻击者用伪造 LNK 让系统把恶意文件当可信本地文件执行，绕过 SmartScreen、UAC 等层层防护，2026 年 2 月补丁修复，CVSS 8.8，当时已在野。

这两个例子说明两件事：一是 Windows 平台的高危提权/绕过在 2026 年确实处于被 APT 与犯罪团伙密集利用的状态；二是**即便厂商月度补丁节奏很快，从漏洞披露到全员打补丁之间永远存在暴露窗口**，而 0-day 售卖帖瞄准的正是"还没有补丁"的那段时间。

至于 0-day 交易市场本身：dbugs 这类平台一边发布 PT 自有研究成果，一边转述地下市场情报；地下论坛里 Windows 提权类利用的标价跨度极大，从几千美元到数十万美元不等，取决于能否到 SYSTEM、是否稳定、是否可公开。2 万美元处于偏低区间，与"UAC 绕过（到管理员）"的定位相互印证，但仍属推测。

## 四、没有补丁的窗口期，怎么防

这是本文最实际的部分。由于这是 0-day、技术未公开、微软尚未发布补丁，**任何"打某个补丁就能解决"的说法都是错的**；当前能做的只有纵深防御，把 UAC 绕过一旦发生时的危害压到可控范围：

**1. 收紧权限基线（治本）**

* 日常办公账户**不要保留本地管理员权限**；管理员账户仅在需要时单独使用。UAC 绕过的目标就是把低权限进程提上来，若本来就没有管理员可提，攻击链条会断在起跑线。
* UAC 设置调到"始终通知"，并关闭"静默自动提升"类的宽松策略。

**2. 监控 UAC 绕过的已知行为面（治标 + 预警）**
UAC 绕过在实战中多借助"自动提升（AutoElevate）"的 COM 接口、计划任务、注册表或二进制侧加载来触发。防御方不必知道本次的具体载体，也能监控一类**异常行为模式**：

* 进程完整性级别从 medium 异常跳到 high/system，且父子进程关系不符合正常管理操作；
* 已知会被滥用的自动提升组件（如 fodhelper、eventvwr、sdclt 等经典载体）被异常调用或配合可疑子进程；
* 从用户可写目录向系统目录注入 DLL、或对自动提升二进制做侧加载的可疑文件活动。

EDR / 行为监控应把这些模式纳入高优先级告警，而不是只靠特征库。

**3. 缩小攻击面**

* 启用 Attack Surface Reduction（ASR）规则，限制 Office / 脚本 / 宏类载荷的后续行为。
* 对不再需要的自动提升入口做盘点与限制（属于系统加固范畴，按企业自身基线执行）。

**4. 切断提权之后的去向**
UAC 绕过只是手段，攻击者真正要的是凭据与横向移动。凭据防护（Credential Guard）、网络分段、限制本地管理员在域内的横向权限，能在"已经被提到管理员"之后继续挡住后续危害。

**5. 审计与响应**
定期审计本地管理员组成员、自动提升配置与异常的计划任务；对高风险主机做好全量遥测留存，以便在暴露窗口内做回溯狩猎。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GB2SDSedYHYXlAlUOkSLJ4ibJhQvicDhq0QMVfpbjsk3aZicnkzwcHAfRcibgFcib5omm7GE9iaAfan63Y1OEWIN6WyL1wK09UiaZKHE/640?wx_fmt=png&from=appmsg)

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0G9Z5bRrBPpYJ6aM4ibe1fXibj3Ox45f8qZY5rNsr2sLeHqDB5GjUO5WFlZz03yVRJ64HSics3YmwKIYSSO359Ml244dscAf8r41c/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外等平台- 搜索的内容通过结合编写 -

公众号 | AnQuan7 (Ots安全)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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