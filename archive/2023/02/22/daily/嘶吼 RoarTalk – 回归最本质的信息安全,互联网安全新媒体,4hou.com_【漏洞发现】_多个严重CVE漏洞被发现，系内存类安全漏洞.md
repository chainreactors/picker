---
title: 【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞
url: https://www.4hou.com/posts/xjYq
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-22
fetch_date: 2025-10-04T07:41:12.444540
---

# 【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞

【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞

云起无垠
[漏洞](https://www.4hou.com/category/vulnerable)
2023-02-21 10:19:03

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)207168

收藏

导语：近日，云起无垠的无垠代码模糊测试系统通过对json parse库、MojoJson进行检测发现多个CVE漏洞，漏洞编号为：CVE-2023-23083 ~ CVE-2023-23088，该系列漏洞皆为内存类漏洞，漏洞允许攻击者执行恶意代码进行攻击，从而造成严重后果。其中，CVE-2023-23086~CVE-2023-23088已公开。

**1.漏洞描述**

近日，云起无垠的无垠代码模糊测试系统通过对json parse库、MojoJson进行检测发现多个CVE漏洞，漏洞编号为：CVE-2023-23083 ~ CVE-2023-23088，该系列漏洞皆为内存类漏洞，漏洞允许攻击者执行恶意代码进行攻击，从而造成严重后果。其中，CVE-2023-23086~CVE-2023-23088已公开。

MojoJson 是一个极其简单且超快速的JSON 解析器。解析器支持解析Json 格式，并提供简单的API 来访问不同类型的 Json 值。此外，核心算法可以很容易地用各种编程语言实现。

JSON.parse()是Javascript中一个常用的 JSON 转换方法，JSON.parse()可以把JSON规则的字符串转换为JSONObject，JSON.parse()很方便，并且几乎支持所有浏览器。

针对此类漏洞，无垠代码模糊测试系统均给出了相应建议。

**2.漏洞详情**

① CVE-2023-23086 func SkipString中堆缓冲区溢出

MojoJson v1.2.3中的缓冲区溢出漏洞允许攻击者通过SkipString函数执行任意代码。

漏洞等级：严重；CVSS v3.1漏洞评分：9.8

检测截图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/4vD467VsKgLDias1THZZgbkvSTU5FYIibvehicxiaS6EX8msoicyLSuUdibgia5EWd2ibHvUiaiaL5pPPGd1VZVEGM7vaQtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/4vD467VsKgLDias1THZZgbkvSTU5FYIibvyM4OoW6usZjWoDnbVEoHf6McPAEkHg4D4icBLePKUmpG9cR5WZpFafg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

② CVE-2023-23087 函数Destory中指针错误

在MojoJson v1.2.3中发现了一个问题，允许攻击者通过destroy函数执行任意代码。

漏洞等级：严重；CVSS v3.1漏洞评分：9.8

检测截图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/4vD467VsKgLDias1THZZgbkvSTU5FYIibvibNX4Gl3ctYSlEWDbRdfGW5ntiaGgUF6SX1W7MJ4RZf22hLRpuzAIILA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/4vD467VsKgLDias1THZZgbkvSTU5FYIibva0YRs4EnKGVxI38cajb5TvqfONrWXXaYicrG1vsN19UvORU1ZJjbSibg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

③ CVE-2023-23088 json\_value\_parse堆缓冲区溢出

Barenboim json-parser master和v1.1.0中的缓冲区溢出漏洞已在v1.1.1中修复，允许攻击者通过json\_value\_parse函数执行任意代码。

漏洞等级：严重；CVSS v3.1漏洞评分：9.8

检测截图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/4vD467VsKgLDias1THZZgbkvSTU5FYIibvarbsTnrM7wIVeAgmOpARW15Dia4xEriajzpbzDcz4VlyRETbg5xUvA9g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/4vD467VsKgLDias1THZZgbkvSTU5FYIibvqdEYJibJfaTpdSUjVwSiceSiaGSTSACAtIDpzicnXOnv1iatW8RPwyLab1g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**3.解决方案**

无垠代码模糊测试系统针对每一个CVE漏洞都给出了处置方案，可参照如上截图细看。

**4.无垠代码模糊测试系统**

无垠代码模糊测试系统是一款基于Fuzzing技术研发的灰盒检测工具，通过它不仅可以发现逻辑类漏洞，还能找到内存破坏的漏洞，比如缓冲区溢出、内存泄露、条件竞争等。该产品技术基于海量测试用例，融合覆盖引导、人工智能AI等关键技术，赋能软件开发的开发、测试、运维、部署等阶段，在软件上线之前发现已知及未知漏洞，可以更好的防止业务系统带病上线。(云起无垠-李唯）

参考链接：

https://nvd.nist.gov/vuln/detail/CVE-2023-23086

https://github.com/scottcgi/MojoJson/issues/2

https://nvd.nist.gov/vuln/detail/CVE-2023-23087

https://github.com/scottcgi/MojoJson/issues/3

https://nvd.nist.gov/vuln/detail/CVE-2023-23088

https://github.com/Barenboim/json-parser/issues/7

云起无垠（https://www.clouitera.com）是新一代智能模糊测试领跑者，采用新一代Fuzzing技术全流程赋能软件供应链与开发安全，基于智能模糊测试引擎为协议、代码、数据库、API、Web3.0等应用提供强大的软件安全自动化分析能力，从源头助力企业自动化检测并助其修复业务系统安全问题，为每行代码安全运行保驾护航。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uBUmQoRO)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/portraits/f212c0a38fbb2cb3b0c0a7d31fac289a.png)

# [云起无垠](https://www.4hou.com/member/wLAX)

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/wLAX)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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