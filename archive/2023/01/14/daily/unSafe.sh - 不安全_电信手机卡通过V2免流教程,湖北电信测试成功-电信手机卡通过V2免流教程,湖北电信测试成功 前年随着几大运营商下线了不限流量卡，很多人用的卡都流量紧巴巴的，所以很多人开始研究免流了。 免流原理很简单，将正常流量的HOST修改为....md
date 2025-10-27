---
title: 电信手机卡通过V2免流教程,湖北电信测试成功-电信手机卡通过V2免流教程,湖北电信测试成功 前年随着几大运营商下线了不限流量卡，很多人用的卡都流量紧巴巴的，所以很多人开始研究免流了。 免流原理很简单，将正常流量的HOST修改为...
url: https://buaq.net/go-145423.html
source: unSafe.sh - 不安全
date: 2023-01-14
fetch_date: 2025-10-04T03:51:09.881492
---

# 电信手机卡通过V2免流教程,湖北电信测试成功-电信手机卡通过V2免流教程,湖北电信测试成功 前年随着几大运营商下线了不限流量卡，很多人用的卡都流量紧巴巴的，所以很多人开始研究免流了。 免流原理很简单，将正常流量的HOST修改为...

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

![](https://8aqnet.cdn.bcebos.com/0c830b21e85932b344cbe7906258f945.jpg)

电信手机卡通过V2免流教程,湖北电信测试成功-电信手机卡通过V2免流教程,湖北电信测试成功 前年随着几大运营商下线了不限流量卡，很多人用的卡都流量紧巴巴的，所以很多人开始研究免流了。 免流原理很简单，将正常流量的HOST修改为...

首页>> 技术文档>>电信手机卡通过V2免流教程,湖北电信测试成功 2022-3-9 电信手机卡通过V2免流教
*2023-1-13 19:47:52
Author: [www.xgiu.com(查看原文)](/jump-145423.htm)
阅读量:62
收藏*

---

[首页](http://www.xgiu.com/)>> [技术文档](http:////www.xgiu.com/sort/2)
>>电信手机卡通过V2免流教程,湖北电信测试成功

![](http:////www.xgiu.com/content/templates/Fys/images/tupian/6.jpg)

2022-3-9

## 电信手机卡通过V2免流教程,湖北电信测试成功

![](https://api.qrserver.com/v1/create-qr-code/?data=http:////www.xgiu.com/dianxin-ty-mljc)手机扫码查看

电信手机卡通过V2免流教程,湖北电信测试成功
前年随着几大运营商下线了不限流量卡，很多人用的卡都流量紧巴巴的，所以很多人开始研究免流了。
免流原理很简单，将正常流量的HOST修改为免费流量的h......

电信手机卡通过V2免流教程,湖北电信测试成功

前年随着几大运营商下线了不限流量卡，很多人用的卡都流量紧巴巴的，所以很多人开始研究免流了。

电信的免流相对容易，因为它基本不限端口，不像联通那样要80才能行(但是需要手机卡有定向流量包，电信的免流依赖于定向，连自家的掌厅也要有定向才能免流)。

既然电信不限端口，随便自家宽带搭建个V2服务器就可以给自己使用了。

V2那玩意没法多说，我是用的矿渣[赚钱宝PRO这刷OpenWRT](http://www.xgiu.com/zhuanqianbao_pro_openwrt)后[搭建V2](http://www.xgiu.com/openwrt-for-v2server)提供免流的。
赚钱宝只有百兆端口，但是它是真的没利用价值了所以超便宜。
(如果自己没条件搭建，可以入手加速器网站)

搭建好后，我的电信卡有天翼视讯定向流量包和天翼云盘定向流量包，于是先用一个天翼云盘定向包来测试。
设置如下(抱歉软件自己找哈,本站不提供下载)
[![填写免流混淆Host](http://www.xgiu.com/content/uploadfile/202203/f48e1646824661.jpg "填写免流混淆Host")](http://www.xgiu.com/content/uploadfile/202203/f48e1646824661.jpg)

刷了几个小时的直播，效果还是不错的。
流量查询如下
[![电信免流效果图](http://www.xgiu.com/content/uploadfile/202203/1abd1646824661.jpg "电信免流效果图")](http://www.xgiu.com/content/uploadfile/202203/1abd1646824661.jpg)

电信我问过一些大佬，基本全国的电信免流只要有定向流量包，基本就是不限端口免流的。
电信的公网IP很容易得到，可以通过DDNS+公网IP更新IP地址。
如果像移动宽带那样没有公网IP的话该咋办？

此处内容已隐藏，[评论](#comment-post)后刷新即可查看！

> 关于跳点：谷子用的WS连接模式，亲测湖北电信的免流跳点蛮低的，也问过别人TCP=HTTP也不高。在意的话用脚本呗。
> 关于定向包：电信的一些卡如无忧卡都是不带任何定向流量包的，可以尝试下载天翼视频客户端开通天翼视讯(20G)，或者开通电信5G会员后开通云盘流量包(50G),电信老卡很多不限量流量包的。
> 为啥有定向包不免: 手机卡如果开通了5G SA网络，很可能就不能免了，可以问电信客服要求取消5G SA。
> 湖北电信可以停机上网吗？湖北电信手机卡可以停机上网(停机后用wap.hb.189.cn)，但是限速1M :(

天翼全家桶的几个混淆：
> 天翼VR: vod5gct.yvr5g.tv189.com
> 天翼云盘 : cloud189-anhui-home.oos-ahwh.ctyunapi.cn
> 天翼云游戏 : cdn.cloud.play.cn
> 天翼视讯: vod1.nty.tv189.com

*×*
![mrhee](http:////www.xgiu.com/content/templates/Fys/img/fys.png)

感谢您的支持，我们会一直保持!

![扫码支持](http:////www.xgiu.com/content/templates/Fys/img/alipayimg.png "扫一扫")

请土豪扫码随意打赏

![支付宝](data:image/png;base64...)

![微信](data:image/png;base64...)

打开支付宝扫一扫，即可进行扫码打赏哦

分享从这里开始，精彩与您同在

打赏作者

### 相关推荐

* [华为云DNS/支持地域解析/运营商线路解析的免费域名DNS服务](http:////www.xgiu.com/huawei_DNS)
* [ios系统iPhone苹果手机小火箭免流跳点高怎么办?](http:////www.xgiu.com/ios-gb-udp)
* [[原创]礼品盒的简单摄影](http:////www.xgiu.com/photograph_box)
* [[技巧]利用国内CDN,加速国外VPS建站优化访问方法](http:////www.xgiu.com/cdn_speedup_vps)
* [通过IP自定义ghs.google.com使用Google邮局(Google Apps)等服务的自定义域名](http:////www.xgiu.com/ghs_google_ip)
* [[原创]QQ聊天记录意外删除的恢复-EasyRecovery软件篇](http:////www.xgiu.com/qq_chat_message)

文章来源: http://www.xgiu.com/dianxin-ty-mljc
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)