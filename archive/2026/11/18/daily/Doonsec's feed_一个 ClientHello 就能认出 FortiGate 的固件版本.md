---
title: 一个 ClientHello 就能认出 FortiGate 的固件版本
url: https://mp.weixin.qq.com/s/09_Z_MC-zvjPgT-2XWINAg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:25.345528
---

# 一个 ClientHello 就能认出 FortiGate 的固件版本

# 一个 ClientHello 就能认出 FortiGate 的固件版本

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 互联网上躺着 37 万多台把 FGFM 管理端口直接暴露出去的 FortiGate。这些设备本身不主动报版本号——全量 FortiOS 主机里只有 0.03% 会告诉你自己跑什么。但它们的 ClientHello 会。用 JA4 指纹能把这些设备分成六代，圈定 FortiOS 版本区间和对应的 CVE。至少 16 万台落在已知漏洞的影响范围内，其中 11,264 台无一幸免。

2026 年 10 月 14 日到 11 月 12 日，Target Intelligence 数据集里出现了 375,904 台暴露 FortiGate-to-FortiManager（FGFM，FortiGate 与 FortiManager 之间的管理协议）端口的互联网主机。Fortinet 白纸黑字说过这个端口不该对公网开放。光这一条就够让人皱眉了。

同一时期，被识别为 FortiOS 的主机有 838,100 台，其中只有 269 台会主动公布版本号——0.03%。剩下 99.97% 的设备在扫描器面前是哑巴。

FGFM 端口给了一条侧门。每台暴露的主机都会发出一个 TLS ClientHello，用 JA4 指纹做归类，正好能把这些设备切成六代，每一代对应一段 FortiOS 版本区间，以及落在这段区间上的 CVE。

结果是：6.8% 到 36.1% 的主机跑在已经停止支持的 FortiOS 分支上。区间为什么这么宽？因为有一代把已经 EOL（End of Life，生命周期终止）的 7.0、7.2 和仍在支持期的 7.4、7.6 混在了一起，没法再细分。

还有一个数字：至少 16 万台设备的版本对应着某个已知 CVE。这里面包括全部 11,264 台 Gen 2 主机，跑的是 FortiOS 5.4 到 6.0.4——每一台都受 CVE-2022-42475[1]影响。那是一个预认证 SSL-VPN 堆溢出漏洞，和勒索软件团伙挂过钩。

## 数据是怎么翻出来的

这事起点很随意。我决定花点时间看看 Target Intelligence 里那堆所谓的"未识别数据"（call unknown data）。里面全是我们的解析器认不出来的 banner 抓取结果。

以前我们靠这堆东西补过协议实现。有些协议跑出了古怪的变体，我们看明白了，回头给扫描器加上解析逻辑；Initial Access 团队的一些研究也是从这儿起的头。

### 一堆不认识的 TLS ClientHello

上一份工作里，我对着 PCAP 数据看了几百个小时。分析各种奇葩的协议实现是那份活儿里最有意思的部分。最书呆子的超能力，就是盯着 hex dump 说一句"嘿，这玩意儿像 RFC X"。

这次就是靠这个：一簇以 `16 03 01 03 c8 01` 开头的数据，一眼认出来是 TLS ClientHello。有点意思。banner 抓取里出现 ClientHello 只有两种可能——服务器把我们发的东西原样丢回来了，或者它在尝试建立 TLS 会话。前者很快排除了：这些记录彼此并不相同，而我们的 TLS 扫描器用的是固定 ClientHello。

找它们只需要一条查询：匹配 TLS 握手记录（`16 03`），首条消息类型为 01（ClientHello），在 30 天的未识别数据里按端口统计主机数。

WITH ClientHellos AS (
  SELECT ip\_int, port
  FROM target\_intelligence.unknown\_parsed
  WHERE timestamp >= TIMESTAMP\_SUB(CURRENT\_TIMESTAMP(), INTERVAL 30 DAY)
    AND STARTS\_WITH(banner, 'FgM')
    AND SUBSTR(SAFE.FROM\_BASE64(SUBSTR(banner, 1, 8)), 6, 1) = b'\x01'
)
SELECT port, COUNT(DISTINCT ip\_int) AS hosts
FROM ClientHellos
GROUP BY port
ORDER BY hosts DESC

