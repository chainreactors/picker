---
title: 【技术原创】vRealize Log Insight漏洞调试环境搭建
url: https://www.4hou.com/posts/xjP9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-13
fetch_date: 2025-10-04T11:44:33.721501
---

# 【技术原创】vRealize Log Insight漏洞调试环境搭建

【技术原创】vRealize Log Insight漏洞调试环境搭建 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】vRealize Log Insight漏洞调试环境搭建

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-06-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)128400

收藏

导语：本文记录从零开始搭建vRealize Log Insight漏洞调试环境的细节。

**0x00 前言**

本文记录从零开始搭建vRealize Log Insight漏洞调试环境的细节。

**0x01 简介**

本文将要介绍以下内容：

vRealize Log Insight安装

vRealize Log Insight漏洞调试环境配置

数据库操作

**0x02 vRealize Log Insight安装**

参考资料： https://docs.vmware.com/en/vRealize-Log-Insight/index.html

**1.下载OVA文件**

下载页面：https://customerconnect.vmware.com/evalcenter?p=vr-li

下载前需要先注册用户，之后选择需要的版本进行下载

**2.安装**

(1)在VMware Workstation中导入OVA文件

(2)配置

访问配置页面https://

选择Starting New Deployment，设置admin用户口令

**3.开启远程调试功能**

(1)查看所有服务的状态

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834169635817.png "1677833510986927.png")

![下载.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834170208245.png "1677833543123898.png")

定位到web相关的服务为loginsight.service

(2)查看loginsight.service的具体信息

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834170125204.png "1677833586190639.png")

结果如下图

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834170380587.png "1677833627173516.png")

定位到服务启动文件：/usr/lib/loginsight/application/bin/loginsight

(3)查看进程参数

执行命令：ps aux|grep java

返回结果：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834171184109.png "1677833723193653.png")![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834173993632.png "1677833733139221.png")![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834174541204.png "1677833742118404.png")![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834175161464.png "1677833752152940.png")结果分析如下：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834175106478.png "1677833817111588.png")![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834176206490.png "1677833825103612.png")

**0x03 数据库操作**

**1.重置web登陆用户admin口令**

实现文件：/usr/lib/loginsight/application/sbin/li-reset-admin-passwd.sh

从文件中可以获得数据库操作的相关信息，如下图

![下载 (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834177139890.png "1677833870528702.png")

**2.连接数据库的命令参数**

实现文件：/usr/lib/loginsight/application/lib/apache-cassandra-3.11.11/bin/cqlsh-no-pass

文件内容如下：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834178107947.png "1677833937993673.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834178200028.png "1677833946859058.png")![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834179142026.png "1677833973212254.png")

**3.连接数据库的用户名口令**

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834179875930.png "1677834012124895.png")

**4.连接数据库的配置信息**

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834180201228.png "1677834059212935.png")

(1)使用封装好参数的文件

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834180482437.png "1677834100137500.png")

(2)使用参数连接

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834181797487.png "1677834130199599.png")

从返回结果可以看到数据库使用了CQL(Cassandra Query Language)

查询用户配置的命令：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834181832320.png "1677834158146305.png")

**5.界面化操作数据库**

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834199597760.png "1677834199597760.png")![下载 (2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677834217393477.png "1677834217393477.png")

**0x04 小结**

在我们搭建好vRealize Log Insight漏洞调试环境后，接下来就可以着手对漏洞进行学习。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?cUGXL1nD)

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