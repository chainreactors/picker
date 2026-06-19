---
title: FIFA世界杯流媒体后台被曝高危漏洞：公开注册账号即可访问核心直播配置
url: https://mp.weixin.qq.com/s/C-g4nMzVf2INSkT6BpJJhA
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:52.503380
---

# FIFA世界杯流媒体后台被曝高危漏洞：公开注册账号即可访问核心直播配置

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQq6jtSct9QpeBzQT4MAjzs18NQrXYndfZ4zwV745LoCQBru4oNCFdrib4meRia4EofEOFG9SfUia10F36IpaPibBfJKQaMyMeXZc60/0?wx_fmt=jpeg)

# FIFA世界杯流媒体后台被曝高危漏洞：公开注册账号即可访问核心直播配置

原创

bobdahacker
bobdahacker

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

就在 2026 年 FIFA 世界杯激战正酣进行之际，安全研究者 BobDaHacker 发布了一篇关于 FIFA 内部系统授权缺陷的长文。文章标题直指事件核心，只需要一张身份证，理论上就可能影响整个 FIFA 世界杯直播链路。

这个标题听起来非常夸张，但报告披露的技术路径并不复杂。研究者并没有使用复杂的 0day，也没有依赖高难度的漏洞利用链，而是从一个公开的 FIFA 经纪人注册入口开始，通过正常注册流程进入 FIFA 的 Microsoft Entra 租户，随后发现多个内部平台只在前端做了角色拦截，后端 API 并没有严格执行服务端授权。

更严重的是，这个授权缺陷并没有停留在普通后台数据层面。根据原始报告，研究者最终能够访问 FIFA Football Data Platform 的 Streaming Management 面板，看到世界杯赛事的流媒体配置、RTMP 推流入口、预览流地址、输出清单以及部分控制按钮。由此可见，这不是一个简单的「后台可见」问题，而是一个可能触及全球赛事直播信号链的高危授权漏洞。

这也是这起事件真正值得关注的地方。它暴露的不是某个单点系统缺陷，而是大型组织在统一身份、外部注册、内部平台和生产级流媒体基础设施之间，权限边界被错误打通后可能产生的连锁风险。

## 1. 漏洞起点，公开的 FIFA 经纪人注册平台

整条攻击链的入口，是 FIFA Agent Platform。这个平台面向足球经纪人开放，用户提交身份证照片、完成邮箱验证后，即可注册账号。按照正常业务理解，这类账号应当只拥有与经纪人业务相关的有限权限，不应该影响 FIFA 内部赛事数据平台或转播系统。

报告中提到，研究者前两次注册都失败了，原因是身份证照片光线不符合要求。这个细节本身并不重要，但从安全视角看，它形成了一种反差，身份材料审核流程看起来较为严格，但后续系统之间的权限隔离却没有达到同等严谨程度。

![01-registration-failed](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQop4ZG0KVj7xFBq0ofOBaQS91Ku818nP5PLcnpjm6Ck2cDnqOXnOdoibg7h6QB9DkxB71Kjzp91qNicWIwcbZL36TH7NQic8QbhaM/640?wx_fmt=png&from=appmsg)

01-registration-failed

*FIFA Agent Platform 注册流程中，身份证照片校验失败的提示页面。*

第三次注册成功后，研究者收到了 FIFA Agent Platform 的确认邮件。至此，他拥有了一个通过公开入口注册而来的 FIFA 相关账号。

![02-fap-confirmation](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrwcdMicWhMicmFqDCo6eMraUdm7CtzzFEGrxBBceH9O6AGeiaCZWzX5fn2TmE2y2ck2A8PQB0tLqibI36Ky5S6uBv01alZvcCh7ro/640?wx_fmt=png&from=appmsg)

02-fap-confirmation

*FIFA Agent Platform 注册成功后的确认邮件，标题中出现 FAP CONFIRMATION。*

关键问题出现在账号归属上。注册成功后，该账号被加入 FIFA 的 Microsoft Entra 租户。Microsoft Entra 的前身是 Azure AD，是企业常用的统一身份系统，用于管理账号、组织归属、登录认证和角色声明。

