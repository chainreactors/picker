---
title: CSOP-2023：云上攻防的点-线-面-体
url: https://buaq.net/go-170916.html
source: unSafe.sh - 不安全
date: 2023-07-01
fetch_date: 2025-10-04T11:51:04.553557
---

# CSOP-2023：云上攻防的点-线-面-体

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

![](https://8aqnet.cdn.bcebos.com/7d0e496df5822252a549ad10c6817da1.jpg)

CSOP-2023：云上攻防的点-线-面-体

注：本议题公开发布于CSOP-2023（北京站）。
议题演讲材料下载：安全小飞侠\_CSOP 2023北京站\_云上攻防的点-线-面-体
*2023-6-30 20:26:9
Author: [avfisher.win(查看原文)](/jump-170916.htm)
阅读量:58
收藏*

---

注：本议题公开发布于CSOP-2023（北京站）。

[![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.001](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.001.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.001.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.003](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.003.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.003.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.004](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.004.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.004.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.005](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.005.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.005.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.006](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.006.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.006.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.007](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.007.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.007.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.008](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.008.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.008.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.009](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.009.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.009.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.010](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.010.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.010.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.011](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.011.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.011.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.012](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.012.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.012.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.013](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.013.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.013.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.014](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.014.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.014.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.015](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.015.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.015.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.016](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.016.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.016.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.017](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.017.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.017.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.018](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.018.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.018.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.019](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.019.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.019.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.020](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.020.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.020.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.021](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.021.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B9-%E7%BA%BF-%E9%9D%A2-%E4%BD%93.021.png) [![安全小飞侠_CSOP 2023北京站_云上攻防的点-线-面-体.022](http://avfisher.win/wp-content/uploads/2023/06/安全小飞侠_CSOP-2023北京站_云上攻防的点-线-面-体.022.png)](http://avfisher.win/wp-content/uploads/2023/06/%E5%AE%89%E5%85%A8%E5%B0%8F%E9%A3%9E%E4%BE%A0_CSOP-2023%E5%8C%97%E4%BA%AC%E7%AB%99_%E4%BA%91%E4%B8%8A%E6%94%BB%E9%98%B2%E7%9A%84%E7%82%B...