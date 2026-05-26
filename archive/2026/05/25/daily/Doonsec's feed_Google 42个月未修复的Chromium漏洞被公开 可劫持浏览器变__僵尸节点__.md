---
title: Google 42个月未修复的Chromium漏洞被公开 可劫持浏览器变\"僵尸节点\"
url: https://mp.weixin.qq.com/s/wGRVggdfNW1XsC8tpIhYNw
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:17.882515
---

# Google 42个月未修复的Chromium漏洞被公开 可劫持浏览器变\"僵尸节点\"

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1SfkU98PuQWFo050nEnmzkmPRlicDHmLz31yvYibEUoo8fAX2YEJwKedTEr81iaalpbUg7JYIzga0N3O5sq44xhHice3Hz9G1mlZk/0?wx_fmt=jpeg)

# Google 42个月未修复的Chromium漏洞被公开 可劫持浏览器变"僵尸节点"

FreeBuf
FreeBuf

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0mqFQb9Nv73U9fOibEXjhsdeAAu6veUKs47zsMhiaALh5teXUGXJZ1j5yoqNWGwArc07tPH83peEd9TFd2UbD2fsn6icReAfOLaM/640?wx_fmt=gif)

![微信图片_2026-05-25_134918_119](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX31hSHmvtTo0IGFDmyDxWXEicJ1W0OYMV3raaIySocpEVobkTvMpC7zgQTTKicnVrOibWlJHNtca4vfwFzdLbpibg6J6HjaVCkwibhM/640?wx_fmt=png)

谷歌近日公开了Chromium代码库中一个严重未修复漏洞的概念验证（PoC）利用代码，可能导致全球数百万使用Chrome、Microsoft Edge及其他基于Chromium的浏览器用户遭受隐蔽的僵尸网络攻击。

Part01

漏洞技术细节

该漏洞最初由独立安全研究员Lyra Rebane于2022年底报告，至今42个月仍未修复。根据Chromium漏洞分类框架，该漏洞被评定为优先级1（P1）和严重性2（S2），属于高危安全问题。

漏洞存在于Browser Fetch API中，该功能原本设计用于通过Service Workers在后台持续下载视频等大文件。但Rebane发现，攻击者可滥用此机制创建永不终止的任务，持续与攻击者控制的基础设施保持通信。

利用此漏洞，攻击者能在受害者浏览器与命令控制（C2）服务器间建立隐蔽通信通道。值得注意的是，在Microsoft Edge等实现中，即使关闭浏览器或重启系统，连接仍可能持续存在。

Part02

仅需访问网页即可触发攻击

该攻击方式因操作简单而尤为危险——用户只需访问恶意或被攻陷的网站，其浏览器就会悄无声息地加入僵尸网络。Rebane在报告中指出，攻击者可通过部署含有Service Worker的恶意网页，启动永不终止的后台获取任务，从而在受害者设备上持续执行JavaScript代码。

"获取数万次页面浏览以构建'僵尸网络'完全可行，而用户根本不会察觉其设备正在远程执行JavaScript代码。"Rebane在原始报告中强调。

虽然受浏览器沙箱限制，该漏洞仍具有大规模风险，潜在滥用场景包括：

分布式拒绝服务（DDoS）：操控被入侵浏览器对目标基础设施发起流量攻击

* 代理网络：通过受害者浏览器路由恶意或匿名流量
* 流量重定向：将用户悄无声息导向攻击者控制的目标
* 活动监控：有限度地追踪用户浏览行为及网络活动

Part03

漏洞修复现状与缓解措施

谷歌在发布补丁前公开利用代码的决定引发安全社区担忧。Rebane表示，虽然扩大攻击规模需要额外基础设施，但PoC代码显著降低了威胁分子的利用门槛。

Chromium问题追踪系统中，多名开发者承认该漏洞的严重性，称其为"重大安全漏洞"。

受影响平台包括：

* Google Chrome
* Microsoft Edge
* Brave Browser
* Opera
* 其他基于Chromium的浏览器

在官方补丁发布前，用户及组织可采取以下缓解措施：

* 通过企业浏览器策略限制Service Worker使用
* 如可配置则禁用后台获取功能
* 使用网络级监控检测异常出站浏览器连接
* 在企业环境中部署浏览器隔离技术

目前漏洞利用代码已公开且无补丁可用，这为企图构建大规模浏览器僵尸网络的威胁分子提供了绝佳机会窗口。

参考来源：

Google Publishes Exploit Code for Unfixed Chromium Bug Exposing Millions of Users

https://cybersecuritynews.com/google-publishes-chromium-exploit-code/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1SRP5DY7WibSicW4eWTtYzFWDTfVGMqCQ4UicdvaeHbSfA0ReLjXu6why8RH43kXBsNQ39qgiaxrmAsN9kbEnVENaHKmtQZib2otm8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338613&idx=1&sn=d0ae0c38319293b058cc4ff73b9319ae&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2SyOCpMWiaRGCVOcBia89UPEschd9VicMFd7SM1rhpC18v24yZmRTYBC8tEqUDDS3qdYSfbjKdJickyhKGibU8gBkvBNA4wk6YmXR4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1Mc3ZOqCiaDRJcWldjwND8b2QZM5VGZJe2eAfXLW0rCCWDKS4ocS8UZCD3aK9eqUoWb7r1P0XvabDoCCiaONhhhdpONOIsq1FTs/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2Az1vOlhlAErAwmh4fywticBYdb15B9lwtbKiaElQ1VIL9SPNNRjtcLhMIled4SREdBLeRagMicK8MMoP7JiawWfibePrQB2mPwtk0/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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