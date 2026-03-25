---
title: “养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示”
url: https://www.4hou.com/posts/DxMk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-24
fetch_date: 2026-03-25T04:15:55.405419
---

# “养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示”

“养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示” - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示”

梆梆安全
[行业](https://www.4hou.com/category/industry)
18小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6553

收藏

导语：OpenClaw作为一款开源AI智能体，存在功能局限尚无法胜任复杂任务，且伴有安全漏洞与使用成本问题。

3月10日，国家互联网应急中心CNCERT于发布“关于OpenClaw安全应用的风险提示”。具体内容如下：

近期，OpenClaw（“小龙虾”，曾用名Clawdbot、Moltbot）应用下载与使用情况火爆，国内主流云平台均提供了一键部署服务。此款智能体软件依据自然语言指令直接操控计算机完成相关操作。为实现“自主执行任务”的能力，该应用被授予了较高的系统权限，包括访问本地文件系统、读取环境变量、调用外部服务应用程序编程接口（API）以及安装扩展功能等。然而，由于其默认的安全配置极为脆弱，攻击者一旦发现突破口，便能轻易获取系统的完全控制权。

![](https://pic4.zhimg.com/80/v2-f6913c2faf63270f07647748447f8f7f_1440w.jpg)

前期，由于OpenClaw智能体的不当安装和使用，已经出现了一些严重的安全风险：

1. “提示词注入”风险。网络攻击者通过在网页中构造隐藏的恶意指令，诱导OpenClaw读取该网页，就可能导致其被诱导将用户系统密钥泄露。

2. “误操作”风险。由于错误的理解用户操作指令和意图，OpenClaw可能会将电子邮件、核心生产数据等重要信息彻底删除。

3. 功能插件（skills）投毒风险。多个适用于OpenClaw的功能插件已被确认为恶意插件或存在潜在的安全风险，安装后可执行窃取密钥、部署木马后门软件等恶意操作，使得设备沦为“肉鸡”。

4. 安全漏洞风险。截止目前，OpenClaw已经公开曝出多个高中危漏洞，一旦这些漏洞被网络攻击者恶意利用，则可能导致系统被控、隐私信息和敏感数据泄露的严重后果。对于个人用户，可导致隐私数据（像照片、文档、聊天记录）、支付账户、API密钥等敏感信息遭窃取。对于金融、能源等关键行业，可导致核心业务数据、商业机密和代码仓库泄露，甚至会使整个业务系统陷入瘫痪，造成难以估量的损失。

建议相关单位和个人用户在部署和应用OpenClaw时，采取以下安全措施：

1. 强化网络控制，不将OpenClaw默认管理端口直接暴露在公网上，通过身份认证、访问控制等安全控制措施对访问服务进行安全管理。对运行环境进行严格隔离，使用容器等技术限制OpenClaw权限过高问题；

2. 加强凭证管理，避免在环境变量中明文存储密钥；建立完整的操作日志审计机制；

3. 严格管理插件来源，禁用自动更新功能，仅从可信渠道安装经过签名验证的扩展程序。

4. 持续关注补丁和安全更新，及时进行版本更新和安装安全补丁。

来源：国家互联网应急中心CNCERT

“养龙虾”（OpenClaw）近期在开发领域获得广泛关注。然而，热度背后需关注官方发布的相关安全风险提示。需要认识到，OpenClaw作为一款开源AI智能体，存在功能局限尚无法胜任复杂任务，且伴有安全漏洞与使用成本问题。面对新技术浪潮，建议基于实际需求评估其适用性，避免盲目跟风，在部署前做好安全防护。让技术回归工具定位，在可控范围内探索其应用价值。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iAxRVyas)

#### 你可能感兴趣的

* [![]()

  “养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示”](https://www.4hou.com/posts/DxMk)
* [![]()

  美国国务院发布全球范围安全警示](https://www.4hou.com/posts/6MrN)
* [![]()

  意大利最高国防委员会会议使用录音屏蔽器](https://www.4hou.com/posts/Zglg)
* [![]()

  360“安全龙虾”全国巡回汕头站火爆开局，全民AI热潮席卷50城](https://www.4hou.com/posts/l0K1)
* [![]()

  从“可用”到“可信”：梆梆安全打造省级政务APP安全建设新标杆，护航政务服务行稳致远](https://www.4hou.com/posts/KGM8)
* [![]()

  【附下载】深度拆解OpenClaw“龙虾”风险：AI时代供应链安全，为何成了行业致命软肋？](https://www.4hou.com/posts/5MqX)

![](https://img.4hou.com/portraits/e3b60d4465a093e3518f9cbe37a778ff.png)

# [梆梆安全](https://www.4hou.com/member/qoj2)

梆梆安全|保护智能生活

#### 最新文章

* [“养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示”](https://www.4hou.com/posts/DxMk)
  2026-03-24 17:36:40
* [美国国务院发布全球范围安全警示](https://www.4hou.com/posts/6MrN)
  2026-03-24 17:34:47
* [意大利最高国防委员会会议使用录音屏蔽器](https://www.4hou.com/posts/Zglg)
  2026-03-24 17:33:09
* [360“安全龙虾”全国巡回汕头站火爆开局，全民AI热潮席卷50城](https://www.4hou.com/posts/l0K1)
  2026-03-24 17:14:34

[查看更多](https://www.4hou.com/member/qoj2)

# 相关热文

* [“养龙虾” 安全危机！官方发布 “关于OpenClaw安全应用的风险提示”](https://www.4hou.com/posts/DxMk)

  梆梆安全
* [美国国务院发布全球范围安全警示](https://www.4hou.com/posts/6MrN)

  RC2反窃密实验室
* [意大利最高国防委员会会议使用录音屏蔽器](https://www.4hou.com/posts/Zglg)

  RC2反窃密实验室
* [360“安全龙虾”全国巡回汕头站火爆开局，全民AI热潮席卷50城](https://www.4hou.com/posts/l0K1)

  企业资讯
* [从“可用”到“可信”：梆梆安全打造省级政务APP安全建设新标杆，护航政务服务行稳致远](https://www.4hou.com/posts/KGM8)

  梆梆安全
* [【附下载】深度拆解OpenClaw“龙虾”风险：AI时代供应链安全，为何成了行业致命软肋？](https://www.4hou.com/posts/5MqX)

  网络伍豪

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