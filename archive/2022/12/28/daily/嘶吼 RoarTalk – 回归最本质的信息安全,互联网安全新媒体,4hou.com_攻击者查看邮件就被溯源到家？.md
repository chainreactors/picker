---
title: 攻击者查看邮件就被溯源到家？
url: https://www.4hou.com/posts/mXoG
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-28
fetch_date: 2025-10-04T02:35:11.384467
---

# 攻击者查看邮件就被溯源到家？

攻击者查看邮件就被溯源到家？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者查看邮件就被溯源到家？

矢安科技
[资讯](https://www.4hou.com/category/info)
2022-12-27 15:39:08

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)119194

收藏

导语：本文通过分享实际攻防演练中真实案例，防守方在未暴露任何敏感信息的情况下，仅通过邮件往来最终溯源到攻击方相关真实信息。 作为攻击溯源技术的引子，供各位从业和爱好者交流学习。

本文通过分享实际攻防演练中真实案例，防守方在未暴露任何敏感信息的情况下，仅通过邮件往来最终溯源到攻击方相关真实信息。
作为攻击溯源技术的引子，供各位从业和爱好者交流学习。

**场景描述**

攻击者伪造邮件，称其申请防守方靶标系统测试账号，诱骗防守方为其开通系统账号权限。防守方通过相关话术及技术，最终溯源到攻击方成员。

**场景再现**

某日在攻防演练日常防守过程中，业务小组成员收到主题为“申请XXXX账号”的邮件，邮件内容为系统内张一（化名）需要使用系统，请管理员为其新建账号密码。经与张一本人确认邮件中工作单位、研究方向、联系方式等属实，但邮件为他人冒充发送，故第一时间反馈研判分析小组。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126705889134.png "1672124234107428.png")

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126707315449.png "1672124238143250.png")

**简单分析**

通过导出邮件为eml格式，并以文本格式查看后，获取到其邮件中关键信息如下（已脱敏）：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126707187964.png "1672126624365374.png")

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126708109699.png "1672125676126354.png")

分析其使用的zhangyi@21cn.com邮箱，发现其为攻击者特意注册针对员工张一姓名全拼的21cn.com邮箱。

**反制邮件**

鉴于钓鱼邮件中手机号码为张一本人而非攻击者手机号码，经决策后防守方拿出多年积累的花式话术，回复其邮件称密码已发送短信至手机，并在签名处加入防守方可控的图片：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126709532700.png "1672124457104165.png")

随后，在防守方服务器上监控签名处图片访问情况，发现攻击者于当日晚间23点、次日上午9点左右多次查看收件箱：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126711139470.png "1672124470190020.png")

故此，获取到攻击者信息如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126711150323.png "1672126660157142.png")

**再次钓鱼**

次日，防守方收到第二封钓鱼邮件，主题同样为“申请XXX账号”，邮件内容为王一（化名）需要使用系统，希望管理员新建账户，并附上手机号码。通过分析，猜测为攻击者因第一封邮件手机号码非攻击者可控，无法接受短信获取系统密码，故更换联系方式发送钓鱼邮件。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126712110004.png "1672124490957918.png")

导出邮件分析后得到以下信息（已脱敏）：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126713825058.png "1672126677100029.png")

随后同样发送带有防守方可控的图片作为邮件签名，监测其查看邮件时间、频率。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126714127174.png "1672124508176737.png")

**反制溯源**

发现其收件IP地址1.1.1.2与张一的收件IP地址一致，结合邮件主题、话术、攻击手法确认两封钓鱼邮件为同一攻击者，决定并案处理。通过尝试申请重置其21cn.com的邮箱密码，发现其绑定了手机号1314444：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126714133433.png "1672124517111814.png")

根据其泄漏的IP地址1.1.1.1、1.1.1.2、1.1.1.3、2.2.2.1等归属地均在哥谭市，故查询哥谭市所有131号段：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126715114621.png "1672125017131442.png")

组合其号段，逐一尝试21cn.com的注册情况，最终发现存在3个对应的手机号码注册了21cn.com邮箱：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126705162135.png "1672126705162135.png")

对这三个手机号码进行大数据排查、信息收集，发现13140114444曾经绑定微博、微信、支付宝等账户，且其社交媒体活动规律符合网络安全从业者特征，尤其是其手机号绑定了某招聘网站显示其具有从事网络安全相关工作经验。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126716453167.png "1672125027214394.png")

