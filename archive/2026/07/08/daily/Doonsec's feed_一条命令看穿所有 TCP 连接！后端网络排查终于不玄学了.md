---
title: 一条命令看穿所有 TCP 连接！后端网络排查终于不玄学了
url: https://mp.weixin.qq.com/s/fnco2rckJM_aukYq3M04Ew
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:57:55.631447
---

# 一条命令看穿所有 TCP 连接！后端网络排查终于不玄学了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfxcPnL1KuibjvPwdI8hvxqQER6MheocrRcJORic2bNKYHz8Pic8B3Diad6DKOvPl5PZ5BiaBsXnozYCLhO9rfTqmnQQ1tC6vBBddEfA/0?wx_fmt=jpeg)

# 一条命令看穿所有 TCP 连接！后端网络排查终于不玄学了

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

TOOL预计阅读 6 分钟 · 共 2112 字

tproxy：把网络行为变成肉眼可见的数据流

轻量级 TCP 代理 · 网络排查效率神器

tcpdump抓包太原始？Wireshark 过滤太繁琐？tproxy让你用一条命令实时拦截并转发任意 TCP流量，gRPC连接建立、MySQL连接池状态、重传率和 RTT 等指标全部清晰可见。

HIGHLIGHT

一句话定位 tproxy

轻量级开源网络代理工具

tproxy 不是简单抓包，而是把网络行为变成肉眼可见的清晰数据流。一条命令即可实时观测任意 TCP 连接全生命周期，支持 gRPC、HTTP2、Redis、MongoDB 等协议自动解析。

![tproxy 运行界面](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzIRYxT3hktmMHjLADdEgxvm9zBQKZznGv4bwhZllh1Dvg2uKnpiaM2EvyPJVsSqHc3w3z8pzvJ1vsIadWZp3h2wRAO108D2LLQ/640?wx_fmt=png&from=appmsg)

CHAPTER 01

**01****核心能力一览**观测 · 解析 · 模拟

CAPABILITIES

五大核心能力

1

实时观测

任意TCP连接全生命周期

2

智能协议解析

支持 gRPC、HTTP2、Redis、MongoDB 等，自动识别业务内容

3

网络性能指标直出

重传率、RTT、丢包情况一目了然

4

接池状态透视

总连接数、活跃/空闲连接、最大并发等关键数据实时显示

5

延迟转发|上下行限速

轻松模拟弱网环境，压测和问题复现超方便

CHAPTER 02

**02****真实使用案例**从实战中验证效率

[案例 01]

gRPC 接口偶发超时

tproxy -p 8088 -r localhost:8081 -t grpc -d 100ms，立刻看到连接建立、断开、重连全过程，5 分钟定位问题。

![gRPC 案例截图](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfxdAx8Aic1qQvGPfVYpj5wBKEd74LicG0kGoKSmqMIn2HyZib2NomHjCcN7p8EcgMgKb1N9BvvmCGNlOFEmsmibhdINHBHQWBN1ad8/640?wx_fmt=png&from=appmsg)

[案例 02]

MySQL 连接池打满

tproxy -p 3307 -r localhost:3306 -s -q，实时监控连接数变化与池生命周期，瞬间判断是配置问题还是流量突增。

![MySQL 连接池案例截图](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwbydz6BYRVZZmYYIfSC1UxwjR4OTdwOAbFxKv0VCUUp0UKibAQ6GsCcJCPUPdOqKhYpI9ibvicMt805KT425xS9sMXzJTHwmmhUM/640?wx_fmt=png&from=appmsg)

[案例 03]

分析 MySQL 连接

tproxy -p 3307 -r localhost:3306，直连观测连接行为。

![MySQL 连接分析截图](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfy57K24a487MGqypTSsRiaibXOlJVbHLxVOgo54mpWETEPgfqVGhv4ibese7ib1BQ4sAmkweLBtDxuX3RKAiceWfISnbdguBNaYk6zw/640?wx_fmt=png&from=appmsg)

[案例 04]

看网络状况（重传率和RTT）

tproxy -l 0.0.0.0 -p 7777 -r host.docker.internal:8888 -s -q，直接输出重传率和 RTT，快速判断是网络抖动还是服务端问题

![网络状况截图](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyvXng8e5Pp7yiaggx8Jo3licJ9AHuPsZ2B0JlEoVZlU08lgiazsHrOFkNVphR0KcneC50gWd92l7fLYHzohItn1tXhYtC9casyRQ/640?wx_fmt=png&from=appmsg)

CHAPTER 03

**03****超简单上手方法**安装 · 命令 · 参数

01

安装方式（任选其一）

INSTALL

1

Go 安装（推荐）

go install github.com/kevwan/tproxy@latest

2

Docker 快速启动

docker run --rm -it -p [listen-port]:[listen-port] kevinwan/tproxy:v1 tproxy -l 0.0.0.0 -p [listen-port] -r [target-host]:[target-port]

3

Windows 用户

用 Scoop 一键安装：scoop install tproxy

02

核心命令参数

-p   # 本地监听端口

-r   # 目标远程地址（host:port）

-t   # 协议类型（grpc/http2/redis/mongodb）

-d   # 添加延迟（模拟弱网）

-s   # 开启统计（RTT、重传等）

-q   # 安静模式，只显示关键信息

CHAPTER 04

**04****谁强烈推荐使用？**适用人群

日常写业务的后端开发

需要排查线上疑难杂症的 SRE

做压测和稳定性建设的同学

所有讨厌网络问题变成**玄学**的开发者

网络排查不再是玄学，把效率拉满，把时间留给更有价值的事情！

喜欢 tproxy？

点个 Star 支持作者，方便以后随时调用 ⭐

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

GitHub 地址：https://github.com/kevwan/tproxy

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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