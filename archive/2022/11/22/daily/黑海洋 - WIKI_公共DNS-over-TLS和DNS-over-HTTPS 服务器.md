---
title: 公共DNS-over-TLS和DNS-over-HTTPS 服务器
url: https://blog.upx8.com/3104
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:14.909238
---

# 公共DNS-over-TLS和DNS-over-HTTPS 服务器

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 公共DNS-over-TLS和DNS-over-HTTPS 服务器

发布时间:
2022-11-21

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
20826

## 一、国内服务商

### 1、阿里公共DNS

阿里提供的DNS，测试阶段，存在污染。
**DoT地址：**
`dns.alidns.com`
`223.5.5.5`
`223.6.6.6`

**DoH地址：**
RFC8484地址：
`https://dns.alidns.com/dns-query`
`https://223.5.5.5/dns-query`
`https://223.6.6.6/dns-query`

JSON地址:
`https://dns.alidns.com/resolve`
`https://223.5.5.5/resolve`
`https://223.6.6.6/resolve`
`http://dns.alidns.com/resolve`
`http://223.5.5.5/resolve`
`http://223.6.6.6/resolve`

### 2、DnsPod 公共DNS

腾讯提供的DNS，测试阶段，存在污染。
DoT地址：`dns.pub` 或者 `doh.pub`
DoH地址：`https://doh.pub/dns-query`

### 3、360DNS

360提供的DNS，360浏览器内置的DOH服务地址，存在污染。
DoT地址：`dot.360.cn`
DoH地址：`doh.360.cn`

开发者调用：
DoH的调用方式支持RFC8484和JSON两种调用方式：
RFC8484：`https://doh.360.cn/dns-query`
JSON：`https://doh.360.cn/query?`

### 4、中国下一代互联网公共DNS.

DoT地址：`dns.cfiec.net`
DoH地址：`https://dns.cfiec.net/dns-query`

### 4、红鱼dns

DoT地址：`rubyfish.cn`
DoH地址：`https://rubyfish.cn/dns-query`

### 5、GEEKDNS

公益性站点，不做稳定性承诺，支持 EDNS-Client-Subnet。
DOH地址(国内) : `https://i.233py.com/dns-query`
DOH地址(国外)：`https://dns.233py.com/dns-query`

## 二、国外服务商

### 1、Cloudflare 公共DNS

知名云服务商 Cloudflare 提供的解析服务器。
**DoT地址：** `1.1.1.1`
`1.0.0.1`
`cloudflare-dns.com`

**DoH地址：**
`https://1.1.1.1/dns-query`
`https://1.0.0.1/dns-query`
`https://1dot1dot1dot1.cloudflare-dns.com`

### 2、Google 公共DNS

**DoT地址：**
`dns.google`
`8.8.8.8`
`8.8.4.4`

**DoH地址：**
RFC8484(GET/POST)：
`https://dns.google/dns-query`
`https://8.8.8.8/dns-query`
`https://8.8.4.4/dns-query`

JSON(GET)：
`https://dns.google/resolve`
`https://8.8.8.8/resolve`
`https://8.8.4.4/resolve`

### 3、DNS.SB

服务器位于国外，但延迟使用体检较为可观，支持EDNS-Client-Subnet。
**DoT地址：**
`dns.sb`
`185.222.222.222`
`185.184.222.222`
`2a09::`
`2a09::1`

DoH地址：`https://doh.dns.sb/dns-query`

### 4、AdGuard DNS

存在广告拦截,采用Anycast，全球多地存在节点。

**DoT地址：**
默认服务器：`dns.adguard.com`
家庭保护服务器：`dns-family.adguard.com`
非过滤服务器：`dns-unfiltered.adguard.com`

**DoH地址：**
默认服务器：`https://dns.adguard.com/dns-query`
家庭保护服务器：`https://dns-family.adguard.com/dns-query`
非过滤服务器：`https://dns-unfiltered.adguard.com/dns-query`

**DNS-over-QUIC地址：**
默认服务器：`quic://dns.adguard.com`
家庭保护服务器：`quic://dns-family.adguard.com`
非过滤服务器：`quic://dns-unfiltered.adguard.com`

**DNSCrypt地址：**
默认服务器：`sdns://AQIAAAAAAAAAFDE3Ni4xMDMuMTMwLjEzMDo1NDQzINErR_JS3PLCu_iZEIbq95zkSV2LFsigxDIuUso_OQhzIjIuZG5zY3J5cHQuZGVmYXVsdC5uczEuYWRndWFyZC5jb20`
家庭保护服务器：`sdns://AQIAAAAAAAAAFDE3Ni4xMDMuMTMwLjEzMjo1NDQzILgxXdexS27jIKRw3C7Wsao5jMnlhvhdRUXWuMm1AFq6ITIuZG5zY3J5cHQuZmFtaWx5Lm5zMS5hZGd1YXJkLmNvbQ`
非过滤服务器：`sdns://AQcAAAAAAAAAFDE3Ni4xMDMuMTMwLjEzNjo1NDQzILXoRNa4Oj4-EmjraB--pw3jxfpo29aIFB2_LsBmstr6JTIuZG5zY3J5cHQudW5maWx0ZXJlZC5uczEuYWRndWFyZC5jb20`

### 5、Quad9 公共DNS

IBM提供的公共DNS服务器。
DoT地址：`dns.quad9.net` 或 `9.9.9.9` 或 `149.112.112.10`
DoH地址(EDNS-Client-Subnet)：

| 服务 | DOH地址 | DNSSEC | 恶意拦截 | 加密 | IP地址(IPv4/IPv6) |
| --- | --- | --- | --- | --- | --- |
| 安全(推荐) | `https://dns.quad9.net/dns-query` | 是 | 是 | 是 | `9.9.9.9` `149.112.112.112` `2620:fe::fe` `2620:fe::fe:9` |
| 安全 | `https://dns9.quad9.net/dns-query` | 是 | 是 | 是 | `9.9.9.9` `149.112.112.9` `2620:fe::9` `2620:fe::fe:9` |
| 不安全 | `https://dns10.quad9.net/dns-query` | 否 | 否 | 是 | `9.9.9.10` `149.112.112.10` `2620:fe::10` `2620:fe::fe:10` |
| 安全(支持ECS) | `https://dns11.quad9.net/dns-query` | 是 | 是 | 是 | `9.9.9.11` `149.112.112.11` `2620:fe::11` `2620:fe::fe:11` |

[取消回复](https://blog.upx8.com/3104#respond-post-3104)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")