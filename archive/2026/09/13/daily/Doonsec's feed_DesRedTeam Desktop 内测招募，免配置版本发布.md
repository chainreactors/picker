---
title: DesRedTeam Desktop 内测招募，免配置版本发布
url: https://mp.weixin.qq.com/s/_VgFKksZRzDR8soICkLgmQ
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:19:12.884869
---

# DesRedTeam Desktop 内测招募，免配置版本发布

# DesRedTeam Desktop 内测招募，免配置版本发布

赤弋安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于教红队的Des
，作者Des

![](https://wx.qlogo.cn/mmhead/gWicbXPiajJnibib89sJhGaEHGqA0RF5os7gNWrOEHTXvibJj2oLOz1Hib2uiaiadK0XFrXbaBibZz0NyQUE/0)

**教红队的Des**
.

分享web安全、红蓝攻防、应急响应、攻防打点案例相关内容，定期通知和直播公开课，同步课件资料靶场环境等，加我 wechat：desredteam

各位师傅，大家好！

DesRedTeam Desktop正式面向企业安全团队定向开放。本产品基于 DSH Desktop 二次开发，是一款综合性网络安全检测与运维工具，旨在快速资产发现、识别、检测，构建基础资产信息库，协助甲方安全团队或安全运维人员有效侦察和检索资产，发现存在的薄弱点和攻击面。本次内测采用授权准入与限量发放机制，仅面向具备合法授权场景的企业安全团队开放，首轮内测名额 100 个，额满即止，本文承诺该平台不收取任何费用，但严格要求内测用户在授权范围内展开有限的渗透测试行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjQIFfaib13ExNE5N5WDfIOBTSZHNXfbUXw4ZyUBCwD8aEK7o372CauSiacSj7Yku76vI2zplU8ibNxNLMD7pkPU8WqWMZLkCibIia4Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjTU4GseGfB9Src3WWWCBibjIzflhKINE46sahMIMw4NXpNYnjGDOmhZph7ajqNmibLRfWUoRg9xC3djGPict7CBvHmwOxP8wTDicZc/640?wx_fmt=png&from=appmsg)

## 01产品定位

DesRedTeam Desktop 将一次完整授权评估所需的作业环节收敛至同一工作终端。在传统作业模式下，信息收集、资产测绘、渗透链路记录、资产台账、漏洞台账与项目管理分散于多个独立工具，数据在工具之间反复搬运与转录，作业上下文难以持续。本产品将上述环节统一承载，使数据在单一边界内闭环流转。

以前用过老版本的同学都知道，源码编译dsh、drt确实头痛，还有各种小bug，后续4.1基于插件发布，依然有用户反馈跟dsh版本不对齐导致平台兼容出现小问题。

本产品使用流程极其简单，解压双击DesRedTeam Desktop.exe即可运行，配置key后即可开展授权渗透测试，内置 Git 开源 skills 与 Des 师傅对外免费提供的信息收集 skills，采用内存加密与准入校验机制：仅通过准入的授权用户方可获取，即便被恶意传播，skills 本体仍无法解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjQ3A6yH5fukO1rjMVY1aic7nfzYc0sicVLYnHkPZMaEeqU9NITRCNicIhytG4RS3r24ytKNibcgeYFtZ8lkOzbtyM1ib2iadckG8JSAM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjRNu9hteJX7tN17AOfZr0S6CxDosdYf3jbnrc0vicciaHtoYyVdsYftsPToslsnOXRaicxtqCvct4klwJr7icF3u2vHVT0elS4BcHk/640?wx_fmt=png&from=appmsg)

Desktop 版本自带 Electron 桌面界面，基于 DSH Desktop 二次开发；同时保留 Web 端形态，本机 8080 端口可直接访问，两种形态共用同一套数据与作业上下文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjRNGgjxZ6LTTAou0wm0iaPJk5ZfIZw5hbcGd8GHA9Vds2oFuCWNQsceyq47JhgNggKFGDFdbO5SLh7oYU7mPtbribSfxylPFIZcc/640?wx_fmt=png&from=appmsg)