376,794 台发送 ClientHello 的主机里，375,904 台（99.8%）走的是 541 端口。除非另外注明，本文所有主机数都覆盖同样的 30 天区间：2026-10-14 至 2026-11-12，查询时间为 2026-11-13。

### 该开 Wireshark 了

下一步是批量下载这批数据，用 Scapy 塞进 PCAP，然后打开 Wireshark 的图形界面，让我的 hex 眼睛歇一歇。

立刻见效——满屏 Fortinet 的 SNI。

SNI（Server Name Indication，服务器名称指示）是客户端在 TLS 握手时填的扩展字段，用来告诉服务器它想访问哪个服务。多站点共用 IP 的场景下这玩意儿用得极多，一个 IP 上挂几百个网站是常事。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibexkcxFH83qUicGPADafBpyTFTI0npLWhiaoqM5MicENKbTrejrcNiaGX7aFb9L9fOIgKCC7myCwxhgHNYexpRxIg5lX6G2E4fT2RQ/640?wx_fmt=png&from=appmsg)

▲ 到达 541 端口的 ClientHello，每条都带着 support.fortinet-ca2.fortinet.com 这类 Fortinet SNI。

顺着这条线索查下去，指向 FortiGate 的 FGFM 管理服务——跑在 TCP 541（IPv6 上是 542）。和我看到的端口对得上。

如果你知道 CVE-2024-47575[2]，也就是 FortiJump，那看到一台 FortiGate 把 541 敞开在公网上，第一反应必然是心里一沉。那是 FGFM 守护进程里的认证缺失漏洞，2024 年被野外利用过。

这个直觉错了。FortiJump 是 FortiManager 的漏洞，而在 541 端口上，FortiManager 是以 TLS 服务端的身份应答的。FortiGate 才是主动发 ClientHello 的那一方。

对扫描数据来说，这个方向是反的：我们是客户端，我们连过去的主机本不该反过来给我们发 ClientHello。541 端口是唯一一处出现这种情况的地方，也正是这些 banner 掉进"未识别数据"的原因。

---

说实话，这恰好解释了为什么这批数据在库里躺了那么久没人管。扫描器按"我是客户端、对面是服务端"的模型解析响应，一台设备反手甩过来一个 ClientHello，解析器只会当作垃圾丢掉。而对我们来说，这个"垃圾"里恰好藏着版本信息。

先排除一种误判：这会不会是 FortiManager 的行为，而不是 FortiGate？我翻了扫描器根据 TLS 证书标记为 FortiManager 的 30 台主机，没有一台回吐 ClientHello。所以这就是 FortiGate 的特性。

541 端口上真正对得上的漏洞是 CVE-2024-23113[3]，FortiOS 的 FGFM 守护进程里一个预认证远程代码执行，已进入 VulnCheck 的已知被利用漏洞（KEV，Known Exploited Vulnerabilities）清单。影响范围是 FortiOS 7.0.0 到 7.0.13、7.2.0 到 7.2.6、7.4.0 到 7.4.2。

不管具体版本是多少，541 端口上的 FGFM 是一条设备管理通道，本来就不该从公网可达。Fortinet 自己的建议是移除 fgfm 访问[4]。而这批主机每一台都在把 FortiGate 的控制平面摊开给任何能建立 socket 连接的人——这已经不是"配置疏忽"能轻轻带过的级别了。

## 版本发现

VulnCheck 提供 CPE 到 CVE 的查询能力，Target Intelligence 用它给主机打 CVE 标签。我接下来的目标很直接：能不能靠这些 ClientHello 拿到带版本号的 CPE，甚至圈出受 CVE-2024-23113 影响的版本区间。

分组用的是 JA4——FoxIO[5]设计的算法，从 ClientHello 里提取非临时性特征，生成一个大致人能读的字符串。它由 JA4\_a、JA4\_b、JA4\_c 三段组成，下划线分隔。

看下面截图里的第四行和第五行：JA4\_a 和 JA4\_b 完全一致，只有 JA4\_c 不同。差异来自多出的一个签名算法 ML-DSA，2024 年发布的后量子密码数字签名方案。按常识推断，这大概是更新的版本。这个猜测只对了一半——第四行实际是 FortiOS 7.4.12，它固定了自己的 TLS 设置，细节见附录里的"Fixed and Configurable TLS Settings"。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdYsjmDDec0LbS3pq1y1l9eW57Gnw2WXJUYubuaB2sFapmtlHlm54D7xOL2UY2sEv3fgjQpYtjeU3TSsYicfOeugPej8GoJNicwQ/640?wx_fmt=png&from=appmsg)

