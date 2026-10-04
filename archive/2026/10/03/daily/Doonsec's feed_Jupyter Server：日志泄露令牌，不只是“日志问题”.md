---
title: Jupyter Server：日志泄露令牌，不只是“日志问题”
url: https://mp.weixin.qq.com/s/xadpyERPGkZgCHD4rrB7Hg
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:36:06.247627
---

# Jupyter Server：日志泄露令牌，不只是“日志问题”

# Jupyter Server：日志泄露令牌，不只是“日志问题”

原创

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 9 月 17 日，Jupyter Server 披露 GHSA-c3mw-737p-c7g2（CVE-2026-86049，高危）：在特定条件下，5xx 错误日志会把携带令牌的 Referer 请求头原样写盘，导致访问令牌以明文形式落入日志文件。Jupyter Server 常常是数据科学团队和 AI 训练环境的主要入口，它的令牌一旦落到日志里，等于把整个工作区交出去——而这些日志又往往被采集到共享平台，被更多人可读。

这篇记录的实验有一个容易被忽略的结尾：修复版本确实堵住了一处，但同一份日志里还有另一处在继续泄露。

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqos1nj2PD7e9KVgN3ZRPQTvNsNfXctJ80KZ20EIZqicjyA2ExwRfc9ib1jopbcR781BsxrKSoyJiacGkicaxef96rUAqib37STFqiaLtE/640?wx_fmt=png&from=appmsg)

## 实验：造一次必然失败的请求

隔离环境里跑着 jupyter\_server 2.20.0，监听 127.0.0.1:8899，访问令牌设为 tok-lab-7ad4c1（模拟运维方的真实令牌）。脚本构造一个必然返回 5xx 的请求：向 /api/kernels?token=… 发 POST，请求体里把字段类型写错（name 传数字），同时在 Referer 里带上 /tree?token=tok-lab-7ad4c1。服务端返回 500。

然后读日志增量。这一轮新增 53 行，与 Referer 有关的记录里，请求头 JSON 块原样写着 "Referer": "http://127.0.0.1:8899/tree?token=tok-lab-7ad4c1"。也就是说，只要有人打开带 token 的页面、页面里又触发了 5xx，令牌就被完整地抄进了日志文件。任何能读日志的人可以直接复用——不需要破解，也不需要猜测。

## 2.21.0 的修复，只覆盖了一处

升级到 2.21.0 后，请求头块里的 Referer 变成了 "Referer": "http://127.0.0.1:8900/tree?token=[secret]"，脱敏形式 [secret] 在增量日志里出现 3 次，修复点确实生效了。

但脚本继续统计了“其它位置仍含明文令牌的行数”，结果是 2 行：

```
                             [E 2026-09-29 17:50:10.235 ServerApp] Uncaught exception POST /api/kernels?token=tok-lab-7ad4c1 (127.0.0.1)      HTTPServerRequest(protocol='http', host='127.0.0.1:8900', method='POST', uri='/api/kernels?token=tok-lab-7ad4c1', versio…
```

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqotS6FX5v6vR2GyaDJffNWcYkaQ7uxQoEW6h1Of6Zdx7F7SQzUuH06K1iaOibdtQ8o23BoyUFP5RdaT72SOfdBuah0keEWel1ZHh8/640?wx_fmt=png&from=appmsg)

两处分别是异常摘要行和 HTTPServerRequest 的 uri 字段——它们都把 URL 原样记录下来，而令牌就在 URL 的 query 里。

这不是“修复不认真”，而是说明了一个更本质的事实：只要令牌出现在 URL 里，日志就有无数种方式把它抄下来；堵住一处，还有下一处。把 ?token= 这种传参方式本身当成根因，比逐个给日志脱敏更可靠。

## 该改的是“用 URL 传令牌”这件事

第一个动作是停用 URL query 传令牌，改用 Authorization 头或 Cookie，并把旧方式在服务端显式拒绝。如果业务上短期无法改，至少要在日志层做统一的脱敏规则，覆盖请求头、请求行和 uri 三处，而不是只改一处。

第二个动作是收敛日志的读取权限。Jupyter 的日志经常和容器标准输出、采集管道、共享存储绑在一起，实际可读范围比运维想象的大得多。把日志当作凭据存储来管理：访问控制、保留期、导出审计一个都不能少，并定期检查有没有人在批量拉取历史日志。

第三个动作是轮换。凡是可能进过日志的令牌都要换，包括历史令牌——攻击者往往在很长时间之后才用到它。

## 检测与复测

在日志采集端加规则：命中 token=、Authorization，以及 Referer 里带凭据的模式都要告警。Jupyter 的 5xx 会整块记录请求上下文，所以异常量突增时，要同时检查是否伴随凭据落盘。

复测这一次要盯三处：请求头 JSON 块、异常摘要行、HTTPServerRequest 的 uri。只验证其中一处，就会得到“已经修好了”的错误结论——这正是本次实验最有价值的地方。

## 令牌出现在 URL 里，就是一连串问题的开始

把访问令牌放进 query string，会同时带来四种后果：它会进入服务端访问日志、进入浏览器历史记录、进入 Referer 请求头、还会进入上游代理与 CDN 的日志。Jupyter 这次的修复只覆盖了其中一条路径，就是因为根因在 URL 而修复在日志。

所以判断一个系统的凭据处理是否健康，可以问一个很具体的问题：把它的日志、代理日志和浏览器历史记录合起来看，能不能拼出一个可用的令牌？如果答案是“能”，那么日志脱敏做得再细，也只是把暴露面从三处缩到两处。

## 一句话总结

修复覆盖的是“日志里的某个位置”，而根因是“凭据出现在了不该出现的地方”。前者可以逐个补，后者只能一次改掉。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

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