---
title: AI渗透的拐点已至？我是如何通过AI纯黑盒挖到通用产品的9.8分RCE 0day漏洞
url: https://mp.weixin.qq.com/s/--YqoyfqPOxN6HI3Mkt4yA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:05:17.997076
---

# AI渗透的拐点已至？我是如何通过AI纯黑盒挖到通用产品的9.8分RCE 0day漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Lf9Eic6Vdf3dBbHt0GWuPxBgYZsfKOZLu4cdTxjeSlElBeK4wfMdrQd0RL4VtBquaL65guDpDhUiab4fib3Qiae5NxCFh5CvxnVUqx9L8tPZE14/0?wx_fmt=jpeg)

# AI渗透的拐点已至？我是如何通过AI纯黑盒挖到通用产品的9.8分RCE 0day漏洞

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

牛 大佬( ఠൠఠ )ﾉ

以下文章来源于ChainReactor
，作者MelinaSec

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6kIoeKia9PeYaereDc4YFTc1fFanicxeC2GwKSqsGOkdpQ/0)

**ChainReactor**
.

致力于下一代AI原生的进攻性基础设施(AI Naitve Offensive Infrastructure) 和 全流程智能化渗透

## AI渗透的拐点已至？我是如何通过AI纯黑盒挖到通用产品的9.8分RCE 0day漏洞

> 标题党了， 但是过程是真实的， 是我们在测试新的工具第一天发现了一个高价值0day的真实过程。

> 我们让三个 DeepSeek agent 扫描一组目标。它们从公开漏洞情报中定位到攻击面，绕过了厂商对历史漏洞的修复，拿到了 RCE。我们以为这是个已知漏洞， 直到厂商确认是新的，发了奖金。CVSS 9.8。

在今天之前很多人怀疑 AI 能替代顶级红队，我们也怀疑 AI在真实攻防场景中的能力。各种各样的开源或者创业公司的项目和介绍， 总是在靶场和CTF中， 偶尔有能投入到SRC的， 从来没有公开的黑盒挖掘到高价值漏洞的案例。 我们自己的几套系统在实战中也遇到了这个问题， **AI能挖到的漏洞往往传统扫描器也能挖到**，只不过AI能帮忙进行复现和验证。

Anthropic 扫描生产级开源项目，找到了 500 多个漏洞，有些藏了几十年没人发现。他们后来的 Mythos Preview 在主流操作系统和浏览器中挖出了上千个高危 0day，包括一个藏了 27 年的 OpenBSD TCP 漏洞和一个藏了 16 年的 FFmpeg 编解码器缺陷。**这些是LLM擅长的领域，基于代码白盒审计**

xbow 用全自动 AI 扫描拿下了 HackerOne 全球排行榜第一，提交 1,060+ 份漏洞报告，不过HackerOne 联合创始人 Michiel Prins 的评价：量产能力强，业务深度不够。Anthropic 白盒审计找到的那 500 个开源漏洞也类似，数量可观，**但没有一个需要你理解目标业务逻辑、构造多步利用链、绕过 WAF 才能打通。** 至于AI在高强度对抗的实战效果，目前业界还没有很好的案例。

