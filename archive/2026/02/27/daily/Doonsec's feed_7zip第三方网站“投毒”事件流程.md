---
title: 7zip第三方网站“投毒”事件流程
url: https://mp.weixin.qq.com/s/9GfscqhyjwW6WLaa6XDluQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:58:54.848494
---

# 7zip第三方网站“投毒”事件流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2xCpgJcagf9vq3XboibbH1HCYX38xl0ibZhYMKfo6MiajT6hskAsMw6peNOMxh2DPlGvAxTnTglQze2DAlEEPXsB254rZssL9TQ2b4SwjhMnUM/0?wx_fmt=jpeg)

# 7zip第三方网站“投毒”事件流程

松杨网络安全资料库

![]()

在小说阅读器中沉浸阅读

风险通告

近期监测发现，存在仿冒 7-zip**官方网站的第三方站点，通过篡改下载链接传播恶意程序，用户下载安装后可能面临终端感染风险。**

该仿冒网站在特定时间段内将原本指向官方安装程序的下载链接替换为带有恶意可执行文件的伪装安装程序，具有较强迷惑性。

官网与仿冒网站的对比

7-zip官网： https://www.7-zip.org/

![](https://mmbiz.qpic.cn/mmbiz_png/2xCpgJcagficH3YwMbfgrNuUSJrQjPdeGBuu2h6Q8icUGLCeSLia6V9pRPH26YgDibDaVNxgpYhiaqe5lDa7gjP9ibmib5oSxtibXry5njbK5hzUgic0/640?wx_fmt=png&from=appmsg)

第三方网站：https://7-zip.com/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2xCpgJcagf96wpHh3baAz9XLPEVMFjvTVYSEo8dNURTDBpZxZ0LDLCX0gwpwsMS5yqP80n3otxOhpoyaI23kFniaswZCd9myCY0XQg4p1nNA/640?wx_fmt=png&from=appmsg)

仿冒网站在页面布局、视觉风格、下载说明等方面与官方网站高度一致，普通用户难以通过界面区分。

在正常情况下，该站点下载链接指向官方程序，但在2026年1月12日-2026年1月22日期间被替换为仿冒安装程序，从而实施“投毒”行为。

事件分析

本次事件具有以下特征：

1.域名高度相似：

通告注册与官方网站高度相似的域名，提高用户的识别难度。

2.页面完成一致：

网站界面、下载按钮、版本说明均与官网一致，提高用户的信任。

3.特定时间段替换文件：

长期挂载官方安装程序，在特定的时间段将指向官方安装程序的链接替换为恶意程序的链接。

4.利用软件下载环节实施供应链攻击：

攻击的目标不是软件本身，而是利用用户对软件的信任作为突破口。

此次事件是一例经典的供应链投毒事件。

攻击链路

1.引流阶段

通过注册与官网相似域名如https://7-zip.com，样式与官网页面相同，提升可信度。

用户可通过搜索引擎结果进入仿冒网站。

2.下载阶段

仿冒网站下载链接常态指向官方安装程序。但在2026年1月12日-1月22日期间，下载链接被替换成伪装成7-zip安装程序的恶意可执行文件，该文件文件名、图标、版本信息与官方版本高度一致。

3.执行阶段

用户运行安装程序后：

（1）恶意代码被加载执行

（2）释放后续载荷（如信息窃取模块或远控组件）

（3）建立持久化机制（启动项/计划任务/注册表项）

4.控制与利用阶段

感染终端可能被用于：

（1）窃取浏览器凭据、Cookie、账号密码。

（2）收集本地文件信息并外传。

（3）作为内网横向移动跳板。

（4）为后续勒索攻击或数据窃取行动做准备。

攻击链路图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2xCpgJcagf8FuQFhs87NsfRGHugFlLoKreEiaCSS4XB9WAxd0WDiah98AV9rSpC9XVE6AeCjDtQqgu56zUHia1rMZoH5mnqB1WTOtria4drrO7U/640?wx_fmt=png&from=appmsg)

排查措施

1.文件来源

7-zip文件是否从官方网站https://www.7-zip.org获取下载。

2.恶意文件存在

文件夹C:\Windows\SysWOW64\hero\是否存在。

3.查看服务

"Helper Service"服务是否存在。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过