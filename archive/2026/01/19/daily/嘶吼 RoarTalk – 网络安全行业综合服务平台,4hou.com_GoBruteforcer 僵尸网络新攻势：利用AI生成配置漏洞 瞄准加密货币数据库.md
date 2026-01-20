---
title: GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库
url: https://www.4hou.com/posts/nl2Y
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-19
fetch_date: 2026-01-20T03:30:56.685993
---

# GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库

GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7265

收藏

导语：在近期的攻击活动中，GoBruteforcer的活跃度之所以激增，是因为大量服务器复用了由大语言模型（LLM）生成的通用配置片段。

GoBruteforcer（又名GoBrut）僵尸网络发起新一轮恶意攻击，目标直指暴露在公网的服务器，特别是那些疑似使用AI生成示例配置的加密货币及区块链项目数据库。

该恶意软件基于Golang编写，通常针对暴露的FTP、MySQL、PostgreSQL及phpMyAdmin服务发动攻击。它往往利用已沦陷的Linux服务器扫描随机公网IP，并实施暴力破解登录。

**利用薄弱防御实施入侵**

研究人员估计，目前互联网上可能有超过5万台服务器易受GoBrut攻击。攻击者通常通过运行XAMPP的服务器上的FTP服务获取初始访问权限。这是因为除非管理员手动进行安全配置，否则默认配置往往包含极易被破解的弱口令。

当攻击者利用标准账户（通常为daemon或nobody）和弱默认密码成功登录XAMPP FTP后，典型的下一步操作是将Web后门（Web Shell）上传至网站根目录。

攻击者也可能通过其他途径上传Web后门，例如配置不当的MySQL服务器或phpMyAdmin面板。感染链条随后继续延伸，通过下载器获取IRC僵尸程序及暴力破解模块。

恶意软件在延迟10至400秒后启动，在x86\_64架构上可启动多达95个暴力破解线程，扫描随机公网IP段，但会自动跳过私有网络、AWS云服务段及美国政府网络。

每个工作线程生成一个随机公网IPv4地址，探测相关服务端口，尝试提供的凭证列表，随后退出。系统会持续生成新的工作线程以维持设定的并发级别。

FTP模块依赖于直接嵌入在二进制文件中的22组硬编码用户名密码对。这些凭证与XAMPP等虚拟主机套件中的默认或常见部署账户高度吻合。

**AI生成配置与老旧套件助长攻势**

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260108/1767857532123469.png "1767857532123469.png")

GoBruteforcer的感染链

研究人员指出，在近期的攻击活动中，GoBruteforcer的活跃度之所以激增，是因为大量服务器复用了由大语言模型（LLM）生成的通用配置片段。这导致了大量弱口令和可预测的默认用户名（如appuser、myuser、operator）的泛滥。

这些用户名频繁出现在AI生成的Docker和DevOps操作指南中，研究人员据此推测，这些配置已被应用到真实系统中，从而使其极易遭受密码喷洒攻击。

助长该僵尸网络近期攻势的第二个原因是过时的服务器套件（如XAMPP）。这些套件在部署时仍保留默认凭证和开放的FTP服务，暴露了脆弱的网站根目录，使攻击者能够轻松植入Web后门。

一起典型的攻击案例是一台受感染的主机被植入了TRON钱包扫描工具，该工具会对TRON和币安智能链（BSC）进行全网扫描。攻击者使用一个包含约2.3万个TRON地址的文件，通过自动化工具识别并掏空余额非零的钱包。

为防御GoBruteforcer攻击，管理员应避免使用AI生成的部署指南，并使用非默认用户名搭配强密码。 同时，及时检查FTP、phpMyAdmin、MySQL和PostgreSQL是否存在暴露的服务，并考虑将XAMPP等过时软件套件替换为更安全的替代方案。

文章来源自：https://www.bleepingcomputer.com/news/security/new-gobruteforcer-attack-wave-targets-crypto-blockchain-projects/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?aGLrMazj)

#### 你可能感兴趣的

* [![]()

  GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)
* [![]()

  CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
* [![]()

  HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)
* [![]()

  Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
* [![]()

  WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
* [![]()

  MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)
  2026-01-19 12:00:00
* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
  2026-01-16 11:17:10
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)
  2026-01-16 10:52:54
* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
  2026-01-12 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)

  胡金鱼
* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)

  山卡拉
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)

  山卡拉
* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)

  胡金鱼
* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)

  胡金鱼
* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)

  胡金鱼

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