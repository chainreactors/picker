---
title: 【一天一个nacos漏洞·第十天】【高危】AI供应链缺陷
url: https://mp.weixin.qq.com/s/KjexYUESi7msesB5Ys9UoA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:07.780238
---

# 【一天一个nacos漏洞·第十天】【高危】AI供应链缺陷

# 【一天一个nacos漏洞·第十天】【高危】AI供应链缺陷

原创

YNsec
YNsec

YNsec安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【一天一个nacos漏洞·第十天】【高危】审的是 A，上的是 B

> "
>
> 安全研究 · 漏洞利用链拆解 · 靶场实录

**摘要**

今天换个方向，讲**发布审核**。前面九天都在说"谁能进来"，今天说的是"**进来的东西，是不是被检查过的那个东西**"。

两道题，两种换法：

一个在**时间**上换——审核通过之后、正式发布之前，内容还能被改掉。

一个在**集合**上换——审核扫了五个文件，实际下发了六个。

> **免责声明**：测试全部在授权靶场完成，主机地址、账号与口令均未写入本文。内容仅用于安全学习与防御加固。

---

01

一、先说这条流水线

Nacos 的 AI 资源（AgentSpec、Skill 之类）有一套发布治理：

```
text

提交 submit  →  审核 reviewing  →  通过 reviewed  →  发布 publish  →  online
                    ↑
              交给 skill-scanner 扫一遍
```

设计意图很明确：**东西上线之前，得先被扫一次。**

而 `publish` 那道门也确实在拦：

```
java

if (execution.getStatus() != APPROVED) {
    throw ... "Pipeline not approved, cannot publish";
}
```

**问题在于：它只校验"审核通过了"，从不校验"通过的是不是现在这份"。**

|  | VE-0415 · 时间上换 | VE-0534 · 集合上换 |
| --- | --- | --- |
| 分数 | **8.1** | **7.7** |
| 一句话 | 审核后、发布前，内容被改掉 | 审核漏扫了空白名资源 |
| 换法 | 换内容 | 换文件 |
| 最低权限 | 普通开发者（Config 写权限） | 普通开发者（AI 写权限） |
| 命令执行 | 否 | 否 |

---

02

二、VE-0415：审核通过之后，内容还能改

### 2.1 提交时，内容还没读

提交那一步，看着像"开始审核"，其实只是**登记了一个读取动作**：

```
java

ctx.setFilesLoader(() -> {                 // ← 只是注册回调，此刻不读内容
    return buildPipelineFiles(loadAgentSpecFromStorage(namespaceId, name, finalTarget));
});
...
resourceManager.moveToReviewing(...);      // 状态改成 reviewing
resourceManager.runPipelineExecution(...); // 异步跑，稍后才真正 getFiles()
```

真正的读取发生在异步流水线里，**而且读的是当时的存储**。这就埋下了一个时间窗。

### 2.2 发布时，只问两句话

```
java

// 1) 状态对不对
if (!REVIEWING.equals(v.getStatus()) && !REVIEWED.equals(v.getStatus()) && ...) {
    throw ... "Only reviewing version can be published";
}
// 2) 流水线是不是 APPROVED
if (execution.getStatus() != APPROVED) {
    throw ... "Pipeline not approved, cannot publish";
}
// 没有第三句：现在的内容，和审核时的内容，是不是同一份？
```

**它问的是"有没有盖过章"，不是"盖的是不是这一页"。**

### 2.3 而内容，恰好有另一个入口

AgentSpec 的正文存在 Nacos Config 里：

```
text

group  = agentspec__enc.〈hex(name)〉__enc.〈hex(version)〉
dataId = manifest.json
```

而 **Config 的权限域，和 AI 资源的对象级权限是两套独立的东西**。

于是出现一个很微妙的组合：

```
text

devuser 调 AI 接口改这个 AgentSpec  → 403 No permission to modify agentspec
devuser 调 Config 接口改同一个 group/dataId → 200 success
```

**同一个字节，一扇门锁着，另一扇门开着。**

### 2.4 完整的一次替换

测试用的探针扫描器会把扫到的东西记下来，结果很直白：

```
text

【提交】内容 = BENIGN_REVIEW_CONTENT_v1
【审核】扫描目录里：manifest.json → BENIGN_REVIEW_CONTENT_v1
                    SKILL.md      → BENIGN_REVIEW_CONTENT_v1
       结果：APPROVED

【中间】用 Config 接口覆盖同一 group/dataId
       内容 = MALICIOUS_AFTER_REVIEW_CONTENT_v2
       版本状态仍是 reviewed，流水线记录仍是 APPROVED

【发布】publish → 200 ok
【上线】客户端读到：MALICIOUS_AFTER_REVIEW_CONTENT_v2
```

