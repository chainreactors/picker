---
title: 银狐云端“生死簿”：从“无条件返回”到“黑名单”机制
url: https://blog.netlab.360.com/yin-hu-yun-duan-sheng-si-bo-cong-wu-tiao-jian-fan-hui-dao-hei-ming-dan-ji-zhi/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-09-14
fetch_date: 2026-09-15T07:02:08.387371
---

# 银狐云端“生死簿”：从“无条件返回”到“黑名单”机制

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

[SilverFox](/tag/silverfox/)

# 银狐云端“生死簿”：从“无条件返回”到“黑名单”机制

#### [Youngs](/author/youngs/), [HamaPea](/author/hamapea/)

14 Sep 2026
• 37 min read

[Share](#/share)

2026年9月，360威胁情报中心对银狐仿冒投递链进行持续性追踪，结合历史样本与本轮抓包，梳理出其投递与对抗演化的四个阶段：无条件返回、白名单限制、基于白名单的批量探测，以及当前的黑名单机制。

最早阶段，访问中转节点即可获得恶意样本下载地址，服务端不区分请求来源。随后，银狐引入**白名单机制**：仅当请求头 `Referer` 指向在投仿冒域名时，`api.php` 才下发真实载荷，其余请求拿不到有效载荷。利用这一特征，我们对最近注册的二级域名进行了**批量遍历探测**，识别出一批新投放的仿冒域名。

批量探测之后，我们在 9 月 12 日凌晨的双站抓包中，观察到同一台 `api.php` 出现两种结果；当日 04:35 UTC 的七组对照复测确认：**云端决策模型已切换为“黑名单”——只有被拉进失效名单的域名才返回微信官方安装包等无害素材，名单之外的一切（在投域名、全新域名、甚至不带 `Referer` 的请求）照常下发真实载荷**。推测批量探测可能被银狐侧感知，策略切换发生于其后。

策略切换后，白名单阶段“返回真实载荷即名单命中”的识别方法失效；但新机制留下了新的识别信号：返回微信包的域名，即为已被处置、识别或失效的银狐仿冒域名。

---

# 一、背景

银狐的仿冒下载站是个长期存在的威胁：伪造赛睿、必剪这类热门软件的官网，通过 SEO 将页面排在搜索结果前列，诱导用户主动点击"下载"。本次追踪的核心发现是，投递链背后的服务端决策机制已具备随探测行为调整的能力。

本次追踪覆盖四个阶段。前两个阶段是服务端投递策略，第三阶段是利用策略缺陷开展的探测行动，第四阶段是银狐针对探测行为采取的策略调整。

| 阶段 | 性质 | 服务端行为 | 可观测结果 |
| --- | --- | --- | --- |
| 第一阶段：无条件返回 | 服务端投递策略 | 访问中转节点即可返回恶意样本地址 | 任意请求均可直接取样 |
| 第二阶段：白名单限制 | 服务端投递策略 | 仅对白名单中的 `Referer` 域名返回真实载荷 | 返回真实载荷即可确认域名在投 |
| 第三阶段：批量探测 | 探测行动 | 利用白名单的可观测差异遍历候选域名 | 识别出一批新投放仿冒域名 |
| 第四阶段：云端黑名单 | 服务端对抗调整 | 黑名单域名返回无害素材，名单外统一返回真实载荷 | 返回无害素材可提示域名已失效或被处置 |

**第一阶段：无条件返回。** 早期调度层不校验请求来源。只要访问中转节点，`api.php` 就直接返回恶意样本下载地址；请求是否来自银狐仿冒站、是否携带 `Referer`，都不影响结果。这一阶段的主要问题是中转节点暴露后，任何人都可以直接获取载荷。

**第二阶段：白名单限制。** 银狐的调度层 `api.php` 开始消费一个变量——请求头 `Referer` 中的注册域名是否为银狐在投的仿冒域名。是，则下发真实银狐下载地址；否，则不下发有效载荷。

**第三阶段：基于白名单的批量探测。** “Referer 即钥匙”使白名单成为可观测信号：构造 Referer 探测 `api.php`，返回真实载荷即可视为命中银狐在投域名。我们以最近注册的二级域名作为候选池，逐个遍历探测，识别出一批仿冒域名并持续跟踪。这一阶段不是银狐新增的投递策略，而是对其白名单缺陷的利用。

**第四阶段：云端黑名单。** 9 月 11 日下午，白名单策略仍在生效；9 月 12 日凌晨的抓包中，同一台 `api.php` 出现“一个域名返回微信包、一个域名返回银狐载荷”的分裂结果；当日全量复测确认，**决策机制已从白名单切换为云端黑名单**。

切换之后，"Referer 即钥匙"的溯源方法失效——黑名单模型下几乎所有请求都返回真实载荷，无法再以"返回载荷"区分银狐域名。但新机制同时提供了新的识别信号：**凡被 `api.php` 判为命中黑名单、返回微信官方包的域名，即为已暴露、已被处置的银狐仿冒域名**。

本文按“**无条件返回 → 白名单限制 → 批量探测 → 黑名单切换**”的次序，完整复盘这一过程。目前整个**银狐木马仿冒域名攻击链路**如下图：

![](https://blog.netlab.360.com/content/images/2026/09/SilverFox-AttackChain-v10.png)

****图1 银狐木马仿冒域名完整攻击链路****

---

# 二、时间线

* 第一阶段（无条件返回）：访问中转节点即可获得恶意样本下载地址，不校验请求来源；
* 第二阶段（白名单时期）：`api.php` 仅对“Referer=银狐在投域名”下发真实载荷；
* 第三阶段（批量探测）：引入最近注册二级域名数据，构造 Referer 批量遍历探测，识别出银狐新投放仿冒域名；
* 第四阶段（黑名单时期）：名单内域名返回微信官方安装包或其他无害素材，名单外请求返回真实载荷；
* 2026-08-12 08:32:31 GMT：中转池 `relays.json` 最后修改（`v`/`updated_at` 时间戳 `1786523551` 与响应头 `last-modified` 交叉验证一致），此后一个月未变更；
* 2026-09-11 下午：白名单策略仍生效；
* 2026-09-12 01:46:27 UTC：捕获 `gg-steelseries.com.cn` 完整请求包（7 个请求）；
* 2026-09-12 01:47:07 UTC：捕获 `org-bcut.com.cn` 完整请求包（8 个请求），与前者间隔 40 秒；
* 2026-09-12 04:35 UTC：七组对照实验全量复测（17 次 curl 请求，全部 200），确认当前为**云端黑名单**模型；

---

# 三、两个仿冒域名对比

本次研究的两个仿冒站均为 .com.cn 后缀，与真实官方域名高度相似：

| 仿冒域名 | 伪装对象 | 页面标题 | 调度层决策 |
| --- | --- | --- | --- |
| `gg-steelseries.com.cn` | 赛睿 SteelSeries GG 电竞软件 | "赛睿GG官方下载 - 赛睿GG | 官网正版安全下载" | 已失效 → **命中黑名单** |
| `org-bcut.com.cn` | B站必剪 PC 客户端 | "必剪电脑端 – 必剪全平台 | 超燃音乐库与专业画面特效…" | **正常收量（名单外）** |

两个站点均为静态单页，但"官网感"做得很足：SEO 元信息齐全（title / description / keywords / robots）、JSON-LD 结构化数据（`SoftwareApplication`、`FAQPage`）、FAQ 、响应式导航一应俱全；同时统一接入 51.LA 统计（ID：`3QIMielUrIaXc63E`、`3QbvgmKU4mQXDLRW`），用于受害者流量计数与站点存活监控。

```
<!-- gg-steelseries.com.cn 页面源码节选 -->
<script>LA.init({id:"3QIMielUrIaXc63E",ck:"3QIMielUrIaXc63E"})</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "赛睿GG官方版",
  "applicationCategory": "UtilitiesApplication",
  "operatingSystem": "Windows, macOS",
  "downloadUrl": "https://gg-steelseries.com.cn/",
  "url": "https://gg-steelseries.com.cn/"
}
</script>
```

有一点需要提前说明：**访问者的每一次到访，攻击者都是看得见的**。两组数据中都能看到 `collect-v6.51.la/v6/collect` 的上报请求——每一次访问都会进入攻击者的存活监控面板。这一点与后文的决策机制放在一起看，构成了一个完整的闭环：访问会被感知，暴露会被处置。

---

# 四、流量侧复盘：两条链路，新旧同框

### 0x01: 场景 A：gg-steelseries.com.cn —— 旧版逻辑"尸体"还在，新版逻辑接管

时间线（UTC，`gg-steelseries.com.cn.har`，共 7 个请求，耗时均为实测值）：

```
T+0.000s  01:46:27.316  GET https://gg-steelseries.com.cn/
          → 200 OK（858ms，HTML 24952 字节，gzip）
          Referer:        （无）
          Server: nginx / Last-Modified: Wed, 12 Aug 2026 10:29:58 GMT
          HSTS: max-age=31536000

T+0.840s  01:46:28.156  GET https://sdk.51.la/js-sdk-pro.min.js
          → 200 OK（147ms，51.LA 统计 SDK v1.58.5）
          Referer:        https://gg-steelseries.com.cn/
          Sec-Fetch-Dest: script / Sec-Fetch-Mode: no-cors / Sec-Fetch-Site: cross-site
          UA: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
              Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0

T+0.998s  01:46:28.314  POST https://collect-v6.51.la/v6/collect?dt=4
          → 200 OK（140ms，请求体 625 字节，加密上报数据）
          Referer:        https://gg-steelseries.com.cn/
          Origin:         https://gg-steelseries.com.cn
          Sec-Fetch-Dest: empty / Sec-Fetch-Mode: cors

T+1.006s  01:46:28.322  GET https://api.new-noah.top/api.php
          → 状态码 0（228ms 后放弃，请求未达服务器）
          Referer:        https://gg-steelseries.com.cn/
          UA:             （同上，Edge 152）

T+1.007s  01:46:28.323  GET https://noah-ssh.com.cn/relays.json?_=1789177588323
          → 200 OK（605ms）
          Referer:        https://gg-steelseries.com.cn/
          Origin:         https://gg-steelseries.com.cn
          Cache-Control:  no-cache / Pragma: no-cache（脚本显式声明）
          Sec-Fetch-Dest: empty / Sec-Fetch-Mode: cors / Sec-Fetch-Site: cross-site
          UA:             （同上，Edge 152）

T+1.247s  01:46:28.563  GET https://gg-steelseries.com.cn/favicon.ico
          → 404 Not Found（180ms，响应体 4118 字节，内含 r6 调度脚本，见"花絮"一节）
          Referer:        https://gg-steelseries.com.cn/
          Server: nginx / ETag: W/"6a7c4b26-1016"

T+1.487s  01:46:28.803  GET https://noah-ssh.com.cn/api.php?t=1789177588803
          → 200 OK（172ms）
          Referer:        https://gg-steelseries.com.cn/
          Origin:         https://gg-steelseries.com.cn
          Cache-Control:  no-cache / Pragma: no-cache
          Sec-Fetch-Dest: empty / Sec-Fetch-Mode: cors / Sec-Fetch-Site: cross-site
          UA:             （同上，Edge 152）
          返回数据：
{"download_link":"https://dldir1v6.qq.com/weixin/Universal/Windows/WeChatWin_4.1.13.exe"}
```

说明："状态码 0"表示该请求未完成（DNS 解析失败或连接被拒），并非 HTTP 响应状态——旧版 API `api.new-noah.top` 已无法解析，请求未达服务器。

先注意一个贯穿整条时间线的细节：**从 `sdk.51.la` 开始，页面发出的所有跨域请求都自动携带了 `Referer: https://gg-steelseries.com.cn/`**——这是浏览器跨域 fetch 的默认行为。也就是说，调度层从 `relays.json` 阶段就能拿到"受害者来自哪个仿冒站"，后文的决策机制正是建立在这个头之上。

页面加载后约 1.5 秒内，两套脚本先后开火：

1. 旧版脚本（T+1.006s）向 `api.new-noah.top/api.php` 发起请求——域名已失效，请求未达；
2. 新版脚本（T+1.007s，仅晚 1 毫秒）走 `relays.json → api.php` 链路，成功拿到"下载链接"。

也就是说，这个页面是新旧两代投递逻辑的活体同框：旧代码没有被清理，只是被新的调度框架接管了下载职责。

### 0x02: 场景 B：org-bcut.com.cn —— 新版逻辑

时间线（UTC，`org-bcut.com.cn.har`，共 8 个请求，比场景 A 晚 40 秒）：

```
T+0.000s  01:47:07.242  GET http://org-bcut.com.cn/
          → 307 Temporary Redirect（32ms）
          Location: https://org-bcut.com.cn/
          Non-Authoritative-Reason: HttpsUpgrades（浏览器自动 HTTPS 升级）
          Referer:        （无）

T+0.032s  01:47:07.274  GET https://org-bcut.com.cn/
          → 200 OK（872ms，HTML 33850 字节，gzip）
          Referer:        （无）
          Server: nginx / Last-Modified: Wed, 02 Sep 2026 15:14:59 GMT

T+0.957s  01:47:08.199  GET https://sdk.51.la/js-sdk-pro.min.js
          → 200 OK（309ms，同一份 51.LA SDK）
          Referer:        https://org-bcut.com.cn/
          UA:             （同上，Edge 152）

T+0.958s  01:47:08.200  GET https://org-bcut.com.cn/logo.png
          → 200 OK（514ms）
          Referer:        https://org-bcut.com.cn/

T+1.284s  01:47:08.526  POST https://collect-v6.5...