统一身份系统本身并没有问题，大型组织让外部合作方、供应商、临时人员或业务用户进入同一个身份体系，也是常见架构选择。真正危险的是，系统把「通过身份认证」和「拥有内部资源访问权限」混在了一起。

身份认证解决的是「这个人是谁」。

授权控制解决的是「这个人能做什么」。

这两个问题一旦被混淆，公开注册入口就可能变成内部系统的低成本入口。

## 2. 前端拒绝访问，后端却没有同步拦截

注册完成后，研究者访问了 `fdp.fifa.org`，也就是 FIFA Football Data Platform。页面最初给出的反馈是拒绝访问，提示该账号没有分配任何 FIFA Football Data Platform 角色。

从用户体验上看，这似乎是一次正常的权限拦截。账号可以登录，但没有角色，因此不能进入平台。

然而，BobDaHacker 进一步分析后发现，这个拒绝访问主要发生在前端。前端应用检查 JWT 中的角色信息，识别到该账号处于 `NO_ROLES` 状态，于是渲染出一个访问拒绝页面。问题在于，后端 API 并没有同步验证这个账号是否具备访问对应资源的角色。

这类问题在 Web 安全中非常典型。前端可以隐藏菜单、隐藏按钮、展示拒绝页面，也可以让界面看起来像一套完整的权限系统。但只要后端没有在每一次请求中验证用户身份、角色、资源范围和操作权限，前端拦截就只是一层界面逻辑，并不能构成真正的安全边界。

也就是说，页面告诉用户不能访问，但 API 仍然返回数据。

研究者绕过前端判断后，进入了 Streaming Management 面板。按照报告描述，这不是测试环境，不是样例数据，也不是废弃系统，而是 FIFA 世界杯相关的生产流媒体管理面板。

![03-streaming-panel-overview](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqb2XYBzKcnLyXr26kb7FIaZtLCSUjL9sNYY9icmq6UzgeOsDCONz3E1u0y3iaiadsFEwYNHiaZiciaNG6WEUibM8VCBEMshPpsiaUeerg/640?wx_fmt=png&from=appmsg)

03-streaming-panel-overview

*Streaming Management 面板中展示的世界杯赛事流媒体管理列表。*

从这一刻开始，事件性质发生了变化。它不再只是一个普通的客户端授权绕过问题，而是开始触及世界杯直播系统的核心链路。

## 3. Streaming Management 面板暴露了什么

世界杯直播系统和普通 Web 系统不同。普通后台发生越权，影响通常集中在数据泄露、业务操作或管理功能滥用。但赛事直播系统连接的是摄像机信号、转播基础设施、广播合作伙伴和最终观众，任何异常操作都有可能被快速放大。

报告显示，Streaming Management 面板中列出了世界杯赛事及其多个摄像机角度。单场比赛下包含 PGM 主节目流、战术视角、普通摄像机、高位后方视角等多个 feed。每个 feed 旁边又关联了不同类型的地址和配置，包括 RTMP ingest URL、preview manifest 和 output URL。

![04-streaming-panel-expanded](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqiaXwhAbGm7NhAF5ucic6IPE53TLIiaIFNIh1G7Q4B56HU13Wo7HIjhJx78tuyiaoxicNjtwEsbCg5dx0uQrtI1ibq9o84ZZYjqSeh4/640?wx_fmt=png&from=appmsg)

04-streaming-panel-expanded

*单场比赛展开后的流媒体配置，包含多个摄像机角度和对应流地址。*

RTMP ingest URL 可以理解为摄像机或上游系统把画面推入转播基础设施的入口。preview manifest 则用于预览对应画面，output URL 通常对应对外分发或提供给转播合作方的 HLS 清单。

这些内容出现在未经服务端角色校验的后台里，风险已经非常高。更进一步，报告中还提到，同一场比赛的多个机位可能共享 stream key。stream key 如果泄露，攻击者理论上就具备向对应入口推送视频流的条件。研究者明确表示没有向任何 RTMP 端点推流，也没有测试替换信号，但仅从暴露内容看，风险边界已经非常清晰。

为了确认预览流是否有效，研究者将一个 preview manifest 复制到 VLC 中打开。报告显示，VLC 能够播放实时比赛画面，且研究者随后立即关闭播放器，没有继续扩大测试。

