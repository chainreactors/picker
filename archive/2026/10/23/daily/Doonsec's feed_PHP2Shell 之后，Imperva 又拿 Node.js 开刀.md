---
title: PHP2Shell 之后，Imperva 又拿 Node.js 开刀
url: https://mp.weixin.qq.com/s/YURJgMvQT_fxGT4Q2_hkAw
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:02.935110
---

# PHP2Shell 之后，Imperva 又拿 Node.js 开刀

# PHP2Shell 之后，Imperva 又拿 Node.js 开刀

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HeZib37jhib9W8HHWDHn54MBeeOfsyYgqVH0R89MffSj8MpARkqrRhsaAD2t6fubkBYPfmPgBmXmFDUKUdSQ5aUM5GfATloOgbU/640?wx_fmt=png&from=appmsg)

近期的 PHP2Shell（PHP 引擎双 RCE）的余波还没平，Imperva 威胁研究团队又扔出一篇 **Node2Shell**：他们针对 **CVE-2026-111497**——Node.js 捆绑的 Brotli 解码器里的一个堆越界写——做了独立验证，在**官方原版 Node.js 镜像**上跑通了代码执行。同一周、同一家厂商、同一个主题：**运行在每天用的 Web 应用底下的那些运行时，正在变成内存安全漏洞的新战场。**

这篇文章我们做一次完整技术拆解：漏洞在哪、怎么触发、实测到什么程度、和另一条公开 PoC 的分歧在哪、以及防御上真正该做什么。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GjGspVFaiblZ1rmlVRZTak4ecK4kibvqLN7zqwOygt96Y7r5dvTm81yVgKSlbvlAeE0EFzBM7I5a9ZwicEibIUBXOELRgFerR3icI4/640?wx_fmt=png&from=appmsg)

## 一、CVE-2026-111497 速览

先把关键事实摆清楚（来源：Node.js 官方 10 月 21 日安全公告 + Imperva 研究 + 多家独立转述）：

* **CVE 编号**

  ：CVE-2026-111497
* **等级**

  ：高危（High），Node.js 官方定级
* **组件**

  ：Node.js 捆绑的 Brotli 解压解码器（第三方 C 库，随 node:zlib 静态集成）
* **问题类型**

  ：堆内存越界写（Out-of-Bounds Write），官方称可导致远程代码执行
* **影响分支**

  ：22.x / 24.x / 26.x 三条受支持线全中
* **修复版本**

  ：22.23.4 / 24.22.1 / 26.12.1（2026-10-21 发布）
* **披露时间线**

  ：2026-10-21 安全发布，10-22 Imperva 公开实测研究
* **致谢（以官方公告为准）**

  ：Matteo Collina 报告，Antoine du Hamel 修复

一个需要先记住的结论：**这个漏洞不在任何业务代码里，而在运行时捆绑的第三方解码器中**。应用开发者翻遍自己的仓库也找不到可修的东西——这也是本文后面反复要回到的点。

## 二、背景：Brotli 数据的两条进城之路

Node.js 服务在两种场景下会把不可信数据送进这个解码器：

**路径一：出站，消费别人的压缩响应。** 应用用内置 `fetch()` 请求外部服务，对方返回带 Brotli 编码的响应体，运行时自动解压。只要攻击者能影响那个远端服务返回的内容（恶意上游、被篡改的 CDN、供应链投毒），压缩数据就带着攻击载荷进了你的进程。

**路径二：入站，解压客户端提交的请求体。** Express 5 在请求体解析器里支持 Brotli 解码（body-parser 从 2.0.0 起支持）。 Imperva 实测了 Express 5.0.0–5.3.0 配 body-parser 2.0.0–2.3.0，用 `raw()` 和 `json()` 两种解析器都跑通了。**未认证的请求体可以直接到达解码器。**

两条路看似无关，**指向的是同一个捆绑解码器**——所以修复也只有一处：升级运行时。

