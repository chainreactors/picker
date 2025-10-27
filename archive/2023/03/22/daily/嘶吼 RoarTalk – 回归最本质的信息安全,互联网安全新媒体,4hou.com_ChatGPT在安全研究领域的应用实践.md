---
title: ChatGPT在安全研究领域的应用实践
url: https://www.4hou.com/posts/6VL9
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-22
fetch_date: 2025-10-04T10:13:54.629481
---

# ChatGPT在安全研究领域的应用实践

ChatGPT在安全研究领域的应用实践 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ChatGPT在安全研究领域的应用实践

盛邦安全
[行业](https://www.4hou.com/category/industry)
2023-03-21 14:40:20

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)129128

收藏

导语：ChatGPT应用于安全研究领域能做什么？

**引言**

ChatGPT是一个人工智能技术驱动的自然语言处理工具，它能够通过理解和学习人类的语言来进行对话，并能进行连续对话。目前ChatGPT已经官方已经更新模型到4.0版本，宣称它是“最先进的系统，能生产更安全和更有用的回复”。当前使用ChatGPT进行问答也越来越方便，本文总结了一些ChatGPT在安全研究领域的一些应用实践，有了人工智能的帮助，我们更轻松高效的完成部分研究工作。

**01**

**防护规则编写**

ChatGPT能很方便的帮助我们编写各类防护规则。除开规则本身，它还帮你写好了注释，让你不光能快速编写，还能根据注释进行学习。

对于给出的规则编写要求，ChatGPT也不拘泥于给定的条件和范围，会尝试进行发散。如在下图的案例中，在我们原本提的需求之外，ChatGPT在检测的文件内容里脑补了“<?php”字符串，消除了部分误报；同时在上传文件名里除了php外，对php3、php5也做了限制，消除了部分漏报。

![1679366007197378.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366478620861.png "1679366007197378.png")

除此之外，对于一些指纹类的事件型规则，我们可以很方便的利用ChatGPT完成相应规则的收集，后续只需要做好验证工作就行了。

![1679366066760420.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366479998061.png "1679366066760420.png")

**02**

**检测规则编写**

ChatGPT虽然不能直接帮我们写poc（主要是考虑到了漏洞利用造成的影响），但是对于一些检测插件，还是能很快帮我们写出检测demo示例来：

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366480160155.png "1679366109805848.png")

当需要转换语言或转换poc格式时，利用ChatGPT也能很轻易的帮忙完成相关工作：

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366482171148.png "1679366145900859.png")

**03**

**代码审计&漏洞挖掘**

我们当然希望通过ChatGPT帮我们做更多有意义的安全研究工作，比如自动化漏洞挖掘。就笔者目前的测试情况来看，对于逻辑较为简单的代码，ChatGPT能很快找到脆弱点，但稍微设置些“坑”上去，ChatGPT的表现效果就不那么友好了。

我们以一个最简单的sql注入为例，看看ChatGPT的表现效果如何。首先在不做任何过滤的情况下，ChatGPT能很快识别到sql注入：

![1679366173123995.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366483262716.png "1679366173123995.png")

我们加一个简单的过滤条件，把get方法里获取的参数过滤了，但是查询语句里还是使用request方法获取请求数据，很显然使用post方法传递数据依然可以造成sql注入，我们看看ChatGPT能发现吗？

![1679366204751057.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366485205612.png "1679366204751057.png")

这里ChatGPT回避了我们设置的“坑”，开始扯怎么绕过正则的问题。这并不是我们想要的答案，在稍加提示后ChatGPT给出了正解。

![1679366235155537.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366486206068.png "1679366235155537.png")

现在我们难度进一步升级，过滤request里的参数，然后将get里的参数拼接进sql语句，我们先来看看ChatGPT能否帮我们找到突破点。

![1679366260144825.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366487128973.png "1679366260144825.png")

ChatGPT在这里出现了代码理解错误，认为$\_GET没有做任何过滤。我们想让它知道$\_GET在$\_REQUEST里已经被过滤掉了，于是开始引导：

![1679366313167743.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366488195763.png "1679366313167743.png")

![1679366328179875.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366490330626.png "1679366328179875.png")

ChatGPT在思考了一阵好发现确实是自己错了，该代码不存在sql注入，并开始道歉。这时候再给它一点提示，剧情又反转了过来。

![1679366353928876.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366491174877.png "1679366353928876.png")在一步步引导后ChatGPT终于发现了漏洞点在哪里，并给出了最终的绕过方案。从这个案例可以看出，ChatGPT在基于安全视角的代码理解上还需要不断学习和打磨。

**04**

**社会工程学应用**

作为“写小作文”的能手，ChatGPT自然在社会工程学上也有广泛的应用，例如我们可以利用它轻松写一封钓鱼邮件：

![1679366381663157.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366493158274.png "1679366381663157.png")

当然也可以用它来做钓鱼邮件识别和检测，我很乐意看到它自相矛盾的样子：

![1679366410558692.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366494127414.png "1679366410558692.png")

除此之外，我们可以根据所掌握的信息，利用ChatGPT生成口令字典：

![1679366466111491.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230321/1679366496675038.png "1679366466111491.png")

**总结**

事实上ChatGPT凭借其强大的训练集有能力帮我们做更多安全研究方面的事情，比如漏洞复现、木马免杀、代码混淆等，只是很多偏攻击向的成果已经被列为了黑名单。在上个月我们还能用ChatGPT辅助生成免杀的webshell，今天尝试的时候同样的请求已经被禁止了。但无论如何，人工智能的存在势必能提高我们的研究效率，也能帮我们探索出更多创新性的研究场景和方向。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8YrTBdbd)

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

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

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