![05-vlc-live-feed](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoo0fSqEP4G6l4k3WoRiaBYdtEnf5xxNfB8pxZ0ghkPsMhqiadD4ZMicpsdYR4tWLUIqg5v0D07dIXXI6FHyq3l7LibKLnFjSLNkicQ/640?wx_fmt=jpeg&from=appmsg)

05-vlc-live-feed

*VLC 中打开的实时预览流，画面显示为比赛战术视角。*

这个验证动作说明，暴露的并不是静态配置或历史数据，而是实际可用的实时预览链路。对于直播系统而言，这已经足以证明风险存在。

更敏感的是，面板中不只是存在读取信息，还出现了开始、停止、调度等控制能力。

![06-stream-control](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQq8gx0y4J7XibpGx9BQf7kWricWWUNcfXx7NLU4TBRgic3L5dz2uZTMtuiaozMHQfOqYcukWR0F6z5aFuVS6WlLNw4rmbZKediaCbTI/640?wx_fmt=png&from=appmsg)

06-stream-control

*流媒体控制确认弹窗，面板中存在停止流等控制动作。*

如果攻击者拥有同样访问能力，并且进一步操作控制按钮，理论上可能中断某个直播流。如果攻击者结合暴露的 RTMP 地址和 stream key 推送自定义内容，则可能造成更严重的信号替换风险。原报告用 Rickroll 或 Subway Surfers 画面作为类比，表达的是同一个问题，一条面向全球转播的生产链路，差点被一个无角色账号触及。

需要强调的是，研究者没有执行破坏性验证，也没有推送任何内容。风险判断来自已经暴露的生产配置、可播放的实时预览流以及面板中存在的控制入口。

## 4. FDP 其他模块和赛事数据系统同样暴露

Streaming Management 面板并不是唯一暴露的部分。研究者的 `NO_ROLES` 账号还能够访问 FIFA Football Data Platform 的其他模块，包括竞赛、比赛、球队、工具、Exchange Platform、分析仪表盘、评论员信息系统、FIFA AI Pro 和 Admin 等入口。

![07-fdp-full-nav](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqWdR8Q2fChSsvSsKe8a7s5BSqEosu9mRUPldc4ibDESuRaiaiaW8KibEg7KPZS2ZuhMlDxatS2urPdt07jJ0gRP8uqcs08y7HJ7Aw/640?wx_fmt=jpeg&from=appmsg)

07-fdp-full-nav

*FDP 导航栏中展示的多个内部功能模块。*

这类大型平台常见的问题在于，多个业务模块共享同一套身份体系、前端路由和 API 后端。一旦最外层授权边界失效，风险就不会局限在某一个页面，而可能横向扩展到整个平台。

其中，live match dashboard 页面包含嵌入式视频、实时事件时间线、比赛官员信息等内容。这些信息看似只是赛事数据，但对于转播和解说来说非常重要。现代体育直播并不只是摄像机画面的实时传输，还依赖大量结构化数据来支撑比分、统计、战术分析、解说提示和屏幕包装。

![08-fdp-match-overview](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQo5CmS0HklmibX7dQ9icSN09W6kAI5ftFgJNXZBwsCZUGH9cD5rTTrLiaSgf8pOXm3ZEagr4u0z8ZqHKp6yptUZwZIpcibRg4L8nSE/640?wx_fmt=jpeg&from=appmsg)

08-fdp-match-overview

*FDP 比赛总览页面，包含实时视频、事件时间线和裁判信息。*

高级分析页面中还包含控球、进攻、跑动、恢复球权等实时数据。这类数据可能用于导播、评论员、技术分析团队，也可能影响电视画面中展示的统计信息。

![09-advanced-analytics](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQoxDtHY9B13eCqtRt7jfweGPwNwW9YD2veB0MYxyyZJzROJxiaS8M7sUUmX39J87o1s2UIWcnZm1J85PokHPsHINEuibzswbN0EY/640?wx_fmt=png&from=appmsg)

09-advanced-analytics

*高级分析页面，包含控球、进攻、跑动等实时数据。*