**章是给 A 盖的，B 拿着这张章上线了。**

### 2.5 最狠的一处：md5 是事后算的

发布时会把内容算个 md5 存进版本表，看着像是"内容指纹"。

但看它的执行顺序：

```
java

resourceManager.doPublish(...);                          // 先发布
computeAndStoreContentMd5(namespaceId, name, version);   // 之后才按当前存储算
```

**先发布，再按"当前（已经被改过的）内容"计算指纹。**

所以最终落库的 md5，和篡改后的内容完全对得上：

| 内容 | 期望 MD5 |
| --- | --- |
| `BENIGN_REVIEW_CONTENT_v1`（被审核的） | `262899de…` |
| `MALICIOUS_AFTER_REVIEW_CONTENT_v2`（实际上线的） | `adbffde2…` |

落库的是 `adbffde2…`——**系统给自己签了一个完全自洽的字。**

这个设计有个名字，叫**事后自证**：它不是用来发现问题的，是用来证明"现在这份是对的"。

---

03

三、VE-0534：审核扫的文件，比下发的少一个

### 3.1 一个名字是空白的资源

写 AgentSpec 的时候，可以带一堆资源文件。如果把某个资源的 `name` 设成空格 `" "` 或者空串 `""`：

* **能写进去**——入口只校验顶层 `name`，不看 `resource.name`；
* **能落盘**——`generateResourceId` 把空白名归一成空串，路径固定成 `resource_.json`；
* **能登记**——生成 manifest 时用的是同一份 resource map，所以引用列表里也有它。

三步都成功了。**资源真实存在于存储里。**

### 3.2 但审核看不见它

构造"交给扫描器的文件列表"时，有这么一段：

```
java

for (AgentSpecResource resource : agentSpec.getResource().values()) {
    if (resource == null || StringUtils.isBlank(resource.getName())) {
        continue;                    // ← 空白名，直接跳过
    }
    files.add(new ResourceFileContent(buildResourcePath(resource), ...));
}
```

**它的名字是空白的，所以它不在审核清单里。**

而且不止这一处——三条路都看不到它：

```
text

① buildPipelineFiles   → isBlank 直接 continue，不进扫描集
② 扫描器拿到的 manifest.json → 只有主内容，不含 resources 引用列表
③ 扫描器合成的 SKILL.md     → 基于①②的文件集，自然也没有它
```

### 3.3 但下发的时候，它又回来了

发布之后，客户端拉取走的是另一条路径——**按 manifest 的引用列表逐条读**：

```
java

String resourceId = generateResourceId(resourceRef.getType(), resourceRef.getName());
byte[] resourceBytes = storageRouter.route(resourceKey).get(resourceKey);
resourceMap.put(resourceId, resource);       // 空白名 → key ""
```

于是：

```
text

审核扫描的文件集 = { manifest.json, config/benign.md, SKILL.md }
实际下发的文件集 = { manifest.json, config/benign.md, SKILL.md, resource_.json }
                                                    ↑ 未审核的这一份，跟着上线了
```

**审核输入是下发集合的真子集。** 差的那个，正好是藏东西的地方。

### 3.4 对照组，把话说死

测试时建了两个 AgentSpec，**标记字符串完全一样**，只差放在哪个文件里：

| 组 | 标记放在哪 | 扫描器看到 | 结果 |
| --- | --- | --- | --- |
| 对照组 | `config/evil.md`（正常名字） | **HIT sentinel** | REJECTED → publish 400 |
| 绕过组 | 空白名资源（`" "`） | 看不到 | **APPROVED → online 200** |

**同样的内容，换个文件名就能过审。** 这比任何理论分析都有说服力——它证明审核门禁本身是有效的，只是**它的视野被缩小了**。

下发之后，客户端拿到的 `resource` 里确实有那个 `""` key，内容完整。

### 3.5 一个能说明问题的对比

同一个项目里，Skill 那边也有一份 `buildPipelineFiles`：

```
java

// SkillOperationServiceImpl：只跳过 null
if (resource == null) { continue; }
```

**AgentSpec 这边多了一个 `isBlank`。** 就是这三个单词，让"空白名资源"从审核视野里消失了。

> 🔍 这类缺陷特别值得记的地方在于：它**不是故意留下的后门**。写这段代码的人大概率是在做"防御性编程"——“名字是空的，那就算了吧”。结果"算了"的那一份，照样会被存下来、照样会被下发。

---

04

四、两个合起来，其实是同一个问题

```
text

VE-0415：审核结论 = APPROVED  →  但没绑定"哪一份内容"
VE-0534：审核输入 = 部分文件   →  但下发的是全部文件
```

一个是**时间上没有快照**，一个是**空间上没有对齐**。但根子是同一句：

**审核这个动作，和"最终要上线的那份东西"，中间没有一根绳子拴着。**

