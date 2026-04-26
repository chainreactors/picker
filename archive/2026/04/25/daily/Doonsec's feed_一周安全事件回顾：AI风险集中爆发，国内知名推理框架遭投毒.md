---
title: 一周安全事件回顾：AI风险集中爆发，国内知名推理框架遭投毒
url: https://mp.weixin.qq.com/s/XhJhK_T0JdmheWQ34yklIw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:01:03.701809
---

# 一周安全事件回顾：AI风险集中爆发，国内知名推理框架遭投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mSqhDgeKrPBWl9ZroaAAczqVK8P5WGiawNCNVPgT81KhPL7vkEInuGTK9vMiayMQf2Zua5tK1jjAeYGOhPuR6xK319cTOjeIc0LoicjQTGFKpA/0?wx_fmt=jpeg)

# 一周安全事件回顾：AI风险集中爆发，国内知名推理框架遭投毒

奇安信集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![安全态势头图](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarbeibXRgFiaLhJj1QdgPcxzLh3OFl0EicBlXUMStdia9vxEro6xT4wLKAYU4rUOOX1ibfaUpT6ZRibL4gw/640?wx_fmt=jpeg&from=appmsg)

本周安全事件集中暴露AI生态快速扩张下的典型风险：默认配置缺陷、供应链投毒与攻击门槛急降。Lovable权限逻辑失误令所有用户项目数据被公开暴露，Xinference因PyPI仓库被劫持植入后门以窃取云密钥和数据库密码，更有安全研究员仅用约1.5万元成本驱动大模型，便将旧版软件漏洞转化为可实际运行的攻击工具，预示未及时修复的系统将面临极高的利用风险。建议立即审查所有AI相关服务与开源组件的默认权限和依赖来源，建立面向AI供应链的持续监控，并将安全校验嵌入开发全流程，防止极速交付牺牲基础安全防线。

## [因默认设计不安全，知名AI编程公司Lovable所有用户数据公开暴露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515858&idx=1&sn=d28bb9b88c16814f1c969ac84c30ad0a&scene=21#wechat_redirect)

4月23日安全内参消息，瑞典AI编程公司Lovable近期曝出严重安全缺陷。因其后端权限逻辑在2月份统一权限时发生失误，意外重新开启了对“公共项目”聊天记录的访问权，导致2025年11月前所有默认公开的项目代码、AI 对话及客户敏感数据可被外部账户直接查看，波及英伟达、微软及Spotify等名企员工账号。该公司最初否认数据泄露，称有意如此设计，后致歉称系内部配置失误。AI编程工具普遍缺乏默认安全配置且底层安全建模粗放。这种“盲目追求极速交付”的模式，引发了大众对数据安全被牺牲的担忧。

## [国产AI开源组件Xinference遭供应链投毒，用户访问凭证和密钥等或泄露](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247518509&idx=1&sn=bef0b7230e3d69d03629a6f6c6ee60bb&scene=21#wechat_redirect)

4月23日奇安信威胁情报中心消息，国产AI推理开源组件Xinference被披露存在供应链投毒风险。攻击者通过窃取Python官方代码仓库（PyPI）项目维护者发布权限，在2.6.0、2.6.1和2.6.2三个版本中植入后门程序，一旦开发者安装或导入受影响版本，程序便会在后台自动运行，窃取SSH远程登录密钥、云服务平台访问密钥、数据库连接密码及加密货币钱包等敏感数据，并发送至攻击者控制的远程服务器。在用户报告可疑行为（例如发现搜索密码的grep活动）后，维护者已将这些版本从PyPI撤回。

## [仅花1.5万元，就能把关键漏洞变成直接运行的网络武器](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515853&idx=1&sn=a118f98eb5fcb3846c4194b9f9d94d3b&scene=21#wechat_redirect)

4月22日安全内参消息，一位安全研究员近期公布了一项实验，尝试用Claude Opus 4.6模型，为Discord客户端内置的Chrome（v138旧版本）编写漏洞利用，在消耗20个小时2.3T词元（价值约1.5万元）后，成功构建了CVE-2026-5873的漏洞利用工具。这一实验意味着，旧版本软件关键漏洞的可利用性未来将逼近100%，漏洞武器化与补丁更新的时差越来越大，企业应及早变革网络防御体系。

## 法国国家重要证件管理机构遭网络攻击，部分用户信息泄露

4月20日央视新闻消息，法国国家安全证件管理局确认，其信息系统于4月15日发生安全事件，导致部分用户个人数据遭未经授权访问。法国内政部表示，受影响信息可能包括姓名、电子邮箱、出生日期，以及部分用户的住址、出生地和电话号码等，但不涉及办理证件时提交的附件材料，也无法直接用于登录账户。相关部门称已启动技术调查，并采取措施加强系统安全，同时正向受影响用户发送通知。法国司法部门已介入调查。法国国家安全证件管理局负责办理法国护照、身份证、居留证及驾驶执照等重要证件业务。此次事件引发外界对公共机构网络安全的关注。

安全内参：https://www.secrss.com/articles/89625

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

奇安信集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

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