## 02准入与合规

本产品采用授权准入制，仅向已完成资格确认的用户发放激活凭据。准入流程由三道强制环节构成，任一环节未完成均无法进入产品。

### 激活码准入

首次启动需填写内测激活码完成准入校验。激活码一码一人，与内测资格绑定，不可转让、不可共享、不可二次分发。内测期间不收取任何费用，激活码本身不具备商业价值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjSzreInjXR6KDnwrrhaRZPvEEvaicZGciaOraXJRfB1RPVWhiaofiaFSia9xHPiaeibLuibibDcyYFvwxFlibazJoPDk0xS6v5flMBxpjs6k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjSTA3wKxRsqokqwCtpbhTUuyJBXUBmWgGeicwqMBtficp13OYGiavQ0AXZXv0ia2NibhDEEcuBY67akTQPnrxaVWsWT88rKGNicOArPA/640?wx_fmt=png&from=appmsg)

### 源 IP 存档

启动过程仅记录源 IP 作为存档信息，用于配合相关主管部门依职权查阅。该记录不用于商业用途、不对外提供、不作行为画像，仅在合法合规的调阅场景下按流程配合。

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjSBHvu5eaz232aAGFbQ52k6uJdoWZ6FkxqW5Udiadk1LozjcEibAMfbVpALuXHDe4iauHuog5b1yR4JJZTd5acyicFyKQ1xIZGmKTg/640?wx_fmt=png&from=appmsg)

### 免责条款强制确认

使用前必须完整阅读并同意免责条款，未同意条款无法进入产品。该项为强制校验环节，不可跳过。

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjRokAL2KsiayOAkPx1honxI0Tf22BXeX2JY3xkaibsregyl4Qlicq4FR26B333ntX15HLFARunp1vy8auIyz32HyMZUjX6TGGxdb0/640?wx_fmt=png&from=appmsg)

部署边界

为简化使用，内测版本未设置后台认证。因此请勿将本产品搭建于局域网或公网场景，仅限在单机、受控、可信环境中使用。产品内集成的 GSL C2 属于能力不可控的渗透工具，只对具备授权的企业客户提供，仅限用于企业内部资产测试与内部红队钓鱼演练。

## 03功能模块

内测版本能力覆盖信息收集、资产测绘、渗透链路、资产管理、漏洞视察与项目管理六大模块，全部功能在同一界面内完成，无需在多个工具之间切换。

| 模块 | 职责 | 作业价值 |
| --- | --- | --- |
| 信息收集 | 目标画像与范围结构化 | 任务书一次生成，范围清晰 |
| 资产测绘 | 检索与结果导出 | 检索筛选导出一体化 |
| 渗透链路 | 链路、资产、漏洞关联展示 | 链路即证据、即交付物 |
| 资产管理 | 域名 / IP / 端口 / 服务台账 | 一项目一资产库 |
| 漏洞视察 | 漏洞定性、分级与复现步骤 | 无复现步骤不计入台账 |
| 项目管理 | 项目上下文隔离 | 跨项目不串数据 |

### 信息收集

在信息收集面板输入目标与收集模式，系统生成结构化任务书，复制后粘贴进对话页回车即可执行。任务书包含目标边界、收集范围与角色约束，确保每一次收集都在声明的范围内运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjSklualBQwWR66beUwcRsmBlXYYV5ibVYoP6XicAau4wl4bZ2cQRkGPAgL24p209uXmxNloN0TiaAcgzvKZuNQ48hFQMzto67HlKs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjR6ZeMcOGROJfhvocSbBYGWN8WCIomNaffGw1LUQI4YNm3KfkOelV4uwJZ976mLXsRFfG52h67eMEOqoiaTF5Zw2P7icZZF0EJmo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjS3iaQdlUV60opwaFVBB7C9J0QSdKibS1YYefkPhVibYH3yUxTFWcDjkicS7QI6mpumZlmReTSWEhJNYQK8A6JXNtGj1mZrBN7j3iao/640?wx_fmt=png&from=appmsg)