根据攻击者使用张一身份在工作时间（11:18、17:58等）发送、查看邮件泄漏的IP地址1.1.1.1，使用的邮件客户端MacOS，猜测为工作单位互联网出口IP，通过物理位置定位，可获取到相关地理位置：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126717137413.png "1672125037168838.png")

且物理位置符合其招聘网站显示的工作单位官网办公位置哥谭市钻石区。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126718178853.png "1672125045149641.png")

根据攻击者在非工作时间（21:14、23:58、02:34等）查看邮件泄漏的IP地址1.1.1.2、1.1.1.3、2.2.2.1，使用的邮件客户端189MailiPhone，猜测其为移动客户端进行查看邮件，经过排查确认IP为移动基站，且物理位置距离工作单位较近，猜测为攻击者实际住所。分析其手机号为阿里小号，符合攻防演练中攻击者常见属性之一，猜测手机号为攻击者手机号：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126719755363.png "1672125055172497.png")

通过大数据排查手机号曾泄漏物流信息，符合其工作单位、实际物理住所哥谭市特征：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126719585979.png "1672125062793985.png")

综合信息及身份画像
综上，根据整理已获取到攻击者信息，分析其相关特征（已脱敏），进行攻击者画像：

**![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221227/1672126735707660.png "1672126735707660.png")**

**结语**

本文通过案例形象地再现了钓鱼邮件及钓鱼邮件反制，基于“删繁就简”的原则，在不使用重量级武器如“免杀木马反制”、“钓鱼URL反制”等手段，以信息收集为主要溯源手段，向读者阐述了相关技术，旨在与各位从业及爱好者探讨交流。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TvgA5L9S)

#### 你可能感兴趣的

* [![]()

  【附下载】重庆信通设计院：城市数字公共基础设施标准体系 全景解析](https://www.4hou.com/posts/jBwl)
* [![]()

  【附下载】重庆信通设计院：150+AI 大模型安全常用术语解析](https://www.4hou.com/posts/kgLN)
* [![]()

  伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究](https://www.4hou.com/posts/7M21)
* [![]()

  漏洞预警 | Vite 存在任意文件读取漏洞（CVE-2025-30208）](https://www.4hou.com/posts/KG2x)
* [![]()

  315倒计时！2025年哪些领域将成维权重点](https://www.4hou.com/posts/Dx76)
* [![]()

  中央网信办发布2025年“清朗”系列专项行动整治重点](https://www.4hou.com/posts/Bv7Q)

![](https://img.4hou.com/portraits/de620f130a9785bd8fdb5a7d443befa3.jpg)

# [矢安科技](https://www.4hou.com/member/PyV4)

致力于成为新一代智能安全的领跑者。

#### 最新文章

* [【附下载】重庆信通设计院：城市数字公共基础设施标准体系 全景解析](https://www.4hou.com/posts/jBwl)
  2025-07-01 11:23:43
* [【附下载】重庆信通设计院：150+AI 大模型安全常用术语解析](https://www.4hou.com/posts/kgLN)
  2025-05-09 16:56:03
* [伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究](https://www.4hou.com/posts/7M21)
  2025-04-21 11:06:52
* [漏洞预警 | Vite 存在任意文件读取漏洞（CVE-2025-30208）](https://www.4hou.com/posts/KG2x)
  2025-03-31 11:36:18

[查看更多](https://www.4hou.com/member/PyV4)

# 相关热文

* [【附下载】重庆信通设计院：城市数字公共基础设施标准体系 全景解析](https://www.4hou.com/posts/jBwl)

  网络伍豪
* [【附下载】重庆信通设计院：150+AI 大模型安全常用术语解析](https://www.4hou.com/posts/kgLN)

  网络伍豪
* [伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究](https://www.4hou.com/posts/7M21)

  盛邦安全
* [漏洞预警 | Vite 存在任意文件读取漏洞（CVE-2025-30208）](https://www.4hou.com/posts/KG2x)

  盛邦安全
* [315倒计时！2025年哪些领域将成维权重点](https://www.4hou.com/posts/Dx76)

  企业资讯
* [中央网信办发布2025年“清朗”系列专项行动整治重点](https://www.4hou.com/posts/Bv7Q)

  企业资讯

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![...