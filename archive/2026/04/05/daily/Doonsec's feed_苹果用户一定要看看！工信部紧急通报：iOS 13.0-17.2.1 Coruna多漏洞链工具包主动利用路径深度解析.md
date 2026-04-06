---
title: 苹果用户一定要看看！工信部紧急通报：iOS 13.0-17.2.1 Coruna多漏洞链工具包主动利用路径深度解析
url: https://mp.weixin.qq.com/s/85UkeJBf62NeZKmG2xS0Pw
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:41:33.969032
---

# 苹果用户一定要看看！工信部紧急通报：iOS 13.0-17.2.1 Coruna多漏洞链工具包主动利用路径深度解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0G1g5FXbeL9V63xEW6x16MI9HVZpibFhe2m1r8zs4x4184BjzOBMKby0jm9R6EwkJnW4JlhSWtibygKL3ibmf69VbiaicXzeiaG1uglM/0?wx_fmt=jpeg)

# 苹果用户一定要看看！工信部紧急通报：iOS 13.0-17.2.1 Coruna多漏洞链工具包主动利用路径深度解析

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HhdQmGQ5s55GVDvbrrncVzlyP08tF0ygUT8uXNibAvVjuvhrpHltPia4icdicWaIib1hA8ibzTrvjuA07aL9ZTP343lgyZeeIdCH9Po/640?wx_fmt=jpeg&from=appmsg)

工信部和漏洞信息共享平台（NVDB）于2026年4月3日发布风险提示，监测发现攻击者正针对iOS 13.0至17.2.1版本的iPhone与iPad发起漏洞链攻击。通过诱导用户访问恶意网页，可实现远程代码执行、敏感信息窃取及设备接管。该事件已成为当前iOS安全领域热点，尤其老旧设备面临较高风险。

苹果已通过iOS 18.7.7等安全更新提供修复。本文聚焦此次Coruna等漏洞利用工具包驱动的攻击事件，详细拆解利用路径（含Coruna工具包技术细节与中性技术示例）、TTPs分析，并系统讲解iOS安全核心机制，帮助读者从攻击链视角提升威胁识别能力。

事件背景与时间线

* 2026年4月3日：工信部NVDB发布紧急风险提示，确认攻击者使用成熟漏洞工具包实施定向攻击。
* 攻击演变：攻击活动依托Coruna漏洞利用工具包（包含23个漏洞、5条完整链路），早期针对WebKit等多组件；后续迭代结合dyld等内核组件，覆盖iOS 13.0-17.2.1范围。
* 当前态势：苹果官方安全公告明确，相关漏洞已在iOS 18.7.7及后续系列中完成修复，老旧版本因补丁缺失成为主要攻击面。类似工具包（如DarkSword）显示攻击者持续跟踪未打补丁设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0F7uzlGveg1A6vrvibfrgLibfXriaAsVNDPaER1R1mamICjBz98bibZduqAQtkgksg9toljJFQeKkzjyDo2hywQHwynj2q0JtL3QJo/640?wx_fmt=png&from=appmsg)

图1：Coruna iOS Exploit Kit时间线（基于公开威胁情报报告）

该图清晰展示Coruna工具包从早期CVE补丁到2026年水坑攻击的演进路径，直观反映其利用成功扩散过程。

攻击手法与TTPs分析

攻击采用“钓鱼诱导+浏览器漏洞链+多阶段提权”模式，整个过程隐蔽且高效：

1. 初始接触：通过短信、邮件或网页投毒推送恶意链接，诱导Safari浏览器打开。
2. 漏洞触发：利用WebKit引擎的内存腐败、use-after-free或类型混淆等问题，在渲染阶段实现初始代码执行。
3. 提权与后渗透：借助内存读写原语，逐步绕过沙箱与内核防护，最终植入远程控制组件。
4. 持久化：窃取通讯录、定位、浏览记录等数据，实现长期驻留。

利用路径中性描述（技术分析参考，仅供研究）：

