---
title: 【技术原创】域渗透——利用GPO中的脚本实现远程执行
url: https://www.4hou.com/posts/RBxE
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-15
fetch_date: 2025-10-04T06:35:41.505576
---

# 【技术原创】域渗透——利用GPO中的脚本实现远程执行

【技术原创】域渗透——利用GPO中的脚本实现远程执行 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】域渗透——利用GPO中的脚本实现远程执行

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-02-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)121919

收藏

导语：本文将要介绍类似的另外一种方法：通过域组策略(Group Policy Object)的脚本实现远程执行。

**0x00 前言**

在之前的文章《域渗透——利用GPO中的计划任务实现远程执行》介绍了通过域组策略(Group Policy Object)远程执行计划任务的方法，本文将要介绍类似的另外一种方法：通过域组策略(Group Policy Object)的脚本实现远程执行。

**0x01 简介**

本文将要介绍以下内容:

通过Group Policy Management Console (GPMC) 实现脚本的远程执行

通过命令行实现脚本的远程执行

新建GPO实现远程执行

修改已有的GPO，实现远程执行

实现细节

**0x02 通过Group Policy Management Console (GPMC) 实现脚本的远程执行**

**1、创建GPO**

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715897898626.png "1672714339132472.png")

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715900802567.png "1672714553514003.png")![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715901614244.png "1672714562117749.png")![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715902187510.png "1672714572797536.png")

**0x03 通过命令行实现脚本的远程执行**

**1.作用于全域**

**![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715903495078.png "1672714684718941.png")![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715904105642.png "1672714697199943.png")****2.作用于指定目标**

**![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715905145000.png "1672715593156882.png")![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715906969001.png "1672715559148891.png")**

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715907152038.png "1672715639185896.png")

**0x04 修改已有的GPO，实现远程执行**

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715909165827.png "1672715702152326.png")![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715909944024.png "1672715740397364.png")![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715911159387.png "1672715769632194.png")

**0x05 直接执行远程脚本**

当我们选择直接执行组策略文件夹中的bat文件，会弹框提示无法执行，如下图

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715912197896.png "1672715833123408.png")

![27.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715912949170.png "1672715864182085.png")![28.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672715914346866.png "1672715885143804.png")

**0x06 小结**

本文介绍了通过域组策略(Group Policy Object)中的脚本实现远程执行的方法，分享实现细节和利用思路。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6bUPEJ7n)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/83af13989dee96c0471f.jpg)

# [3gstudent](https://www.4hou.com/member/bmZO)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bmZO)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)