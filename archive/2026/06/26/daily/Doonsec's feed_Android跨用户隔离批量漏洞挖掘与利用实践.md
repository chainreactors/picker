---
title: Android跨用户隔离批量漏洞挖掘与利用实践
url: https://mp.weixin.qq.com/s/zZXEFpxBT8kBf806tmGbUA
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:57.665859
---

# Android跨用户隔离批量漏洞挖掘与利用实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dBEVa0kEoRDPwsbEB5HTDZictIVxkx09vz3NvvmNDxq6zm1FgTj2y4bOTMKqpJNZYBiaqVyPUzMNbl6seJkM49fykRIUxUQy0jIuIZKQpbMmg/0?wx_fmt=jpeg)

# Android跨用户隔离批量漏洞挖掘与利用实践

国家网络空间安全云社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**摘要**

本文主要围绕Android系统的多用户隔离机制展开，结合AI辅助技术探讨新型攻击面的产出、威胁模型的建立以及批量化漏洞挖掘的方法和成果。全文共分为四个核心部分：

* 多用户安全机制基础——深入分析Android底层的多用户隔离设计、账户类型及权限架构。
* AI辅助攻击面产出以及威胁模型建立——介绍基于AI的自动化日志与补丁分析平台，构建边界组件与接口的注入威胁模型。
* 批量化漏洞挖掘方法实践——阐述漏洞挖掘的完整工程化流水线，并结合典型内置组件及服务漏洞进行深度解构。
* 成果展示以及总结——汇总团队挖掘的AOSP与主流厂商漏洞，并展望AI赋能下安全审计模式的颠覆性变革。

**多用户安全机制基础**

**01**

**研究背景与安全切入点**

Android 的多用户机制（Multi-User）支持在同一台物理设备上创建多个相互独立的账户。每个账户拥有独立的运行环境、应用数据和系统设置，该机制广泛应用于平板电脑、共享设备及企业移动设备管理（MDM）等高隔离性场景。

本研究高度聚焦于系统跨用户资源访问的输入路径污染问题。在多用户环境中，当特权系统组件未能对跨边界输入的资源路径进行有效审计时，极易导致数据越权交叉访问。基于此切入点，安全研究团队已成功挖掘出多个高危逻辑漏洞。

**02**

**AOSP 账户基本类型架构**

* **主用户 (Primary User):**设备初始化时创建的首个用户，拥有完整的系统控制权限，是系统中唯一可触发系统 OTA 升级的实体。
* **次用户 (Secondary User):**类似于系统的独立子账户，各个次用户相互隔离。次用户不具备设备管理权限，且无法接收和执行系统 OTA 升级。
* **访客用户 (Guest User):**一种临时性账户，当用户退出该环境后，系统将彻底且强制性地擦除此环境下的所有运行痕迹与暂存数据。
* **配置文件 (Profile):**主要用于企业 BYOD（自带设备）场景下的工作资料（Work Profile）与受限配置文件，可在单一用户内部实现轻量级的受控环境隔离。

**03**

**核心权限隔离机制与底层防护现状**

为了在底层和应用层彻底隔绝越权风险，Android系统建立了严密的沙箱与隔离防线：

* 权限独立授权：各个用户环境下的应用权限属于完全独立授予状态。在一个用户环境下为某应用授予的敏感权限，绝对不会影响或污染其他用户下的同名应用。
* 跨用户通信限制：Android 严格禁止任意的跨用户进程通信（IPC）。任何合法的跨账户数据流转必须显式依赖系统最高特权许可，普通三方应用默认被彻底沙箱化，无法通过常规手段进行跨边界越权访问。
* 路径与边界审计：由于多用户资源通常以通用资源标识符（URI）的形式在系统内部进行流转、定位与共享，当前的防护和漏洞挖掘重点高度聚焦于对 URI 校验边界的完整性审查。

在Android系统底层，URI的访问权限由 ContentProvider 统一提供接口和控制。当用户A的应用携带特定 URI 发起某个 Action 请求时，系统组件会通过调用链进入 queryContentProviders 方法来处理和校验该 URI 的访问权限。其核心安全校验点包括：

* 发起请求的userId与当前活跃的currentUserId 之间的安全一致性校验。
* 发起进程是否具备INTERACT\_ACROSS\_USERS或 INTERACT\_ACROSS\_USERS\_FULL的跨用户交互特权权限判断。

