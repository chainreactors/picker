---
title: 注意！终端管理工具MobaXterm中文版暗藏木马陷阱
url: https://buaq.net/go-140736.html
source: unSafe.sh - 不安全
date: 2022-12-21
fetch_date: 2025-10-04T02:04:17.359615
---

# 注意！终端管理工具MobaXterm中文版暗藏木马陷阱

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2535da0d53bddc25cdb2f4e81d5cf18d.jpg)

注意！终端管理工具MobaXterm中文版暗藏木马陷阱

概述近期，奇安信网络安全部在日常运营过程中通过天擎EDR发现，有攻击者以知名终端管理工具MobaXterm中文版为诱饵传播木马程序，威胁情报中心跟进了此次事件，并进行了分析拓展。MobaXterm本身
*2022-12-20 19:3:29
Author: [mp.weixin.qq.com(查看原文)](/jump-140736.htm)
阅读量:174
收藏*

---

概述

近期，奇安信网络安全部在日常运营过程中通过天擎EDR发现，有攻击者以知名终端管理工具MobaXterm中文版为诱饵传播木马程序，威胁情报中心跟进了此次事件，并进行了分析拓展。

MobaXterm本身有免费版本，但用户界面目前不支持中文，攻击者抓住了国内用户这方面的需求，在CSDN和知乎等社区平台发布文章推广带有后门的MobaXterm下载地址。下载得到的压缩包中携带恶意载荷，最终会加载Gh0st木马，执行远程控制和窃密行为。

事件详情

国内搜索引擎搜索“MobaXterm中文版”，搜索结果中排名第一的文章就是在推广带毒的MobaXterm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIzv7WW9M3NTyibGvOT6YkjwrGGLly7xtiajapprJLgu65SHm8Vfib54SYA/640?wx_fmt=png)

CSDN显示该用户于10月19日创建，目前已注销，从11月4日开始发布文章，发布的7篇文章基本是在推广带毒的MobaXterm应用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIeeahdfeXJ0lOc9Xia3sAAe97Mv27B8xfUq3TrJY50gQq7RNecQDUc2w/640?wx_fmt=png)

攻击者在知乎也发布了一篇推广“MobaXterm中文版”的文章。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIczhn4zWjGWjRMQTDEx4Ke5E6YEUBtUT5rEtJQNh0fqYTIyCAoqDvHw/640?wx_fmt=png)

带毒应用的托管域名（mobaxterm[.]info）模仿成与MobaXterm有关。左上角包含MobaXterm图标的图片上还有CSDN水印（”CSDN @cantaly”），水印中的ID（cantaly）也在该带毒应用的CSDN推广文章中出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIb7y4gFwzDKux3HibiazUFkwe39icugo0QTSHRsHzTapLMZbr0tNcicicaPg/640?wx_fmt=png)

而MobaXterm的官方网站域名为mobaxterm.mobatek.net。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIaVicbm6Qj0ibVHISNtIHWbdSicLTWgj5eheibg3TrS1Bys4sekmgpzYvPw/640?wx_fmt=png)

攻击者使用的域名注册时间是11月3日，就在CSDN和知乎文章发布前不久。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIlmU6VGiaRicjVkYRJ6ibbmWcqWIhesS65kj6UqFoF4YJzmM2rlnouK94g/640?wx_fmt=png)

该域名自注册以来的访问趋势如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgI6oicPb5dTfZibyX0luiaxIZpmHxl3gmibGibTTnarEhXIPsvRvENsZmh0AA/640?wx_fmt=png)

样本行为

带毒应用的压缩包有如下内容，其中at.mdb文件是主要恶意载荷（后续也会从C2服务器再次拉取at.mdb）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIkOF91ffp950wzzh6nZibqSr0XLTUqTict91umfqhib8er1kXrAUjq0LtQ/640?wx_fmt=png)

执行流程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgI1vlbM4uicCFpFXc7UwEu4DxqvPHIHhlHJjEPA45pvKtGp7ib5Dq9IAhw/640?wx_fmt=png)

(1) MobaXtermPersonal.exe请求mobaxterm[.]info，下载3dsystem.exe；

