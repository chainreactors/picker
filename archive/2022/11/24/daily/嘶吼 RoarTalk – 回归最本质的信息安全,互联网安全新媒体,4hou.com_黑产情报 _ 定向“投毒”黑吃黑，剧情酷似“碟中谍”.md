---
title: 黑产情报 | 定向“投毒”黑吃黑，剧情酷似“碟中谍”
url: https://www.4hou.com/posts/KENJ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-24
fetch_date: 2025-10-03T23:36:49.784426
---

# 黑产情报 | 定向“投毒”黑吃黑，剧情酷似“碟中谍”

黑产情报 | 定向“投毒”黑吃黑，剧情酷似“碟中谍” - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑产情报 | 定向“投毒”黑吃黑，剧情酷似“碟中谍”

360反诈中心
[行业](https://www.4hou.com/category/industry)
2022-11-23 10:39:45

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)803606

收藏

导语：这……狠起来连“自己人”都黑

![banner.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668567588964036.png "1668567588964036.png")

黑产江湖纷争不断

而今天要说剧情酷似“碟中谍”

Did you hear me?

The list is in the open.

你听见了吗？名单已经外泄。

——《碟中谍》

故事要从最早我们熟知的微商套路说起，微商朋友圈最常晒的除了豪车豪宅、名包名表，还有各种收款截图，营造一种轻轻松松赚大钱的迷惑氛围，当然最终目的就是：卖产品、招代理，“收割”这路子算是就这么打开了。

再后来，在一些诈骗案件中，也发现了不法分子制作虚假的转账截图行骗的情况。

从早期的调研情况看，此类截图很多来自于转账生成器或图片生成网站，类似于图片模板，快速生成银行转账截图、身份证照片。

这就有一个问题

如果对方要求提供录制的转账视频

这种手法显然无法满足

近期在黑灰产渠道，捕获到部分仿冒银行类应用，这些仿冒应用的作用原理就是通过云端配置+仿冒银行APP上下游配合，实现定制化的虚假转账过程，再录制转账视频，其效果比转账生成器或图片生成网站更加逼真。

在对产业分析的过程中，发现黑灰产人员一方面利用此类仿冒银行APP录制虚假转账视频进行欺诈行为，一方面利用仿冒银行APP为噱头，针对黑产人员群体进行定向投毒，增加自己的“肉鸡“数量及设备数据。

**仿冒银行APP，可伪造转账截图和银行流水**

根据情报渠道的演示视频，在管理后台，设置转账后的效果，如转账成功、转账失败、账户已冻结。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668566986786435.png "1668566561153803.png")

在仿冒银行APP中输入任意账户转账，可以得到最终的转账效果。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668566987105962.png "1668566607102152.png") 通过管理后台，还可以设置银行卡的信息、银行流水情况。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668566989159492.png "1668566617114874.png") 仿冒银行APP将展示伪造后的银行转账信息。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668566990334303.png "1668566676102088.png")黑产在玩一种很新的东西？

不确定，再看看

**仿冒银行APP生产链路分析**

从黑产渠道获取的多个样本APP下载链皆指向同一域名A，虽然应用已失效，但不同的仿冒APP皆对应域名A下不同的子域名。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668566992117011.png "1668566933523078.png")

对仿冒APP的通联域名，其使用的服务器时间线进行了梳理发现，每个2个月就更换服务器，这也比较符合黑产的行为特征。

故推测仿冒APP自2022年3月份上线后，期间通过不同的域名、不同的服务器生成不同的包名、签名应用，并存活至今。

终于！！！

最绝的定向“投毒”环节来了

**关联黑吃黑手法**

在黑灰产交流群里，群主除提供仿冒APP的下载链外，还同步提供仿冒APP的管理后台程序，而这个程序是一个带“毒”的zip格式压缩包。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668566985677465.png "1668566985677465.png")

经过分析发现，该压缩包程序实际上是远控类木马，比对多个威胁情报平台捕获到的同源样本来看，木马伪装的程序名称包括接码、代付、诈骗话术等与黑产相关的“黑话”，推测“投毒”的目标是黑灰产从业人员。

这就很有意思了

黑产人员在给同行提供便利的同时

自己还留了后门

而通过这个后门

可以随时控制“肉鸡”设备

这……狠起来连“自己人”都黑

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?MxGgOT94)

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

![](https://img.4hou.com/portraits/068e4092bab6e0b00b3c9e62609dd402.png)

# [360反诈中心](https://www.4hou.com/member/mx20)

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

[查看更多](https://www.4hou.com/member/mx20)

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