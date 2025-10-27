---
title: bshare分享插件被黑？百万级网站被劫持事件
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247513994&idx=1&sn=215f43f75089a70e967562ff9cb233a4&chksm=ea6640fddd11c9ebd873c8a5113d9d372006161766f94d417d689c768426fd3279b6b7e9d971&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2025-02-17
fetch_date: 2025-10-06T20:34:35.721183
---

# bshare分享插件被黑？百万级网站被劫持事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9crcwzYmib0n1UUetScibAR0LIVAicVByCWnYQThmEvhsHuJbPDFzhXH3y2FaVjw0rHmKFia14Jg0Heg/0?wx_fmt=jpeg)

# bshare分享插件被黑？百万级网站被劫持事件

原创

红雨滴团队

奇安信威胁情报中心

概述

奇安信网站云监测和奇安信威胁情报中心在日常威胁狩猎活动中，发现很多站点在晚上9点至凌晨5点使用安卓UA的设备访问时，会跳转至同一色情网页。起初我们认为这批站点由于自身安全缺陷导致被黑产组织攻破利用，经过进一步分析，发现这些网页都引用了名为bshare的分享按钮插件，该插件对应的服务域名为static.bshare.cn；最后通过对域名static.bshare.cn的分析，我们确认这是一起通过抢注过期通用插件服务域名来实施大范围网页劫持的攻击事件。

所有直接或间接使用了bshare分析插件的网页都会受到影响。根据评估，恐怕会影响百万级别的网页。奇安信威胁情报中心在此提醒目前仍在使用bshare插件的用户，需要尽快更换或者停用bshare分享插件。

事件分析

安全监测系统监控到许多网页存在JS异常跳转：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0hagPsekqy80aKBRevcq8CeVby78302dGU1xuMSoEoPnJia7zfGD2jwg/640?wx_fmt=png&from=appmsg)

经审查，页面包含以下源码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0sdJqFusskuLXmBJ7aIXib5PGiaVeEwftK6npFxyibqm8f9iceUZibg9a0yQ/640?wx_fmt=png&from=appmsg)

static.bshare.cn原本是个用来实现分享功能的按钮组件，使用该组件后可在网页上提供一键分享的按钮样式及功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0EzzE2iaibe9BOlHxuu7Niaaicpet2EbZWABAqtWSzAVJkuP1tJzAxl6G5w/640?wx_fmt=png&from=appmsg)

使用该组件的需要在原网页中插入bshare网站的js资源，通常是hxxp://static[.]bshare.cn/b/bshareC0.js、hxxp://static[.]bshare.cn/b/buttonLite.js。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0ibfAO10euNBzwR59A75ibAh8S77cQh5jBrKW0ibk6awRibANLPBiajWmHCg/640?wx_fmt=png&from=appmsg)

恶意的JavaScript代码主要位于bshareCO.js文件，网页组件调用的buttonLite.js或者bshareC0.js也会进一步加载bshareCO.js文件。该文件经解混淆后主要代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0gcsxU5cMP6mmrqkAGJPsnogricxsUU5iaW95Q8RMmib6C7F9UoKkQ0rvA/640?wx_fmt=png&from=appmsg)

主要功能为对用户进行监测，如果为安卓用户且时间点为晚上21点到凌晨5点，则进行色情网页弹窗，实现推流效果。同时收集用户的设备和浏览器信息，并生成一个唯一的访客 ID，以便进行用户统计分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0tYMDQibiaakonCaMjTO8xP7KVP7D3kwesPwgJsQYKzD8eujrKRnDYKNQ/640?wx_fmt=png&from=appmsg)

最终跳转到色情网页：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0tOvyXD1rBAqN5DtAct3aE75mkR6mO9MN0vjMNtV616EJKhjicicIibfyw/640?wx_fmt=png&from=appmsg)

溯源分析

bShare是擘纳(上海)信息科技有限公司旗下产品, 而擘纳(上海)信息科技有限公司在2018-02-18已经注销.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0YVhcLn6yXiaeFqPgCG9LWDUvzibp9y9DYz2xg9khHDwRtDAzEZRicicJrw/640?wx_fmt=png&from=appmsg)

但是2020-01-27时，bshare.cn的whois显示其依然有效，并且注册人联系邮箱为sa@i-click.com，与 擘纳(上海)信息科技有限公司的邮箱域名一致（上图）；而i-click.com和 i-click.cn的域名相似且2021年3~4月份曾同时解析到210.5.172.215上；i-click.cn的ICP备案为爱点击（北京）数据科技有限公司（京ICP备13006473号-1）；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0tpcBnrxvAbyB56iauHYibMqIIvn2kObZw1iaaCwibeBEYLNPGNl2MIAarg/640?wx_fmt=png&from=appmsg)

在2023-09-07，bshare.cn的备案信息显示为爱点击（北京）数据科技有限公司（京ICP备13006473号-1）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0YkSxE9WRyseVTAy3cFicmicSbib0p7iczWrSm9Vicbb91nHmvtqQKLfDqZQ/640?wx_fmt=png&from=appmsg)

此时 bshare.cn的whois信息显示也是一致的，也就是说爱点击（北京）数据科技有限公司和擘纳(上海)信息科技有限公司有一定关系，bshare.cn在2024-10-20 09:16:24之前一直是有效的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0avCrkSyWkOQFIq1sbjWsTBNFX3lqOXTcib2l0B3MQMeSJveKenRI61g/640?wx_fmt=png&from=appmsg)

