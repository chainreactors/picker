---
title: 大量中文网站被黑，嵌入世界杯相关关键词用于黑帽SEO
url: https://www.freebuf.com/articles/network/351899.html
source: FreeBuf网络安全行业门户
date: 2022-12-09
fetch_date: 2025-10-04T01:00:12.089052
---

# 大量中文网站被黑，嵌入世界杯相关关键词用于黑帽SEO

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

大量中文网站被黑，嵌入世界杯相关关键词用于黑帽SEO

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

大量中文网站被黑，嵌入世界杯相关关键词用于黑帽SEO

2022-12-08 16:09:50

所属地 北京

在黑帽 SEO 中，经常会出现的是被黑网站的 `<title>`标签被修改为中文关键词，使搜索引擎的检索结果中明显可见。但如果使用浏览器打开时，则会显示原始未修改的标题。

黑帽 SEO 经常会推广中文的赌博、体育彩票类网站，研究人员发现此类攻击已经产生了巨大的影响。根据 PublicWWW 的数据，失陷的站点数量应该已经超过 5 万个。近期，攻击者开始利用世界杯作为话题进行引流。

## 嵌入世界杯关键词

最近，很多失陷网站都更新了关键词，主要是与 2022 年卡塔尔世界杯的标题。

> 卡塔尔世界杯赛事分析·(中国)世界杯赛事中心
>
> 2022世界杯买球投注-世界杯安全买球网站【官方平台】
>
> 世界杯赛事预测世界杯在线直播世界杯赛时间 – 体育新世界

重定向的站点通常也是世界杯相关主题的，如下所示：

![image.png-1051.1kB](https://image.3001.net/images/20221208/1670486990_63919bcecf75c27517423.png!small)重定向网站

检查失陷网站的 HTML 源代码，其中 `<title>`与 `<meta>`中有很多关键词：

![image.png-613.1kB](https://image.3001.net/images/20221208/1670486992_63919bd0a45af04f7b276.png!small)失陷网站的标题

这些 HTML 实体使用 UTF-8 中的字符代码表示 Unicode 字符。以 title 标签为例：

> <title>&#19990;&#30028;&#26479;&#22806;&#22260;&#32593;&#31449;&#45;&#105;&#111;&#115;&#47;&#23433;&#21331;&#47;&#25163;&#26426;&#29256;&#97;&#112;&#112;&#19979;&#36733;</title>

解码后汉字为 `<title>世界杯外-围网站-ios/安卓/手机版app下载</title>`。

## title 切换

使用浏览器打开失陷网站时，就看不到与赌博和世界杯相关的内容。攻击者使用的 HTML 脚本会检查访问者是不是中文搜索引擎爬虫，即时将 title 修改为原始内容。

目前在失陷网站上部署了两个主要的变种：

### 只匹配百度的爬虫

```
<script>if(navigator.userAgent.toLocaleLowerCase().indexOf("baidu") == -1){document.title ="<real site title>"}</script>
```

### 匹配包括百度在内的其他爬虫

```
<script>if(!navigator.userAgent.match(/baiduspider|sogou|360spider|yisou/i)){document.title ='<real site title>'}</script>
```

在某些站点上，还发现了其他脚本，这些脚本会控制页面内除了 title 以外的其他内容切换。

## 范围与影响

在撰写本文时，PublicWWW 在 50172 个网站上发现了第一个脚本，在 14010 个网站上检测到第二个脚本。

看似已经很多了，但实际上相比前几年超过十万的规模已经收缩了不少。而且失陷网站大多数是中文网站，在全球其他地方的曝光度较低。

## 赌博网站重定向和混淆脚本

攻击者还使用了几种不同类型的重定向脚本。最简单的重定向脚本没有经过任何混淆，检查访问者是否来自搜索引擎，满足条件的重定向到赌博网站。

![image.png-119.4kB](https://image.3001.net/images/20221208/1670486993_63919bd196c0f1327b5dd.png!small)没有混淆的重定向脚本

还有经过混淆的脚本，如下所示。解码后，可以得到外部链接 `hxxp://tongji.68010[.]com/4/tzm.js`。

![image.png-90.8kB](https://image.3001.net/images/20221208/1670486994_63919bd28f8f534dd764f.png!small)使用 HTML 实体进行混淆

还有攻击者常用的 eval 混淆方式，如下所示。解码后，可以得到外部链接 `hxxps://www.makeafortune88[.]com/bb.js`。

![image.png-303.9kB](https://image.3001.net/images/20221208/1670486995_63919bd3639428858d903.png!small)eval 混淆

## 外部链接

外部链接也有多种变种，如：

![image.png-155.1kB](https://image.3001.net/images/20221208/1670486996_63919bd4965be5fd55b61.png!small)外部链接变种

![image.png-124.7kB](https://image.3001.net/images/20221208/1670486997_63919bd59a9c5d924f937.png!small)外部链接变种

![image.png-229.5kB](https://image.3001.net/images/20221208/1670486998_63919bd6569078f55d75a.png!small)外部链接变种

在满足特定条件时，将访问者重定向到赌博网站。也有部分外部链接是针对移动设备的：

![image.png-281kB](https://image.3001.net/images/20221208/1670486999_63919bd7863e2f5acdde5.png!small)移动设备重定向

脚本中会预制许多赌博网站，将用户重定向到其中之一。

![image.png-121.4kB](https://image.3001.net/images/20221208/1670487000_63919bd8a814f05ff8c63.png!small)多个网站

攻击者利用百度的自动推送功能，提高攻击效率。每当访问者打开失陷网站时。脚本都会向百度发送将 URL 添加到索引中的请求。注：百度站长服务平台在 2020 年 12 月宣布停用自动推送功能。

![image.png-184.7kB](https://image.3001.net/images/20221208/1670487001_63919bd981a8797f68c64.png!small)搜索引擎诱导

## IOC

> 154.38.227.98
> www.tbty20000[.]com/tb.js
> www.niubjsc20226688.com/tbsjb.js
> 154.22.124.28
> qitasjb2022[.]com/yb.js
> sjb2022ky[.]com/yb.js
> qitajs1002[.]com/yb.js
> ybjs0726[.]com/yb.js
> ceshi963ly[.]com/yb.js
> 154.222.103.43
> tongji.68010[.]com/5/tzm.js
> 155.159.144.129
> diltsportajohn[.]com/shell.js
> 128.14.75.59
> www.ly66666[.]vip/ly/ly.js
> www.telegeramguanwangfangwangzhan20220924[.]com/telegeram/telegeram.js
> 206.119.125.190
> www.makeafortune88[.]com/bb.js
> www.makeafortune66[.]com/bb.js
> www.bobsjb2022[.]com/bobsjb.js
> 206.233.132.188
> www.sjb4[.]cc/bob.js
> www.ag857[.]cc/ag.js
> www.sjb2[.]cc/bob.js
> www.sjbs[.]cc/bob.js
> www.ttdbty[.]cc/bob.js
> 143.92.32.243
> www.yigexiaomubiao2022[.]com/bb.js
> 23.248.203.3
> www.360360365[.]com/360.js
> efhfuh[.]com/365.js

## 参考来源

> [Sucuri](https://blog.sucuri.net/2022/12/chinese-gambling-spam-targets-world-cup-keywords.html)

# 黑帽seo # 博彩 # 世界杯 # 博彩引流

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

嵌入世界杯关键词

title 切换

* 只匹配百度的爬虫
* 匹配包括百度在内的其他爬虫

范围与影响

赌博网站重定向和混淆脚本

外部链接

IOC

参考来源

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