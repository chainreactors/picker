---
title: 第五章xa0-xa0重生之我是AI人：ReAct 决策循环 — LLM 怎么\"思考\"
url: https://mp.weixin.qq.com/s/KUM7vV5SEmfGGEHd08aesQ
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:02:52.898128
---

# 第五章xa0-xa0重生之我是AI人：ReAct 决策循环 — LLM 怎么\"思考\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0LGiaGIrzXulOab4Fy1slKXNUzE3sQTwuPBO2oN0IKBcTHabAIFc2oLechCkLNwIQ4vNiafINFskkABNgAIDlCtqhAW3B8gupdudXFRyLBSwc/0?wx_fmt=jpeg)

# 第五章 - 重生之我是AI人：ReAct 决策循环 — LLM 怎么"思考"

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于威胁情报Z分析
，作者Gachong

![](http://wx.qlogo.cn/mmhead/j8cooK2zCqoqY1ibzIuH0db0U6NFgdx4PahHyU6OOprunMrA5RzXbibpMcUA18kVOibjEK1IK7HQ28/0)

**威胁情报Z分析**
.

国际网络安全威胁情报，地缘政治事件分析。

1. ReAct 是什么

ReAct = Reasoning + Acting。2022 年 Yao 等人提的论文。核心思想：

```
LLM 不应该一次性给答案，而应该：1. 想(Reason)：分析当前情况2. 做(Act)：执行一个动作3. 看(Observe)：观察动作的结果4. 再想：基于新情况继续5. ...循环到收敛
```

跟普通 Chain-of-Thought 区别：

● CoT：一次性推理

● ReAct：循环推理 + 动作

为啥渗透测试场景特别需要 ReAct？因为这是一个探索性任务。你不知道前面会遇到什么 — 试 SQL 注入没成功，可能需要换 XSS;XSS 也没成功，可能要看认证绕过。每一步的选择依赖上一步的结果。CoT 搞不定这种动态分支。

2. Hati 的 4 选 1 决策

LLM 每次循环，要从 4 个动作里选 1 个(其实更多，有 6 个，我下面展开)：

```
class ActionSchema：    execute_tool： str          # 调 MCP 工具    execute_skill： str         # 跑攻击技能    query_rag： str             # 查 RAG    generate_poc： str          # LLM 自己生成 POC    auth_bypass： str           # 认证绕过测试    complete： str              # 任务完成
```

为啥是这 4-6 个，不是更多也不是更少？

● 少了不行：如果只有 execute\_tool，没法利用技能库;如果只有 execute\_skill，没法处理技能没覆盖的情况

● 多了不行：LLM 选 7 个动作，准确率掉到 60%，工程上不划算

● 6 个是经验值：再多就用 query\_rag + generate\_poc 兜底

3. ActionSchema 的设计

看 agents/orchestrator.py：82-200 的 think()：

```
ACTION_SCHEMA = """你是一个渗透测试调度员。当前状态：- 目标： {target}- 已收集信息： {page_info}- 已尝试： {history}
可选动作：1. execute_tool   - 调用 MCP 工具(适合：通用扫描、nmap、nuclei)2. execute_skill  - 执行攻击技能(适合：已知类型的漏洞)3. query_rag      - 查 RAG 知识库(适合：想参考历史 POC)4. generate_poc   - 自己生成 POC(适合：现有知识都不匹配)5. complete       - 任务完成
请输出严格 JSON：{{  "action"： "..."，  "reasoning"： "..."，  ...}}"""
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXumrYwSuO1mrOdetiaYTHOG57LWLeCCLEtgDiaavGnicUwQ91cAmNdM3X9eS6IiazEcPqQ2nicynEJvygtRF0uc30F7YxSN9V1j4A7hw/640?wx_fmt=png&from=appmsg)

有意思的设计点：

● JSON 严格输出：用大括号包起来，让 LLM 知道要结构化输出

● reasoning 字段必填：强制 LLM 说理由，逼它想清楚再动手 — 这就是 ReAct 的"Reasoning"

● history 字段：把前几轮的执行结果喂回去，让 LLM 不要重复试已经试过的

4. Prompt 怎么写：分层设计

文件：config/prompts\_layered.py(422 行)

这是另一个值得展开的话题 — 分层 Prompt。

传统做法：

```
[巨大的 system prompt][用户 prompt][对话历史][当前问题]
```

问题：每次只改一点点，但整个 prompt 都失效，KV-cache 命中率掉到 30%。

Hati 的做法：

```
[系统层：固定不变，KV-cache 命中] - system_prompt[任务层：本任务不变] - task_prompt[动态层：每轮变化] - dynamic_prompt[结果层：上一轮结果] - last_result
```

为啥这样？因为 LLM 服务端通常做 KV-cache。prompt 前缀不变就命中缓存，省 token 费 + 加速。Hati 跑得便宜(单任务 0.5-1 元)很大程度靠这个。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXulmGp2Oliakuq0ibv7GC0bCRmGCT4FNNCOyChib6XrRoibE5djqBdKt9hrztBSvjTicFaHNFR9Wlgccg5Idlibw0VRoViarHzyg96ws8I/640?wx_fmt=png&from=appmsg)

5. 8 轮迭代：为什么是 8？

这是经验值，不是理论最优。

我跑过 3 轮 / 8 轮 / 20 轮的对比实验：

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXukziauL13o1Q32iaCoZ79MekALp8frEpI0MAEQmoVW7eLqdbJMj7j5Np4wgSRQyZHC2NTMoUI0hrXgBEHt4DXhlWZX7nsWoFA8vU/640?wx_fmt=png&from=appmsg)

为啥不是无限循环？

● 8 轮后边际收益骤降：多数目标的攻击面就那几个，8 轮基本遍历完

● LLM 上下文有限：超过 10 轮，早期信息开始被压缩/遗忘

● 成本：LLM 每次决策都烧钱，8 轮已经是性价比拐点

早停策略：LLM 输出 complete 立即结束(可能 3 轮就停)。8 是上限，不是必跑。

6. 决策解析的容错

文件：agents/orchestrator.py：312-331

LLM 不是 100% 听话的。偶尔会输出：

● "我建议用 sqlmap 测一下 SQL 注入"(自然语言)

● "json\n{...}\n"(代码块包裹)

● "对不起，我无法..."(拒答)

Hati 的容错策略：

```
def _parse_decision(self， response)：    # 1. 优先用正则抓 JSON    json_match = re.search(r'\{.*\}'， response， re.DOTALL)    if json_match：        try：            return json.loads(json_match.group())        except json.JSONDecodeError：            pass
    # 2. JSON 失败 → 关键词匹配    response_lower = response.lower()    if "auth_bypass" in response_lower：        return {"action"： "auth_bypass"}    elif "skill" in response_lower：        return {"action"： "skill_based_attack"}    elif "rag" in response_lower or "poc" in response_lower：        return {"action"： "rag_poc_attack"}    else：        return {"action"： "complete"}  # 兜底
```

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXumar6L0DjMWFRzH4SGcamiblnJ4dbkMbiazRodEQPF1LYibFx9AMYUyRmlRYOIFAhJ2yz2VTTvF77KPJO7LMcDPt2sfhGueiblpX7Y/640?wx_fmt=png&from=appmsg)

为啥不直接 retry？因为 LLM 拒答可能是策略原因(retry 也拒)，关键词匹配虽然粗糙但能跑通，任务不中断。

7. 一个真实的 ReAct 轨迹(完整复现)

目标：http：//testphp.vulnweb.com

第 1 轮

LLM 输入：

```
目标： testphp.vulnweb.com技术栈： PHP， Apache， MySQL端口： 80， 3306已尝试： 无
```

LLM 输出：

```
{  "action"： "execute_skill"，  "skill_name"： "sqli-sql-injection"，  "target_param"： "artist"，  "test_url"： "http：//testphp.vulnweb.com/artists.php？artist=1"，  "reasoning"： "3306 端口开放 + PHP+MySQL，SQL 注入概率高，优先测"}
```

执行结果：

```
请求： GET /artists.php？artist=1' OR '1'='1响应： You have an error in your SQL syntax near '' OR '1'='1'状态码： 200特征匹配： ["SQL syntax"， "MySQL"]
```

判定：✅ 确认 SQL 注入，severity=high，入栈 state["vulnerabilities"]。

第 2 轮

LLM 输入：

```
目标： testphp.vulnweb.com技术栈： PHP， Apache， MySQL已发现： 1 个 SQL 注入 (high)已尝试： sqli 技能
```

LLM 输出：

```
{  "action"： "execute_skill"，  "skill_name"： "xss-cross-site-scripting"，  "test_url"： "http：//testphp.vulnweb.com/search.php？search=<script>alert(1)</script>"，  "reasoning"： "首页有 search 框，可能存在反射型 XSS，顺手测一下"}
```

执行结果：

```
请求： GET /search.php？search=<script>alert(1)</script>响应： <p>Results for <script>alert(1)</script>：</p>...特征匹配： 原样反射
```

判定：✅ 确认反射型 XSS，severity=medium，入栈。

第 3 轮

LLM 输入：

```
目标： testphp.vulnweb.com已发现： SQL 注入(high)， XSS(medium)已尝试： 2 个技能
```

LLM 输出：

```
{  "action"： "complete"，  "reasoning"： "已发现 2 个漏洞，首页没有更多攻击面，任务完成"}
```

任务结束。只跑了 3 轮，不到 4 分钟。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunErHM2rQbyRS34xjXzfd3ntFibxUd2VJvVuxXpMxu8jV6WhMVZSZA4Mbqsv17s7JDC8Uo5pMjTOsyQcLY2WKAnNVp4P9PNib5b0/640?wx_fmt=png&from=appmsg)

8. 反思：这套机制的局限

最后老实说，ReAct 不是银弹。已知问题：

1. 上下文爆炸：超过 10 轮，早期信息被压缩(state/context\_compressor.py 在处理这个)

2. 状态污染：早期错误决策影响后续(LLM 看到错误信息可能误判)

3. LLM 偏置：对热门漏洞类型有偏好(老提 SQL 注入，很少提 SSRF)

4. 8 轮过早收敛：有些目标其实需要更长时间

我们的应对：

● state/context\_compressor.py：对历史结果做摘要

● state/diversity\_injector.py：强制多类型漏洞尝试

● 多模式确认：不依赖 LLM 自评，用特征字符串二次确认

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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