这里有个容易被误读的澄清：Imperva 明确说明，**裸的 Node.js HTTP 服务器不会因为「收到了」Brotli 请求体就自动解码**，需要配置了会解压 br 的中间件（Express 5 / body-parser 2 这类）才会把数据喂给解码器。所以「所有 Node.js 应用都中招」是夸大，准确的说是「会把不可信 br 数据喂给解码器的应用」。

## 三、根因：一个自相矛盾的块切换，被当成了「还要更多数据」

Brotli 流在解码过程中会描述可用的块类型。Imperva 的测试输入走到了一个**块类型切换**节点，而这个切换是流自身结构所不允许的。阿里云 AVD 的技术描述更直白：

1. 数据流声明块类型数量为 1——按格式规定，此时**不存在块类型切换树**；
2. 但流里却仍然发出了块切换命令；
3. 这个校验失败的结果，被上层**三个返回类型为 void 的包装函数逐层丢弃**——错误没人接住；
4. 解码器于是**带着未被有效赋值的块类型和一块不一致的内部状态继续解码**；
5. 越界的索引随后被用于访问 **Huffman 表与上下文映射**；
6. 结果是**堆内存越界写**。

Imperva 对这个过程的描述是：在漏洞版本里，这个无效条件「看起来像请求更多输入」，处理就带着坏状态继续了下去。他们另外用内存 sanitizer 复现了越界写——但注意，**sanitizer 只是用来解释根因的，实测代码执行并不需要它**。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0F7VROFTicSib0iaump5rqnGORTcNGLkHic1jRibkWZLxgXVLa4BrYSmQvDljCiam8gJQqficmH9gC1sn6cVrDWa0h58n2CenGk3WnjRw/640?wx_fmt=png&from=appmsg)

上游 Brotli 的修复（commit `0ed4268`）思路很直接：遇到这种无效块切换，**直接返回格式错误并传给调用方**，解码不再继续。Node.js 的修复就是把这个上游 commit cherry-pick 进运行时。同一修复也发在了 Brotli 1.2.1 / 1.1.1 / 1.0.10（10-21 同步发布）——**其他自己捆绑 Brotli 的软件同样要排查**，别只盯着 Node.js。

## 四、实测：官方镜像上到底跑没跑起来

这是 Imperva 这篇研究最有信息量的部分，也是需要 careful 读的地方。

**他们做到了什么：**

* 在全新的容器里跑**官方 Node.js 24.22.0 Linux arm64 镜像**（打补丁前的版本）；
* 测试应用自身**没有任何创建标记文件的代码**——收到 Brotli 数据后，标记文件出现了：**藏在数据里的代码在目标进程里执行了**；
* 不需要调试器，不需要改过的二进制；
* 同一份输入打到 **24.22.1**：被拒绝，无标记文件，服务保持运行；
* 两条路径分别验证：`fetch()` 消费外部 br 响应、Express/body-parser 解压入站 br 请求体。

**他们自己承认的限制：**

* **并非每次尝试都成功**

  ——「execution took multiple attempts in our setup」；
* 利用可靠性受运行时版本、构建形态、内存分配器布局影响（AVD 同样指出这点）；
* 他们没有测遍所有 Node.js 构建和所有应用。

**还有一个必须诚实告诉你的分歧：** 据 The Hacker News 等转述，10-22 出现的另一个公开 PoC，**在标准构建上只拿到崩溃和有限的进程内存读取，未能执行代码**；其作者称代码执行只在一个被故意弱化的测试构建上成功。Imperva 的结论（官方镜像上 RCE）与这个转述存在出入。两者可能是不同的 PoC、不同的构建与尝试次数，也可能有一方更乐观。**在更进一步的独立复现出现前，建议按「高危、利用有门槛、但不是不可能」来定级和排期**，而不是按「一键 RCE」来恐慌。

## 五、影响范围：三条支持线全中，EOL 无补丁，同批还有三个高危

