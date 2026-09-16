---
title: Prometheus配半天只为看机器还活着？这个5MB工具刚够用
url: https://mp.weixin.qq.com/s/uWDPVoL9YPyvUs_l2u90Ig
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:03:52.578060
---

# Prometheus配半天只为看机器还活着？这个5MB工具刚够用

# Prometheus配半天只为看机器还活着？这个5MB工具刚够用

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

自托管预计阅读 5 分钟 · 共 1713 字

Prometheus配半天只为看机器还活着？这个5MB工具刚够用

一个 5MB Agent 撑起的家用监控方案

#beszel#轻量监控#自托管#Docker

READING PATH

阅读路线

5 个章节

01

它是什么：一个 5MB Agent 的监控平台

-

02

怎么装：两条 compose 就起来

-

03

三件事，为什么它刚好够用

-

04

它适合谁，不适合谁

-

05

写在最后

家里跑了几台小机器。一台 NAS，一台吃灰的小鸡，上面挂着各种服务。以前隔三差五就得 ssh 上去看一眼——负载多少、内存还剩多少、有没有进程悄悄挂了。

服务一多，人肉巡检根本不现实。但真要装监控，主流方案是 Prometheus 加 Grafana，光配置就能写半天，还占资源。你只是想随时确认一句"我的机器还好吗"，不是想建一套监控中台。

直到遇到 beszel，我才觉得这事本来就该这么简单。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfzoBpLYPV3K4Yic18njm7IPxj16t9ibnEUhslBIh7ibR4Xq0wWvFgNzQmzpHOvJC3nWrlqvQtFSBNZJQ1LHiaHGPlVnx9ouNciaDRe4/640?wx_fmt=jpeg&from=appmsg)

CHAPTER 01

**01****它是什么：一个 5MB Agent 的监控平台**WHAT IS BESZEL

轻量

beszel

Go 编写的轻量服务器监控平台

#看指标#存历史#发告警

每台机器装一个 Agent，二进制只有 5MB 左右。Hub 端常驻内存 20 到 50MB。浏览器打开就是一套清爽的监控界面。  它支持 Docker 容器级别的 CPU、内存、网络历史统计。告警能覆盖 CPU、内存、磁盘、带宽、温度、风扇转速、负载这些常见项。还带多用户、OAuth、自动备份和 API。

CHAPTER 02

**02****怎么装：两条 compose 就起来**INSTALLATION

beszel 用 Docker 部署，Hub 和 Agent 各一条 compose 搞定。

DEPLOY

两条 compose 起来

1

Hub 端

你看监控的那台服务器，跑 beszel 容器，暴露 8090 端口

2

Agent 端

你要监控的每台机器，跑 beszel-agent，挂载 docker.sock

3

连接

浏览器打开 Hub 的 8090，添加 Agent，填 IP+45876 端口，粘密钥

Hub 端，也就是你看监控的那台服务器，跑这个：

yaml

services:

beszel:

image: henrygd/beszel

container\_name: beszel

restart: unless-stopped

ports:

- 8090:8090

volumes:

- ./beszel\_data:/beszel\_data

Agent 端，也就是你要监控的每台机器，跑这个：

yaml

services:

beszel-agent:

image: henrygd/beszel-agent

container\_name: beszel-agent

restart: unless-stopped

volumes:

- /var/run/docker.sock:/var/run/docker.sock:ro

ports:

- 45876:45876

两条 compose 起来，浏览器打开 Hub 的 8090 端口。添加 Agent，填 Agent 机器的 IP 加 45876 端口，生成一串密钥粘回去，指标就来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfxAnOA3a4nnvVYOq5nb5hGHDg3mib8LZCz3BOibrKYOln1NsQ6a5NHeolIFE8plGBCIK1ibqiaTc5Bp7bRXx44rcHQPDEc8ibTrFsdo/640?wx_fmt=jpeg&from=appmsg)