▲ 第一轮得到的五组 JA4 指纹。第 4、5 行共用 JA4\_a 与 JA4\_b（t13d171100\_a02ea570dccb），只在 JA4\_c 上分开：第 5 行多了 ML-DSA，而第 4 行是 FortiOS 7.4.12 固定的 TLS 配置（Gen 5P）。

这五个值的逐项拆解放在"JA4 Breakdown"附录里。关键结论只有一句：每一个都比前一个多带了点 SSL/TLS 生态里更新的东西。

于是我有理由相信，这五个 JA4 值对应 FortiOS 的不同版本，且依次变新。后来实测固件，五个变成了六个：下表中的 Gen 1 到 Gen 5，再加一个 Gen 5P，P 代表 pinned（固定），因为 FortiOS 7.4.12 和 7.4.13 把 TLS 设置写死了。

## OpenSSL 版本发现

随手搜了一下，FortiOS 打包了 OpenSSL。再回头对照 JA4 值，每个值都能映射到一个更新的 OpenSSL 版本。运气不错。

用 fortitool[6]——官方描述是"一个静态 Go 二进制与库，用于解密和拆包 Fortinet 固件"——我跑了 FortiOS 7.6.7，识别出 OpenSSL 3.5.5。

写了点脚本，加一个小的 Claude 技能，就能批量跑多个版本，得到下面这张表，假设成立。

| Gen | FortiOS 版本 | OpenSSL | 完整 JA4 |
| --- | --- | --- | --- |
| 5P | 7.4.12 · 7.4.13（7.4.12 起加固定） | 3.5.5，已固定 | t13d171100\_a02ea570dccb\_9482eddbd848 |
| 5 | 7.4.9 · 7.4.11 · 7.6.7 · 8.0.0 · 8.0.1 | 3.5.0–3.5.7 | t13d171100\_a02ea570dccb\_168ae6a8d753 |
| 4 | 7.4.8 · 7.6.1–7.6.4 | 3.4.0 | t13d171100\_a02ea570dccb\_412547015303 |
| 3 | 6.0.5–6.0.11 · 6.2.0 · 7.0.13 · 7.2.4 · 7.4.0–7.4.7 · 7.6.0 | 1.1.1–3.1.4 | t13d251000\_d50cb0bd0c54\_5ac7197df9d2 |
| 2 | 5.4.12 · 5.6.14 · 6.0.0–6.0.4 | 1.0.2k–1.1.0h | t12d220700\_ad4cf32d3c22\_a8cc486ca5dc |
| 1 | 无实测\* | 1.0.2 或更早 | t10i310400\_9d330406ce80\_282f11336259 |

\* 我们启动过的版本里，没有一个发出 Gen 1 的 ClientHello。能启动的最老版本 5.4.12 发的是 TLS 1.2（Gen 2）。更早的 5.4 版本我们只拿到硬件固件，而 5.4.0 到 5.4.12 每一版都带 OpenSSL 1.0.2、TLS 客户端方法相同，所以从固件本身判断不出谁发了 TLS 1.0。Gen 1 最可能是 5.4 或更老的固件，或者是我们没复现出来的某种配置；另外我们那批没授权的 6.4 实验虚机也发了 TLS 1.0。它的 CVE 统计按 5.4.0 计。

这张表的用法：只要看到某个 JA4 命中上面某一行的特征，就能给出该主机对应的 FortiOS 版本区间。

换个说法——OpenSSL 越老，FortiOS 越老。这招管用。

要提醒的是，每一代是一个 JA4 变体家族，不是单一值；而且我们没能测遍所有 FortiOS 版本，缺口见"JA4 Breakdown"和"Versions We Could Not Measure"两个附录。

## Target Intelligence 数据

接着，我们把 30 天窗口内 541 端口 FGFM 队列里每台主机的 JA4 全部重算了一遍，发现 375,904 台主机在往外泄露自己的版本区间。

把每条原始 banner（服务器在握手时返回的响应）的 JA4 重新计算一遍，每台主机就能归入一个代际（generation，指同一时期一组 OpenSSL 版本对应的固件家族）。分桶语句放在“JA4 Generation SQL”附录里。所谓锚定版本（anchor version），是指我们确实拿到固件样本、实测过 JA4 的那些 FortiOS 版本。

