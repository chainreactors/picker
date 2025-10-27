---
title: APP漏洞挖掘之某款APP开发商通用漏洞的挖掘
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247504035&idx=1&sn=84908b67217a82438cd8f506fefcc839&chksm=ce5df2c2f92a7bd4610396f7707d667fb2920bf8cf8fdbe6440492b1048370df037fee7fa578&scene=58&subscene=0#rd
source: Tide安全团队
date: 2022-12-07
fetch_date: 2025-10-04T00:42:57.820630
---

# APP漏洞挖掘之某款APP开发商通用漏洞的挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMNuuMyY6apynmQ8HakcIU3zCLM82mRoicwdomVCtA1AndibibiaicmNh4xEA/0?wx_fmt=jpeg)

# APP漏洞挖掘之某款APP开发商通用漏洞的挖掘

原创

池羽

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

# 0x01 前言

参加某众测项目时，测某APP时，根据信息收集+测试，发现APP的后台系统存在SQL注入、XSS、弱口令、信息泄漏等漏洞，此APP本身存在逻辑漏洞与SQL注入漏洞，再通过观察酷传搜索的结果发现此APP开发商开发了三十几个APP，猜测可能存在相同类型的漏洞，经测试猜测被证实，可以刷一波积分。此文仅作为学习记录，仅提供思路，所述漏洞均已提交并修复。

# 0x02 第一个APP

根据众测平台要求从豌豆荚下载APP，再通过酷传查看下载量、开发商，再上企查查看注册资资本。（PS:如果注册资金超过5000个w，就能去cnvd碰碰运气混个证书)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQM4MJfZnicQvxenoSn3Uqx5xlznL003oEp5K0xVFBia6SoF86S09pVgkeQ/640?wx_fmt=png "null")

1000个w，证书看来是无望了，那就刷积分攒经验吧。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQM9rzThbCkTCXcZlNfntVUVt9Cm0ibOwzNQYPGnM1mThwQqn43t1QJYdw/640?wx_fmt=png "null")

AppInfoScan收集资产，找出几条有用的资产，做记号后挨个测试。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMCGcQ9eOte3BPVDutt0CvuiaI5gbo0bicBJfiaREiakD3XqnEtvVGkLe96A/640?wx_fmt=png)

## 漏洞一：信息泄漏

打开链接直接是个报错页面，暴露ThinkPHP版本信息与网站绝对路径，用工具扫，未发现历史版本漏洞。虽然CNVD不收，但也算是个漏洞，可以为之后的挖掘提供帮助。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMBia5yooibeRY0ozPZ5JqTsjGKQv35Mc06BLd2PWZoLcWwcOBHTOGAxXQ/640?wx_fmt=png "null")

## 漏洞二：后台系统存在SQL注入漏洞

打开资产表中的链接，其实未打开前就在想“链接后方有参数，可能存在SQL注入”，打开之后看到页面的报错信息毫不犹豫的上SQLmap，果然存在注入。系统使用MySQL数据库、Apache。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMoxXjlgj4oFEVTy07aWfEibzicrobJvoOQxSHc6iaAPpYDKuYIvwuibudqQ/640?wx_fmt=png "null")

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMic1wt0SrXXic6WMu5RFkBhxBfF1Q9V3WDibajlXaKaZ5K6lW83zrUTEYg/640?wx_fmt=png)

在上级目录页面【电话统计】处也存在SQL注入。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMBJhuwUydYw8mibmUYL5Eicw8tdF55bxE3FicP0wAibXxxKm6NANjxE0Vgw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMsQibEuIBrzzy2PUsptG7vGmmszqiaEoVQmv0RyKO3LCiclBiccsNMA6ibng/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQM8UUGAY2X3dFnQdpqUPyqOKmTPZuXE4icjIKeRWNCibVgwRSH39dzOZEA/640?wx_fmt=png)

## 漏洞三：APP后台管理系统弱口令漏洞

再根据漏洞二的链接，向上一级一级访问获得APP管理系统的某个页面，这个页面可以点击【登录后台】跳转至后台登录页面。页面下方的【设计师】、【框架整理】暴露了与登录用户相关的信息，在未登录的情况下点击【账户管理】，可直接查看到超级管理员、普通管理员和高级管理员的登录名。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMBzOjCgzgH5ibprlQN58Iia0t3Y7eknv9iaY3ibXyS4tzjxauW9FDxW9icVw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMPhicaYkQH182UrrvSFjnU45K4nA7hjMItHlDvcrpHy3EXFvjyB28c3Q/640?wx_fmt=png "null")

根据【账户管理】暴露的用户名猜出超级管理员的密码，登录后可获取大量用户的电话、地址、IP等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMGfv0FtEfmQibRnjia6UUVQAePZgicnwtHRUyfz1DpiaSiaiaDgGG1ia2np9zg/640?wx_fmt=png "null")

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMPdrrWKHD38y4O4ed6eYkmsYSZUhSw1UmTG8unAOVKDdGwWaO4xYsicA/640?wx_fmt=png)

## 漏洞四：APP后台管理系统存储型XSS漏洞

登录后台系统，在菜单栏某个模块的【添加】功能处，添加Payload，触发存储型XSS漏洞，此处未做任何输入输出过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQM3ibqv6UvjbnqtGUsgKGnEG2vU3Npm6rZuDXhHTFNQ3XYE1ArUEctKaA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVKStXKbU56tPfjfqQMbVhNAkeO8h4m2WFTibWBfFUfgmI22lAWqPfug/640?wx_fmt=png)

## 漏洞五：APP存在逻辑处理漏洞

安卓手机下载此APP。注册用户，随意填写手机号等注册信息。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMibwt9GRgSrCBCNA8AEnqyHIGeKxREibMOEiaZMBhcvSa3nBlibh1T8qK4Q/640?wx_fmt=png "null")

