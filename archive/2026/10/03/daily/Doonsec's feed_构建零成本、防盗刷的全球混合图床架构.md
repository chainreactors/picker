---
title: 构建零成本、防盗刷的全球混合图床架构
url: https://mp.weixin.qq.com/s/uHRbztGcrFgJXW_ZiTo5EQ
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:34:23.645569
---

# 构建零成本、防盗刷的全球混合图床架构

# 构建零成本、防盗刷的全球混合图床架构

原创

XRSec
XRSec

XRSec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 在构建个人博客或开源项目时，海外图床（如 S3/R2）虽免费但国内降速；国内大厂 CDN 虽快，一旦被盗刷便极易产生天价账单。

> 本文将分享一套**清新、低碳且防弹的全球混合图床架构**（基于 Cloudflare、腾讯云 DNSPod、腾讯云 CDN、缤纷云 Bitiful 与 Vercel）。通过 DNS 精准分流与七层边缘防护，完美实现“访问提速、源站隐身、绝对防刷”。

---

## 架构概览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/suvHboWUldf58Hz19a3fC0QzAcUZQHVXOBBRxvduWMibMPJBQtK8QZiakxibZffF4tmxW2q9LuibLvXsfxEad4kw6Ast90NeCFBKa9GwuGkBcjk/640?wx_fmt=png&from=appmsg)

## 第一层：DNS 智能分流解析

为了兼顾国内外用户体验，我们需要利用精准的智能解析。

### 1. Cloudflare NS 委派

* **🎯 架构目标**：保留主站的 CF 保护，将图床专属域名独立控制。
* **⚙️ 关键配置**：在 Cloudflare 为子域名（如 `z.nb888.com`）设置 NS 记录，委派至腾讯云 DNSPod。

![Cloudflare NS](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUlddgnibV2ZJmnoPQGGndLbWfjdWeoQmrkLpONtiaue00XL97jwibczZkSgiaicn9FqQZ0hoic37S9rSrG2e4bfC7zBTtg06QKozrzgo4Y/640?wx_fmt=png&from=appmsg)

### 2. 腾讯云 DNSPod 境内外分流

* **🎯 架构目标**：国内走高速 CDN，海外走免费 Vercel 边缘。
* **⚙️ 关键配置**：

+ **境内线路**：CNAME 解析到腾讯云 CDN（`img.nb888.com.cdn.dnsv1.com`）。
+ **默认线路（海外）**：CNAME 解析到 Vercel（`cname.vercel-dns.com`）。