**AI辅助攻击面产出以及威胁模型建立**

**01**

**AI Log攻击面产出平台**

在开源且大规模的代码环境下，传统人工审计补丁和日志的效率极低。团队构建了 AI Log攻击面产出平台，通过智能化手段实现海量补丁的自动化过滤和高价值攻击面提取。其核心运作流程和模块设计如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRApWTjDON6HJ0Df6ibrMiacHA1HSa6GnLvuSpiaHwn1WDia49ExEXIooYjRZeEUrfV6NPzNMmqxnLzz2iaNQWRmaia2XraFdf9LvYMnk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDIBEzzvoXBmEj9b7ibCD4T5xSOpGddicRoXGibDHkqgicWoazg18rCPkPuyy5cFduianPYcIK6icZ7kkrLW8T01RNMdOttabYicOiabdc/640?wx_fmt=png&from=appmsg)

**1.1 平台架构与核心模块**

* **用户交互层：**用户通过指定特定的时间段、目标模块或期望的攻击效果等信息，向系统发起分析请求。
* **核心业务层：**包括Git解析引擎模块（负责目标Git仓库自动解析）、智能分析引擎模块（集成大语言模型LLM分类识别补丁特征）、项目管理与批处理引擎。
* **数据访问层：**依托数据库连接池管理基础数据，沉淀大模型筛选结果，对接人工验证。

**1.2 平台核心能力**

该平台能够从海量的 commit log 信息中快速定位与安全相关的补丁信息，精准筛选出最新的潜在攻击面。系统在接收命令后对 commit 信息进行安全判定，直接输出结构化报告，为后续的批量化扫描和漏洞挖掘注入精准的“弹药”。

**02**

**核心威胁模型建立**

**模型 01: 导出组件与 URI 注入威胁模型（组件边界安全模型）**

* 特权应用背景：携带 ACROSS\_USERS 特权权限的系统级应用或厂商预装 APK。
* 攻击向量：目标应用中存在导出的（Exported）Activity 或 Receiver 组件，且这些组件匹配了图片、音频等通用文件类型的 Intent Filter。
* 漏洞核心：导出的组件在接收外部传入的 userid@URI 输入时，其内部业务代码逻辑完全缺失了对 UserId 的有效权限检测，从而形成了“混淆代理”漏洞。
* 风险后果：允许恶意普通用户应用诱导系统特权进程跨越用户隔离边界，越权窃取、读取其他用户的敏感私有资源。

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRCaNuAcg7a0WZwb5pSdJzHt7vk8SGVkp9WmdLhQq7XibcZVEwVSiaBia1o3uuB1nUiclDRO5bdibMPqMHx9BjFBSLYHxicczbbeOlMYw/640?wx_fmt=png&from=appmsg)

**模型 02: 扩展服务与 API 重载注入威胁模型（API 接口越权访问模型）**

* 特权服务背景：系统中常驻内存且拥有 CROSS\_USER 权限的可扩展系统服务（如 TileService 等扩展 Service）。
* 攻击向量：三方应用通过这些系统服务的 API 重载（Override）接口，输入图片、视频或通用文件的 URI。
* 漏洞核心：在系统服务的接口底层实现层，未能对传入 URI 中的 UserId 与调用者自身的真实 UID 进行强制一致性校验。
* 风险后果：攻击者可完全绕过常规权限管控，利用高特权的系统服务读取其他用户（如主用户或企业空间）的私有应用数据。

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAGfIuPksuNCr3ZsjVV6yf6U7vkibM9fuJlKLOyJngWBK8ACHacd4Gh7Px6AQoRRPUuubIibuT0k1WEoOVecn0jqpR7A8pqGEr0o/640?wx_fmt=png&from=appmsg)

**批量化漏洞挖掘方法实践**

**01**

**批量漏洞挖掘流水线流程**

[ROM输入] ──> [Unpack拆解] ──> [Decompile反编译] ──> [可疑service/apk识别] ──> [Call Chain构建] ──> [威胁Rule Engine匹配] ──> [结果输出]

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDNqAQsrvyHBoSf7XknP2IlUicv75vHEsGMGxVH40cq6UY1R5a7ParaWSu3db9D3eTSFHNqu44P4mtYHyLt69W6shTkmB02ia1LY/640?wx_fmt=png&from=appmsg)

