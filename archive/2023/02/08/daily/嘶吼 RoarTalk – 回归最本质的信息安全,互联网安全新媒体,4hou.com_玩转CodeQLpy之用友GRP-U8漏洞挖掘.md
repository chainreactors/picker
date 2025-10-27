---
title: 玩转CodeQLpy之用友GRP-U8漏洞挖掘
url: https://www.4hou.com/posts/3JZO
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-08
fetch_date: 2025-10-04T05:56:23.417388
---

# 玩转CodeQLpy之用友GRP-U8漏洞挖掘

玩转CodeQLpy之用友GRP-U8漏洞挖掘 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 玩转CodeQLpy之用友GRP-U8漏洞挖掘

盛邦安全
[漏洞](https://www.4hou.com/category/vulnerable)
2023-02-07 10:54:52

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)188790

收藏

导语：本文旨在阐述CodeQLpy在代码审计中的作用，文章后续所有漏洞均以提交CNVD，以此漏洞从事任何攻击行为均属于违法行为，与本文作者无关。

**0x01 前言**

CodeQLpy是作者使用python3实现的基于CodeQL的java代码审计工具，github地址https://github.com/webraybtl/CodeQLpy。

![1675737470204633.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738088210152.png "1675737470204633.png")

通过CodeQLpy可以辅助代码审计人员快速定位代码中的问题，目前支持对SprintBoot的jar包，SpringMVC的war包，直接下载的源码文件夹，maven项目源码等方式进行自动化代码审计，详细使用方式参考github。

本文旨在阐述CodeQLpy在代码审计中的作用，文章后续所有漏洞均以提交CNVD，以此漏洞从事任何攻击行为均属于违法行为，与本文作者无关。

**0x02 案例**

用友GRP-U8是一款常见的WEB应用，经常参加比赛的小伙伴一定不会对这个产品陌生，在高校和政府有不错的使用量。如图2.1所示。

![1675737521106706.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738089129526.png "1675737521106706.png")

图2.1 GRP-U8产品界面

使用CodeQLpy可以直接从目标源码中找到上百个高危的漏洞，包括但不限于反序列化，任意文件上传，任意文件删除，SQL注入，SSRF，XSS等，如图2.2所示。

![1675737556862683.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738091176940.png "1675737556862683.png")

图2.2 使用CodeQLpy之后的部分结果

总计结果数接近1000个，其中有效漏洞超过100个。找了几个有代表性的漏洞来演示。

1） 任意文件删除漏洞

POST ViewExcel?djlxid=902&url=logs/info.log.1

![1675737591100389.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738092810718.png "1675737591100389.png")

漏洞对应的代码在com.ufgov.midas.yy.servlet.ViewExcelServlet，其中用户可控的source参数是url。

![1675737618177147.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738093127502.png "1675737618177147.png")

继续跟踪readExcelContent方法，内部处理逻辑很多，可以只关注我们关心的部分。

![1675737648487673.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738094150040.png "1675737648487673.png")

继续跟踪deleteFile方法，这里可以很清晰的看的文件删除的操作。

![1675737668294015.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738095899574.png "1675737668294015.png")

2）SQL注入漏洞

/listSelectDialogServlet?slType=slFZX&slCdtn=1=2;waitfor%20delay%20'0:0:3'

![1675737697171712.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738097279842.png "1675737697171712.png")

漏洞代码在com.ufgov.midas.yy.servlet.ListSelectDialogServlet

![1675737726142543.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738098123281.png "1675737726142543.png")

继续跟踪getProjectLevel方法，这里可以很清晰的看到进行了SQL语句拼接的操作。

![1675737773145999.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738100963870.png "1675737773145999.png")

3）任意文件上传漏洞

![1675737799240950.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738102630930.png "1675737799240950.png")

上传之后会在WEB跟目录生成文件2222.jsp

漏洞代码在com.mobile.action.U8AppProxy

![1675737891172910.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738104186764.png "1675737891172910.png")

继续跟踪doGet方法

![1675737917156263.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738105821411.png "1675737917156263.png")

跟进doPost方法，当id=saveheder时会进行文件上传操作

![1675737946202702.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738106449547.png "1675737946202702.png")

跟进uploadBytes方法，这里就是标准的文件写入的操作

![1675737971146038.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738108123545.png "1675737971146038.png")

**0x03 技巧**

由于项目最终保存的结果时csv文件，不利于数据流追踪，可以结合Visual Studio Code(后续简称VS)查看完整的流。

利用CodeQLpy生成的数据库，结合CSV文件中保存的有结果的插件名称，可以在VS中复现漏洞查找过程。

1） 从项目的plugins/java或者plugins/java\_ext目录中找到漏洞扫描插件，并复制到VS中。

2） 要查看流，必须使用下面的写法，如图3.1所示。其中下面方框中的注释必须要有，并且最终的查询结果有四列，最好按照图3.1的写法。

![1675738015342460.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738109213702.png "1675738015342460.png")

图3.1 查看流的ql脚本写法

3） 查看结果中的flow流，可以看到完整的数据流，如图3.2所示。

![1675738052271591.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675738110453676.png "1675738052271591.png")

图3.2 查询ql完整的flow流

**0x04 总结**

类似的漏洞还有几百个，把发现漏洞交给工具，把验证漏洞留给自己。目前工具仍处于前期测试阶段，如果有任何bug请在github的issue中提出。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KMot0OVc)

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
[知乎](https://zhuanlan.zhihu.com/roartal...