| 版本线 | 状态 |
| --- | --- |
| 22.x（< 22.23.4） | 官方已修复，升级 22.23.4 |
| 24.x（< 24.22.1） | 官方已修复，升级 24.22.1 |
| 26.x（< 26.12.1） | 官方已修复，升级 26.12.1 |
| 20.x 及更早 / 21.x、23.x、25.x | EOL，无补丁，须迁移到受支持分支 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0FxPsAQoiaAhjVyougXzlTeQSAHspX7lf7dw6VXQic4cBCjY3bqic0ribbfIgZsOoIDEHmPgqAo324OibkpbPewln2GFdx5wnxM5Hu0/640?wx_fmt=png&from=appmsg)

几个范围上的要点：

* Node.js 官方立场：**EOL 版本在安全发布时永远算受影响**，别指望 backport，只有迁移一条路。
* 台湾數位發展部資安署 10-22 已发文要求公私部门加速更新，并特别提醒**容器化镜像**要一并排查——这正好戳中下面防御部分的重点。
* **别只盯着 Brotli**

  ：同一批发布里还有三个高危——`dns.resolve` 对含 NUL 字符主机名的截断（CVE-2026-105482）、TLS 证书主机名校验绕过两个（CVE-2026-105483 全角数字 IP、CVE-2026-106069 宽松解析 IP），以及应对 eMudhra 中间 CA 私钥泄露事件的证书列表更新。一次安全发布，值得全量过一遍。
* 截至 10-22，各信源均未报告在野利用。

## 六、防御与处置：先换运行时，再收暴露面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0GjgTCCicLWzvIt8ULic1gZ58YwRnvpJ7aUj9q15fpxQFBeu7ZtQZ1V0WVJzice5y8GqPgAsdxlDAE2I6nQWa8gcDK9KQcZ8tufiaA/640?wx_fmt=png&from=appmsg)

**先换运行时：完整修复只有这一条路**

1. 按各自分支升级到 22.23.4 / 24.22.1 / 26.12.1；
2. **容器镜像要重建**

   ：镜像里捆绑的 node 二进制才是实际运行的代码，只改宿主机或只 `npm update` 都没用，重建镜像 + 重启服务；
3. 排查范围要超出生产服务器：构建机、CI/CD、开发机、以及托管服务商/Serverless 平台里跑的 Node 版本——**包清单扫描会发现不了镜像里藏的旧运行时**；
4. EOL 版本制定迁移计划，短期内至少把互联网暴露面服务先挪走。

**横向——缩小暴露面（争取时间，不是修复）：**

* 梳理**出站**：哪些服务用 `fetch()` 消费外部 br 响应，上游内容是否真的可信；
* 梳理**入站**：哪些接口配了会解压 br 的解析器（Express 5 / body-parser 2 / @fastify/compress 等），阿里云 AVD 还特别指出部分路径在**鉴权前**就完成了解压；
* 过渡期可在网关侧临时限制不可信来源的 br 流量（注意先灰度，别误伤正常业务）；
* **WAF 虚拟补丁**

  ：Imperva 已针对该 CVE 发布规则，并验证可检测/阻断其可复现的利用尝试——这是给升级窗口买时间的现实手段；
* 监测信号：解压过程中的**进程异常退出、解码错误**可以帮助排查看哪里值得查，但 Imperva 明确提醒：这**不是**可靠的单独利用指标，需要结合部署的运行时版本、应用日志和压缩数据来源一起判断。

## 七、三点评论：比漏洞本身更值得注意的事

**1. 运行时层正在成为内存安全漏洞的「新前线」。** 把 Node2Shell 和上周的 PHP2Shell 放在一起看：一个打在 PHP 引擎，一个打在 Node.js 捆绑的 C 解码器，同一周披露、同属「应用代码无辜、运行时买单」的形态。Imperva 自己在文末也做了这个对照。对防守方来说，这意味着**漏洞管理的清单必须覆盖运行时本身**，而不只是依赖库。

**2. 「你的代码没有 bug，但你还是被 RCE 了」——供应链式修复困境。** 这类漏洞的修复动作不在开发团队的代码库里，而在运维的运行时版本里。可现实中，Node 版本往往跟着镜像基线走，一躺就是几年。这次真正考验的是组织的**运行时资产管理能力**，而不是开发能力。

