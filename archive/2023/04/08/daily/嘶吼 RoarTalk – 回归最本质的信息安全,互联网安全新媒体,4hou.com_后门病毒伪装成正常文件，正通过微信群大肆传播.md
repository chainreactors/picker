---
title: 后门病毒伪装成正常文件，正通过微信群大肆传播
url: https://www.4hou.com/posts/1pw3
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-08
fetch_date: 2025-10-04T11:29:36.938650
---

# 后门病毒伪装成正常文件，正通过微信群大肆传播

后门病毒伪装成正常文件，正通过微信群大肆传播 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 后门病毒伪装成正常文件，正通过微信群大肆传播

火绒安全实验室
[行业](https://www.4hou.com/category/industry)
2023-04-07 09:26:19

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)98724

收藏

导语：火绒威胁情报系统监测到一款名为“DcRat”的后门病毒新变种，正通过伪装成正常文件名的方式在微信群中大肆传播。经分析发现，该病毒入侵电脑后，存在收集用户隐私信息、远控用户电脑等危害。这是继“Xidu”病毒后又一款通过伪装来诱导用户，并通过即时通讯软件传播的病毒，用户一不小心就会中招，短期内火绒已拦截数千台受影响终端，还请广大用户保持警惕。

火绒威胁情报系统监测到一款名为“DcRat”的后门病毒新变种，正通过伪装成正常文件名的方式在微信群中大肆传播。经分析发现，该病毒入侵电脑后，存在收集用户隐私信息、远控用户电脑等危害。这是继“Xidu”病毒后又一款通过伪装来诱导用户，并通过即时通讯软件传播的病毒，用户一不小心就会中招，短期内火绒已拦截数千台受影响终端，还请广大用户保持警惕。

 ![Image-0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680779955380032.png "1680779955380032.png")

病毒传播趋势图

该黑客团伙将病毒伪装成的各类文件（文档、图片、视频等）发送给微信群聊中的用户，并诱导用户打开，随后实施收集信息等恶意行为。

病毒伪装所使用的文件名列表，如下图所示：

![Image-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680779966314175.png "1680779966314175.png")

病毒伪装的文件名列表

火绒安全实验室分析发现，该病毒运行后，会窃取用户电脑中文件，并收集用户信息如用户名、操作系统版本，记录键盘、麦克风和摄像头数据。除此之外还可远程控制受害者终端执行任意操作。

为了长久驻留用户电脑中，该病毒还会添加注册表和计划任务来进行持久化。同时与安全软件做对抗，如通过加载执行远程恶意模块对抗安全软件查杀、结束安全软件进程等，行为十分恶劣。

在此，火绒工程师提醒大家时刻注意群聊中发送的陌生文件，建议先查杀再使用。目前，火绒安全产品可对上述病毒进行拦截查杀。已中毒的用户，可使用火绒【全盘扫描】彻底查杀该病毒。

![Image-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680779974111392.png "1680779974111392.png")

# **一、****样本分析**

病毒执行流程，如下图所示：

![Snipaste_2023-04-06_19-05-08.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680779999891287.png "1680779999891287.png")

病毒执行流程图

该病毒启动后，会从C&C服务器下载执行shellcode，相关代码，如下图所示：

![Image-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780027828058.png "1680780027828058.png")

下载执行shellcode

在shellcode中会内存加载.NET后门模块来躲避杀毒软件的查杀，相关代码，如下图所示：

![Image-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780038250920.png "1680780038250920.png")

shellcode内存加载.NET后门模块

该.NET后门模块为开源远控DcRat，该远控具备各种恶意功能如：键盘记录、文件窃取、远程控制、录音录像等恶意功能，大部分恶意功能都是以插件的形式下发执行。远控客户端收集受害者信息如：用户名、操作系统版本、是否存在摄像头、是否存在杀毒软件等信息（个别变种还会收集QQ号）并发送给C&C服务器，相关代码，如下图所示：

![Image-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780049207266.png "1680780049207266.png")

发送受害者信息

还会结束安全工具和安全软件进程，防止自身暴露，相关代码，如下图所示：

![Image-7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780058207569.png "1680780058207569.png")

结束安全工具和安全软件进程

还会检测虚拟机环境，相关代码，如下图所示：

![Image-8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780077126931.png "1680780077126931.png")

检测虚拟机环境

还会添加注册表和计划任务来进行持久化，相关代码，如下图所示：

![Image-9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780086124092.png "1680780086124092.png")

添加持久化

键盘记录、文件窃取、远程控制、录音录像等恶意功能都是以插件的形式下发执行，相关代码，如下图所示：

![Image-10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780095152083.png "1680780095152083.png")

接收执行插件

# **二、附录**

C&C：

![Image-11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780108168117.png "1680780108168117.png")

HASH：

![Image-12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230406/1680780115176826.png "1680780115176826.png")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ARhfXHbp)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/bd78904bb3471e1110e8.jpg)

# [火绒安全实验室](https://www.4hou.com/member/ep86)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/ep86)

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