### 资产测绘

内置资产测绘面板，输入正确的查询语法即可完成检索，并支持将结果集直接导出为结构化数据。检索、筛选、导出在同一工作区内完成，无需手工转录。

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjQtMic5UUlvOicQakhTMuvIWyVelxkC0UH0US5E5Bm7qyEmKFOI7xvCY02fAq23clrfPKv7j2uDpP476icyQm8ictFHw0nia0ZbBTB4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjR77R5lLS8ic1UptIjrubpcicDlKKghmutLgZciaKzYBtd4dTKtqcYUlxDXic4yjxTSv3mOAVOxaTaplmmPvpLAHIl959MChn4ezSg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjTVIV5Ls2RWMEwFDFFDpKjOT5BGTd1KWd7aIU8ds9Cia8FiaqeQbmu38nH45yOSzbj5u34eVjTPU53Cgjbs3oJicFNtGAeEcTzNgs/640?wx_fmt=png&from=appmsg)

### 画板模式

独立展示渗透测试链路、资产与漏洞三类节点及其关联关系。一次评估的攻击路径以图形方式实时呈现，链路即证据、即交付物，可直接用于内部复盘与客户汇报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjT6oWJ66wshEicwicszYCIyoibGghBjYINJ2GQP5mZFT7xdtCKe18zWF0u6BHiazxkVESbSbfnZmibmxPKmnnZZXGIwRNQjWFCScmpI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjQZA2FhFVDIrgPEwbmCwktQo00p09mtSmfK3WzECr1NthE1MQ8CSwsED8B1UnlvZZj0g2abpjiaveprMxUUsYKtOJm6ZhHuHPdM/640?wx_fmt=png&from=appmsg)

### 资产管理 漏洞视察 项目管理

三个独立管理界面分别承载资产台账、漏洞台账与项目上下文。资产、漏洞、项目三者之间的引用关系可追溯：每一条漏洞均可回溯至其影响的资产，每次资产变更均可回溯至所属项目。

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjQJTGWqwXPJGvfHEpG0RodBlmWibH6OOPicqWuXBeiblbHS10eC6EFyefq5Iibbz9e9AgKiaJzMQW12UOV6XVN8M04X8m9WfM0DObWU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjS6aPT0faHVs5B3RunWAQoYLH7JcI0DWib93MfhDYWAVyQHTl80G8zNk2MAVN5oictag7bjOpVtQkdm7rNuwlVa1tBiaasuIoe9TU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjRvZ8oWmCbbOcRarsAYeathyITe8FHAmibT7ku5ZSvKC2n9rLNuHPRhWsibC9yPePns7dLk5aAWp3O487PpjmZbPsBib3VG5LFkibY/640?wx_fmt=png&from=appmsg)

## 04内测资格

首轮内测采用限量定向发放方式。名额有限，按提交顺序审核，仅限前 100 名，额满即止，本轮不再增补。

名额说明

首轮内测共 100 个名额。审核按提交时间顺序进行，额满即停止受理，本轮不再增补名额，亦不设候补通道。

| 项目 | 规则 |
| --- | --- |
| 名额数量 | 仅限前 100 名 按提交时间排序 |
| 朋友圈要求 | 转发本文至朋友圈 + 点赞满 6 个 |
| 保留时长 | 不少于 24 小时，不得设置分组可见 |
| 提交方式 | 填写问卷星申请表单，为唯一提交入口 |
| 必填项 | 行业背景 / 学生身份 · 微信号 · 使用目的 · 转发集赞截图 |
| 审核周期 | 1 至 3 个工作日 |
| 内测费用 | 免费激活码不可转让或售卖 |
| 本轮增补 | 额满即止，本轮不再增补 |

## 05申领流程

内测资格申领共两步：完成朋友圈转发后，通过问卷星表单提交申请。

https://v.wjx.cn/vm/P5SXtk9.aspx

表单为唯一提交入口，不接受公众号后台留言、私信或其他形式提交。