![](https://mmbiz.qpic.cn/mmbiz_png/Lf9Eic6Vdf3eCBCKzdPpibHZzw4aakagoUjTic4nkqW44D3VckwYEicQLY3v4fe3ngRGsvbjuuDHyOdesdmQoEEJ6uhrDdd7f8IRvJkjw7ONLwY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Lf9Eic6Vdf3dHNSW4HLqiccFTYHiaQn0FaWONDrQicJoQlZ3jXDicO1ibIUSXcx0MPfNicHmbvECJ8oO1zmBib552uO7XskZBZIPhickgry7z9O92f1A/640?wx_fmt=png&from=appmsg)

国内，腾讯第二届 TCH（云黑客松）可能是最接近实战，610 支参赛队伍 。我们参加了两届三个方案：第一届主要是开源的xbow的CTF题 Antix 第四，第二届更接近真实渗透场景 Bytex 第三（唯一 AK，54/54 flag）和 For Future 第七。

有一个共同问题， 大部分队伍的设计， 包括我们自己的三套设计， **总是想通过某种框架去提供模型在安全方面的能力， 不管是极繁还是极简的架构， 都逃不出框架的范畴。**

这次我们再次抛开了所有的任何样式的框架， 通过一个有趣的设计， 让AI首次在real world中发现了一个高价值0day。

## 发现过程

目标是一套国内使用广泛的 ERP 系统，在多次 HW 和红蓝对抗中频繁出现。我和几个做红队的朋友都审计过这套系统的源码，到 2026 年能挖的漏洞已经不多了。

### Phase 1: 侦察（DeepSeek，~17:50）

aiscan agent 收到任务后，执行了以下工具调用链：

```
1. spray → 4个目标跑指纹/敏感文件/爬虫 → 全部失败 (yaml decoder bug)
2. web_search × 7 → 搜索目标漏洞情报
   └─ 命中: 多个已知 CVE (SSTI, 路径遍历, 反序列化)
3. cyberhub_search → 搜索相关 POC 模板
4. bash (curl) × 4 → 探测4个目标首页
5. bash (curl) × 4 → 探测常见路径 (/admin /swagger /actuator /.env /.git ...)
6. bash (curl) → 发现业务服务路径返回 200
   └─ 4个服务端点均可达
```

spray 因为 yaml 解析 bug 全部失败，但 agent 没有停下来。它切换到 web\_search 搜索目标相关的公开漏洞情报，然后用 curl 逐路径探测。在发现某个路径返回 200 后，agent 进一步探测该路径下的子端点，确认了4个活跃的业务服务接口。

Phase 1 产出：目标平台在线、4个业务服务端点、产品版本号、已知 CVE 列表。耗时约10分钟。

### Phase 2: 验证（DeepSeek，~18:00）

Verify agent 的工具调用链更长，也更有针对性：

```
1. web_search × 3 → 搜索 'BinaryFormatter exploit'
2. web_fetch × 4 → 抓取 POC 源码
   ├─ GitHub 安全公告 → 漏洞确认
   ├─ POC 合集 → 利用代码
   └─ 技术分析博客 → 学到关键路由参数
3. bash × 18 → 逐个验证端点
   ├─ 默认口令登录尝试 → 404 (已切换OAuth2)
   ├─ 文件上传接口 → 404
   ├─ 路径遍历 CVE → 404 或 WAF 418
   ├─ 带路由参数的服务端点 → HTTP 200 ← 行为变化
   ├─ format=2 → 响应泄露: 二进制序列化已启用
   └─ format=3 → 触发 DeserializeParameters 调用, 完整堆栈泄露
```

这个阶段的关键转折是 agent 从一篇公开的技术分析文章中学到了一个路由参数。不带该参数时端点返回 404，带上后返回 200 并进入了服务处理管道。agent 随后测试了不同的 `format` 值，发现 `format=2` 的响应中包含配置信息——二进制序列化已启用，默认格式为 Binary。而 `format=3` 直接触发了 `BinaryFormatter.Deserialize()` 调用，服务端返回了完整的 .NET 异常堆栈。

Phase 2 产出：确认 BinaryFormatter 反序列化入口、二进制序列化配置已启用、4个端点均受影响、完整的 .NET 技术栈信息泄露。

### Phase 3: 利用尝试（DeepSeek，~18:30）

Exploit agent 从公开来源找到了完整的利用方法：

```
1. web_search × 5 → 搜索 'BinaryFormatter ysoserial exploit'
2. web_fetch × 4 → 抓取实际 exploit 代码
   ├─ Python RCE 脚本 (含完整 payload 构造)
   └─ 完整漏洞分析 (含路由参数来源和利用原理)
3. bash × 7 → 端点确认 + 参数测试
4. write × 2 → 尝试写 payload 文件 → JSON 截断失败
5. bash × 5 → 尝试发送 exploit → 全部截断失败
```

agent 正确理解了利用链的每个环节，但在生成 payload 时遇到了 DeepSeek 模型的输出长度限制。BinaryFormatter 序列化数据经过 Base64 编码后通常有数千字节，超出了模型单次输出的 token 上限，导致 JSON 被截断。

这是当前 LLM 在漏洞利用领域的一个真实边界：信息收集和漏洞理解没有问题，但精确的二进制 payload 生成不是 token 预测模型的强项。

### Phase 4-5: 验证与 RCE（Claude Opus 4.6，~18:15-19:00）

到这个阶段，三轮 DeepSeek agent 已经在 IOA Space 中积累了大量发现。人类通过 Claude Code 读取了消息图中的工具调用日志，看到了 agent 报告的反序列化入口和堆栈泄露——但这些可能是幻觉。需要用更强的模型去实际验证。

切换到 Claude Opus 4.6 后，验证分为几个阶段。

**确认反序列化入口。** 向 agent 发现的端点发送一个 `System.Data.DataSet` 的 BinaryFormatter 序列化对象：

```
POST /[REDACTED]/ServiceGateway.svc HTTP/1.1
Content-Type: application/json

{"ap0":"<base64-encoded DataSet>","format":"3"}
```

服务端返回：

```
"类型'System.Data.DataSet'的对象无法转换为类型'[REDACTED].BusinessInfo'"
```

这条错误说明 \*\*\*\* 反序列化已经成功执行——DataSet 被正确还原了，只是在后续类型转换时失败。任意 .NET 对象都会在服务端被反序列化。DeepSeek 的发现得到了确认。

**WAF 规则定位。** 用 ysoserial.net 生成标准 gadget chain（TypeConfuseDelegate、WindowsIdentity、ClaimsPrincipal 等），全部返回 HTTP 406——存在 WAF。

为了找到 WAF 的具体拦截规则，采用二分法逐步增加 payload 字节数：

| 发送字节数 | HTTP 响应 |  |
| --- | --- | --- |
| 前 500 字节 | 200 |  |
| 前 1000 字节 | 200 |  |
| 前 1300 字节 | 200 |  |
| 前 1356 字节 | 200 |  |
| **前 1357 字节** | **406** | ← 触发点 |

对偏移 1327-1367 的 hex dump：

```
Offset 1327-1367:
HEX:   39 5D 2C **** .... 63 73 2E 50 72 6F 63 65 73 73 ...
ASCII: 9],[*** ...
```

WAF 的检测规则是匹配序列化数据中的 `***` 类名。所有通过 `***` 执行命令的标准 gadget chain 都包含这个特征。

不同 gadget chain 的 WAF 测试结果：

| Gadget Chain | 包含 Process 特征 | WAF 结果 |
| --- | --- | --- |
| TypeConfuseDelegate | 是 | 406 拦截 |
| WindowsIdentity | 是 | 406 拦截 |
| ClaimsPrincipal | 是 | 406 拦截 |
| **ActivitySurrogateSelectorFromFile** | **否** | **200 通过** |

**WAF 绕过。**`ActivitySurrogateSelectorFromFile` 的工作原理与标准 gadget chain 不同：

1. 1. 攻击者编写自定义 C# 类（如 `ExploitClass.cs`）
2. 2. ysoserial.net 在本地编译该类，将 IL 字节码嵌入序列化数据
3. 3. 服务端反序列化时通过 `ActivitySurrogateSelector` 机制加载并实例化该类
4. 4. 自定义类的构造函数被执行

序列化数据中不包含 `System.Diagnostics.Process` 字符串——自定义代码以 IL 字节码形式存在，WAF 的字符串匹配规则无法检测。

**时间盲注确认 RCE。** 编写验证用的 Exploit Class：

```
public class ExploitClass
{
    public ExploitClass()
    {
        Thread.Sleep(5000);
    }
}
```

生成 payload 并发送：

| 测试 | 端点 | 响应时间 | 基线 | 延迟 (Δ) |
| --- | --- | --- | --- | --- |
| Sleep(5000) | DevReport | 5151ms | ~150ms | +5001ms |
| Sleep(5000) | InOutData | 5147ms | ~150ms | +4997ms |
| Sleep(8000) | DevReport | 8607ms | ~150ms | +8457ms |
| Sleep(8000) | InOutData | 8259ms | ~150ms | +8109ms |

延迟量精确跟随 `Thread.Sleep()` 参数变化，排除网络抖动。

**文件写入确认。** 最终通过 `File.WriteAllText` 向 webroot 写入验证文件，HTTP 访问确认内容正确。服务器环境：Windows Server 2022、.NET Framework 4.8、以 SYSTEM 权限运行。

### 复盘

三轮 DeepSeek agent 的工具调用统计：

| 工具 | Scan Agent | Verify Agent | Exploit Agent | 总计 |
| --- | --- | --- | --- | --- |
| bash (curl/scan) | 15 | 18 | 7 | 40 |
| web\_search | 7 | 4 | 5 | 16 |
| web\_fetch | 0 | 7 | 4 | 11 |
| cyberhub\_search | 1 | 4 | 0 | 5 |

几个值得记录的观察。

从侦察到确认反序列化入口，DeepSeek agent 用了大约20分钟和72次工具调用。整个过程中 agent 的信息来源只有三个：**搜索引擎、目标的 HTTP 响应、和公开的 POC 仓库**。它从公开技术文章中自主学到了关键路由参数，又通过调整 `format` 值发现了二进制序列化的配置泄露。这条从公开情报到漏洞确认的推理链是 agent 自己构建的。

模型切换的时机值得讨论。DeepSeek 在信息收集和模式匹配上表现够用，成本也低。但到了需要构造精确 payload、分析二进制数据、设计 WAF 绕过方案的阶段，我们切换到了 Claude Opus 4.6。这种分层策略在实践中是有效的：用便宜模型做探索，在需要深度推理时升级。

IOA 的消息图在模型切换时体现了价值。Opus 4.6 接手时不需要从零开始理解目标——**前三轮 agent 的搜索结果、HTTP 请求和响应、成功和失败的尝试全部记录在 Space 中**。这让切换成本接近于零。

## 新的架构形态---从端侧agent重新出发

> 本文不是正式工具发布， 是新架构的预告，介绍了几个核心设计。 预计6月初发布全新的智能化渗透工具 aiscan。主打 极简、高效、实战化

回到 Phase 1：agent 从公开漏洞情报中自主定位到攻击面，用 curl 逐路径探测确认了活跃端点，最终推动了整条漏洞发现链。

没有人写好工作流告诉它该搜什么、该探测哪些路径。一个没有框架、没有 MCP server、没有外部编排的单文件二进制，是怎么做到的？

### 框架是笼子

前文提到，**大部分队伍的设计都逃不出框架的范畴**。

框架的本质问题是：它在模型和工具之间插入了一个编排层——本质上都是在处理 "调哪个工具、什么顺序、什么条件分支"。但这些决策恰恰是模型最擅长的事。各种框架使用各种或简单或复杂的机制（知识管理机制、工具调用机制、推理机制、校验机制、Harness机制等等），但**一到了real world 就水土不服**。

**框架在代替模型思考，而不是帮助模型思考。**

当编排层的假设对新场景失效时（它们总会失效 ），框架就从助力变成了笼子。

### 端侧 agent

aiscan 的回答是：不做框架，做**端侧 agent**。受 pi-mono 的启发，整个 agent 只有 `bash`、`read`、`write`、`glob` 四个基础工具，没有编排层，所有决策由模型在运行时做出。

|  | 框架思维 | 端侧思维 |
| --- | --- | --- |
| **决策者** | 编排层（代码写死） | 模型（运行时推理） |
| **工具接口** | 专用 API / MCP | bash 伪命令 |
| **工具文档** | 全量注入 system prompt | 按需读取 SKILL |
| **扩展方式** | 加概念、加节点、加状态 | 不变，组合涌现 |
| **训练复用** | 模型需学习新协议 | 免费复用 CLI 训练数据 |

### 为什么是 4 个而不是 40 个

给模型注册越多的工具，它花在"选哪个工具"上的推理预算就越多，留给"解决实际问题"的就越少。

工具爆炸不是在增强 agent，而是在消耗它的注意力。

4 个通用工具把认知负担压到最低——模型不需要在 20 个专用工具之间做选择，只需要想"下一步该执行什么命令"。

### SKILL：使用手册而非SOP

SKILL在大部分人的思维惯性中， 将其当作...