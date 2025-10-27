---
title: 没有资源的情况下如何熬过攻防演练？
url: https://www.freebuf.com/news/372246.html
source: FreeBuf网络安全行业门户
date: 2023-07-18
fetch_date: 2025-10-04T11:55:54.770683
---

# 没有资源的情况下如何熬过攻防演练？

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

没有资源的情况下如何熬过攻防演练？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)
* [攻防演练](https://www.freebuf.com/articles/defense)

没有资源的情况下如何熬过攻防演练？

2023-07-17 12:00:22

所属地 上海

继续是这个扯淡的话题……也以此作为这次攻防演练过程的记录，以后可以纪念一下。所以，这一篇归类到“科技奇趣”，哈哈。

想了一下，这个过程大约可以分为以下几种态度去应对：

## 一、看戏模式

可乐瓜子零食马扎备好，用一堆电脑屏幕围住自己，每个屏幕显示一台安全设备的仪表板界面，全部设置不会超时自动登出......大约就是这样：

![](https://image.3001.net/images/20230717/1689565856_64b4baa07f64ed424ac58.png!small)

没毛病，是吧。

话说这些界面都有各种 UI 缺陷，或者字太少，或者无法定制内容。最典型如右边是 WAF 的输出，没有把整个屏幕利用好，浪费了三分之一的空间。

怒了。于是直接调出浏览器的开发者工具，改页面 HTML 结构、CSS 定义和 JS 里面的循环滚动控制，就可以增加显示的记录数。

如果想避免下次再登录进入 WAF 时还得重新改一次的情况，可以用 greasemonkey / tampermonkey 扩展，把修改设置为一键应用。

具体改了什么这里不介绍了。

那些实时事件，要不要细看就取决于自己能力水平，以及看了之后能干什么。

## 二、演员模式

演员就是要动手了。

随着演练开展，发现攻击队利用了任意文件上传漏洞上传 WEBSHELL。于是登录切换到 ROOT，一边 KILL 进程，一边查日志找对方IP地址和漏洞位置，设置临时过滤和限制写入等等措施。

这个时候，需要开多个窗口同时观察和处置，在默念“论一个演员的自我修养”的同时，想想仪式感还是要拉满才行。

于是用一堆 PUTTY 窗口把屏幕摆满，各种持续显示系统日志：

> # tail -f /var/log/message

倒是要说一下，不是所有的服务器环境都是看系统日志，比如可以看tomcat的输出（路径不是真实的）

> # tail -f /opt/tomcat/logs/debug\_

话说窗口的摆放需要有点技巧和美感，这样才能充分投入。

于是在结合了《黑客帝国》的垂直信息流和《旗鱼行动》的环绕阵势之后，堆出来这个桌面：

![](https://image.3001.net/images/20230717/1689565988_64b4bb24dd11e58af05ff.png!small)

这个桌面如果手工排布就很花时间，所以最右边已经懒了，不是 Putty，而是 Kali Linux 运行 WireShark 在抓包，人肉观察内网有无异常流量。

Windows 11 提供的窗口排布功能并不支持这么复杂的排布。一般情况下，显卡的控制中心软件会提供类似的功能，而我这电脑的厂商也提供了一个显示窗口控制排布的软件，可以方便地设置窗口排布。

如果啥事都没发生，实在闲得无聊的话，可以留一个显示器，运行一个看上去花里胡哨的系统外壳，比如：

[科幻感满分的终端模拟器eDEX-UI](#wechat_redirect)

![](https://image.3001.net/images/20230717/1689566394_64b4bcbacb201431fe63f.png!small)

不仅能操作，有人来看的时候还特能唬弄人，哈哈。

## 三、编剧模式

最后是编剧模式。导演确实是轮不到自己了，但还可以做做编剧，只需要一点文字能力。

剧本就是每天的防守报告。我们要按照源于生活高于生活的要求，把剧本啊不是，把报告内容充实起来。

1、首先是无论有事没事，各种安全设备日志截图贴满；

2、然后把疑点异常记录勾出明示；

3、再然后批注解析摘抄网络协议技术说明等等写满；

4、最后结论部分知网上找论文引用一番。

总之就是越高技术，越看不懂就越好，比如下面这张 SELinux 的结构图：

![](https://image.3001.net/images/20230717/1689566044_64b4bb5c9fe6f974c8991.png!small)

这图还确实值得认真学习。

## 结论

其实坚持就是胜利，无论打到最后多少分，重要的是参与。

负分丢脸？

记住只要自己不尴尬，尴尬的就是别人哦。

注：本文来源于“﻿wavecn”公众号

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

一、看戏模式

二、演员模式

三、编剧模式

结论

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)