| 代际 | OpenSSL 版本与发布时间 | 锚定版本 | 支持状态 | 主机数 | 占比 |
| --- | --- | --- | --- | --- | --- |
| Gen 5 | 3.5.x（被 FortiOS 固定在 P 分支）·2025 年底→2026 | 7.4.12、7.4.13 | 受支持 | 98,797 | 26.3% |
| Gen 5 | 3.5.x · 2025 年底→2026 | 7.4.9、7.4.11、7.6.7、8.0.0、8.0.1 | 受支持 | 102,560 | 27.3% |
| Gen 4 | 3.2–3.4 · 2024 年底→2025 年中 | 7.4.8、7.6.1–7.6.4 | 受支持 | 38,829 | 10.3% |
| Gen 3 | 1.1.1–3.1 · 2019→2024 年中 | 6.0.5–6.0.11、6.2.0、7.0.13、7.2.4、7.4.0–7.4.7、7.6.0 | 混合：6.0/6.2/7.0/7.2 已 EOL | 110,078 | 29.3% |
| Gen 2 | 1.0.2k–1.1.0 · 约 2017–2021 | 5.4.12、5.6.14、6.0.0–6.0.4 | EOL | 11,264 | 3.0% |
| Gen 1 | 1.0.2 或更早 · 约 2017 年前 | 无实测样本 | EOL | 14,376 | 3.8% |
| 合计 | — | — | EOL 占 6.8%–36.1% | 375,904 | 100% |

支持状态以 2026-11-13 为准，取自 Fortinet 的产品生命周期页面[7]，需要登录；公开摘要见 endoflife.date[8]。Gen 2 对应 FortiOS 5.4、5.6 和早期 6.0，Gen 1 更老，两者早就过了支持期。真正麻烦的是 Gen 3。

Gen 3 是一个混合体。6.0 在 2022-09-29 终止，6.2 在 2023-09-28，7.0 在 2025-09-30，7.2 在 2026-09-30，可它的锚定版本里还带着仍在维护的 7.4 和 7.6。JA4 分不开这些分支。所以 EOL 份额只能给区间：6.8% 只统计 Gen 1 和 Gen 2，绝对数约 25,640 台；36.1% 把整个 Gen 3 也算进去，约 135,718 台。两者相差五倍多，这个宽度本身就是结论：对近三成的主机，JA4 已经失去分辨力。

表里“受支持”三个字最容易被误读。它说的是分支还在厂商维护周期内，不代表这台设备打到了最新补丁。Gen 5 里躺着 7.4.9 和 7.4.11 的主机，分支没问题，patch level 可能是几个月前的。

FortiCare Elite 客户能把 7.2 的延长支持买到 2028-03-31，Gen 3 里有小部分设备实际仍在覆盖范围内。这会让区间下限略微上移，但改变不了 Gen 3 内部良莠不齐的事实。

### 怎么确认这批主机真是 FortiGate

95% 的主机在 ClientHello 里就自报家门了：SNI（Server Name Indication，客户端在握手时声明的目标域名）里写着 Fortinet，或者受信 CA 列表里全是 Fortinet 的证书。剩下 5% 是老式 TLS 1.0/1.2 握手，压根不带主机名。

这 5% 靠旁证。拿我们自己的扫描数据交叉比对，凡是它们暴露了其他信息的，表现和已确认的 FortiGate 几乎一样：在别的端口凭 HTTP 和 TLS banner 被判定为 Fortinet 的比例是 86%，已确认主机这一项是 83%；它们开放 10443 端口（FortiGate 的 SSL-VPN 端口）的比率是全网平均的 15 倍，已确认主机是 14 倍。两个数字都比对照组略高，反而更像而不是更不像。完整证据在“Checking the Cohort Is FortiGate”附录。

### 同一批数据里的对照组

同样看 Target Intelligence 这 30 天，有 838,100 台主机被识别为 FortiOS，其中只有 269 台（0.03%）公开广播了版本号，而且清一色是 7.2.1 到 7.2.3。三千多台里才有一台肯说出自己是谁。指望读版本字符串做资产测绘，在这个目标群体上基本等于放弃。

### CPE 到 CVE 的查询

用上面这张结果表，配上 VulnCheck 的 CPE to CVE 数据[9]，查每一代锚定版本对应的 ...