直到2024-11-23，bshare.cn域名的状态从ok变为了clientHold锁定状态，clientHold状态是由域名注册商设置的，域名可能被设置为 clientHold 的原因包括：域名注册或续费费用未支付、未能提供正确的注册信息、违反了注册商的使用条款或政策、涉及法律纠纷或争议等。同时bshare.cn的ICP备案也已经过期，最后一次查到的时间在23年9月。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0UwCv7T7XiceNv00HsjbxiaBEMPrx7f616CArbuW3ndE14bwOUibYY9V0g/640?wx_fmt=png&from=appmsg)

几乎同一时间static.bshare.cn域名的基础组件也更换为了历史从未出现过的OpenRestyWeb：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0AkNU9Cy2ROGwujviauPVHSkv6ls3FibDw82Z6icPBF6BcIDiaSFWx6ImicA/640?wx_fmt=png&from=appmsg)

我们利用passiveDNS数据对static.bshare.cn解析到的IP地址进行分析发现，域名在2024年10月到期前解析的IP所属地理位置一直是大陆，而被抢注后解析的IP位置变为了港澳与海外。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0j3slMq0zbgWbu6CE4uVfsdZeHfgllb9zevgvRwweRDRFzJlOD3xqMQ/640?wx_fmt=png&from=appmsg)

综合以上分析我们判断bshare.cn在2024-10-20过期，然后被人抢注，不再属于爱点击（北京）数据科技有限公司。所以2024-10-20之后，bshare分享插件实际上已经不再可用了；而bshare.cn域名到期后，使用了bshare组件的网页并不会自动更新或者删除相关引用代码，访问这些网页仍旧会自动请求hxxp://static[.]bshare.cn/b/bshareC0.js、hxxp://static[.]bshare.cn/b/buttonLite.js。

Bshare.cn域名在被人抢注后，域名拥有者可以非常方便地通过修改hxxp://static[.]bshare.cn/b/bshareC0.js、hxxp://static[.]bshare.cn/b/buttonLite.js的JS代码来进一步控制所有引用了bshare插件的网页，从而进行推流或是其他网络攻击行为，比如推送钓鱼页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0NuoXx0NnOEQdD90KOYCDkao7ibQiaCdia4tNzhOAT1m6JDkGc1WJpT2FA/640?wx_fmt=png&from=appmsg)

2024年12月，我们披露了UTG-Q-015组织利用bshare.cn域名进行钓鱼攻击的活动（见参考链接[1]）。在处理24年12月的UTG-Q-015攻击事件的应急中，我们也发现了包含了色情推流相关代码的hxxp://static[.]bshare.cn/b/bshareCO.js，该JS代码中引流的色情网址是hxxps://360bs[.]xyndt.com/?bs，如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR01ymjJsIQL0gJ286sibK1pVUicuNVBsJ8ibfgSx0K6m14aKGpGj0wjQniaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0J0IyLLbDLicYoT85Pa9qTialQBkia35Ptdd9DeaGWqju76KTGreVqjWGQ/640?wx_fmt=png&from=appmsg)

本次事件的色情推流代码中，涉及的色情网址则是hxxps://360bs[.]julupan.com/?bs, 可以发现这两个网址的结构基本一致。鉴于两次事件发生的时间都是在static.bshare.cn域名被重新接管使用后，并且时间接近，应是同一黑产团伙所为。至于这个接管了bshare.cn的黑产团伙与UTG-Q-015是否有直接关系，目前还不明确；但是从恶意代码涉及到的“业务”来看，我们认为该团伙可能是以盈利为目的、出售引流推广和网页劫持服务的黑产团伙。

事件影响范围

**受影响对象**：所有直接或间接引用上述恶意脚本的网页。

根据测绘数据显示，引用该组件的量巨大，而且这还不包括网站二级目录的页面，受影响的网站恐达百万级别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0koNQiaCmF0lQLTP7dYm1Sl6WEDQ0ibMHQjzj03Pwr9g7x3MhPa0vOwLw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9crcwzYmib0n1UUetScibAR0xNiaRw26BcSQ8h5EEgpOAyM7MK2RKsBmdspzdfNKgib12q1c5V3k1viaA/640?wx_fmt=png&from=appmsg)

紧急应对措施

**1. 立即下线恶意脚本**

* 请所有相关业务团队立即排查并停止引用 static.bshare.cn 域名的两个JS文件，建议替换为可信来源的静态资源或临时关闭相关功能模块。
* 清除浏览器缓存并重启服务，避免本地缓存导致持续风险。

**2. 用户侧防护建议**

* 建议安卓用户在上述时段避免访问相关页面，或使用安全防护软件拦截异常跳转。
* 若已发生跳转，请立即关闭页面并对设备进行全盘扫描，以防个人信息泄露。

**3. 全面安全排查**

* 对所有第三方依赖脚本进行安全审计，重点关注异常网络请求、跨域加载及代码混淆行为。
* 检查服务器日志，追踪攻击者注入路径及潜在后门。

IOC

# 目前国内大量网页依然存在引用static.bshare.cn的代码，直接加黑可能导致大量告警，需谨慎评估是否加入黑名单中。

**Domain**

Static[.]bshare.cn

360bs[.]julupan.com #色情域名

360bs[.]xyndt.com #色情域名

360[.]baohuajs.com #色情域名

**URL**

hxxp://static[.]bshare.cn/b/bshareC0.js

hxxp://static[.]bshare.cn/b/buttonLite.js

hxxp://static[.]bshare.cn/b/bshareCO.js

参考链接

[1] https://mp.weixin.qq.com/s/qQw1DXE25Gkz\_P8pEPVaHg

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic9crcwzYmib0n1UUetScibAR0FO4Qj3ibQT6FNtwcmRGjSUj3jSPRd7LGZjO8QaPAOMEFhahG0Zz1DpQ/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 8.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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