截取发送短信的数据包，短信验证码在返回包中明文显示。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMXbUDjJDib1tJ5uWHfJnLc8a13yUh3chY8t1XnWLVkzA9w3tw3aES8pQ/640?wx_fmt=png)

使用刚注册的手机号进行登录，登录成功。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMyUHmZ4ahNA1MZF1sNHlXMAzt25MH5DC0ibgzDKVQS6UqnibLib2pFFBxg/640?wx_fmt=png)

## 漏洞六：APP搜索框存在SQL注入漏洞

看到搜索框第一反应就是SQL注入、XSS，先抓取搜索框的数据包看看。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMk8DohiapMBCYA3B1lcVjfPgV6fwKLcMYrutVNm1ouZGCbbibcED2hP9g/640?wx_fmt=png)

GET请求数据包，直接用BurpSuite的SQLMap插件跑一跑。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMglQr4ykLxIL6OLCJaOdIky2Y0ficIH8UkQtJKZKndrhe9cN0y5ylEAg/640?wx_fmt=png)

布尔盲注，注出数据库为MySQL、框架为ThinkPHP。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMl6IiarYyicR2IicZHgSzxwEUiaFAExTtJVDmhGKJJTU9FkPI007H857AEA/640?wx_fmt=png)

# 0x03 其他APP

在酷传上搜索这款APP时发现，列出了很多与这款APP包名类似的APP，仔细观察并打开多个APP，开发商都为同一家公司，而且APP类型都一样，只不过有普通用户、某些角色不同、以及地区城市不同。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQM7xXIMDjQe8gayIiaTqewfnicWYaJPo5qD1bH735DicZn7EPBGFwQhXyLA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMmiayEHqqf2V6Xgr0oqN5QN0X9SWEzT1LkOOZUuSG7k93uUOJxtsfR5g/640?wx_fmt=png)

随意打开一个，查看【同开发商应用】，发现共有34款APP，既然有这么多款而且刚才又发现其中一款存在逻辑处理漏洞、SQL注入漏洞，不妨试试其他APP是否也存在相同漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMibCZny3ujyaQHtpFTlSffOic5Qu5Zyey8pTwnOXwR5bdCjNxzEuyeCpA/640?wx_fmt=png "null")

#### 例1：某APP存在SQL注入漏洞

打开APP，点击【首页】➡【XXXXX APP】，进入【XXXX详情】页面，截取此请求数据包。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMPHFpWWiaC9e4X1nFcsG1y4umnF9mXUvgleECKFUkhnavjcF2ItO5GVQ/640?wx_fmt=png)

GET请求数据包，使用SQLMap测试，存在SQL注入漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMMGt3x90bmL5icAPXOQr12GMmnVIcj2kfL3bBpVtewq2AxnNBxTfmOPA/640?wx_fmt=png "null")

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMeg8CoUnR2tjfwoYD0hicPT8XZiace3X8YqZ69UbPgfOLkC6omw7wDH9Q/640?wx_fmt=png)

#### 例2：某APP存在逻辑处理漏洞

打开APP，进入用户注册页面，输入手机号、密码，点击【获取验证码】，3秒后验证码会自动显示在页面中，点击【立即注册】，注册登录成功。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMnmERXBibutgFRJYmT3sibCetgcg91U42E88PLBGibA1RaCLUGNaqK1ibIQ/640?wx_fmt=png)

# 0x04 结语

其他剩余的30几个APP基本上都存在SQL注入漏洞与逻辑处理漏洞，只是有点细微的区别。比如，注入点随着APP功能不同而不同，多观察也可以找到。这类APP的逻辑处理漏洞在于返回包中明文显示验证码、或者验证码直接回显到APP验证码填写处，也不难发现。

```
**漏洞的挖掘未必有多难，胜在细致入微的观察。**
```

![](https://mmbiz.qpic.cn/mmbiz_gif/rTicZ9Hibb6RWbGNtVfIZbm2rmGO4hQDzQUrLN62vEGlA4fPmib5utUAp9gbQicb6FC82RjsVI5vx7wEc9yAAiaFEoQ/640?wx_fmt=gif)

E

N

D

**知识星球产品及服务**

**团队内部平台**：潮汐在线指纹识别平台 | 潮听漏洞情报平台 | 潮巡资产管理与威胁监测平台 | 潮汐网络空间资产测绘 | 潮声漏洞检测平台 | 在线免杀平台 | CTF练习平台 | 物联网固件检测平台 | SRC资产监控平台  | ......

**星球分享方向**:Web安全 | 红蓝对抗 | 移动安全 | 应急响应 | 工控安全 | 物联网安全 | 密码学 | 人工智能 | ctf 等方面的沟通及分享

**星球知识wiki**：红蓝对抗 | 漏洞武器库 | 远控免杀 | 移动安全 | 物联网安全 | 代码审计 | CTF | 工控安全 | 应急响应 | 人工智能 | 密码学 | CobaltStrike | 安全测试用例 | ......

**星球网盘资料**：安全法律法规 | 安全认证资料 | 代码审计 | 渗透安全工具 | 工控安全工具 | 移动安全工具 | 物联网安全 | 其它安全文库合辑  | ......

扫码加入一起学习吧~

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn4bib2lic6dng5krLaNOdrDVLcLylWP1Op3Kibz2n6pOZjibrFd1xATEoZ6dXhaicMLgRQSicNQwGmDwicvA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUGxmZ0l89buUNbyVALKxic2nM7hnDCkAKIrjKhdcDfVkGq3PxNzgs7m55BBMwmicc0AvFpYcrd6J6Q/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

Tide安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

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