**技术演进：**随着大模型能力的引入，目前整个分析流程可通过 Decompile Dex + MCP (Model Context Protocol) + 大语言模型 的全新组合进行完全替换。通过大模型的语义理解替代传统的IR（中间表示）和调用链拓扑补全，显著提升了工程效率。

**02**

**典型实战案例解构**

**2.1 DeskClock（系统内置闹钟）跨用户越权漏洞（案例1）**

* **受影响模块：**com.android.deskclock（系统内置内置闹钟应用）
* **风险组件：**HandleSetAlarmApiCalls (状态为 Exported，允许外部调用)
* **漏洞成因：**在处理 SET\_ALARM 的 Intent 请求时，该系统应用通过 getAlertFromIntent 提取音频资源的 URI。由于业务层完全缺失对跨用户 userID 的合法性检查，攻击者可以向其注入指向其他用户目录的恶意 URI。
* **深度调用链：**

HandleSetAlarmApiCalls / HandleSetAlarm
  └── onCreate()
      └── handleSetAlarm()
          └── updateAlarmFromIntent()
              └── alarm.alert = getAlertFromIntent(intent, alarm.alert!!)
                  └── val alert = intent.getStringExtra(AlarmClock.EXTRA\_RINGTONE) (完全未检查 URI 设置过程)

* **漏洞利用与验证：**在非0（如普通次用户）的 userId环境下，发起 AlarmClock.ACTION\_SET\_ALARM的 Intent请求，并在参数中携带恶意构造的跨用户 URI：content://0@media/external/audio/media/xxx\_id。

* **攻击后果：**攻击者可以通过批量遍历音频文件的 \_id，跨越隔离边界，实现对管理用户（User 0）私有铃声、录音等敏感音频文件的任意读取。

**2.2 TileService 快捷设置扩展服务跨用户图片泄露漏洞（案例2）**

* **技术背景：**TileService 是 Android 7.0（API 24）引入的 Quick Settings 扩展服务，允许应用在系统快速设置面板中添加自定义图块以提供快捷功能。由于其特殊的系统级定位，该扩展服务天然自带 cross\_user 权限。
* **风险调用链：**触发重载的 onClick 事件时，外部应用可通过调用 getQsTile().updateTile() 进行图标（Icon）的动态设置和刷新。
* **底层漏洞成因：**当系统执行 updateTile() 动作时，底层的详细调用流转如下：

com.android.systemui.qs.tileimpl.QSTileImpl.handleRefreshState
  └── com.android.systemui.qs.external.CustomTile.handleUpdateState
      └── android.graphics.drawable.Icon.loadDrawable
          └── android.graphics.drawable.Icon.getUriInputStream
              └── android.content.ContentResolver.openInputStream

* **漏洞效果与Tips：**攻击者只需编写并安装一个没有任何额外敏感权限的普通应用程序，即可通过构造特定 URI 诱导系统服务，从而任意泄露多用户环境下的其他用户的私有图片。在确定了此调用链后，研究人员直接将调用链拓扑喂给大语言模型，即可自动化生成高稳定的漏洞验证 PoC。

**安全研究范式变革总结**

* **过去的研究范式：**在进行批量漏洞挖掘时，漏洞研究员往往需要将 80% 的精力 耗费在编写静态分析引擎、调试 IR（中间表示）、补全复杂的调用链拓扑等底层的“脏活累活”上，最终只有 20% 的精力 能够真正投入到对核心漏洞业务逻辑的审计和精细化分析中。
* **现在的研究范式：**通过“大模型语义理解（承担底层工程实现） + 人工漏洞威胁模型输入（通过 Skill / Prompt 进行专家级控制）”的黄金组合，攻防的杠杆发生了彻底改变。研究人员能够用更少的精力、更快的速度拿到成倍的安全成果。
* **未来的研究范式：**安全研究将向极致的轻量化和智能化演进。安全研究员可能仅仅需要依赖顶尖的大模型底座能力，通过编写最简单、最高效的 Prompt 或定制化 Skill 去启发 AI 的“安全专家思维”，即可在极短的时间内完成以往需要一整个专家团队耗时数月才能覆盖的百万行级别代码审计规模。

-END-

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibiaMN9FTPWAS1TQMIhBskub3h6JDA6eRQVElKiccYfkLq8UNjNRSx9XVJBy8ucZGfgicrRq04dCeDCA/0?wx_fmt=png)

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