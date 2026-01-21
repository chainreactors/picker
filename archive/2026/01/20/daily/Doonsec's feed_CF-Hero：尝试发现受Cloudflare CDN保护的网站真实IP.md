---
title: CF-Hero：尝试发现受Cloudflare CDN保护的网站真实IP
url: https://mp.weixin.qq.com/s/kOnI5Ssz674KuGK8_DpYCQ
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:33.431069
---

# CF-Hero：尝试发现受Cloudflare CDN保护的网站真实IP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9ugoxfeOwuv2GCL8h9d59qZEiaeLDEob0kwUSJjZ437xUQWdXjg6AT8UFm5Nj0tHZq7iaeVQyCwVsB9A/0?wx_fmt=jpeg)

# CF-Hero：尝试发现受Cloudflare CDN保护的网站真实IP

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Yakit：一款集成的强大黑客工具（抓包，中间人劫持，漏洞利用）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486052&idx=1&sn=c3af88f16854d54bc1aab8269b3acf2a&scene=21#wechat_redirect)

·[在Kali上部署HexStrike Ai：让Ai用kali进行全自动渗透测试和CTF解题](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486029&idx=1&sn=ba0ff37837ecc19bf7add1528fdbc669&scene=21#wechat_redirect)

·[近期你还有这些CTF比赛可以参加](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485991&idx=1&sn=0b4a6008c576aba3da570cccfc6f555d&scene=21#wechat_redirect)

·[SpringBoot-Scan：针对Spring Boot的漏洞扫描和渗透工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485898&idx=1&sn=e1eb04e1d90f09ea5cfa447fac6ad66a&scene=21#wechat_redirect)

·[针对 Oracle WebLogic 中间件的一体化渗透测试工具：WeblogicTool](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485969&idx=1&sn=72169d6201cb7966e222cfc64535fbd5&scene=21#wechat_redirect)

·[Burp插件-BurpFingerPrint:被动指纹识别与弱口令爆破](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485896&idx=1&sn=ca895f451df48ff7e310794c1eee3627&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

介绍

CF-Hero是一款用Go语言开发的综合侦察工具，专门用于发现受Cloudflare保护的Web应用程序的真实 IP 地址。它通过多种方法和数据源进行多源情报收集，以识别潜在的源 IP 地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9ugoxfeOwuv2GCL8h9d59qZEzJMEqL6K56WRuKtr6d0SPoGeaiayL40oUeTD7CRxWtxUeK3ClDxaBQg/640?wx_fmt=jpeg)

项目地址:

```
https://github.com/musana/CF-Hero
```

## 核心功能

DNS 侦察

```
检查当前 DNS 记录（A、TXT）历史 DNS 数据分析关联域名发现
```

### 情报来源

```
ZoomEye 搜索引擎Censys 搜索引擎Shodan 搜索引擎SecurityTrails 历史记录主动 DNS 枚举相关域关联分析
```

### 高级特性

```
支持自定义 JA3 指纹并发扫描能力标准输入支持（管道）HTML 标题比较验证代理支持自定义 User-Agent 配置
```

**工作原理**：它并非使用暴力破解，而是通过汇总和分析多个开源情报来源的数据，进行交叉比对和智能验证来寻找可能的真实IP。项目介绍中提到，虽然主要针对Cloudflare，但其方法理论上也适用于其他CDN服务

CF-Hero 通过以下流程工作：

```
1. 检查目标域名的 A 记录2. 确定域名是否受 Cloudflare 保护3. 从多个来源收集情报（历史 DNS、OSINT 搜索引擎、子域名等）4. 对收集到的 IP 地址进行 HTTP 连接测试5. 通过比较 HTML 标题验证结果，减少误报6. 输出真实 IP 地址
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**安装和使用**

安装：

```
go install -v github.com/musana/cf-hero/cmd/cf-hero@latest
```

如果网络不好，可以用：

```
GOPROXY=https://goproxy.cn go install -v github.com/musana/cf-hero/cmd/cf-hero@latest
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugoxfeOwuv2GCL8h9d59qZEkMJiaBp6MoNMOU8NBMBE0QiaaY8wbvDF4QicHYGvw8YR7s5RQQzDnvTsw/640?wx_fmt=png&from=appmsg)

基本用法

```
# 从文件读取域名列表cf-hero -f domains.txt# 使用管道cat domains.txt | cf-hero# 包含特定情报源cf-hero -f domains.txt -zoomeye -shodan -censys
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugoxfeOwuv2GCL8h9d59qZEgvIDBl0zW2GGbuTV49dzgkSn4moFTR7ia7SXz4eIibd2pFlCxgkiborzg/640?wx_fmt=png&from=appmsg)

### 配置 API 密钥

在 ~/.config/cf-hero.yaml 文件中配置各情报源的 API 密钥：

```
zoomeye:  - "api_key_here"securitytrails:  - "api_key_here"shodan:  - "api_key_here"censys:  - "api_key_here"
```

找到了真实的ip

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugoxfeOwuv2GCL8h9d59qZE1lngUg5t4KdicIWEibTtLdic7hhAhI0nmoln4F4hF4eGZzia8tP7S1bZZg/640?wx_fmt=png&from=appmsg)

其中可以根据显示得知哪些是没有被cloudflare的cdn处理的，哪些被处理的网站的真实ip是多少

对比：

当网站使用 Cloudflare 保护时，直接扫描会得到 Cloudflare CDN 节点的 IP 地址（即“虚假 IP”），而不是源服务器的真实 IP。以下是 常见会得到虚假 IP 的工具 ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugoxfeOwuv2GCL8h9d59qZEepRXwCI71iaCkHNDHB0Ik16uC5VyNQww9FDTxjiaOCtxxS4Yj5UFCvkw/640?wx_fmt=png&from=appmsg)

```
工具             示例命令                             结果 nslookup     nslookup example.com         返回 Cloudflare 的 A 记录 IP dig            dig example.com A          返回 Cloudflare 节点 IP host           host example.com           返回 Cloudflare IP 地址 ping           ping example.com           显示 Cloudflare 节点 IPtraceroute   traceroute example.com       路由到 Cloudflare 节点 nmap(基础扫描） nmap example.com           扫描Cloudflare 节点的开放端口 tcpdump     tcpdump host example.com     捕获到 Cloudflare 节点的流量
```

将ping的结果对比cf-hero的结果，发现明显的ip变化：ping得到的结果是经过cloudflare的cdn处理后的受保护的，并非真实的ip。

题外话：

为什么这些工具会得到虚假 IP？

Cloudflare 的核心工作原理是 反向代理 ：

```
1. 网站将 DNS 记录指向 Cloudflare 的 nameserver2. Cloudflare 为网站分配自己的 CDN 节点 IP3. 所有访问请求先到达 Cloudflare 节点，再转发到源服务器4. 源服务器的真实 IP 被隐藏，对外只暴露 Cloudflare 节点 IP
```

如何识别得到的是 Cloudflare 虚假 IP？

1. 检查 IP 归属 ：Cloudflare 有公开的 IP 段，可通过以下方式验证：

```
 在线工具： https://www.cloudflare.com/ips/ 命令行： whois <IP> 查看归属是否为 Cloudflare 代码验证：CF-Hero 等工具内置了 Cloudflare IP 段检查
```

2. 查看响应头 ：

    使用 curl -I 检查响应头，若包含 cf-ray 、 server: cloudflare 等字段，则说明经过 Cloudflare 代理。

3. 对比响应时间 ：

    Cloudflare CDN 节点通常响应更快，而源服务器可能响应较慢（但不绝对）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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