此次攻击链高度依赖Coruna工具包的多漏洞组合设计。该工具包由开发者内部命名为Coruna，采用高度模块化框架，内置5条完整攻击链和23个exploit，支持iOS 13.0-17.2.1全版本指纹识别与自动适配。框架复用部分早期Operation Triangulation内核利用代码，并集成通用模块（如rwx\_allocator用于RWX内存分配绕过、PAC绕过模块），实现“即插即用”链式攻击。典型流程如下（以Coruna工具包常见链路为例，无任何完整可执行代码或EXP，仅概念性技术拆解）：

* 第一阶段：WebKit初始RCE（浏览器上下文代码执行）

攻击者构造恶意网页负载，触发WebKit引擎（如ANGLE图形库或Navigation API）的内存问题。例如，利用use-after-free漏洞：先通过JavaScript释放某个对象（如特定DOM元素或JS对象），随后立即重新分配内存并填充攻击者控制的数据结构，导致类型混淆（type confusion）。此时，原本指向合法对象的指针被篡改，可实现任意内存读写原语（arbitrary read/write）。

Coruna工具包技术示例：Coruna在该阶段集成多条WebKit RCE链路，利用内存腐败或整数溢出技术，通过JS精心安排对象生命周期，在释放后结合堆喷射（heap spraying）或精确分配，使后续访问指向攻击者伪造的“假对象”。框架内置去混淆JS负载与版本适配逻辑，实现低交互触发。该阶段无需用户额外交互，属于典型低交互攻击。

* 第二阶段：沙箱逃逸（Sandbox Escape）

初始RCE发生在WebContent进程的沙箱内。攻击者利用进程间通信（IPC）机制或GPU进程跳转（如Safari WebContent到GPU Process的IPC层漏洞），进一步扩展控制。例如，通过NSExpression等框架构造payload，实现从WebContent进程“跳跃”到更高权限上下文。

Coruna工具包技术示例：Coruna提供专用PAC绕过模块与Mach端口操纵组件，利用已获内存写能力篡改IPC消息句柄或绕过MACF（Mandatory Access Control Framework）策略。部分链路结合共享资源（如Keychain或pasteboard）泄露凭证，实现沙箱边界突破。该步骤是Coruna框架的关键跳板，使攻击从“浏览器限制”进入更广泛的系统进程，模块化设计允许不同链路快速复用逃逸原语。

* 第三阶段：内核/提权与持久化（Kernel-level Escalation）

获得沙箱外执行能力后，攻击者转向dyld（Dynamic Link Editor）等核心组件的内存腐败漏洞，实现系统级代码执行。Coruna在此阶段复用并升级早期Triangulation内核exploit（如CVE-2023-32434相关更新版），结合内核PAC绕过与RWX分配模块完成最终控制。

Coruna工具包技术示例：利用dyld加载动态库时的内存写原语，篡改库加载路径或指针，注入恶意动态库。随后通过内核读写完成持久化（如修改启动守护进程或安装后门）。整个链路高度依赖目标iOS版本的补丁状态，成功后可实现零点击式设备接管。Coruna的5条链路中，内核阶段统一调用内部exploit模块，确保跨版本稳定性。

利用成功示意图（基于公开报告的实际交付链路）：

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HMmuY6VtpxsX6YqY4RM4CQeicEpcAQ1ELJRrUWI2DEzTWs2GibAvggH2MFRl3WA6dgmDBJpkNp0Dpnly9RXZiciaP5k4IUywA4xos/640?wx_fmt=png&from=appmsg)

图2：Coruna工具包在iOS 15.8.5上的完整利用交付链路（HTTP请求日志）

该图展示从Landing Page到WebKit R/W、User-mode PAC bypass、PE loader直至Implant植入的成功流程，直观呈现攻击链“利用成功”后的网络行为特征。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GWVjiaBM8CAYibILOjLGb8L6LhicOuBJdpicKhLLuGUb2PkctAOoITfiaUczJbqo1oRE2HKeJs194EbDeMxmcuxuJwByWriaHnWWDfw/640?wx_fmt=png&from=appmsg)