![Tencent DNSPod](https://mmbiz.qpic.cn/sz_mmbiz_png/suvHboWUldfU5h0J3C3Bz8ZorsUMLFGFnGlFklldp2CBliad5zFiahcdxN2icua16VgTlPZoBRKK2Euw2V1plmcaSsYs7zVjj02YFnEhzLbYW4/640?wx_fmt=png&from=appmsg)

---

## 第二层：腾讯云 CDN 七层防护与源站隐身

国内流量将全部抵达腾讯云 CDN。在这里，我们布下天罗地网，将盗刷成本降至 0。

### 1. 基础配置与源站信息

* **🎯 防护目标**：匿名正常回源。
* **⚙️ 关键配置**：回源指向 `nb888.s3.bitiful.net`。S3 对象存储权限须设为**「公开读」**。
* **🛡️ 安全收益**：确保 CDN 节点能正常拉取文件。通过后文的「源站暗号」来防止 S3 暴漏被直连狂刷。

![Tencent CDN Base](https://mmbiz.qpic.cn/sz_mmbiz_png/suvHboWUldeTuiaOia7DnxLOejH7uRJhCaVKbZ1M9oY1e90YdtNYvkHTZuEaib5oF1NzWZq5DTRjUcOfRG43C52kKpCyar6qebn3icgbfr7s9cg/640?wx_fmt=png&from=appmsg)

### 2. 防盗链与防盗刷 (状态码 566)

* **🎯 防护目标**：拦截跨站盗用与脚本批量直链下载。
* **⚙️ 关键配置**：开启 Referer 白名单防盗链，**禁止空 Referer**。
* **🛡️ 安全收益**：命中即在边缘返回 `566`，不回源、无下行计费。

![Tencent CDN Referer & 防盗刷](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUlde2lwLK4J1gMCbI6HSgGhSljA57QuUvahuKDmic5iaXSs9RbejVNXkfOMkSxYDSwAhQgRzKs2ibzVd9As396QGjuJfHnwExKM4YFw/640?wx_fmt=png&from=appmsg)

### 3. IP 访问限频 (10 QPS)

* **🎯 防护目标**：阻断单机暴破或高频刷图。
* **⚙️ 关键配置**：限制单 IP 最高并发 **10 QPS**。
* **🛡️ 安全收益**：真实阅读文章远不及 10 QPS 并发，超过该阈值瞬间熔断。

![Tencent CDN IP限频](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUldcTibPVibmOuPKxlzaHXNO4JYGlKE2l4S1QlhAxHcULHH3icRuVLvPbRe6wmTHasItibia3DFGRS2zRyJ7dLoRnkpgD83lgicIsHI80w/640?wx_fmt=png&from=appmsg)

### 4. UA 黑白名单配置 (防爬虫)

* **🎯 防护目标**：拒收自动化抓取工具。
* **⚙️ 关键配置**：启用 UA 黑名单，精准拉黑 `*curl*`、`*Apifox*`、`*Python-urllib*` 及各路野鸡蜘蛛。
* **🛡️ 安全收益**：边缘节点直接瓦解非浏览器流量，大幅节约 CDN 算力与带宽。

![Tencent CDN UA 黑白名单配置](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUldcRauXfvFKtLsEYSLfbuYmvoG0ibFy9fZ7KYQCQJUNCwO1G3L5vt2qnia2m4jfzoPvKwjAPIWmRSsOv1r5WOpoSiarxsGzIIfFkXU/640?wx_fmt=png&from=appmsg)

### 5. 下行限速与区域访问控制 (200 KB/s)

* **🎯 防护目标**：杜绝瞬间大流量透支，掐断海外非法扫描。
* **⚙️ 关键配置**：单链接限速 **200 KB/s**，强制 **HTTPS 443** 访问，并开启**仅限中国大陆访问**控制。
* **🛡️ 安全收益**：WebP 压缩后的小图 200 KB/s 足以秒开；同时物理隔绝国外 DCDN 攻击。

![Tencent CDN 下行限速 区域访问控制](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUlddLC0SUyclKKfNxicHQdPGSSzjnMmIJpm0jGrnicddHzuZqn3yic1zHvibXicnxjpKHWMdiarMQGbqUylNEYUFAwiaibYtYOZ8XxOFzXcc/640?wx_fmt=png&from=appmsg)

### 6. 终极防刷托底：用量封顶 (100MB / 1M次)

* **🎯 防护目标**：防穿透、保全钱包。
* **⚙️ 关键配置**：单日流量超 **100MB** 或请求超 **100万次** 立即停服告警。
* **🛡️ 安全收益**：设置安全“熔断器”，牺牲可用性换取资金 100% 绝对安全。

![Tencent CDN 用量封顶](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUlddOgibQhbPF0ThvtfpXzg77aibBVJ0j5TibkMMAf8wVpicdd1G4BqpTslFWFkle0D6tW9usSntwREj7AfL3PQicE8dic41eaj4C5gicl0/640?wx_fmt=png&from=appmsg)

---

> [!TIP]
>
> ### 为什么选择缤纷云（Bitiful S4）作为底层图床？
>
> 在选型过各大主流云厂商的对象存储后，\*\*缤纷云 Bitiful\*\* 是目前个人与开发者搭建高性能图床最具性价比的解决方案：
>
> * 🎁 **永久白嫖额度**：50GB 存储 + 10GB/月 免费流量 + 10 万次 API（免绑卡，月月重置），中小博客基本可以白嫖躺平。
> * ⚡ **100% S3 兼容**：换个 endpoint 直接连，无缝适配 PicGo / rclone / AWS CLI / Typora 等所有 S3 协议工具。
> * 🎨 **CoreIX 实时媒体引擎**：URL 传参（如 ``）即可由边缘引擎毫秒级秒出 WebP/AVIF 与动态水印，源站无需存储冗余衍生图。
> * 💰 **腰斩计费价格**：下行流量仅 ¥0.26/GB 起（闲时 8 折仅 ¥0.21/GB），远低于大厂云定价。

## 第三层：源站暗号伪装 (核心黑科技)

常规防盗链只防前端。若黑客挖出真实 S3 域名直连轰炸，依然会触发高额流量费。为此，我们设计了**回源暗号**机制，使源站实现“伪隐身”。

### 1. CDN 回源 Header 注入

CDN 向源站索取资源时，我们强制为其注入奇葩请求头。

* **篡改 Referer**: `z-nb888.com`
* **篡改 User-Agent**: `z-nb888.com`

![Tencent CDN 回源HTTP头暗号](https://mmbiz.qpic.cn/sz_mmbiz_png/suvHboWUldd9sfxo52GgewoibMXtMrxkmqMMWN71lQS7aMyIQICO5LXRHiaMK6EZMHDlqHCGHQzk3Gib2j9EqNkHNI7ED5LS2joTf2FdetiaOUQ/640?wx_fmt=png&from=appmsg)

### 2. 回源 URL 重写 (适配源站目录)

为了适应 S3 后端特殊的路径结构，利用重写规则隐藏后端复杂结构，使对外图片链接更清爽。

![Tencent CDN 回源URL重写](https://mmbiz.qpic.cn/sz_mmbiz_png/suvHboWUldcae9BFaTiaojMaiaqT5ibHEFrWptLloodjpRWnaeznOgsnGHsDCs7YrXNE0jC0fPqNmyWoSwQmzXicQTZLeMibtNN3icNLy5xlSic8vU/640?wx_fmt=png&from=appmsg)

### 3. Bitiful S3 严苛防盗链拦截

在缤纷云（Bitiful S3）端，开启防盗链：**拒绝空 Referer 和空 User-Agent**，并在白名单里仅填入我们的唯一暗号 `z-nb888.com`。

无论谁直连 `nb888.s3.bitiful.net` 发起攻击，只要没有配对的定制 UA 与 Referer，皆会在入口秒退 `403`。

> 💡 绝大部分对象存储的 HTTP 403 (Egress 流出) 不收流量费！这直接让直连攻击变为无用功。

![Bitiful S3 防盗链](https://mmbiz.qpic.cn/mmbiz_png/suvHboWUldfbQmk8RTYSehApOIKbDQKeNRE3Dy3kHSGxKDfIbaUiawgDc8q6RCNHhicXXWVWgszXOgSbHiarYtcOVmIVMjuLUyKAEN0iatOzy7k/640?wx_fmt=png&from=appmsg)

---

## 第四层：GitHub Actions 与 Vercel 灾备同步

Vercel 不支持优雅地反代 S3，且直接让 Vercel 读取 CDN 并不划算，因此我们使用静态仓库全量同步法：

1. **GitHub Actions 每日增量**：利用 `.github/workflows/sync-oss.yml` 跑 `aws s3 sync` 定期将图片同步到私有/公开图床仓库。
2. **Vercel 无缝部署分发**：一旦增量完成，Vercel 瞬时构建上线。海外全量访问皆由 Vercel 全球边缘节点免费接管。

---

## 架构落地速查总表

为了便于快速复刻此套防护模型，请参考以下控制台操作清单对照表：

| 平台层 | 关键动作与配置值 | 安全与加速效用 |
| --- | --- | --- |
| **Cloudflare NS** | 将子域 `z` 委派至 `f1g1ns1.dnspod.net` | 隔离主站风险，将控制权交由专业精细化路由的 DNSPod |
| **腾讯云 DNSPod** | 境内 CNAME -> 腾讯云 CDN 默认 CNAME -> Vercel CNAME | 实现境内极速拉取，境外零成本分发的高效分流 |
| **腾讯云 CDN** | 拦截空 Referer + 10 QPS 限流 + 200 KB/s 封顶限速 拦截常见脚本 UA (`curl/Python`) | 将 99% 的盗刷爬虫拦截在云端边缘，防穿透、防耗尽 |
| **腾讯云 CDN (高级)** | 日超 100MB 或 1M 次请求触发 **用量封顶** | 极端恶劣攻击下的最后一道绝对保险锁，保全钱包 |
| **缤纷云 Bitiful S3** | 设为**公开读**。 拦截空 Referer/UA，仅放行私有暗号 `z-nb888.com` | 源站隐身：任何不携带特定暗号的请求直接 403，0 Egress 费用 |
| **Github + Vercel** | `aws s3 sync` 触发 Action，部署最新静态库至 Vercel | 为全球用户提供高性能灾备边缘加速服务 |

---

## 快捷入口与 FAQ

**🔗 控制台直达传送门**：

* 腾讯云 CDN 控制台
* 腾讯云 DNSPod 解析
* Cloudflare Dashboard
* 缤纷云（Bitiful）存储控制台
* 缤纷云（Bitiful）官网体验

---

**Q: 腾讯云 CDN 节点拦截盗刷，会收费吗？**A: 不会。当用户因规则（UA/IP/Referer）被拦截时，边缘节点直接返回 566 或 403 状态码。CDN 的计费基准是实际下行的载荷字节，403 的响应体积几十个字节，百万次非法请求造成的流量连 1MB 都不到，无限趋近零成本。

**Q: 如果黑客扫描出我的 S3 域名直接刷 S3 怎么办？**A: 缤纷云 S3 只认暗号 `z-nb888.com`，其余直连全部拒绝。对象存储平台针对 403 阻断拒绝的流出 (Egress) 流量是不收费的，因此直接攻击你的 S3 桶依然不会造成任何账单损失。

通过 Cloudflare + DNSPod + 腾讯云CDN + 缤纷云（Bitiful） + Vercel + Actions 这套闭环架构，我们成功打造了一个低碳、高速且免受账单刺客袭扰的理想图床方案。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rZKyabaSd5TcIz8bZBIGyMNXEk1SDGEJeXnj2gK9KJdUI6OVsyCjTib5t0dN9SWth7wdyA7BAAf71APRIcdjMlg/0?wx_fmt=png)

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