Hub 通过 Agent 的 45876 端口去拉数据，同局域网直接填 IP 就行。跨网络就保证端口可达，端口转发或者穿透都能解决。挂载 docker.sock 是为了让 Agent 读得到容器的 CPU、内存、网络数据。不想暴露就去掉，只是看不到容器级指标。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxmLVZu4cd1wiculIT6AY5z9av4pqiabjv8cFLL1zqvuFy4mIQtpVLmYGoWUTHxYqXtV2OSqibeGdRlVrIqnXCe1fpQEzmF0ZBQEo/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxFAXvDme9xIFAyesFYXMRBBVoWWgicB4w6dJAaPqkHyQrH3zw9tmrZc8yiaYibv2MOCsJ9H2YHu1PGOG2UU5JvCC1tqPtewAKNZw/640?wx_fmt=jpeg&from=appmsg)

CHAPTER 03

**03****三件事，为什么它刚好够用**WHY IT WORKS

01

轻到极致，把门槛拆了

5MB 的 Agent，意味着在任何设备上装它都没负担。对比动不动几百 MB 的监控全家桶，这个差距是本质性的。小主机、树莓派、NAS 上，"装监控不占资源"是硬需求，beszel 直接把这个门槛拆了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxib0z3a7y4xAgOUX605KjD2Qo9UyPwfNEOpVocD7CQKaicIg3aN9yKueoBTXE7KKiaVJcQy9UVzBePicUao2VJLp6WJhKl1tCNkw0/640?wx_fmt=jpeg&from=appmsg)

很多监控工具装上去，机器先卡一半。beszel 反过来，它是那种 **你装完就忘了它存在的工具**。

02

零学习成本，不用学新概念

它不用你理解时序数据库、采集器、告警规则语法这些玩意。装好 Agent、连上 Hub，指标就来了。界面一眼能看到所有机器的状态。

这种零学习成本，对只想确认机器还活着的人太重要。多少人被 Prometheus 的 yaml 劝退，最后监控也没装上。beszel 把这条路直接砍了。

03

两年 2.4 万 Star，踩中了真痛点

2024 年 7 月创建，两年不到涨到 2.4 万 Star。监控工具这个领域不缺大而全的，缺的是刚好够用的。beszel 不建平台、不做复杂报表，就盯住"你的机器状态"这一件事，反而把它做到了最好。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxZpGVUO0T5PcAiaL4tUUedabYdUQOGicBESS6VWn8BsndXhDX5V0libYicE4xvziasGwOicaBqLwXTXwhfz7iaAotxMvmf5icP8YjJsYQ/640?wx_fmt=jpeg&from=appmsg)

现在自托管越来越普及，但配套工具大多还停留在给大厂用的阶段。beszel 把监控从大厂基建拉回了个人刚需，这个定位踩得很准。

CHAPTER 04

**04****它适合谁，不适合谁**WHO IT'S FOR

不适合

重型运维场景

你要的是复杂告警路由、多集群、细粒度报表，它确实不够。要搭监控中台的运维有更重的武器。

适合

家用小机器裸奔

和我一样，只是想让几台小机器裸奔得安心一点，它刚刚好。家里几台机器、想知道它们还好的普通人。

它没想取代 Prometheus，只服务一种人：家里几台机器、想知道它们还好的普通人。

CHAPTER 05

**05****写在最后**CONCLUSION

我很喜欢这种只解决一个问题的工具。现在的技术圈，什么都想做成平台，结果普通人连装都装不起来。

监控的价值，不在你天天盯着指标看。在没出事的那天晚上，你也能睡踏实。

beszel 帮我做到了。

beszel GitHubhttps://github.com/henrygd/beszel

beszel 官方文档https://beszel.dev/

你家里几台机器，现在怎么监控的？

Prometheus 那套还是裸奔？评论区聊聊，转发给还在人肉 ssh 巡检的同事

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

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