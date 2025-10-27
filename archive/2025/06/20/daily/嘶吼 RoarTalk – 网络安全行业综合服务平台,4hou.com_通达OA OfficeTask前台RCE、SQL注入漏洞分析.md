---
title: 通达OA OfficeTask前台RCE、SQL注入漏洞分析
url: https://www.4hou.com/posts/pnjp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-20
fetch_date: 2025-10-06T22:50:24.684555
---

# 通达OA OfficeTask前台RCE、SQL注入漏洞分析

通达OA OfficeTask前台RCE、SQL注入漏洞分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 通达OA OfficeTask前台RCE、SQL注入漏洞分析

盛邦安全
[行业](https://www.4hou.com/category/industry)
2025-06-19 10:10:15

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)37270

收藏

导语：通达OA OfficeTask前台RCE、SQL注入漏洞分析

**一、漏洞概述**

**注:本文仅以安全研究为目的,分享对该漏洞的挖掘过程,文中涉及的所有漏洞均已报送给国家单位,请勿用做非法用途。**

通达OA是国内常用的智能办公系统，为各行业不同规模的众多用户提供信息化管理能力，包括流程审批、行政办公、日常事务、数据统计分析、即时通讯、移动办公等，帮助广大用户降低沟通和管理成本，提升生产和决策效率。

其组件定时任务服务OfficeTask开放udp端口2397，未授权接收数据，并根据数据中的命令控制字符串，执行指定任务。导致存在未授权任意php文件执行、SQL注入漏洞。

**二、影响范围**

最新版通达OA 13.2（更新时间2025-02-14 13:39）

**三、漏洞分析**

使用的版本为官网最新版，通达OA（V13版）13.2。下载地址：

```
https://www.tongda2000.com/download/p2024.php
```

![QQ20250528-114355.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404192157758.png "1748403837121728.png")

安装好后，将创建通达定时任务服务Office\_Task，并开机自启动。

![QQ20250528-114424.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404193159887.png "1748403862947029.png")

通达定时任务服务OfficeTask.exe在0.0.0.0地址开放UDP端口2397，可以被外部直接访问。

![QQ20250528-114449.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404193680057.png "1748403901769102.png")

OfficeTask.exe从2397端口接收到数据后，根据数据中的命令控制字符串，执行指定任务。命令控制字符串与命令参数以空格分隔，任务包括执行php文件，更新、备份数据库等。

![QQ20250528-114456.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404194612882.png "1748403914478492.png")

**四、前台RCE漏洞**

其中命令字符串EXEC\_HTTP\_TASK\_0表示执行指定php文件，命令参数为：php文件名和路径，可控。命令格式为：EXEC\_HTTP\_TASK\_0  \..\poc.php。

![QQ20250528-114552.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404195105256.png "1748403955214243.png")

最终将创建php.exe进程，将需要执行的php文件拼接上通达OA默认安装路径C:\MYOA\webroot\，一同作为参数传递给php.exe进程执行。具体执行的命令，还会保存到默认目录下的C:\MYOA\logs\Office\_Task.log日志文件中。

![QQ20250528-114615.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404196108116.png "1748403975575788.png")

由于是调用php.exe程序来执行，并不能像日志中看到的那样直接闭合双引号来实现任意命令执行，只能通过执行恶意的php脚本文件来RCE。

![QQ20250528-114636.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404197118959.png "1748403997344142.png")

php.exe命令执行时通过-f参数传递待执行的php文件，但是这里并不限制文件后缀必须为php。所以可以通过下面的方式分成两步来达到RCE效果。

![QQ20250528-114657.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404198265408.png "1748404017362667.png")

命令执行成功之后会在网站根目录生成一句话木马，文件路径为webshell /logon.php。

![QQ20250528-114716.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404199346279.png "1748404035998195.png")

对于旧版本（V12.9及以前的版本）的通达OA需要把EXEC\_HTTP\_TASK\_0替换为EXEC\_HTTP\_TASK。

**五、前台SQL注入漏洞**

其中FILE\_SORT\_UPD\_3命令字符串将执行SQL语句update更新数据库表FILE\_SORT的内容。

![QQ20250528-114802.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404200561628.png "1748404084201586.png")

SQL语句中的SORT\_ID值和更新的内容可控，未做任何过滤，存在SQL注入漏洞。

![QQ20250528-114826.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404200167442.png "1748404106202851.png")

比如执行如下FILE\_SORT\_UPD\_3命令：

![QQ20250528-114846.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404201776419.png "1748404127172062.png")

再查看file\_sort表，其中sort\_id=1的SORT\_NAME数据修改为2，这表明SQL注入已经成功。

![QQ20250528-114909.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404202968787.png "1748404149565805.png")

通过上面的分析可以看出此漏洞属于update类型的SQL注入漏洞，只能进行盲注，并且不支持多语句。为了更好的利用此漏洞，作者直接给出可以利用此漏洞通过bool盲注获取数据库中管理员用户密码的exp脚本。

![QQ20250528-114939.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250528/1748404203117398.png "1748404180153914.png")

对于旧版本（V12.9及以前的版本）的通达OA需要把FILE\_SORT\_UPD\_3替换为FILE\_SORT\_UPD。

**六、参考链接**

```
https://www.ddpoc.com/DVB-2025-8979.html
https://www.ddpoc.com/DVB-2025-8971.html
```

[原文链接](https://mp.weixin.qq.com/s/SkUghnlVQNd6Z65Ubc-KwA)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?MSutDpIL)

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