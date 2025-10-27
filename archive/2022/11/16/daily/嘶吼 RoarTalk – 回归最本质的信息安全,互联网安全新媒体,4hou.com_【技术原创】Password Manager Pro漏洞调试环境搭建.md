---
title: 【技术原创】Password Manager Pro漏洞调试环境搭建
url: https://www.4hou.com/posts/QLBq
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-16
fetch_date: 2025-10-03T22:51:57.236222
---

# 【技术原创】Password Manager Pro漏洞调试环境搭建

【技术原创】Password Manager Pro漏洞调试环境搭建 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】Password Manager Pro漏洞调试环境搭建

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-11-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)167168

收藏

导语：本文记录从零开始搭建Password Manager Pro漏洞调试环境的细节。

**0x00 前言**

本文记录从零开始搭建Password Manager Pro漏洞调试环境的细节。

**0x01 简介**

本文将要介绍以下内容：

Password Manager Pro安装

Password Manager Pro漏洞调试环境配置

数据库连接

**0x02 Password Manager Pro安装**

**1.下载**

最新版下载地址：https://www.manageengine.com/products/passwordmanagerpro/download.html

旧版本下载地址：https://archives2.manageengine.com/passwordmanagerpro/

最新版默认可免费试用30天，旧版本在使用时需要合法的License

注：

我在测试过程中，得出的结论是如果缺少合法的License，旧版本在使用时只能启动一次，第二次启动时会提示没有合法的License

**2.安装**

系统要求：https://www.manageengine.com/products/passwordmanagerpro/system-requirements.html

对于Windows系统，需要Win7以上的系统，Win7不支持

默认安装路径：C:\Program Files\ManageEngine\PMP

**3.测试**

安装成功后选择Start PMP Service

访问https://localhost:7272

默认登录用户名：admin

默认登录口令：admin

如下图

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282726191917.png "1665281707356942.png")

本文以Windows环境为例

**1.Password Manager Pro设置**

查看服务启动后相关的进程，如下图

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282726208741.png "1665281734482036.png")

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282727187627.png "1665281847393912.png")java进程的父进程为wrapper.exe，启动参数：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282728775787.png "1665281912265640.png")查看文件C:\Program Files\ManageEngine\PAM360\conf\wrapper.conf，找到启用调试功能的位置：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282728988019.png "1665281954115538.png")取消注释后，内容如下：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282729841950.png "1665282010706130.png")

注：

Address的配置不需要设置为address=\*:8787，会提示ERROR: transport error 202: gethostbyname: unknown host，设置address=8787就能够支持远程调试的功能

重启服务，再次查看java进程的参数：wmic process where name="java.exe" get commandline

配置修改成功，如下图

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282730112455.png "1665282060190279.png")

**2.常用jar包位置**

路径：C:\Program Files\ManageEngine\PMP\lib

web功能的实现文件为AdventNetPassTrix.jar

**3.IDEA设置**

远程调试设置如下图

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282731338834.png "1665282103392418.png")

远程调试成功，如下图

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282732222434.png "1665282143924428.png")

**0x04 数据库连接**

默认配置下，Password Manager Pro使用postgresql存储数据

配置文件路径：C:\Program Files\ManageEngine\PMP\conf\database\_params.conf

内容示例：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282733968850.png "1665282226703878.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282733447087.png "1665282236147027.png")

**1.口令破解**

数据库连接的口令被加密，加解密算法位于C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar中的com.adventnet.passtrix.ed.PMPEncryptDecryptImpl.class

密钥固定保存在com.adventnet.passtrix.db.PMPDBPasswordGenerator.class，内容为@dv3n7n3tP@55Tri\*

我们可以根据PMPEncryptDecryptImpl.class中的内容快速编写一个解密程序

解密程序可参考：https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/

注：

文章中涉及数据库口令的解密没有问题，Master Key的解密存在Bug，解决方法将在后面的文章介绍

解密获得连接口令为Eq5XZiQpHv

**2.数据库连接**

根据配置文件拼接数据库连接的命令

(1)失败的命令

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282734134141.png "1665282598759483.png")

(2)成功的命令

将localhost替换为127.0.0.1，连接成功，完整的命令为：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282734168155.png "1665282644327498.png")(3)一条命令实现连接数据库并执行数据库操作

格式为psql --command="SELECT \* FROM table;" postgresql://

示例命令：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282735366644.png "1665282678157057.png")输出如下：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665282736351019.png "1665282713198984.png")

发现password的数据内容被加密

**0x05 小结**

在我们搭建好Password Manager Pro漏洞调试环境后，接下来就可以着手对漏洞进行学习。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7VpT1bIX)

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
[RSS](https://w...