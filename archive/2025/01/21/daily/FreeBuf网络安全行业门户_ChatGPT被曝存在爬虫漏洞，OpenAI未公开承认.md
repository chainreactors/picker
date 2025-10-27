---
title: ChatGPT被曝存在爬虫漏洞，OpenAI未公开承认
url: https://www.freebuf.com/news/420273.html
source: FreeBuf网络安全行业门户
date: 2025-01-21
fetch_date: 2025-10-06T20:10:18.498831
---

# ChatGPT被曝存在爬虫漏洞，OpenAI未公开承认

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

ChatGPT被曝存在爬虫漏洞，OpenAI未公开承认

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

ChatGPT被曝存在爬虫漏洞，OpenAI未公开承认

2025-01-20 10:40:16

所属地 上海

![](https://image.3001.net/images/20250120/1737353745_678dea1157e14e0eac4a5.jpg!small)

**OpenAI的ChatGPT爬虫似乎能够对任意网站发起分布式拒绝服务（DDoS）攻击，而OpenAI尚未承认这一漏洞。**

本月，德国安全研究员Benjamin Flesch通过微软的GitHub分享了一篇文章，解释了如何通过向ChatGPT API发送单个HTTP请求，利用ChatGPT爬虫（特别是 ChatGPT-User）向目标网站发起大量网络请求。攻击者可以将单个API请求放大为每秒20到5000次甚至更多的请求，持续不断地发送到目标网站。从实际操作来看，这种连接的洪流虽然不足以使任何网站瘫痪，但仍被认为是一种潜在的危险，也暴露了OpenAI 的疏忽。

Flesch在他的报告中指出：“ChatGPT API在处理向 <https://chatgpt.com/backend-api/attributions>发送的HTTP POST请求时，表现出严重的质量缺陷。”他提到的API端点，被ChatGPT用于返回聊天机器人输出中引用的网络来源信息。当ChatGPT提到特定网站时，它会调用“attributions”接口，并附带这些网站的URL列表，供爬虫访问并获取相关信息。如果向API发送一个包含大量URL的列表，每个URL略有不同但都指向同一个网站，爬虫会立即访问所有这些URL 。

Flesch写道：“API期望在参数urls中接收一个超链接列表。众所周知，指向同一网站的超链接可以以多种不同的方式编写。由于编程实践不当，OpenAI没有检查列表中是否多次出现指向同一资源的超链接。 OpenAI也没有对urls参数中存储的超链接数量设置上限，从而允许在单个HTTP请求中传输数千个超链接。”

因此，攻击者可以使用Curl等工具向ChatGPT端点发送HTTP POST请求，无需身份验证令牌。OpenAI在微软Azure上的服务器将响应此请求，并为通过urls[]参数提交的每个超链接发起HTTP请求。当这些请求指向同一个网站时，可能会使目标网站不堪重负，出现DDoS症状——由Cloudflare代理的爬虫每次都会从不同的IP地址访问目标网站。

“受害者永远不会知道发生了什么，因为他们只看到同一时间，ChatGPT机器人从大约20个不同的IP地址访问他们的网站。”Flesch说。他还补充道，即使受害者启用了防火墙来阻止ChatGPT机器人使用的IP地址范围，机器人仍然会发送请求。“因此，一个失败或被阻止的请求，不会阻止ChatGPT机器人在下一毫秒再次请求受害者网站。由于这种放大效应，攻击者可以向ChatGPT API发送少量请求，但受害者将收到大量请求。”

Flesch 通过多个渠道报告了这一未经身份验证的反射型DDoS漏洞，包括OpenAI的BugCrowd漏洞报告平台、OpenAI安全团队的电子邮件、微软和HackerOne，但至今未收到任何回复。

Flesch认为更大的问题是这个API还容易受到提示注入攻击。Flesch质疑，为什么OpenAI机器人没有实现简单且成熟的方法，以正确去重请求列表中的URL，或者限制列表的大小，也没有解决在ChatGPT主界面中已修复的提示注入漏洞。

Flesch 说：“在我看来，这个小API似乎是ChatGPT AI代理的一个示例项目，任务是从用户提供的数据中解析出URL，然后使用Azure抓取网站。‘AI代理’没有内置安全功能吗？显然，处理 urls[]参数的‘AI 代理’没有资源耗尽的概念，也不明白为什么在同一秒内向同一网站发送数千个请求是愚蠢的。难道它没有意识到victim.com/1和victim.com/2都是指向同一个网站victim.com吗？如果victim.com/1的请求失败了，为什么还会立即向victim.com/2发送请求呢？这些都是人们多年来在软件中实施的验证逻辑，以防止此类滥用现象出现。 ”

Flesch表示，唯一能想到的解释是OpenAI正在使用AI代理来触发这些HTTP请求。“我无法想象一个高薪的硅谷工程师会设计出这样的软件，因为ChatGPT爬虫已经像谷歌爬虫一样在网络上爬行了多年。如果爬虫不限制对同一网站的请求数量，它们会立即被屏蔽。”

**参考来源：**

> <https://www.theregister.com/2025/01/19/openais_chatgpt_crawler_vulnerability/>

# 资讯

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