图3：Coruna工具包中触发CVE-2024-23222的混淆JS代码片段（高亮关键触发逻辑）

图中清晰标注Utility functions、Obfuscated constants及Trigger for CVE-2024-23222，辅助理解WebKit RCE阶段的内存操作实现。

此类TTPs与已知商用间谍工具高度吻合，核心在于“精确的内存原语构建 + 模块化链式绕过”：Coruna工具包的工程化设计显著降低了攻击门槛，从WebKit浏览器级漏洞起步，逐步升级至内核级控制。

影响范围与受害者画像

* 受影响版本：iOS 13.0至17.2.1（含对应iPadOS）。
* 设备类型：iPhone 8及以上早期机型、部分无法升级至最新系统的iPad。
* 典型目标：高价值个人、企业高管及敏感行业用户，攻击者倾向精准社交工程投递或水坑攻击。

潜在后果包括隐私数据泄露与设备失控风险，已观察到从定向间谍向金融动机攻击扩散的趋势。

iOS安全核心知识分享

iOS安全设计采用纵深防御理念，核心机制包括：

* 代码签名与沙箱隔离：所有进程强制签名，运行于独立沙箱，严格限制资源访问。
* ASLR与PAC：地址空间布局随机化结合指针认证技术，大幅提升内存攻击难度（Coruna等工具包需专用模块绕过）。
* WebKit防护：浏览器引擎内置站点隔离与内容安全策略，但仍需系统级补丁支撑。
* 更新机制：支持Background Security Improvements，即使主版本未升级，也可快速下发关键修复。

理解这些机制，能帮助用户判断自身设备暴露面，避免成为低挂果实。

DarkSword工具和Coruna工具有什么区别

* Coruna：针对较旧版本，主要影响 iOS 13 至 iOS 17.2.1（2023年12月左右的版本）。这覆盖了大量仍未更新的旧设备，用户基数大。
* DarkSword：针对较新版本，主要影响 iOS 18.4 至 iOS 18.7（2025年发布的版本）。它对iOS 18系列的威胁更大，尤其在iOS更新推广较慢的情况下。

实际影响：Coruna影响更多“老旧”设备，DarkSword则瞄准了“相对较新但未及时打补丁”的设备。目前仍有大量用户未更新到最新iOS，导致两者共同威胁数亿台Apple设备。

漏洞利用链和复杂度

* Coruna：包含 5条完整利用链，共23个漏洞（部分为已知CVE，部分为高级绕过技术）。框架工程化程度高，包含多种远程代码执行（RCE）、沙箱逃逸、权限提升等模块。有些分析认为它与早期的“Operation Triangulation”攻击框架有演进关系，可能源自美国政府承包商（如L3Harris）开发的监控工具，后流向黑市。
* DarkSword：使用 6个不同漏洞（部分为0-day），完整攻击链更精简。全部基于JavaScript实现（无传统二进制文件），部署更简单，能注入系统进程（如configd、wifid等）快速窃取数据。复杂度略低于Coruna，但针对性更强。

总结与学习启示

本次工信部风险提示再次印证：iOS虽具备完善安全架构，但未及时更新的老旧版本仍是攻击者重点目标。通过对Coruna工具包利用路径的深度拆解（5条链路、23个exploit的模块化设计与Triangulation框架演进）及利用成功示意图，读者可清晰看到攻击者如何层层突破防御，从WebKit RCE到内核提权的完整链路。

关键启示：

* 及时更新是最低成本、最高效的防御手段；
* 掌握内存原语、沙箱逃逸及PAC绕过等技术概念，有助于从攻击者视角评估风险；
* 日常养成不点击不明链接、不越狱、不安装未知来源App的习惯，可大幅降低暴露面。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EjOhDVdNzFVl2SOSGDMz8EYKgiclyXqQ9uAOwzyskagTR0IFHz0ZxP0mILtQsjHDfYBvl34p2l1TCV6EXibBia9UYeZkbePEE0lI/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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