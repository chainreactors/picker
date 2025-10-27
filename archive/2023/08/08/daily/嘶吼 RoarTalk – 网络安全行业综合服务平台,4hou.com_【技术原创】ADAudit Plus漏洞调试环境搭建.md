---
title: 【技术原创】ADAudit Plus漏洞调试环境搭建
url: https://www.4hou.com/posts/L18W
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-08
fetch_date: 2025-10-04T11:59:57.731714
---

# 【技术原创】ADAudit Plus漏洞调试环境搭建

【技术原创】ADAudit Plus漏洞调试环境搭建 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】ADAudit Plus漏洞调试环境搭建

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-08-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)108900

收藏

导语：本文记录从零开始搭建ADAudit Plus漏洞调试环境的细节，介绍数据库用户口令的获取方法。

**0x00 前言**

本文记录从零开始搭建ADAudit Plus漏洞调试环境的细节，介绍数据库用户口令的获取方法。

**0x01 简介**

本文将要介绍以下内容：

ADAudit Plus安装

ADAudit Plus漏洞调试环境配置

数据库用户口令获取

**0x02 ADAudit Plus安装**

**1.下载**

全版本下载地址：https://archives2.manageengine.com/active-directory-audit/

**2.安装**

安装参考：https://www.manageengine.com/products/active-directory-audit/quick-start-**guide-overview.html**

**3.测试**

访问https://localhost:8081

**0x03 ADAudit Plus漏洞调试环境配置**

方法同Password Manager Pro漏洞调试环境配置基本类似

**1.开启调试功能**

(1)定位配置文件

查看java进程的信息，这里分别有两个java进程，对应两个不同的父进程wrapper.exe，如下图

wrapper.exe的进程参数分别为：

“C:\Program Files\ManageEngine\ADAudit Plus\bin\Wrapper.exe” -c “C:\Program Files\ManageEngine\ADAudit Plus\bin\..\conf\wrapper.conf”

“C:\Program Files\ManageEngine\ADAudit Plus\bin\wrapper.exe” -s “C:\Program Files\ManageEngine\ADAudit Plus\apps\dataengine-xnode\conf\wrapper.conf”

这里需要修改的配置文件为C:\Program Files\ManageEngine\ADAudit Plus\conf\wrapper.conf

(2)修改配置文件添加调试参数

找到启用调试功能的位置：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413163113919.png "1682412675198920.png")

将其修改为

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413164164330.png "1682412684645580.png")

注：

序号需要逐个递增，此处将wrapper.java.additional.3=-Xdebug修改为wrapper.java.additional.25=-Xdebug

(3)重新启动相关进程

关闭进程wrapper.exe和对应的子进程java.exe

在命令行下执行命令：

![微信截图_20230425165255.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413164169212.png "1682412722164220.png")

**2.常用jar包位置**

路径：C:\Program Files\ManageEngine\ADAudit Plus\lib

web功能的实现文件为AdventNetADAPServer.jar和AdventNetADAPClient.jar

**3.IDEA设置**

设置为Remote JVM Debug，远程调试成功如下图

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413165116868.png "1682412761177728.png")

**0x04 数据库用户口令获取**

默认配置下，ADAudit Plus使用postgresql存储数据，默认配置了两个登录用户：adap和postgres

**1.用户adap的口令获取**

配置文件路径：C:\Program Files\ManageEngine\ADAudit Plus\conf\database\_params.conf，内容示例：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413166178274.png "1682412829205191.png")![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413166105114.png "1682412839210202.png")

其中，password被加密，加解密算法位于：C:\Program Files\ManageEngine\ADAudit Plus\lib\framework-tools.jar中的com.zoho.framework.utils.crypto->CryptoUtil.class

经过代码分析，得出以下解密方法：

密钥固定保存在C:\Program Files\ManageEngine\ADAudit Plus\conf\customer-config.xml，内容示例：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413167607333.png "1682412879638026.png")

得到密钥：CryptTag为8ElrDgofXtbrMAtNQBqy

根据以上得到的密文cb26b920b56fed8d085d71f63bdd79c55ea7b98f8794699562c06ea1bedbec52087b394f和密钥8ElrDgofXtbrMAtNQBqy，编写解密程序，代码如下：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413168213197.png "1682412994509676.png")![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413168109500.png "1682413003307614.png")![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413170741853.png "1682413013571305.png")

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413171448420.png "1682413022979423.png")

程序运行后得到解密结果：Adaudit@123$

拼接出数据库的连接命令："C:\Program Files\ManageEngine\ADAudit Plus\pgsql\bin\psql" "host=127.0.0.1 port=33307 dbname=adap user=adaudit password=Adaudit@123$"

连接成功，如下图

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413171110270.png "1682413057895801.png")

**2.用户postgres的口令获取**

口令硬编码于C:\Program Files\ManageEngine\ADAudit Plus\lib\AdventnetADAPServer.jar中的com.adventnet.sym.adsm.common.server.mssql.tools->ChangeDBServer.class->isDBServerRunning()，如下图

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413172591165.png "1682413088460276.png")

得到用户postgres的口令为Stonebraker

拼接出数据库的连接命令："C:\Program Files\ManageEngine\ADAudit Plus\pgsql\bin\psql" "host=127.0.0.1 port=33307 dbname=adap user=postgres password=Stonebraker"

连接成功，如下图

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413172305323.png "1682413117152171.png")

一条命令实现连接数据库并执行数据库操作的命令示例："C:\Program Files\ManageEngine\ADAudit Plus\pgsql\bin\psql" --command="SELECT \* FROM public.aaapassword ORDER BY password\_id ASC;" postgresql://postgres:Stonebraker@127.0.0.1:33307/adap

返回结果示例：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682413173658959.png "1682413154116421.png")

发现password的数据内容被加密

**0x05 小结**

在我们搭建好ADAudit Plus漏洞调试环境后，接下来就可以着手对漏洞进行学习。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0V33Jh07)

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
[更新日志](https://www.4hou.com/about?title=更新...