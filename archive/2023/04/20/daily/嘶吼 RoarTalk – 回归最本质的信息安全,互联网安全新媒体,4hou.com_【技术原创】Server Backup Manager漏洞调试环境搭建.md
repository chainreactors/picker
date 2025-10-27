---
title: 【技术原创】Server Backup Manager漏洞调试环境搭建
url: https://www.4hou.com/posts/ZXJ5
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-20
fetch_date: 2025-10-04T11:31:36.747456
---

# 【技术原创】Server Backup Manager漏洞调试环境搭建

【技术原创】Server Backup Manager漏洞调试环境搭建 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】Server Backup Manager漏洞调试环境搭建

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-04-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)104232

收藏

导语：本文介绍了在搭建Server Backup Manager调试环境过程中一些问题的解决方法，分析用户数据库文件提取的方法，给出检测CVE-2022-36537的建议。

**0x00 前言**

Server Backup Manager(SBM)是一种快速、经济且高性能的备份软件，适用于物理和虚拟环境中的Linux和Windows服务器。本文将要介绍Server Backup Manager漏洞调试环境的搭建方法。

**0x01 简介**

本文将要介绍以下内容：

环境搭建

调试环境搭建

用户数据库文件提取

CVE-2022-36537简要介绍

**0x02 环境搭建**

安装参考资料：http://wiki.r1soft.com/display/ServerBackupManager/Install+and+Upgrade+Server+Backup+Manager+on+Debian+and+Ubuntu.html

参考资料提供了两种安装方法，但是我在测试过程中均遇到了缺少文件/etc/init.d/cdp-server的错误

这里改用安装旧版本的Server Backup Manager，成功完成安装，具体方法如下：

**1.下载安装包**

http://r1soft.mirror.iweb.ca/repo.r1soft.com/release/6.2.2/78/trials/R1soft-ServerBackup-Manager-SE-linux64-6-2-2.zip

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729436112527.png "1672727540554080.png")

web管理页面有以下两个:

http://127.0.0.1:8080

https://127.0.0.1:8443

**0x03 调试环境搭建**

研究过程如下：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729437147997.png "1672727623178999.png")

(6)

使用IDEA下断点并配置远程调试，远程调试成功如下图

![下载.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729439179379.png "1672727726424290.png")**0x04 用户数据库文件提取**

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729440889389.png "1672727798216212.png")![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729441839647.png "1672728826127702.png")![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729442451533.png "1672728877539753.png")![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729443695887.png "1672728930703103.png")

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729443688879.png "1672728954367342.png")![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729444417144.png "1672729011790296.png")

从以上代码可以得出用户口令的加密算法

(2)定位用户创建的具体代码实现位置

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729445141859.png "1672729076196530.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729446134916.png "1672729105116862.png")![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729447197037.png "1672729149104687.png")![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729447184010.png "1672729220200763.png")![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729448976560.png "1672729250666684.png")![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729449144828.png "1672729279985473.png")![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729450238282.png "1672729313204670.png")

**0x05 CVE-2022-36537简要介绍**

漏洞分析文章：https://medium.com/numen-cyber-labs/cve-2022-36537-vulnerability-technical-analysis-with-exp-667401766746

文章中提到触发RCE需要上传一个带有Payload的com.mysql.jdbc.Driver文件

这个操作只能利用一次，原因如下：

默认情况下，管理后台的的Database Driver页面存在可以上传的图标，如下图

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729451131639.png "1672729359126681.png")上传后不再显示可上传的图标，如下图

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729454187318.png "1672729390185023.png")![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672729455192518.png "1672729427103401.png")

**0x06 小结**

本文介绍了在搭建Server Backup Manager调试环境过程中一些问题的解决方法，分析用户数据库文件提取的方法，给出检测CVE-2022-36537的建议。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?PiwfqNbO)

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