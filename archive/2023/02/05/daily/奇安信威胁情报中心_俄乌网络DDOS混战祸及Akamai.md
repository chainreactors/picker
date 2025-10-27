---
title: 俄乌网络DDOS混战祸及Akamai
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247505326&idx=1&sn=9136ee31272fd6d4da2eb74cfa53f163&chksm=ea6622d9dd11abcf90b1153ede534f04d81107649ca1d907a68c2b1e31577d187da92b0f0927&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2023-02-05
fetch_date: 2025-10-04T05:45:39.451666
---

# 俄乌网络DDOS混战祸及Akamai

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9QgUINiajR3NP3as93p770AKFWKQTo5W1ibIfetkyJLR5y8yX7nkXKjh2sQQz96jKm1KDayy7EwFsw/0?wx_fmt=jpeg)

# 俄乌网络DDOS混战祸及Akamai

原创

威胁情报中心

奇安信威胁情报中心

Akamai（阿卡迈科技）公司 是 CDN 技术的先驱，当前也是全球CDN服务领域的顶级玩家，其遍布于全球的服务节点承载着海量的互联网流量。以往经常受攻击的是 Akamai 服务的各家客户，Akamai 为他们抵御各种攻击，其抗D能力相当强悍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8jWElbVr6TkrBlu7voVI33icjz3Ugp5c7rQbAPicy1xLicWOHe2AajaDsFUyQWrqPyjpuw2zaZqcMaA/640?wx_fmt=png)

但最近奇安信威胁情报中心监测到 Akamai 自己的官方网站( akamai.com )频繁遭受来Mirai 和 Moobot 家僵尸网络的猛烈攻击。随后，我们第一时间向安全社区发布预警，希望引起国内外安全研究人员对此事件进一步探索与交流：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8jWElbVr6TkrBlu7voVI33JDuVvtv63P5fXk34w50VD4rtBf9Gvbib7Z68UmnHRhUdhXic1LSNXsBw/640?wx_fmt=png)

攻击分析

第一波攻击由一个 Mirai 僵尸网络于北京时间 2023-02-02 03:17:17 发起，攻击方式为 UDP Plain Flood，持续不到 1 分钟。C&C 为 shetoldmeshewas12.uno:38241， C&C 域名当时解析的 IP 地址为 45.12.253.12，该 IP 位于美国。

第二波攻击由一个 Moobot 僵尸网络发起，于北京时间的 2023-02-02 的 03:39, 04:22, 17:02 打出 3 次攻击，又于 2023-02-03 03:14 开始打出更大的一次攻击。每次持续数分钟，攻击方式都是 UDP Plain Flood。发起这波攻击的 C&C 为47.87.230.236:6666，IP 同样位于美国。

Akamai 官方网站的域名解析做了负载均衡，这次受攻击的目标节点IP有：

- 23[.8.7.213

- 95[.101.127.21

- 2[.20.81.128

- 23[.206.85.57

- 23[.42.231.243

鉴于 Akamai 自身的防护能力，根据我们的观察，这两波攻击对 Akamai 官网的访问并没有造成显著影响。

从我们的视野，无从得知针对 Akamai 官方网站的 DDoS 攻击背后由何人发起，但或许可以根据关联线索推测一下。

我们发现 Akamai 官方推特这两天连发两贴关于俄乌战争的分析，重点关注俄方阵营网络攻击组织 Killnet 针对医疗行业的攻击活动：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8jWElbVr6TkrBlu7voVI33r8q3xKqUWgwB7icWhDianXQBdmfbTO6qWHicauoSAPTM6eAZiaUttZudUA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8jWElbVr6TkrBlu7voVI33OibUJdWiaibV6y1ka4uibicdicKyNtLaukesfRChLTGfBibDxAeUCGT5Fw7bQ/640?wx_fmt=png)

参考受攻击的时间线，或许 Akamai 官方网站被攻击是受到了来自亲俄组织的报复。

IoCs

**C&C:**

shetoldmeshewas12.uno:38241

47.87.230.236:6666

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic8jWElbVr6TkrBlu7voVI33B4eP8ACfnwmIKZf8ibFZwFT0EVLAPtgKTO89aMr3XMJIztxb8eoY96A/640?wx_fmt=gif)

点击阅读原文至**ALPHA 6.0**

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