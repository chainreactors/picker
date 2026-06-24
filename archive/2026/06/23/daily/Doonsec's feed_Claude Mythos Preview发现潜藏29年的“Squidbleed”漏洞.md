---
title: Claude Mythos Preview发现潜藏29年的“Squidbleed”漏洞
url: https://mp.weixin.qq.com/s/CnDm2DWTOSZi22ez7el_qw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:39.424247
---

# Claude Mythos Preview发现潜藏29年的“Squidbleed”漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2K3yvU4BAgS7WjVXQh6qtyp2XT31fRgSvibhG3tzTDm5upg5Cgd87wh8Bt7sRZ54XGnobWTWLgZZF5FcicT5z4Vf78avr7qmGvY/0?wx_fmt=jpeg)

# Claude Mythos Preview发现潜藏29年的“Squidbleed”漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2oyCCN02RRU6jMb1Y5tItWicQ2CyVbgP9gkNzYz8XeMauOQax5NyyDnXS2yAPVmeManplP5yiajvby3Jg1Nt1Yz6jYDZD6uVNno/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1jOuwRuoxTEcRIYu7poFI0GXXxN8Ulu2wRXQaqdr5EWSl31JlmYumf5uzRrLSFs4wH0pT1Hj0gHVCbhFqp41padzNibAOGO93A/640?wx_fmt=png&from=appmsg)

安全研究人员在Squid代理软件中发现了一个类似Heartbleed的堆缓冲区越界读取漏洞，该漏洞自1997年以来一直存在，可悄无声息地泄露同一代理上其他用户的HTTP头信息（包括密码和API密钥）。Calif.io的安全研究人员披露了这个名为Squidbleed的关键内存泄露漏洞，其发现得到了Anthropic公司Claude Mythos Preview AI模型的协助。

该漏洞影响所有默认配置下的Squid版本，且已潜伏近三十年之久，甚至早于Squid在GitHub仓库中的所有可用提交记录。

Part01

29年历史的Squidbleed漏洞

Squidbleed（CVE编号待定）是一个存在于Squid FTP目录列表解析器中的堆缓冲区越界读取漏洞。当被利用时，会导致Squid读取超出堆分配缓冲区的内存，并将这些残留数据作为FTP目录列表响应的一部分返回，其中可能包含其他用户的HTTP请求、授权头信息或API密钥。

该漏洞可追溯至1997年1月18日的一个提交，该提交添加了处理NetWare FTP服务器的逻辑，这些服务器在文件修改时间戳和文件名之间放置了四个空格。修复代码引入了一个while(strchr(w\_space, \*copyFrom))循环，旨在跳过额外的空白字符。

然而存在一个关键疏忽：根据C11 §7.24.5.2标准，C语言中的strchr函数将空终止符（\0）视为搜索字符串的一部分。当时间戳后没有文件名时，copyFrom指向一个空字节，但strchr不会停止而是返回非NULL值，导致++copyFrom递增超过缓冲区边界进入相邻的堆内存。

经AddressSanitizer (ASAN)验证，确认存在最多4,065字节的堆越界读取。

Squid在malloc之上使用按大小分类的空闲列表。当4KB缓冲区被释放时，会被回收而不清零。如果受害者的HTTP请求先前存储在MEM\_4K\_BUF中（Squid 7.x上大多数标准HTTP请求都是这种情况，其中CLIENT\_REQ\_BUF\_SZ设置为4096），只有前几十个字节会被简短的FTP列表行覆盖。缓冲区的其余部分仍保留受害者的残留请求数据。

控制可从代理访问的FTP服务器的攻击者，可以通过发送不含文件名的畸形目录列表来触发越界读取，导致Squid返回受害者的回收HTTP数据（包括Authorization头信息和会话令牌）作为FTP响应的一部分。

Part02

Squidbleed攻击面

攻击面具有特定条件但切实存在：

* 必须启用FTP支持（默认开启）
* 攻击者必须控制可从代理TCP端口21访问的FTP服务器（包含在Squid默认的Safe\_ports ACL中）
* 受害者流量必须是明文HTTP或通过TLS终止代理设置（HTTPS CONNECT隧道不透明且不受影响）

研究人员通过共享Squid代理从登录页面泄露Authorization头信息证实了该攻击。GitHub上已公开PoC。

修复方案是在每次strchr调用前添加单行空值检查：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2lcSN1wff48juv9zfeNpGyV0EsxrdiaTlRmyibxXLgLHxicxrKKibwPeWkyR2l1InqRx73s2S8RMt5budaEFtxUAnApbHxozl8wHY/640?wx_fmt=png&from=appmsg)

```

```

该补丁已合并到Squid代码库。强烈建议管理员禁用FTP支持（除非明确需要），因为包括所有基于Chromium的浏览器在内的大多数现代浏览器多年前就已放弃FTP支持，使得合法的FTP代理流量极为罕见。

该发现是通过指导Claude Mythos Preview使用多Agent分析调查Squid的FTP状态机实现的。该模型几乎立即标记出了strchr空终止符行为，展示了基于C标准参考训练的LLM如何能发现人类代码审查容易忽略的微妙API契约违规。

此前该团队曾披露使用OpenAI的Codex Cyber发现的隐藏HTTP/2漏洞，这标志着AI辅助开源安全审计的更广泛趋势。

参考来源：

29-Year-Old 'Squidbleed' Vulnerability Discovered With the Aid of Claude Mythos Preview

https://cybersecuritynews.com/squidbleed-vulnerability/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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