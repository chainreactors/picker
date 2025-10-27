---
title: 武汉大学：如何做好高校电子邮件账号安全防护
url: https://www.4hou.com/posts/6M97
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-21
fetch_date: 2025-10-06T18:25:01.241308
---

# 武汉大学：如何做好高校电子邮件账号安全防护

武汉大学：如何做好高校电子邮件账号安全防护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 武汉大学：如何做好高校电子邮件账号安全防护

CACTER
[行业](https://www.4hou.com/category/industry)
2024-09-20 15:34:49

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)53498

收藏

导语：保障邮件账号的安全需要从源头防止、及时发现和有效阻断攻击，但长远来看，还是要加防御防御能力和用户意识。

上个世纪七十年代，电子邮件占据了互联网的前身ARPANET上流量的75%，是最主要的应用。随着互联网的发展，电子邮件在全面普及后，被各种各样的即时通讯软件抢走了不少风头。然而，其始终还是被社会所认可的主流网络通讯渠道，但是也成为最易被攻击的目标。

当前电子邮件已经成为恶意连接、病毒木马的重要传播途径，研究发现网络安全事件中八成都和电子邮件有关。据Cofense的《2023年度电子邮件安全报告》，2022年全年恶意钓鱼电子邮件增加了569%，与证书/凭据钓鱼相关的活跃威胁报告增加了478%，恶意软件增加了44%。商业电子邮件欺诈（BEC）连续第8年成为最严重的网络犯罪形式之一，在全球90%的地区造成了机构数十亿美元的损失。利用人工智能、机器人进行信息窃取的恶意活动显著增加，攻击成本较低且快速有效，发起的混合攻击更难被检测和发现。

面对高校师生，对外的学术联系非常依赖电子邮件。如何保障好高校电子邮件账号的安全，确保研究人员对外学术联系的安全性、及时性、准确性，是值得电子邮件管理员关注的重要问题。可以在弄清威胁来源的基础上，及时发现并阻断入侵威胁，提升安全防护能力。

**一、了解主要安全威胁来源**

攻击者通过多种方式和渠道对邮件账号发起攻击，常见的手段有：

1.弱密码：使用生日、电话号码等容易被猜测的密码，或者在多个平台重复使用同一密码，都可能让攻击者轻易破解。

2.社交工程攻击：攻击者通过伪装成可信赖的联系人，诱使用户透露敏感信息，如密码、验证码等。

3.钓鱼邮件：伪装成官方邮件，诱导用户点击含有恶意代码的链接，从而获取账号信息。

4.技术漏洞：攻击者利用Webmail、SMTP、POP3、IMAP等攻击渠道和服务协议的漏洞，进行恶意操作，如发送垃圾邮件、盗取用户信息等。

**二、加强异常行为监测与处置**

管理员需要加强对邮件系统的监测，及时发现邮件账号被入侵的情况。定期检查邮件发送和接收的异常行为，如突然增加的邮件数量、非正常时间的登录记录等。深入分析系统日志，寻找异常登录、异常操作等线索，这可能表明账号已经被攻击。可以采取有效措施阻断相关威胁，如自行编写脚本封禁账号，一旦发现账号有异常行为，如发送大量垃圾邮件，应立即封禁该账号，防止进一步的损害。

以Coremail XT5为例，可以编写脚本通过日志排查同时发信给至少20个收件人的发信账号，根据每天最多批量发送3次进行筛选，与批量发信邮箱地址白名单比对后，封禁用户。
其中白名单文件white.list格式为一行一个邮箱地址。

![大咖征稿文章配图-武汉大学.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240920/1726818082436283.jpg "1726795873187111.jpg")

**三、提升邮件系统防御能力**

保障邮件账号的安全需要从源头防止、及时发现和有效阻断攻击，但长远来看，还是要加防御防御能力和用户意识。

**1.提升邮件系统技术防御能力**
可以从启用双因素认证、防密码暴露、防钓鱼邮件和防垃圾邮件等方面，增强邮件系统的技术防护能力。

启用双因素认证：双因素认证增加了额外的安全层，即使密码被盗，攻击者也难以访问账户。可以结合所在高校的实际情况，采取短信验证、硬件令牌、认证APP等方式。除了密码，还需要通过手机验证码、生物识别等方式进行二次验证，增加攻击的难度。

定期更新密码：密码暴露是账户被黑的主要原因之一，可以采取复杂密码策略、定期更换等方式，提升安全性，如可要求用户设置包含大小写字母、数字和特殊字符的复杂密码，并定期提醒用户更改密码，避免重复使用旧密码。

强化技术措施：采取有效的防御措施识别和阻止钓鱼攻击，比如采取SPF、DKIM、DMARC、黑白名单等技术来检查邮件真实性，也可考虑部署邮件安全网关，使用基于规则和机器学习的垃圾邮件过滤器来自动检测并拦截钓鱼邮件、垃圾邮件等威胁。邮件系统应当提供必要的安全设置，如登录警告、IP限制等，增强账号防护。

**2.对敏感数据加强授权管控**
在条件许可的情况下，还可部署数据防泄漏系统，识别可定位敏感数据位置、监控敏感数据的使用情况以及采取阻断和审批加密的策略，有效避免内部人员无意或恶意的数据外泄。

**3.加强用户安全培训**
对师生加强网络安全培训，定期对师生普及网络安全知识，重点针对管理人员、科研人员定期进行安全意识培训，在使用电子邮件时注意防范社会工程学攻击，如钓鱼攻击及欺诈邮件。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lcEdq3eI)

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