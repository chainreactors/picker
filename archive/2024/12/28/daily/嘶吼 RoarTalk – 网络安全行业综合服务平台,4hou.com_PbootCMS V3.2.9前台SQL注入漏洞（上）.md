---
title: PbootCMS V3.2.9前台SQL注入漏洞（上）
url: https://www.4hou.com/posts/zAYO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-28
fetch_date: 2025-10-06T19:36:59.163385
---

# PbootCMS V3.2.9前台SQL注入漏洞（上）

PbootCMS V3.2.9前台SQL注入漏洞（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PbootCMS V3.2.9前台SQL注入漏洞（上）

盛邦安全
[行业](https://www.4hou.com/category/industry)
2024-12-27 15:41:36

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)61013

收藏

导语：PbootCMS V3.2.9前台SQL注入漏洞（上）

**0x01 前言**

PbootCMS是全新内核且永久开源免费的PHP企业网站开发建设管理系统，是一套高效、简洁、 强悍的可免费商用的PHP CMS源码，能够满足各类企业网站开发建设的需要。系统采用简单到想哭的模板标签，只要懂HTML就可快速开发企业网站。官方提供了大量网站模板免费下载和使用，将致力于为广大开发者和企业提供最佳的网站开发建设解决方案。

PbootCMS在国内有非常大的客户使用量，属于国内最流行的企业官网建站程序。截止本文发出前，其github最新版本为V3.2.9。通过互联网资产测绘平台搜索指纹header="PbootCMS"，搜索结果有超过34W+互联网案例。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510023157151.png "1734510023157151.png")

在最新版的PbootCMS V3.2.9中存在前台未授权SQL注入漏洞，攻击者可以通过此漏洞读取系统数据库中的敏感信息，包括后台用户的用户名和密码。

**0x02 漏洞分析**

之前因为某任务进行批量任务扫描时发现很多目标都在报DVB-2021-2510漏洞，其POC大致如下，返回数据匹配到your SQL syntax或syntax error。

```
POST /index.php?p=search
1=select
```

此漏洞是很早以前已经曝出的安全漏洞，对应CVE编号为CVE-2021-28245，但是最大的问题是我在最新版本的V3.2.9上测试仍然存在此漏洞。也就是官网一直都没有修这个漏洞，如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510034190708.png "1734510034190708.png")

由于ddpoc上面的这个脚本主要做poc探测和验证，并不带直接的漏洞利用，需要跟踪源码分析漏洞逻辑。跟踪到漏洞对应的文件apps/home/controller/SearchController.php。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510041368991.png "1734510041368991.png")

PbootCMS有一套复杂的模版替换的逻辑，其中模板替换分成多个步骤，在SearchController类中会通过parserSearchLable方法对模板内容进行解析，跟踪parserSearchLable方法。parserSearchLable方法逻辑很复杂，我直接定位到最关键的部分如下。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510048113328.png "1734510048113328.png")

其中$receive来自于外部输入，遍历$receive变量，会生成新的数组$where3。$where3是后期漏洞利用的关键，但是这里先关注$value = request($key, 'vars')，看一下这里对数据的过滤逻辑。跟进request方法。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510055203491.png "1734510055203491.png")

跟进filter方法，如下图所示，当传入的d\_type(也就是request方法的第二个参数)为vars时，只能包含中文、字母、数字、横线、点、逗号、空格！。而这也为后面的SQL注入的利用埋下了伏笔。

![QQ20241218-141500.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510065701881.png "1734510065701881.png")

回到刚才提到的$where3变量，$where3变量会传入getList方法。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510072680346.png "1734510072680346.png")

继续跟进getList方法，传入的$where3传入到变量$select。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510077292093.png "1734510077292093.png")

跟进变量$select，如下图所示，可以看到其中的$select传入了where方法，这个方法是用于组合SQL语句的查询条件。

![QQ20241218-141600.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510092658726.png "1734510092658726.png")

继续跟进where方法，如下图所示。当$key也就是传入的数据是一个整数时，会直接拼接$value的值，导致SQL注入漏洞。这里为什么不用$key来注入呢？因为$key前面的图里面有限制，只能输入\w\-\.，不允许空格和特殊字符导致无法直接利用此注入点。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510099170672.png "1734510099170672.png")

**0x03 漏洞利用**

漏洞的整个流程已经梳理清楚了，下一步就是漏洞如何利用的问题了。这里由于request($key, 'vars')限制导致不能使用特殊字符。不能使用括号、单引号、注释和逗号会极大的限制整个漏洞的利用方式。

为方便大家直观看到SQL语句效果，我临时把SQL语句打印出来，如下图所示，大致是直接在括号中拼接SQL语句。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510105196430.png "1734510105196430.png")

只能使用\w和空格的注入，极大的限制了注入点的利用，但是仍然可以通过BOOL盲注的方式来达到注入的效果。

1)  使用下面的payload访问目标，显示有搜索结果

1=select 1 from ay\_user where username like 0x6125 limit 1

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510111481890.png "1734510111481890.png")

2）使用下面的payload访问目标，显示无搜索结果

1=select 1 from ay\_user where username like 0x6225 limit 1

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241218/1734510118592915.png "1734510118592915.png")

由此可以证明目标站点ay\_user（管理员用户表）第一个用户的username的第一个字母是a（第一个用户默认一般是admin）。

这里很巧妙的使用mysql的like语句支持16进制编码的特性来避免使用其它特殊字符，但是整个利用过程还是有下面的注意点：

1）仅支持PbootCMS安装选择mysql数据库的网站，PbootCMS默认情况下使用的是sqlite数据库，如果是sqlite数据库，暂时不知道如何在不引入特殊字符的情况下进行注入。

2）因为不能使用逗号，所以不能通过limit 1,1这样的方式来注第二个用户，但是可以通过增加条件的方式来进行注入，例如下面的payload

1=select 1 from ay\_user where username like 0x25 and username not like 0x61646d696e25 limit 1

**0****x04 结论**

DVB-2021-2510（CVE-2021-28245）是一个很好的漏洞，互联网案例足够多，影响大。这是一个经典的有条件的SQL注入漏洞，值得小伙伴们学习研究。

*在下一篇文章中，作者会带来PbootCMS更多有意思的漏洞和利用方式。*

[原文链接](https://mp.weixin.qq.com/s/0PpRUpUDUQlJHWM-qa4cyw?token=1275718495&lang=zh_CN)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7ocCAp8S)

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

[微博](http://...