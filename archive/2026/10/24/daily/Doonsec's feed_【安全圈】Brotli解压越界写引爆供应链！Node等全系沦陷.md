---
title: 【安全圈】Brotli解压越界写引爆供应链！Node等全系沦陷
url: https://mp.weixin.qq.com/s/SyB6puYi_61Vrz03euF_IQ
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:17.908166
---

# 【安全圈】Brotli解压越界写引爆供应链！Node等全系沦陷

# 【安全圈】Brotli解压越界写引爆供应链！Node等全系沦陷

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**核心事实**：Google 维护的通用压缩算法 Brotli 确认底层缓冲区越界写入漏洞（CVE-2026-111497）。由于各编程语言和网关通常直接内置该 C 解码器源码，缺陷已在整个软件基础设施生态引发连锁反应，Node.js、Bun、Python Brotli 库及 Envoy 代理等核心组件全线受波及。Imperva 实验室已在特定无防护 Node.js 镜像上验证远程代码执行（Node2Shell）

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHuHgOwILhoCbKuZe2GtQHDOiaf10uJKIzbAQeVKEc8icy2qwnTkHBVTUQzcQ4uXVvKFfPNpbibSHz4tX98tl6G282SyJ9blU5icibE/640?wx_fmt=other&from=appmsg)

## 💥 解码器越界写入：畸形压缩流破坏内存

漏洞根源存在于 Google Brotli 解码器（C 语言参考实现）处理解压数据流的边界控制逻辑中。当程序解析特制的畸形 Brotli 压缩数据时，解压逻辑会越过预分配的目标缓冲区末尾，直接向临近内存区域写入数据

这种内存越界写入可直接导致服务进程段错误崩溃（DoS），甚至可能被黑客精心构造的恶意负载用于劫持控制流或泄露内存敏感信息。只要目标服务允许客户端提交或从外部拉取 Brotli 压缩数据，攻击者无需身份验证即可发起探测

## 🌐 生态连锁穿透：各主流组件受影响场景

由于各大主流运行时直接打包复用 Google 的 C 解码器源码，导致补丁必须由下游厂商各自独立合并构建，影响范围广泛分布于多个常见栈：

* **Node.js 运行时**

  ：内置 `fetch()` 在接收到响应头 `Content-Encoding: br` 时会自动解压，或 Web 框架（如 Express 5、body-parser 2）开启 Brotli 请求体解析时直接暴露
* **Bun 运行时**

  ：1.4.3 及更早版本在使用内置 `fetch()` 或 `node:zlib` 解码不受信任的 Brotli 数据时同样受波及
* **Python 隐蔽风险**

  ：系统只要安装了 `brotli` 或 `brotlicffi` 模块，主流 HTTP 客户端（requests、urllib3、httpx、aiohttp）就会默认启用 Brotli 自动解压，即便业务代码从未显式 import 它
* **云原生网关 Envoy & Istio**

  ：只有在显式配置开启入站 Brotli 解压缩过滤器时才会被该漏洞触发

## 🔬 实战利用评估：Node2Shell 概念验证

Imperva 威胁研究员已完成针对未打补丁 Node.js 的概念验证利用（Node2Shell），成功跑通了任意代码执行。但该利用高度依赖特定内存布局，在其它软件或开启标准 ASLR/RELRO 防护的生产系统上尚未观察到稳定 RCE

截至目前全球尚未发现针对该漏洞的大规模在野利用，但远程发起 DoS 崩溃的利用门槛极低，极易成为针对核心网关和 API 节点的拒绝服务武器

## 🛡️ 官方修复版本与应急防范清单

各大维护团队已陆续发布修复版本，运维与开发团队请立即核对并升级：

* **Google Brotli 源码**

  ：升级到 `1.2.1`（或对应分支的 1.0.10、1.1.1）
* **Node.js**

  ：升级到 `26.12.1`、`24.22.1` 或 `22.23.4`（Node.js 20 及更早版本已达生命周期终点，建议尽快迁出）
* **Bun**

  ：立即升级到 `1.4.4`
* **Python 包**

  ：更新 `brotli >= 1.2.1`，`brotlicffi >= 1.2.1.0`
* **Envoy / Istio**

  ：升级到 Envoy 1.40.0 / 1.39.3 / 1.38.6，或 Istio 1.31.2 / 1.30.6 / 1.29.9
* **临时规避**

  ：若无法第一时间重启升级，可在入口网关暂时关闭 Brotli 解压缩过滤器，退回仅支持 gzip。

***END***

阅读推荐

[【安全圈】PHP2Shell 遭百万次攻击，竟无一得手](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079470&idx=1&sn=1f84c3759d5f7bf34fcbd56949ea72a3&scene=21#wechat_redirect)

[【安全圈】9.0 分 Linux 内核 RCE，被一封邮件捅穿](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079470&idx=2&sn=f760b577c0f307d90d16107d46ad7e9a&scene=21#wechat_redirect)

[【安全圈】1177 万条！卡普空确认账号库被偷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079470&idx=3&sn=4ed4671e35da838dae890d616c227665&scene=21#wechat_redirect)

[【安全圈】老乡鸡小程序又崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079459&idx=1&sn=9bbd43e57a372693618b7ed16c3c2af4&scene=21#wechat_redirect)

[【安全圈】单连接打崩服务器！HTTP3曝4000倍内存放大漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079445&idx=1&sn=faa0a86fd9d2ee022af099b2286cf0d2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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