STEP 1将本文转发至个人朋友圈，集赞满 6 个，转发内容保留不少于 24 小时，不得设置分组可见、不得仅自己可见。随后截图留存，截图需完整包含朋友圈正文、点赞人头像区域与发布时间，请勿遮挡或后期合成。

STEP 2填写问卷星申请表单并提交。表单为内测资格的唯一受理通道，请如实填写所需信息，信息不实或与截图不符者不予通过。

### 提交入口

问卷星申请表单

提交链接与二维码：[ 待补充 · 问卷星链接 ]
请通过公众号后台回复关键词「内测」获取最新表单入口，或直接使用本文公布的表单链接与二维码提交。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6LUhXwA4EjTicO2ibUhVmzEBLFQ4sEOPiaKGpLSGOMbicMeodvibhepib4G7pS0d7tF2pzJ7LuWicHmPJkmINvt586KibUHrMialb6oPyALhXZz3GRsM/640?wx_fmt=png&from=appmsg)

### 表单填写项

| 填写项 | 要求 |
| --- | --- |
| 行业背景 / 学生身份 | 在职人员填写所属行业与岗位方向（甲方安全团队 / 乙方安服 / 厂商 / 其他）；在校学生填写学校与专业，并注明学生身份 |
| 微信号 | 填写可被检索添加的微信号，用于内测资格核对与激活码发放 |
| 使用目的 | 1 至 3 句说明使用场景与预期用途，须为合法授权场景 |
| 转发集赞截图 | 上传朋友圈转发截图，须清晰体现正文、点赞数与发布时间，点赞不少于 6 个 |

上述四项均为必填项，缺项视为无效提交。表单可重复提交，以最终一次提交为准；仅限提交一次有效申请，同一微信号重复申领不占用额外名额。

### 审核维度

审核维度为三项：提交信息完整性与真实性、行业背景与使用目的的合法授权性、提交时间顺序。三项均通过方可获得内测资格。

### 不予通过的情形

转发截图缺失点赞或发布时间、行业背景与使用目的无法说明合法授权来源、微信号不可检索、同一账号重复提交、将激活码转售或公开分发。触发上述任一情形，申领资格作废，名额顺延给后续申请人。

## 06内测须知

获得内测资格的用户，请确认已知悉以下事项。

· 内测版本为受控试用版本：功能与界面会随反馈迭代，不承诺生产环境下的稳定性与可用性。

· 激活码一人一码：不得转让、出售、公开分发或用于任何形式的二次分发。

· 反馈是内测义务的一部分：请在内测期内提交使用问题、误报与改进建议，这是本轮内测的核心目的。

· 提交信息须真实有效：微信号须可被检索添加，行业背景与使用目的须与实际一致，信息不实或与截图不符者不予通过。

· 使用范围严格受限：仅可用于已取得书面授权的资产与场景，禁止用于任何未授权目标。

· 不提供商用授权：内测版本不构成任何商业授权，商业使用需另行取得书面许可。

## 07后续安排

首轮内测结束后，我们将根据反馈收敛问题、补齐能力，再评估后续开放的规模与形式。未能进入本轮的用户，可关注公众号，后续开放通知将第一时间发布。

内测期间不收取任何费用。内测版本不构成任何形式的商业授权，亦不承诺任何服务等级。

感兴趣的师傅们可以进内测咨询群了解如何领取

![](https://mmbiz.qpic.cn/mmbiz_png/6LUhXwA4EjQpon00ftgEoaWmsqSpICJLHZ4vMKY2mLP6Cw6r7BwIGkcDlnlanuxrkcMksCmicwhf8yPtViccia3qJmmzdLdlP3dUsIlN6sAHyM/640?wx_fmt=png&from=appmsg)

## 08免责声明与使用许可

免责声明 & 使用许可

一、本工具禁止进行未授权商业用途，禁止二次开发后进行未授权商业用途。

二、本工具仅面向合法授权的企业安全建设行为。在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。

三、如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任...