(2) MobaXtermPersonal.exe以/f at.mdb参数启动3dsystem.exe，通过DCOM跨进程的方式绕过UAC，提权后的3dsystem.exe自我复制为DirectXh.exe、ManagerBack.exe，并放到不同目录下；

(3) 提权后的3dsystem.exe将DirectXh.exe注册为自启动服务实现持久化，DirectXh.exe作为服务启动后，进行联网行为，并加载文件at.mdb，最终执行Gh0st后门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIO8ib2NAibia9wL6nEhX81s2bQMvtbI8NWUnF9cv706L0M4MYzicEniatVIQ/640?wx_fmt=png)

Gh0st后门的配置信息如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIrIIBj5nYJQ6EoibuwDFdDsKc0ialJOIyaI9uyPWd1II9JwXd4F86JbUg/640?wx_fmt=png)

我们通过线索拓展，发现了在此次样本以外更多的与攻击活动相关的C2信息（详见IOC列表）。

总结

近年来，利用付费软件破解版和国外软件汉化版为诱饵的软件投毒事件层出不穷，软件使用者需要加强安全意识，仔细鉴别软件下载地址是否为真实官方地址，不使用网上来历不明的软件，避免成为网络攻击者的猎物。

奇安信红雨滴团队在此提醒广大用户，切勿打开社交媒体分享的来历不明的链接，不点击执行未知来源的邮件附件，不运行夸张标题的未知文件，不安装非正规途径来源的APP。做到及时备份重要文件，更新安装补丁。

若需运行，安装来历不明的应用，可先通过奇安信威胁情报文件深度分析平台（https://sandbox.ti.qianxin.com/sandbox/page）进行判别。目前已支持包括Windows、安卓平台在内的多种格式文件深度分析。

目前，基于奇安信威胁情报中心的威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、天擎、天眼高级威胁检测系统、奇安信NGSOC、奇安信态势感知等，都已经支持对此类攻击的精确检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIcfpPySUd2ylnMcfibICTYQMVbAicjF4bCrAqvFKOVAXkd4RWd8E2JWicg/640?wx_fmt=png)

IOCs

**SHA1**

85382BF068218068C0946C15301CC7E949B21BA7 （MobaXtermPersonal.exe, 15609856 字节）

917B4816AA8C40A6F68B564D01E15FE7204D5600 （DirectXh.exe, 53688字节）

A4B09B68DE8955B25A65C32C08BCB6A41314E7E7 （at.mdb, 2505216字节）

**C2**

mobaxterm[.]info

xumming[.]net

www[.]supbrowser.[]com:80

abc[.]masktable[.]com

www[.]masktable[.]com

\*.xumming[.]net

\*.mobaxterm[.]info

\*.supbrowser[.]com

\*.masktable[.]com

\*.hi4089[.]com

macdn[.]cloudcache[.]org

macache[.]globalacceleration[.]net

xinggedafanzei[.]com

qlxytj[.]xyz

agentclub[.]shop

agentclub[.]vip

103.29.70.153:443

43.154.38.3:443

43.155.103.75:443

13.212.84.85:443

154.204.56.229:443

**URL**

hxxp://mobaxterm.info/soft/MobaXterm中文版.zip

hxxp://mobaxterm.info/soft/3dsystem.exe

hxxp://mobaxterm.info/soft/at.mdb

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic8PibSEbXe1iaYncjmY5AiavgIXfoXcwAb8BQJOL9ZSh4M1MibTw0dKFI20qNAA0Z6BKwmcuXH9ucDXBQ/640?wx_fmt=gif)

点击阅读原文至**ALPHA 5.0**

即刻助力威胁研判

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzI2MDc2MDA4OA==&mid=2247504780&idx=1&sn=718613e19290a371d01421651dfe61f8&chksm=ea6624fbdd11adedf98fd936e2e5b1509feba690ab0beb7c465dc1daa880b456beb7fa1899af&mpshare=1&scene=1&srcid=1220qoNtjtWQiO7ezhhkJqbQ&sharer\_sharetime=1671534203761&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)