**3. 披露到利用的窗口在缩短。** Imperva 在结尾提到，PHP2Shell 研究里 AI 参与了漏洞发现与利用开发，Node2Shell 则展示了「不可信压缩数据 → 代码执行」的完整路径。AI 同时在加速研究者和攻击者——**留给「披露后慢慢排期」的时间只会越来越少**。这也正是 WAF 虚拟补丁这类「先买时间、再落地修复」的策略价值上升的原因。

## 八、真实性核实

**已多源确认：**

* CVE-2026-111497 的存在、高危定级、Brotli 解码器越界写类型、可致 RCE 的官方表述（Node.js 官方公告、Beazley Security 通报、Astra、SecurHUB、阿里云 AVD、台湾中央社/資安署报道）
* 影响 22.x/24.x/26.x，修复版本 22.23.4/24.22.1/26.12.1，10-21 发布（上述信源一致）
* 官方致谢 mcollina 报告、aduh5 修复（Node.js 官方公告原文）
* 根因机制（块切换校验失败被丢弃、状态不一致、越界索引访问 Huffman 表/上下文映射）：Imperva 描述与阿里云 AVD 细节互相印证
* 上游 Brotli 1.2.1/1.1.1/1.0.10 同步修复（Node.js 发布说明及多家转述）
* 截至 10-22 无在野利用报告（多家一致）

**单一信源 / 需继续观察：**

* **官方镜像 RCE 实测结论**

  ：目前主要依据 Imperva 一方（附带演示视频）。Beazley 在其通报撰写时甚至表示「尚无已知公开 PoC」——因为 Imperva 的研究比多数二手通报晚一天公开。
* **另一公开 PoC 仅崩溃 + 有限内存读取**

  ：来自 The Hacker News 等转述，未见一手实验数据，与 Imperva 结论存在分歧（见第四节）。
* **发现者归属分歧**

  ：Beazley 称 Node.js 致谢「OpenAI Codex Security 的 Khai Tran 与 Sylvie Mayer」，但官方公告原文写的是 mcollina 报告 / aduh5 修复。以官方公告为准，Beazley 的说法疑为混淆（可能与其他事件或上游 Brotli 修复的发现者混淆），**未能独立证实**。
* **入站可利用的 body-parser 版本下限**

  ：Imperva 实测 2.0.0 起即可，阿里云 AVD 写作 2.1.0 及以上，两者略有出入；Express 官方迁移文档记录 body-parser 自 2.0.0 支持 Brotli。建议按「2.0.0 起即可能暴露」从严排查。
* Imperva 的版本测试矩阵（Express 5.0.0–5.3.0 × body-parser 2.0.0–2.3.0）为其自述，未逐版本独立复现。

**参考来源**

* Imperva Threat Research《Node2Shell: From Brotli Data to Remote Code Execution》（Ron Masas，2026-10-22）https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/
* Node.js 官方：Wednesday, October 21, 2026 Security Releases https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
* Node.js v24.22.1 发布说明 https://nodejs.org/en/blog/release/v24.22.1/
* 上游 Brotli 修复 commit https://github.com/google/brotli/commit/0ed4268a4401abcb44720963
* Beazley Security Labs 通报 BSL-A1236 https://labs.beazley.security/advisories/BSL-A1236
* 阿里云漏洞库 AVD-2026-111497 https://avd.aliyun.com/detail?id=AVD-2026-111497
* Astra Security：Node.js October 2026 Security Release https://www.getastra.com/blog/security-advisory/nodejs-october-2026-security-patches
* SecurHUB：Node.js Security Update Fixes Brotli Decompression Flaw https://www.securhub.pl/en/blog/2026-10-22-node-js-security-update-fixes-brotli-decompression-flaw-that-could

* Express 5 迁移指南（Brotli 编码支持）https://expressjs.com/en/guide/migrating-5/#brotli-encoding-support
* body-parser 发布历史 https://github.com/expressjs/body-parser/blob/master/HISTORY.md

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EibmAUicJficZYs...