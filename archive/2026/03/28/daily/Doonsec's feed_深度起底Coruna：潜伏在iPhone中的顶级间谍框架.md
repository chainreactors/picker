---
title: 深度起底Coruna：潜伏在iPhone中的顶级间谍框架
url: https://mp.weixin.qq.com/s/KfzHFoBom_BKdzUscgV8jw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:36:25.828477
---

# 深度起底Coruna：潜伏在iPhone中的顶级间谍框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/E3ZvvAXyiaibkepHwOW4cOF8l4wqBESvTK6aOSdJYPUsHkjMO7AbnR2AefKLicibOu9q1GCUnZKqibo51ekibHVB3dmACXW58Bw1vF6Ay2iacVZrs4/0?wx_fmt=jpeg)

# 深度起底Coruna：潜伏在iPhone中的顶级间谍框架

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaiblGftcvjtV0OPDDB1nzAayCk2KF9HqYrWFQOo3L9oG8N09U0yBFUBk2U47MRBUTiajFtQwdb9vPiaSxFQY1auibFct4XJ7eDgUNsk/640?wx_fmt=png&from=appmsg)

一个被命名为Coruna的漏洞利用工具包，正将数亿台苹果设备置于前所未有的风险之中。

2026年3月4日，谷歌与iVerify发布了一份令人震惊的报告：一套针对苹果iPhone设备、高度精密化的漏洞利用工具包正在被广泛使用。这套工具包不仅被用于国家级的网络间谍活动，更已流入网络犯罪市场，被用于针对普通用户的牟利攻击。

更令人担忧的是，研究人员发现，这套名为Coruna的工具包，与2023年震惊安全界的“三角行动”攻击活动有着千丝万缕的联系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkaEFEvSOGVNFibghrkBu6aWocGebUbgTdGibqyW33y0w9w5gaW0THvibRPbaTGNR9dmxSvI5yvlRQZoQS3e5zVmHPlR5JZv84geI/640?wx_fmt=png&from=appmsg)

01 从“三角行动”到Coruna

“三角行动”是一场针对iOS设备的复杂移动高级持续性威胁攻击活动。安全人员在监控企业内部Wi-Fi网络流量时，发现了多部iOS设备出现异常行为。

经过长达六个月的调查，确认此次攻击使用了精密的间谍软件植入程序与多个零日漏洞。而Coruna中针对CVE-2023-32434与CVE-2023-38606的内核漏洞利用程序，实际上是三角行动中所使用漏洞利用程序的更新版本。

研究人员还发现，Coruna包含另外四个此前未在三角行动中出现过的内核漏洞利用程序，其中两个是在三角行动被发现之后才开发出来的。

所有这些漏洞利用程序均基于同一套内核利用框架构建，并共享通用代码。这些发现让研究人员得出结论：该漏洞利用工具包并非拼凑而成，而是采用统一思路整体设计的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibk9KansBOKdSibyxxNmHTE1NsiboAic94rgCrwNd2jAquuic26uL4UdPywsWvYNXcaxEia3ZnPHeK0fo492hXVQDBUKyw371qiaBS6Ls/640?wx_fmt=png&from=appmsg)

02 攻击链全解析

Coruna的攻击过程堪称教科书级别的复杂操作，其攻击链设计精密，环环相扣。

第一阶段：浏览器漏洞利用

攻击始于Safari浏览器。一个初始加载程序会识别浏览器特征，根据浏览器版本选择并执行相应的远程代码执行漏洞利用和指针身份验证代码漏洞利用。

第二阶段：组件下载与解密

攻击载荷负责启动内核漏洞利用。初始化后，攻击载荷首先下载一个包含其他可用组件信息的文件。该文件经过多层加密和压缩处理：

• 使用ChaCha20流密码解密

• 得到魔数为0xBEDF00D的容器文件

• 解压后呈现魔数为0xF00DBEEF的容器

• 最终找到魔数为0x12345678的组件信息文件

第三阶段：精准组件选择

利用目标设备所需的组件是使用软件包ID进行选择的。其高字节指定了软件包类型和所需硬件：

• 0xF2/F3：针对ARM64/ARM64E架构的漏洞利用程序

