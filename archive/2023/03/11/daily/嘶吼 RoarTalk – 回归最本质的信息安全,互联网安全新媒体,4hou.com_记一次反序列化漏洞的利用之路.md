---
title: 记一次反序列化漏洞的利用之路
url: https://www.4hou.com/posts/XV3W
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-11
fetch_date: 2025-10-04T09:12:41.827967
---

# 记一次反序列化漏洞的利用之路

记一次反序列化漏洞的利用之路 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 记一次反序列化漏洞的利用之路

盛邦安全
[漏洞](https://www.4hou.com/category/vulnerable)
2023-03-10 16:36:05

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)203360

收藏

导语：记一次反序列化漏洞的利用之路

**0x01 前言**

一次偶然的机会拿到了一套系统的源码，结合CodeQLpy很容易发现了其中存在的反序列化漏洞，如图1.1所示。这是属于标准的java反序列化，也没有进行任何过滤。（关注烽火台实验室Beacon Tower Lab，为您持续输出前沿的安全攻防技术）

CodeQlpy项目地址：

https://github.com/webraybtl/CodeQLpy

![1678435371164884.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436637111525.png "1678435371164884.png")

图1.1 目标源码中存在的反序列化漏洞

**0x02 探索**

1） 确认反序列化漏洞存在

一般来说确认反序列化漏洞都可以使用URLDNS链，因为这条链是属于JDK自带的，不依赖于第三方jar包，只要目标DNS出网一般即可利用成功，具有较强的通用性。

直接使用ysoserial就可以生成URLDNS链需要的序列化内容，为了方便我们使用，需要稍微修改一下ysoserial.payloads.util.PayloadRunner的run方法，如图2.1所示。这里主要修改的内容是保存序列化的数据到文件cc.ser，并且不进行反序列化操作。

![1678435473190992.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436639135269.png "1678435473190992.png")

图2.1 修改yso中的方法保存序列内容

这样之后下一步就可以通过run方法来生成我们想要的序列化内容，如图2.2所示。

![1678435542213540.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436639420343.png "1678435542213540.png")

图2.2 序列化生成

在目标环境下进行测试发现确实可以通过URLDNS链来触发DNS请求，如图2.3，图2.4所示。

![1678435609137780.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436641175555.png "1678435609137780.png")图2.3 发送序列化的数据内容

![1678435655445204.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436641153998.png "1678435655445204.png")

上面URLDNS链的利用情况是很顺利的，也确实证明了这个位置存在反序列化漏洞。但是URLDNS链只能产生DNS请求，并不具有实际的危害，要达到RCE的效果还需要其他利用链。

2） CommonCollections链

CommonCollections链作为反序列化中最常见的链，正好在目标的源码中也存在相应的jar包，如图2.5所示。

![1678435744750592.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436642145937.png "1678435744750592.png")

图2.5 存在CC.jar

起初看到这个jar包是很开心的，认为已经成功了一半，直接用ysoserial中的CC链来生成对应序列化的内容，如图2.6所示。

![1678435839146197.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436642170713.png "1678435839146197.png")

图2.6 生成cc1链对应的序列化文件

但是在实际环境中却失败了，并没有收到ping发出来的dns请求，也就是命令执行失败了。目标环境是linux的，这个已经提前确认。

抱着不死心的态度，把cc1-cc7的整个7条链都试了一遍，都没有成功。基本确认应该是有问题的，这才想起我是有源码的，虽然这个源码并不能完整的搭建，但是调试反序列化还是完全可行的，在目标源码中来反序列化刚才用yso生成的序列化的文件，如图2.7所示。

![1678436177771789.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436644407563.png "1678436177771789.png")

图2.7 目标环境下反序列化cc.ser报错

从图2.7的报错中可以看出这里爆出org.apache.commons.collections.functors.InvokerTransformer反序列化中的异常，根本原因在于目标环境中的InvokerTransformer没有继承Serializable接口，如图2.8所示。

![1678436228195820.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436645132362.png "1678436228195820.png")

图2.8 目标环境下InvokerTransformer类继承情况

这应该是apache官方修复CommonCollections包导致反序列化利用的一种修复方式，所以这里就没办法继续使用CC链来进行攻击了。

3） CommonsBeanutils链

CC链虽然不能用了，但是在系统存在的jar包中发现了CB链对应的jar包，如图2.9所示。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436645174463.png "1678436280169435.png")

图2.9 存在CB.jar

从版本来看是属于有漏洞的版本，但是实际测试的时候还是没有成功，用同样的方式在本地进行调试，报错如图2.10所示。

![1678436306157948.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436646152769.png "1678436306157948.png")

图2.10 直接使用CB链生成的payload反序列化报错

从网上找了一下这个报错的原因，是因为commons-beanutils版本不一致导致的错误。如果两个不同版本的库使用了同一个类，而这两个类可能有一些方法和属性有了变化，此时在序列化通信的时候就可能因为不兼容导致出现隐患。因此，Java在反序列化的时候提供了一个机制，序列化时会根据类的属性和方法，通过固定算法计算出一个当前类的serialVersionUID值，写入数据流中；反序列化时，如果发现对方的环境中这个类计算出的serialVersionUID不同，则反序列化就会异常退出，避免后续的未知隐患。

找到了问题的原因，那解决办法也就很简单了，为了避免其他包的版本不一致导致问题，我直接把ysoserial的源码拷贝到目标源码中来执行，使用目标源码的jar包来作为依赖。如图2.11，图2.12所示

![1678436402109088.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436647138738.png "1678436402109088.png")

图2.11 发送CB链生成的序列化数据

![1678436472163168.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678436648432838.png "1678436472163168.png")

图2.12 使用ping命令查看的DNS日志

到这一步，已经通过CB链来达到RCE的效果。

**0x03 结论**

1、 并不是所有的CommonCollections3.2都是可以作为反序列化利用链

2、 CommonsBeanutils链生成的payload会因为自身jar包版本不同导致serialVersionUID报错

3、 如果直接用ysoserial生成的payload不成功，可以在目标源码环境下来调试，避免jar包版本异常导致的错误

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?b9A3iTZ2)

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

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/9ZO4)

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