而现实里的供应链攻击——从 SolarWinds 到各种 build 投毒——用的都是这一招：**不攻破检查，只让检查的对象和交付的对象错开。**

---

05

五、边界：两个都需要先"打开审核"

得说清楚：这两个洞都**需要启用 AI 发布流水线**（`nacos.plugin.ai-pipeline.enabled=true`）。

而这个开关**默认是关的**。默认状态下 `submit` 直接上线，压根没有审核这一环——那时候就不是"绕过审核"，而是"没有审核"。

所以：

> 📐 **它们的价值不在"默认就能打"，而在"当你以为有审核的时候，审核可能并不覆盖你要上线的东西"。**很多团队是在合规要求下才打开这个开关的。打开之后如果以为"有流水线就安全了"，那反而比不开更危险——**因为你会信它。**

---

06

六、修复：把审核结论和内容焊死

| 问题 | 怎么改 |
| --- | --- |
| 审核结论不绑定内容 | `submit` 时对全部文件算**规范化哈希**并持久化；`publish` 前重算比对，不一致直接拒绝 |
| 惰性加载拉长了窗口 | 流水线执行前一次性快照内容，让扫描器消费快照而不是"当时的存储" |
| md5 事后计算 | `contentMd5` 必须在**发布前**计算，并与审核快照比对；不能"先上线再盖章" |
| 审核输入不全 | 删除 `buildPipelineFiles` 里的 `isBlank` 跳过；或更彻底——**以存储中的实际文件清单作为审核输入** |
| manifest 不含引用 | 给扫描器的 `manifest.json` 要包含完整 `resources` 列表，让审核节点能交叉核对 |
| 集合有差集 | 在 submit/publish 前断言：`待下发集合 − 已扫描集合 = ∅`，不为空就拒绝 |
| 空白名能写入 | 写入侧直接拒绝 `name` 为空/纯空白的资源，返回参数错误 |
| 权限域错配 | Config API 对 `agentspec__*`、`skill__*`、`prompt__*` 等 AI 存储 group 增加 AI 层对象级鉴权 |

> 💡 一句可以写进发布系统设计的话：**审核的产物不该是"通过"两个字，而应该是"通过的是这一份内容"的签名。**前者可以被任何东西借用，后者借不了——因为一旦内容变了，签名就对不上。

---

07

写在最后

第十天了，第一次讲"流程"而不是"鉴权"。

前面九天的问题，基本都能落到某一行代码上：少一个判断、用错一个参数、默认值选错。今天这两个，**每一行单独看都是对的**：

* 提交时不读内容，是为了不阻塞请求；
* 发布时校验 APPROVED，是标准做法；
* 跳过空白名资源，是防御性编程；
* 下发时按 manifest 全量读，是完整性的要求。

**但把它们串起来，中间就出现了一道缝：审核看到的，不是最终上线的那一份。**

这类问题特别难靠代码 review 发现，因为它不在任何单点里，而在**流程的两个环节之间**。要发现它，得问一个很笨但很有效的问题：

> **“这个东西被检查的时候，和它被使用的时候，是同一份吗？”**

如果答案不确定，中间就还有一道缝。

下一天见。

---

> 📚 **系列回顾 · 【一天一个nacos漏洞】**
>
> **第一天**：客户端快照路径穿越，一路退到 `/etc/cron.d`。**第二天**：MCP 与 Skill，鉴权看 A、干活看 B。**第三天**：MCP 与 A2A，名字和版本拼成的 key 不唯一。**第四天**：配置接口的别名错配（9.9），Prompt/Skill 的冒号分隔符碰撞（9.1）。**第五天**：配置接口认错参数（9.6），AI 资源可见性被 Config 通道绕过（9.6）。**第六天**：MySQL 健康检查的 SQL 注入（7.7），鉴权密钥进日志（7.8）。**第七天**：OIDC 信任链两端——不验来源（8.1），不认撤销（7.4）。**第八天**：两处 fail-open——插件缺失即全放行（7.2），空白主体即成管理员（8.1）。**第九天**：服务间共享身份——凭据被主动投递（7.4），静态值可永久重放（8.1）。**第十天**（本篇）：发布审核被架空——审核后换内容（8.1），审核漏扫文件（7.7）。
>
> 文中所有测试均在授权靶场完成，主机与凭据未写入。若在生产环境发现同类问题，请第一时间联系厂商并遵守披露约定。

---

*— 完 —*

*如果这篇对你有帮助，欢迎**在看 / 转发**给做安全的朋友*

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Uzia3lCRCbBE6FMtLakKgM9ReNq8A01Y9HQrR8gdAU0d4FicFanlUibllvBxX3Ufq0PaLO1ibHZ9uRJbYlicCVkNQFA/0?wx_fmt=png)

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