更值得关注的是，Management tab 中还存在写操作。原报告展示了 Update Live Stats 弹窗，其中包含富文本编辑、比赛时间、比分字段以及发布按钮。另一个管理页面中还出现了出勤率、控球率、赛后统计、球队注册统计、分析完成状态、比分与统计、开球时间调整、表现数据、战术阵容发送、事件入口详情等功能按钮。

![10-update-live-stats](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQpggTV3gXG1fgcFia1lLlrAbyzT9XPgb9lPPTg9ibCGS7A86Yk5HJGAJchIic7CWTlEibk5jL5uU2Ngpe1tgOprCsUucpdf3icicIMYc/640?wx_fmt=png&from=appmsg)

10-update-live-stats

*Update Live Stats 弹窗，包含编辑和发布动作。*

![11-management-buttons](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQpCgMysYFicibtL9PmqqiaeSdic5anIod2TudvzuMCXe8DaxBAAOB0G2ZLZYcZUumfX11z9j02QfXO85BzHFiaSBjImViarzpS4atcRk/640?wx_fmt=png&from=appmsg)

11-management-buttons

*比赛管理模块中的操作按钮，涉及统计、开球时间、阵容和数据发布等动作。*

画面劫持当然具有更强的视觉冲击力，但赛事数据被修改同样危险。比分、统计、阵容、开球时间、事件时间线和解说资料不会像直播画面被替换那样瞬间引爆舆论，但它们会影响赛事被记录、被解读和被传播的方式。

体育直播并不只是镜头拍到了什么，也包括系统如何定义刚刚发生了什么。

## 5. 评论员信息系统与内部文件暴露

除了 FDP，研究者还访问到了 `cis.fifa.org`，即 Commentator Information System。该系统面向转播评论员，提供实时比赛视图、比分、阵型、球员位置、技术统计、换人时间线以及编辑笔记等信息。

![12-cis-dashboard](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQpccriaL1DWUAXNGvdXmmCGGYj6MJOb3xNpWXF3u4V32BNkcgTokd6ichwm0A2DTKPXtHwrjYOXQLje8S2ImoMB5ic4ObQw2HBGpc/640?wx_fmt=png&from=appmsg)

12-cis-dashboard

*CIS 仪表盘，展示世界杯赛事、比分和赛程信息。*

![13-cis-live-match](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrj2mBEibORXUMCn4sv4H2Vfs8oo6vWTlxy2cwkVJSmdHry74X8P1unYDtrTibHVuYPlF8LUy2EficsXum64adRXric2uOyqE9wIsg/640?wx_fmt=jpeg&from=appmsg)

13-cis-live-match

*CIS 实时比赛视图，包含阵型、球员位置、统计和替补时间线。*

电视解说中的很多背景信息，并不完全来自评论员记忆，而是来自这类赛事信息系统。球员年龄、历史纪录、国家队数据、战术布置、替补时间线和赛前资料包，都可能由系统集中提供。

因此，CIS 暴露并不是简单的信息查看问题。它涉及赛事传播链中的事实来源。如果这类系统存在未授权访问甚至可写操作，影响范围可能从后台数据延伸到电视解说、图文包装和公众认知。

原始报告还提到一个额外暴露点，一个 Azure Function App 返回了 23 个内部 FIFA 文件的元数据和 Azure Blob Storage 直接下载链接。报告中列举的文件类型包括转会报告、收入对比、董事会级别代表性数据、裁判和教练统计等。这部分虽然与直播控制链路不同，但进一步说明同一类授权问题可能不仅影响赛事转播平台，也影响内部数据资产。

从安全视角看，这类暴露通常意味着问题不只是某一个前端页面写错了判断，而是多个服务对「已认证用户」产生了过度信任。

## 6. 披露过程暴露了另一类基础设施问题

这起事件中，漏洞本身已经足够严重，但披露过程同样值得关注。研究者发现问题时，世界杯比赛正在进行，RTMP 地址可见，预览流可播放，stream key 暴露在后台中。在这种情况下，快速联系到正确的安全响应团队非常关键。

然而，报告显示 FIFA 没有公开 bug bounty 项目，没有清晰的 `security.txt`，也没有易于定位的安全披露入口。研究者先向多个 FIFA 邮箱发送...