• 0xA2/A3：针对ARM64/ARM64E架构的Mach-O加载器

• 2/0xE2：针对ARM64/ARM64E架构的植入程序

软件包ID的其他字节则定义了所支持的固件版本和CPU代次。研究人员观察到的部分软件包ID包括：

软件包ID 描述

0xF3300000 内核漏洞利用（iOS<14.0 beta 7）及其他组件

0xF3400000 内核漏洞利用（iOS<14.7）及其他组件

0xF3700000 内核漏洞利用（iOS<16.5 beta 4）及其他组件

0xF3800000 内核漏洞利用（iOS<16.6 beta 5）及其他组件

0xF3900000 内核漏洞利用（iOS<17.2）及其他组件

第四阶段：内核漏洞利用与植入

在下载完必要组件后，有效载荷开始执行内核漏洞利用程序、Mach-O加载器以及恶意软件启动器。有效载荷会根据固件版本、CPU类型以及是否具备iokit-open-service权限来选择合适的Mach-O加载器。

03 漏洞利用程序的进化

研究人员对该工具包中的全部五个内核漏洞利用程序进行了分析，发现其中一个是在“三角行动”中发现的那个漏洞利用程序的更新版本。

虽然存在许多细微改动，但最显著的改动包括：

• 更精确的版本检查：代码会考虑XNU版本字符串中的更多值

• 支持更新的iOS版本：增加了对iOS 17.2的检查

• 支持更新的处理器：增加了对A17、M3、M3 Pro、M3 Max的检查

• 增加了对iOS 16.5测试版4的检查

如果目标漏洞已在iOS 16.5测试版4中修复，为何该漏洞利用程序仍需检查iOS 17.2和更新的处理器呢？

通过检查其他漏洞利用程序便可找到答案：它们均基于相同的源代码。唯一的区别在于它们所利用的漏洞不同，因此添加这些检查是为了支持更新的漏洞利用程序，并且在重新编译后出现在旧版本中。

04 启动器：攻击的指挥中心

启动器负责协调漏洞利用后的各项活动。它也会利用内核漏洞利用程序及其提供的接口。

由于漏洞利用程序在执行过程中会创建特殊的内核对象，这些对象具备读写内核内存的能力，因此启动器只需重新利用这些对象即可，无需再次触发漏洞或重新走一遍完整的漏洞利用流程。

启动器会执行以下操作：

1. 清理漏洞利用痕迹

2. 从配置文件中获取要注入的进程名称

3. 将初始加载程序注入目标进程

4. 利用该程序执行自身

5. 启动植入程序

05 文件标识符系统

Coruna使用一套复杂的文件标识符系统来管理其组件。研究人员观察到的文件标识符包括：

文件ID 描述

0x10000 植入程序

0x50000 Mach-O加载器（默认）

0x70000 附加组件列表

0x70005 启动器配置

0x80000 启动器（在0xF2/0xF3包中）或Mach-O加载器（在0xA2/0xA3包中）

0x90000 内核漏洞利用程序

0x90001 内核漏洞利用程序（用于Mach-O加载器）

0xA0000 日志清理器

0xA0001 Mach-O加载器组件

0xA0002 Mach-O加载器组件

0xF0000 RPC加载程序

这套精密的标识系统使得Coruna能够根据目标设备的精确配置，动态选择和加载最合适的攻击组件。

此案例再次表明，这类恶意工具的潜在广泛使用所带来的危险性。该框架原本是为网络间谍活动开发的，如今却被更广泛的网络犯罪分子所利用，致使数百万使用未打补丁设备的用户面临风险。

鉴于其模块化设计和易于重复使用的特点，安全专家预计其他威胁行为者将开始将其纳入攻击手段。我们强烈建议所有iPhone用户立即检查系统更新，并安装最新的安全补丁。

在这个数字时代，安全不再是可选项，而是必需品。一次简单的系统更新，可能就是保护你数字生活的最有效防线。

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibnktJXjn2dTEgVUWmIWdKXJgIZS0KhKF8ibmydnqG96GS34rsgMbzVykvVqPDaAXxMfRibxr9eiaAibVFTicLibOYricakqjzPTicBroR0/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

AI紫队安全研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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