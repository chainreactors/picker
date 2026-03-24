---
title: 一次基于Struts框架项目的代码审计
url: https://mp.weixin.qq.com/s/PlWU_oGPLunFf3n07VLejw
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:22.358735
---

# 一次基于Struts框架项目的代码审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVkp9uqJWBbwgibppQnqPD8icTHj6LglezmaQa6iaGicPXnG7eFOM84EznkHclzEQxneCEmiaupJSRQWXL4mn2icWazNwPkaw6r7OFgVc/0?wx_fmt=jpeg)

# 一次基于Struts框架项目的代码审计

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 1368，阅读大约需 7 分钟

## 前言

上周去客户那里做了一个渗透测试+代码审计，黑盒+白盒的项目。

客户给的环境是纯内网，源码不允许出网，久违的体验了一把古法代码审计。

一直引以为豪的奥特手环——AI 大模型用不了。

同样的，因为客户公司的要求，不能使用盗版软件。用的代码审计工具是社区版本的 IDEA，以及社区版本的 Burpsuite 和 Yakit。

客户的主机更是走的虚拟终端，而且是信创后的桌面——麒麟系统。

这几层 buff 叠加下来，福气小的了吗？

## 信息收集

客户提供的 UAT 环境，登录接口 login.do。
一般这种不是 weblogic 就是 struts。
后续看到了 LoginAction，struts 没跑了。

客户的开发人员也是古法编程我看，用的也是古法框架。

古古古。

## 漏洞扫描

Struts 历史漏洞扫一遍。
用到的工具：Struts2VulsScanTools

Struts2VulsScanTools下载链接

![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn0ib0jqGiaBiauXZJxJHJ2d8B8OpemrKCkdhMia5P7hWkriczRY3zfhaU1e2Yw7p1ibrTMnYR4j7ZzmBkicggCQibsftgWucgo72KSUtc/640?wx_fmt=png&from=appmsg)

OK，啥也没扫出来。

不过也在预料之中，客户是公司老客户了。他们公司的两高一弱专项活动，我还用扫描器扫了呢。

但是，虽然没扫到历史漏洞，但报了个 500 的错误。报错是 Tomcat 的框架，里面显示了堆栈信息。

聊胜于无，可以水个低危。

然后在我写报告的时候，偶然看了一眼截图，发现里面不止有 Tomcat 报错的堆栈信息，还打印了 index.jsp 的代码。

因为我把项目的代码都过了一遍，所以对这个 index.jsp 的代码比较有印象。

我重新抓包，把 Poc 调出来，换成别的 jsp 代码，然后也报错 500 打印了完整的 jsp 代码。

虽然不知道为啥会出现 jsp 源码，但就是出现了。

于是我把这个凑数的水洞从低危提到了中危。

## 代码审计

IDEA 社区版用起来是真的很社区。

然后因为缺少依赖包，代码的调用关系也是一片通红。只能靠着搜索定位。

因为客户买了 SCA 系统，依赖的版本号不需要我们操心，只要专注于 Java 代码即可。

项目通过 xxconfig.xml 加载所需的所有 xml，比如数据库的配置文件、API 和类的绑定关系、拦截器等，都是通过 xml 实现的。

路由和 class 的绑定
/api/xxxx.do

```
<action name="xxxx" class="XxxxAction" method="yyyy">
```

### 未授权漏洞

提取出所有的路由后，用 Yakit Fuzzing 跑一遍，根据返回的信息先做一次汇总，排除掉 401、302 的。

200 的里面，像以 List 结尾的，用来展示数据的，都正常跑出来来了，在未授权的显示的信息中，寻找敏感数据，记录接口和对应的代码。

有的时候，我们也会把所有未授权接口都放进报告，让客户排查。这样后续系统放互联网上，被白帽子交漏洞了，也方便甩锅。

### 任意文件下载

在上面跑接口的时候，遇到了一个 DownloadTemp.do 的 API，接口报错，参数不对。

搜索 xml 文件，找到参数是 temp

传入的参数代码里看不出来，从 UAT 前端定位具体的功能点，点击后参数为 doc
拼接

```
/DownloadTemp.do?temp=doc
```

成功下载一个压缩包，代码中也没做../的限制，可以跨目录。

尝试

```
/etc/passwd
../etc/passwd
```

但是都没有成功。

重新看了下代码，发现这个功能点不是下载文件，而是将制定的目录打包成 zip 然后返回。遇到参数值非目录或者不存在的情况，直接报错。

尝试

```
../etc
```

没成功，估计是没权限。

换成上传图片的文件夹

```
/home/xxxx/upload/
```

成功下载 upload.zip 里面包含近期上传的所有文件

该接口理论可以从系统直接下载 jar 包，但我没成功。

原因是打包后的压缩包太大，代码限制直接不给我返回了。

jar 包理论放在 /home/xxx 下面，但是我只能下载一整个目录，这就导致/home/xxx/下其他乱七八糟的东西也会一起打包，加起来就超过了最大上限。

我敢肯定开发一开始写这个限制，绝对不是为了限制别人下他们的 jar 包，但就是做到了。

### 奇妙的历史遗留问题

从这个项目技术选型会是 Struts，就能看出这是一个历史悠久的项目，期间不知道迭代了多少次，更新了多少代码，换过多少开发。

在经历了等保 2.0、数据安全、行业标准等后，这个项目已经为了适配各种情况，不可避免的出现一些遗留问题。

比如在登录接口中，添加一个 xxx=true 后，就能绕过图片验证码的限制，对账号密码进行爆破。

项目里还有古老的存在任意文件上传的 ueditor，可能是因为对接口进行了二开，居然这么多年在互联网就躲过去了。

废弃的 SSO 接口可以实现任意用户登录……

上传的 ZIP 压缩包，解压缩时可以跨目录放文件……

## 总结

古法代码审计确实练人。期间遇到没见过的 Struts 特性和不理解的 xml 文件，用手机偷偷问大模型，帮助确实很大。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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