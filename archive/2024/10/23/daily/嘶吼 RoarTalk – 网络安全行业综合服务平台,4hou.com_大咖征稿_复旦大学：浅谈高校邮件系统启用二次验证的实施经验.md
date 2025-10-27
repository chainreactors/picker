---
title: 大咖征稿|复旦大学：浅谈高校邮件系统启用二次验证的实施经验
url: https://www.4hou.com/posts/42k0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-23
fetch_date: 2025-10-06T18:47:36.831864
---

# 大咖征稿|复旦大学：浅谈高校邮件系统启用二次验证的实施经验

大咖征稿|复旦大学：浅谈高校邮件系统启用二次验证的实施经验 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 大咖征稿|复旦大学：浅谈高校邮件系统启用二次验证的实施经验

CACTER
[行业](https://www.4hou.com/category/industry)
2024-10-22 14:30:22

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)44435

收藏

导语：在降低账号密码被盗的影响方面，开启二次验证登录是有效的办法。

邮箱被盗号并向外发送垃圾钓鱼邮件情况频发，不仅会导致收件人上当受骗，更会影响发信IP的可用度和发信域的声誉，影响域内用户的正常外发。

除了加强对账号异常登录、收发的行为的监控，以及加强对入信中钓鱼邮件的识别，有两个方向的努力也非常重要，一是提高用户的网络安全意识，二是降低账号被盗的概率。
在降低账号密码被盗的影响方面，开启二次验证登录是有效的办法。

**一、高校邮件系统概述**

**1.高校邮箱的主要用途**

高校的电子邮件系统，用户主要为教师和学生，用户量大，日常收发量大。对于教职工而言，除日常工作交流外，最重要的用途便是海内外学术交流和校务、课务通知等。对于学生而言，主要包括接收通知、提交作业、学术交流、找工作等。

**2.高校邮箱用户的现状**

**用户类型**：根据相关要求，高校需加强邮箱账号管理，建立和完善电子邮件账号注销机制，但在一定时间段内，邮件系统中可能同时存在离校学生/员工、在校学生、在校教职工的个人邮箱和院系部处工作邮箱。各高校均不同程度存在长期无人使用或管理的“僵尸账号”。存在被他人利用的网络安全风险。

**使用方式**：在使用方式上，日常以各种第三方邮箱客户端为主的用户不在少数。还存在使用自动转发、日常很少或几乎不登录的用户。

**安全意识**：师生用户网络安全意识参差不齐、警惕性不足，不少用户喜欢使用常见的密码组合或与身份证号、生日、姓名拼音等个人信息相关的字符串。面对各类钓鱼邮件，也时有师生用户“中招”。

**二、实施登录二次验证的流程**

**1.实施前准备工作**

**（1）系统对接与测试**

以Coremail XT6邮件系统为例，其二次验证目前支持Coremail论客App、第三方OTP、手机短信、备用邮箱、微信小程序等多种方式，需根据自身系统情况，对短信平台等进行对接测试，确保相关验证方式能正常运行。

**（2）二次验证流程与信任逻辑的理解**

邮件系统管理员和信息化部门（IT部门）工作人员需要熟悉二次验证绑定设置、使用、解绑全部流程，并进行试用，了解常见问题。
二次验证基本流程：用户登录——校验密码——二次验证请求下发——用户反馈或确认——校验通过——登录到邮箱界面。 建议邮件系统服务商与学校邮件系统管理员进行深入沟通，理清二次验证机制及各种验证方式的信任逻辑，对二次验证中可能存在的风险点或问题点形成更清晰的认识，也有助于出现问题后的排查研判。

例如：

①【豁免时间】

当用户已经绑定/解绑/修改绑定一次后，系统默认会提供15分钟豁免时间。在15分钟内用户再次绑定/解绑/修改绑定前，都不需要先二次验证。
②【Coremail论客App】

当更换设备时，新设备上的App会要求二次验证，这是由于绑定方式与设备相关，原信任设备不可用时，只能通过后台解绑，再绑定新设备。
③【忘记密码】

短息找回密码方式，如果仅在“个人信息”中维护过手机号，此方式不可用，需要在“二次验证”中绑定过手机号，或者在“高级功能”中设置过“绑定手机”；备用邮箱找回密码方式，则在“个人信息”中维护过备用邮箱即可用。
④【客户端专用密码】

如果对组织仅强制启用二次验证，组织内的账号仅在通过web页面登录时会强制跳转到配置二次验证页面。如果不绑定二次验证，用户依然可以使用原账号密码登录客户端协议，通过SMTP发送邮件（已经被盗的账号，依然可以通过客户端协议发送邮件）。因此，组织启用二次验证后，建议在密码策略-高级设置中，同时勾选强制使用客户端专用密码的设置项。

**（3）用户手册的编制**

 面向用户，编写详细的步骤指南，包括绑定设置、使用、换绑或解绑等全流程。并参考服务商和其他兄弟院校的经验，提供常见问题的解答。尤其是，启用二次验证后，客户端软件需要修改客户端专用密码。
基于该用户手册，对服务人员做好培训，以应对可能发生服务量增长。如有知识库或智能问答机器人，可将相关内容导入。

**2.根据实际情况分阶段启用**

分析用户构成情况，制定好通知和启用的计划。

**(1）用户群体的识别与分析**

对用户群体做好分析，例如教师、学生、部门邮箱，离校学生、在校学生，离校职工、在校职工，长期不登录的不活跃账号、6个月内有登录记录的活跃账号等。分析用户结构，为后续分批启用提供参考。

**（2）针对不同用户群体制定启用计划**

针对不同用户群体，分批发送通知，告知二次验证启用事宜，在通知的截止日期操作开启（仅举例供参考，请根据实际情况制定计划）。
例如：

**·**长期不活跃账号：保护性锁定、强制开启二次验证

**·**学生账号：区分在校、非在校状态，先对非在校学生账号强制开启，再对在校学生账号强制开启

**·**教师账号：多次通知，建议开启，后根据启用情况，逐步全面覆盖；离校职工的账号应及时注销或锁定

**·**有被盗记录或大量被攻击的账号：强制开启

**·**部门邮箱：根据实际业务需求启用或设置例外

**·**新开通邮箱：强制开启

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GhQctjkh)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/789873803bbe1d5cf9b06a0859e2af0b.png)

# [CACTER](https://www.4hou.com/member/64Y9)

国内领先企业级邮件安全解决方案提供商，提供一站式防护。

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/64Y9)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)