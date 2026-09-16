---
title: DNSSEC NSEC 遍历（Zone Walking）
url: https://mp.weixin.qq.com/s/2tK1hPA75mmyUhnGr2G3pQ
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:03:15.606088
---

# DNSSEC NSEC 遍历（Zone Walking）

# DNSSEC NSEC 遍历（Zone Walking）

原创

信安路漫漫
信安路漫漫

信安路漫漫

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前言

最近重新在看信息收集的知识，在看子域名收集的时候看到一个DNSSEC NSEC 遍历，以前没有怎么了解过该漏洞，本文记录一下这个漏洞如何去利用。

DNSSEC NSEC 遍历（Zone Walking）是 DNSSEC 设计中一个广为人知的信息泄露漏洞：攻击者可以通过连续查询 NSEC 记录，像“遍历链表”一样完整枚举一个 DNSSEC 签名区域中的所有域名。

目前该漏洞已经很少了，但还是记录一下，作为了解。

NSEC 记录：原理与遍历机制

DNSSEC 需要提供“某个域名不存在”的密码学证明，NSEC（Next Secure）记录正是为此设计的。每个 NSEC 记录包含两个关键信息：

l该记录所属的域名（owner name）

l区域规范排序中的下一个域名（Next Domain Name）

data.lab.test. 3600 IN NSEC help.lab.test. A RRSIG NSEC

上述记录表示：在 data.lab.test 和 help.lab.test 之间，不存在任何其他域名。整个区域的 NSEC 记录构成一个按字典序排列的单向链表，最后一个记录的 Next Domain Name 指回区域顶点（Zone Apex）。

遍历攻击的核心逻辑是：攻击者首先查询一个不存在的域名（如 doesnotexist.lab.test），权威服务器返回一个 NSEC 记录，其中包含“下一个存在的域名”。攻击者读取该域名，再以它为起点继续查询下一个不存在的名称，如此循环，即可在线性时间内枚举整个区域。这种技术被称为 Zone Walking，与需要区域传送（AXFR）权限的传统枚举方式不同，它不需要任何特殊授权，仅依赖标准的 DNS 查询。

通配符记录并不能阻止 NSEC 遍历。即使区域中存在通配符（如 \*.example.com），通配符本身也被签名为 \* 并出现在 NSEC 链中，攻击者仍然可以完成遍历

测试方式

接下来看看如何验证该遍历是否存在

1. 找到权威服务器

dig +short NS example.com

假设返回：

ns1.example.com.

ns2.example.com.

后面直接向权威服务器查询，避免递归解析器缓存干扰。

2. 查询区域顶点的 NSEC 记录

dig @ns1.example.com +dnssec +norecurse example.com NSEC

重点看 ANSWER SECTION：

;; ANSWER SECTION:

example.com. 3600 IN NSEC a.example.com. A NS SOA MX RRSIG NSEC DNSKEY

这表示：

l当前名字：example.com.

l下一个名字：a.example.com.

l中间没有其他名字。

如何返回了NSEC则证明存在

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBzeSE9F8n8h6enwOQRic7J3SE7afEypJIw6rfTP291hkrrVzeuGMOlj17RGwbv8wJibtdQnmamtGNmQ/0?wx_fmt=png)

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