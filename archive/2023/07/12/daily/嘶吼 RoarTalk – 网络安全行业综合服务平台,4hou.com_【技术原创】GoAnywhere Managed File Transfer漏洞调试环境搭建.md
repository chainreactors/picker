---
title: 【技术原创】GoAnywhere Managed File Transfer漏洞调试环境搭建
url: https://www.4hou.com/posts/yk07
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-12
fetch_date: 2025-10-04T11:51:25.474453
---

# 【技术原创】GoAnywhere Managed File Transfer漏洞调试环境搭建

【技术原创】GoAnywhere Managed File Transfer漏洞调试环境搭建 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】GoAnywhere Managed File Transfer漏洞调试环境搭建

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-07-11 11:55:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105504

收藏

导语：本文记录从零开始搭建GoAnywhere Managed File Transfer漏洞调试环境的细节。

**0x00 前言**

本文记录从零开始搭建GoAnywhere Managed File Transfer漏洞调试环境的细节。

**0x01 简介**

本文将要介绍以下内容：

GoAnywhere Managed File Transfer安装

GoAnywhere Managed File Transfer漏洞调试环境配置

数据库操作

**0x02 GoAnywhere Managed File Transfer安装**

参考资料：https://static.fortra.com/goanywhere/pdfs/guides/ga6\_8\_6\_installation\_guide.pdf

下载地址：https://www.goanywhere.com/products/goanywhere-free/download

需要注册账号获得license

GoAnywhere Managed File Transfer可以分别安装在Windows和Linux操作系统

Windows系统下默认的Web路径：C:\Program Files\HelpSystems\GoAnywhere\tomcat\webapps\ROOT

Linux系统下默认的Web路径：/usr/local/HelpSystems/GoAnywhere/tomcat/webapps/ROOT

**1.开启远程调试功能**

通过开启Tomcat调试功能来实现，开启Tomcat调试功能的方法如下：

切换至bin目录

执行命令:catalina jpda start

Tomcat调试功能开启后默认监听本地8000端口

对于GoAnywhere Managed File Transfer，开启调试功能的方法如下：

(1)Windows下调试

修改文件C:\Program Files\HelpSystems\GoAnywhere\tomcat\bin\GoAnywhere.exe的文件属性

双击文件C:\Program Files\HelpSystems\GoAnywhere\tomcat\bin\GoAnywhere.exe，切换到Java标签页，在Java Optinos添加：-agentlib:jdwp=transport=dt\_socket,server=y,suspend=n,address=8090，如下图

重启服务GoAnywhere

(2)Linux调试

修改文件：/opt/HelpSystems/GoAnywhere/tomcat/bin/start\_tomcat.sh，将exec "$PRGDIR"/"$EXECUTABLE" start "$@"修改为exec "$PRGDIR"/"$EXECUTABLE" jpda start "$@"

修改文件: /opt/HelpSystems/GoAnywhere/tomcat/bin/goanywhere\_catalina.sh，将JPDA\_ADDRESS="localhost:8000"修改为JPDA\_ADDRESS="\*:8090"

注：

Tomcat默认的调试端口8000同GoAnywhere Managed File Transfer的Web端口冲突，所以这里选择修改Tomcat默认的调试端口为8090

打开防火墙允许外部访问8090端口：iptables -I INPUT -p tcp --dport 8090 -j ACCEPT

启动GoAnywhere进程：/opt/HelpSystems/GoAnywhere/goanywhere.sh start

**0x03 数据库操作**

GoAnywhere Managed File Transfer使用Apache Derby数据库

Windows下默认数据库存储位置为：C:\Program Files\HelpSystems\GoAnywhere\userdata\database\goanywhere

Linux下默认数据库存储位置为：/opt/HelpSystems/GoAnywhere/userdata/database/goanywhere/

数据库操作的实现细节可从lib文件夹下的ga\_classes.jar获得

从中我们可以得到Web用户口令加密的实现细节，对应位置：C:\Program Files\HelpSystems\GoAnywhere\lib\ga\_classes.jar!\com\linoma\ga\ui\admin\action\user\ChangeUserPasswordAction.class

提取出的Java实现代码如下：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677835495211743.png "1677835367147763.png")

**1.读取Derby数据库**

(1)命令行实现

使用Apache Derby，下载地址：https://archive.apache.org/dist/db/derby/db-derby-10.14.2.0/db-derby-10.14.2.0-bin.zip

运行bin目录下的ij.bat

连接数据库：connect 'jdbc:derby:C:\Program Files\HelpSystems\GoAnywhere\userdata\database\goanywhere;';

查询用户配置：SELECT \* FROM DPA\_USER;

(2)界面化实现

使用DBSchema，下载地址：https://dbschema.com/download.html

启动DBSchema后，选择连接Derby数据库，JDBC Driver选择derbytools.jar org.apache.derby.jdbc.EmbeddedDriver，Folder选择C:\Program Files\HelpSystems\GoAnywhere\userdata\database\goanywhere

查询用户数据表，如下图

![下载.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677835496195940.png "1677835450303986.png")

可以看到默认用户有以下三个：

Administrator，未启用

root，未启用

admin，默认用户

**2.修改数据库**

GoAnywhere Managed File Transfer的Derby数据库使用了内嵌模式，其他应用程序不可访问，所以有以下两种修改数据的方法：

(1)GoAnywhere Managed File Transfer处于运行状态

可以通过写入jsp文件实现数据库的修改

(2)GoAnywhere Managed File Transfer处于关闭状态

可以选择Apache Derby或DBSchema打开数据库文件夹，直接进行修改

修改数据库的命令示例：

启用root用户： UPDATE APP.DPA\_USER SET ENABLED='1' WHERE USER\_NAME='root';

设置root用户口令：UPDATE APP.DPA\_USER SET USER\_PASS='$5$mpoe6zI4B6+LHRMdbFKr8g==$RnAILbYe9KDauKE3wXTFVvlXQNZeM4Z2c7x1aEtME/U=' WHERE USER\_NAME='root';

**0x04 小结**

在我们搭建好GoAnywhere Managed File Transfer漏洞调试环境后，接下来就可以着手对漏洞进行学习。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?i6IimITa)

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