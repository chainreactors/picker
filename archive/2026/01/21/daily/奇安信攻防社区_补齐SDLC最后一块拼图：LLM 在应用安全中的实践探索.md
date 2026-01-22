---
title: 补齐SDLC最后一块拼图：LLM 在应用安全中的实践探索
url: https://forum.butian.net/share/4728
source: 奇安信攻防社区
date: 2026-01-21
fetch_date: 2026-01-22T03:33:36.978016
---

# 补齐SDLC最后一块拼图：LLM 在应用安全中的实践探索

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 补齐SDLC最后一块拼图：LLM 在应用安全中的实践探索

* [渗透测试](https://forum.butian.net/topic/47)

随着DevSecOps的推进，应用安全已逐步融入SDLC各阶段，一个长期存在的问题依然突出：安全工具往往能发现问题，却难以判断其真实性、可利用性及处置优先级。这些持续消耗研发与安全团队的时间精力。近年来随着大语言模型的迅速发展，为这一困境提供了新的可能，本文结合实际应用安全建设经验，重点探讨AI在硬编码、SCA、漏洞挖掘等场景中的应用安全实践方法。

### 导语
随着 DevSecOps 的不断推进，应用安全已被广泛纳入SDLC的各个阶段。然而，在代码扫描、依赖分析、漏洞检测等能力逐步成熟的同时，一个长期存在却难以解决的问题始终横亘在安全工程实践中：\*\*安全工具“能发现问题”，却难以判断问题是否真实、是否可利用、是否值得优先处理\*\*。大量规则驱动的扫描结果不仅带来了高误报率，也持续消耗着研发与安全团队的精力。
近年来随着大语言模型（LLM）的快速发展，为这一困境提供了新的可能。不同于传统规则或静态特征匹配，LLM 在语义理解、上下文推理和条件组合分析方面展现出独特优势，使其具备参与安全“判断层”的潜力。将 LLM 引入 SDLC，不再只是生成代码或辅助文档，而是尝试参与到\*\*安全结果的理解、验证与决策\*\*之中。
本文结合实际应用安全建设经验，围绕 LLM 在 SDLC 中的落地实践展开，重点探讨其在硬编码、SCA、漏洞挖掘等场景中的应用方式与工程化思路。
#### SDLC 应用安全流程
![image-20251217111844592](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251217111844592.png)
#### \*\*SDLC名词解释\*\*
- SAST（静态应用安全测试）通过对源代码或编译产物进行静态分析，在不运行系统的情况下发现潜在的安全缺陷，如 SQL 注入、XSS、不安全函数调用和硬编码敏感信息等，适合在开发阶段提前发现问题。
- SCA（软件成分分析）聚焦于项目中使用的第三方开源组件，识别依赖库及其传递依赖中已知的安全漏洞、风险版本和许可证问题，帮助团队降低因外部组件引入的安全风险。
- DAST（动态应用安全测试）在系统运行状态下，从攻击者视角对应用进行测试，通过捕获流量包修改参数重放，模拟真实攻击行为验证系统是否存在可被实际利用的漏洞，如注入攻击、未授权访问等
- 硬编码（Hard Coding），是指在程序中直接把固定的值写死在源码里，而不是通过配置文件、环境变量等方式获取，比如下面这些情况，都属于硬编码：用户名、密码、token或加密密钥等
#### 为什么我们需要SDLC？
产品一句话需求 → 开发自己理解 → 按照个人习惯去开发 → 功能上线后出现大量漏洞 → 被外部利用造成损失
而SDLC要做的就是把漏洞扼杀于摇篮之中，而不是靠后期凭经验渗透测试发现。
但目前传统的SDLC存在大量告警/误报，推送大量工单给研发会导致业务间摩擦度增加，因此理想情况是把真正需要修复的工单交给研发处理
### 硬编码规则下引入AI判断，减少误报
问题背景：目前硬编码扫描是根据规则的正则匹配，存在一定的局限性和误报
![image-20251217171931177](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251217171931177.png)
#### 整体流程
结合硬编码规则 + AI 判断保留高召回，同时降低误报率
![image-20251230150538531](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251230150538531.png)
\*\*硬编码规则先行\*\*
使用固定规则（正则、逻辑判断）先筛掉明显非风险项，让 AI 只处理模糊/不确定案例
\*\*AI 判断做辅助\*\*
只对硬编码规则未覆盖、可疑的候选项输出风险判断，输出结果可附置信度或分类标签
\*\*置信度 + 白名单控制\*\*
AI 输出带置信度，低于阈值直接忽略，对常见合法值、默认值设置白名单
#### 提示词 promot
通过定位文件的位置，结合上下文判断实际风险等级，把AI分析结果输出
```php
你是一个资深应用安全专家，精通代码安全、凭证泄露、真实攻击利用分析。
现在给你一个【疑似硬编码凭证】的扫描结果，请你进行【可利用性研判】。
输入信息如下（JSON）：
%s
请严格按以下维度进行分析：
1. 该硬编码是否为真实敏感凭证
2. 是否存在被外部攻击者利用的可能
3. 是否依赖运行环境
4. 泄露后的安全影响
5. 修复建议
请以 JSON 格式输出分析结果
```
模型输入字段释义
| | |
|---|---|
| 字段 | 释义 |
| match | 匹配到的硬编码内容（部分脱敏显示） |
| rule | key类型 |
| path | 硬编码所在的完整文件路径 |
| branch | 分支 |
| code | 上下5行代码 |
增加输出长度，避免截断
```php
"extra\_body": map[string]interface{}{
"think\_mode": true,
"max\_output\_tokens": 1024,
```
#### 实现效果
![image-20251217195004928](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251217195009299.png)
如果是走正常的流程，`secret\_value`会被 `generic-api-key`规则名字标记严重程度为`medium`
![image-20251218143042933](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251218143042933.png)
开启AI分析选项后，通过定位文件的位置，结合上下文交给ai分析，AI判断实际危害程度为低
```php
在代码中发现硬编码的敏感信息'DEMO\_SECRET'，其值为'secret\_value'。根据规则'generic-api-key'，这可能是一个API密钥或其他类型的敏感凭证。该变量位于'E:\SDLC平台\backend\uploads\demo.py\_scan\demo.txt'文件中，并且注释表明它看起来像一个Key，但无实际用途。由于这是一个测试环境中的示例代码，风险相对较低。
```
![image-20251218142746712](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251218142746712.png)
#### 掩码输出硬编码片段
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-46560df695b327e9d376cca999399425ac1648b0.png)
代码中存在：
`const apiKey = "sk\_live\_9f83a0b7..."`
AI分析后会直接原样输出，给出完整的佐证片段，这样是不符合数据安全合规要求的，就会产生 \*\*二次扩散风险\*\*。
正确掩码后的做法，AI 只需知道这是一个硬编码密钥
`const apiKey = "\*MASKED\_SECRET\*"`
#### 实现效果
通过 AI 研判对硬编码、潜在风险及非生产路径问题进行自动识别与筛选，各产品待修复量平均下降约\*\*52.8%\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-588a9a2c1c77acf811a1a96ef6253c21ca19f9c5.png)
价值体现：在保证安全覆盖率的前提下，AI 自动化研判显著提升效率，降低人工排查压力，推动安全研判进入智能化阶段
- AI 判断为 False：AI 判定为误报，可直接关闭
- AI 判断为 True 但 NonLive：问题真实但不在生产路径，可降低风险等级处理
- AI 研判后待修复：确认真实且影响生产，需进入修复流程
### SCA可利用性与真实风险判断
从官方文档 <https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components> 描述可看到，涉及版本都需要更新到对应补丁
![image-20251223145325095](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251223145325095.png)
但从甲方安全运营的角度会存在以下这些问题：
1.大版本的更新会存在项目兼容性问题，不好推进
2.涉及仓库数量较多，如果全部同时进行整改将会是极大的工作量
如果我们深入分析后会发现，并不是在版本范围内就存在漏洞，还需要额外的条件满足才能利用
```php
客户端请求 Server Action
↓
执行 Server Action (接收用户输入)
↓
react-server-dom-webpack 序列化响应
↓
【漏洞点】反序列化时未正确验证输入
↓
恶意 payload 被执行 → RCE
```
\*\*必要利用条件\*\*
| 条件 | 是否必须 | 说明 |
|---|---|---|
| App Router | ✅ 必须 | 提供 RSC / Flight 机制 |
| Server Actions | ✅ 必须 | 提供反序列化入口 |
| 用户可控输入 | ✅ 必须 | 构造恶意 payload |
#### 整体流程
- \*\*核心思路\*\*：证明SCA漏洞代码是否被业务代码真实调用，如果不可达那么这个SCA漏洞在该仓库就\*\*不可利用\*\*
- \*\*调用链路\*\*：业务代码中是否存在外部可控输入→ 漏洞组件危险函数的真实可达路径
![image-20251221173914270](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251221173914270.png)
```php
HTTP 请求 (scaHandler) -- 输入CVE编号
↓
CVE 分析 (runSCACVEAnalysis)
├─ 步骤 2.1: Google 搜索受影响版本
├─ 步骤 2.2: Qwen 识别依赖组件搜索官网信息
├─ 步骤 2.3: 搜索引擎寻找对应PoC
├─ 步骤 2.4: Qwen 提取结构化信息
└─ 步骤 2.5: Claude 最终安全分析
↓
仓库分析（可选）
├─ 方法一: 依赖分析 (analyzeRepositoryVulnerability)
└─ 方法二: 锚点分析 (analyzeRepositoryWithAnchor)
```
#### google搜索引擎调用
调用google进行联网搜索，局限性 key限制每天100个
<https://console.cloud.google.com/apis/credentials>
凭证-创建凭证
![image-20251217162129486](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251217162129486.png)
启用custom search api
![image-20251217161840875](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251217161840875.png)
<https://programmablesearchengine.google.com/controlpanel/create>
在这个地方可以定义调用的搜索引擎
![image-20251217162013410](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251217162013410.png)
#### 优化阶段1：多个源进行信息整合导致出错
初步阶段测试发现，Qwen去重整理逻辑导致结果出现缺失
![image-20251223150956095](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251223150956095.png)
因此后续直接选用官方源，保证结果数据的准确性
\*\*官方情报来源\*\*
| 序号 | 来源机构 | 描述 | 链接 |
|---|---|---|---|
| 1 | 美国国家漏洞数据库 (NVD) | 官方 CVE 条目，包含漏洞详情、受影响版本、CWE、CVSS 等信息 | <https://nvd.nist.gov> |
| 2 | CVE 官方记录 (CVE.org) | 官方 CVE ID 登记与记录 | <https://www.cve.org> |
| 3 | React 官方安全公告 (React Team / Meta) | 官方漏洞公告及修复版本说明 | <https://react.dev> |
| 4 | 加拿大网络安全中心 (Cyber Centre) | 官方安全公告、漏洞说明 | <https://www.cyber.gc.ca> |
| 5 | Google Cloud 官方博客 | 官方补丁指引及响应措施 | <https://cloud.google.com> |
#### 优化阶段2：未关联间接受影响组件导致结果不准
在漏洞受影响的范围很多都只提及了react组件，但是有其他间接依赖组件如next也会受到影响，因此在爬取网站内容需要把这部分信息也整理进来
```php
虽然应用使用了受影响的 React 版本（19.0.0）并启用了 React Server Components 功能，但 React Server Components 的漏洞版本范围是 19.0.0-19.2.0，而当前仓库使用的是 react-server-dom-webpack 19.0.0。关键问题是该仓库使用的是 Next.js 16.0.6，而 CVE-2025-55182 主要影响独立的 React Server Components 实现，Next.js 有自己的 Server Components 实现机制，不直接受此 CVE 影响。条件1不满足，因此漏洞不可利用
```
![image-20251223151142011](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251223151142011.png)
#### 优化阶段3：规范性提示词输入
\*\*这里有三个关键点：\*\*
\*\*将「CVE 知识」作为输入，而不是让 LLM 自行理解\*\*
- 不依赖模型对 CVE 的主观理解或记忆
- 由安全侧明确提供：漏洞成因和可利用条件链（Exploit Preconditions）
- 避免模型自由发挥导致的误报或信息污染
\*\*在目标代码仓库中，验证漏洞可利用条件是否成立\*\*
- 不做漏洞解读
- 不做风险定级臆断
- 不基于版本号直接下结论
\*\*将每个 CVE 拆解为一组必须同时满足的利用条件\*\*
- 逐条在仓库中进行验证：任一关键条件不满足 → 漏洞不可达，不构成真实风险
- 代码结构、依赖使用情况及配置与对外暴露面
\*\*最终提示词\*\*
```php
你是一名资深应用安全分析师。请基于我提供的 SCA 扫描结果，对发现的第三方组件漏洞进行【汇总型安全分析输出】，输出需包含以下部分（使用简体中文）：
1. 漏洞基本信息
- 受影响组件 / 编程语言 / 版本
- CVE 编号
- 漏洞类型
2. 漏洞原理说明
- 从安全分析视角解释漏洞成因
- 重点描述漏洞触发机制（如反序列化、解析、路由处理等）
- 对未公开的内部实现需明确说明"细节未披露"，避免推测
3. 影响评估
- 可造成的安全影响（如拒绝服务、信息泄露等）
- 对业务连续性、系统稳定性和可用性的潜在影响
4. 攻击前置条件
- 环境条件（框架、运行模式、功能开启情况等）
- 依赖条件（受影响的第三方组件）
- 攻击者权限要求（是否需要认证、是否可远程触发）
5. 涉及模块或组件范围
- 受影响的框架模块或依赖包名称
- 若具体函数或代码位置未公开，需明确说明
- \*\*必须列出所有依赖关系\*\*：如果漏洞影响底层组件，必须说明哪些上层框架/库可能间接受影响，包括具体的组件名称和受影响版本范围
6. 可利用性与 EXP 情况说明
- 是否存在已公开的 PoC / EXP
- EXP 的公开来源类型（如 G...