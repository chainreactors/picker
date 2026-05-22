---
title: Hx0 数据卫士上线：浏览器里的敏感信息扫描与输入防泄漏工具
url: https://mp.weixin.qq.com/s/wb3MhH1rhBnyjkMcg875IA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:58:40.675161
---

# Hx0 数据卫士上线：浏览器里的敏感信息扫描与输入防泄漏工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rkE16nqDZNW2SuFFVg3X0QBUKAkgcib2HTK5GR6sS7jKbJJxfnkI0ViaTwOicj54INX0Ew69YMiaAtpuRoW9FEwm6V5X7LgNo5h8zU4N0ricVic50/0?wx_fmt=jpeg)

# Hx0 数据卫士上线：浏览器里的敏感信息扫描与输入防泄漏工具

原创

asaotomo
asaotomo

Hx0战队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

你可能不是故意泄漏，只是复制得太顺手

你有没有把日志、配置文件、接口返回、报错堆栈直接复制进 AI 对话框？

很多时候，我们只是想让 AI 帮忙分析问题，却可能顺手把 API Key、数据库连接串、客户手机号、内网地址一起带了进去。内容一旦发出，往往很难再撤回。

同样的问题也出现在前端页面里：有些脚本、注释、接口路径、调试信息，看起来不起眼，却可能暴露出不该公开的线索。

所以我们做了Hx0 数据卫士。

它是一款浏览器侧的本地敏感信息扫描与输入防泄漏扩展。简单说，它做两件事：

往外看：扫描当前页面、脚本和接口路径里的敏感信息与暴露面线索；

往里守：在你向网页输入框、AI 对话框、在线文档粘贴或发送内容前，提醒并拦截可能的敏感信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWOLqSiaGb5l5J3BeMShZhC11OZaguH1VPdWaMIgicSoibDgBFcOh4F9JG1lDKnicyUZmLafbhyn3R77GfdKBXYVJtvmPW9tgbTIibQ/640?wx_fmt=png&from=appmsg)

它不是为了制造焦虑，也不是替代正式渗透测试、代码审计或合规结论。它更像一个轻量的日常安全助手：在你复制、粘贴、扫描、导出报告之前，先帮你多看一眼。

---

# Hx0 数据卫士是什么？

Hx0 数据卫士（Hx0 DataGuard）是 Hx0 战队打造的一款浏览器扩展，面向个人办公防护、开发联调自查、授权安全测试和报告留痕场景。

它的核心链路可以概括为：

> **Scan → Detect → Guard → Report**扫描见风险，输入守边界，报告可研判。

目前，Hx0 数据卫士已在Chrome 应用商店正式上线，Firefox 版已提交 AMO 审核。无法访问商店的用户，也可以通过 Gitee 或 GitHub Releases 获取离线安装包。

项目地址：https://github.com/asaotomo/Hx0-DataGuard

产品官网：https://www.hx0.store/products/dataguard

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWssOwoPicg8tWCVo0B6n4ERQlNqOqJ5DFJ3xibtE5eyRdjjA3lS1CMCicVzklhOkPcKZiaJUzrnDEWwVWbuicjVqSriaUurV4Wc05Pc/640?wx_fmt=png&from=appmsg)

---

# 它主要守住两个入口

## 入口一：网页页面

前端页面、外链脚本、注释、路由片段、接口路径中，可能残留测试 Key、调试接口、内网地址、Webhook、令牌或其他敏感线索。

Hx0 数据卫士可以在授权范围内，对当前页面进行本地扫描，帮助你快速发现这些可疑点，并以结构化方式展示命中来源、风险等级和上下文，方便人工复核。

## 入口二：网页输入框

当你把日志、配置文件、工单内容、客户资料、接口参数复制到 AI 对话框、在线文档或其他网页输入框时，里面可能混入敏感内容。

Hx0 数据卫士可以在输入、粘贴和发送前进行检测。命中后，它会根据你设置的拦截强度，进行轻提醒、居中确认、阻止发送或一键脱敏。

一句话总结：

> **页面往外扫，输入往里守。**

---

# 它解决哪些真实问题？

| 常见场景 | 数据卫士怎么帮你 |
| --- | --- |
| 和 AI 对话时不小心粘贴了 Key、连接串、客户手机号 | 在发送前识别敏感内容，提醒、拦截或一键脱敏 |
| 授权网站前端页面里残留明文密钥、调试接口、内网地址 | 一键扫描 DOM、脚本、注释和接口路径，输出命中上下文 |
| 外链 JS 中暴露了 API、Webhook 或可疑路径 | 提取路径资产，可选进一步 HTTP 探测验证 |
| 扫描结果需要交给开发或甲方整改 | 导出 HTML / Markdown / JSON 报告 |
| 不希望检测工具把页面内容上传到云端 | 本地计算优先，默认流程中不上传整页正文 |

> **说明**：本工具输出仅供辅助研判与安全自检，不能替代正式渗透测试、代码审计或合规结论。扫描和 HTTP 探测能力请仅在授权系统、内部资产或靶场环境中使用。

---

# 场景一：与 AI 对话前，先拦一下敏感信息

现在很多人会把报错、日志、配置、接口返回直接丢给 AI 分析。效率确实高，但风险也明显：

* API Key 混在配置里；
* 数据库连接串混在日志里；
* 客户手机号、身份证号混在测试数据里；
* 内网 IP、接口地址混在报错堆栈里；
* Token、Cookie、Authorization 头混在请求片段里。

Hx0 数据卫士会在你输入或粘贴内容后进行检测。命中敏感内容时，它可以在发送前给出提醒，必要时弹出居中确认框，避免你顺手把不该发的内容发出去。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUWJB18rhKSHDLfeloOGMqrALUBcVN2qkzkZicDvhBwEEDZsn341RgLe10ickIOOrrbhzO7hO6EfbnG3Q4HYVLkSds5RUBbbX2xM/640?wx_fmt=png&from=appmsg)

如果你希望继续发送，也可以先使用一键脱敏，把正文中的同类敏感内容替换为安全占位文本，再确认提交。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNWl09dW376Z6hQuB7ABSOlq4FxfuN4yyeQXbdNKMibwkkZF5yWZufu1bNA4via6kohU4UngRRNMwsEjfQE9RH44Fib0vtfnl5WNu8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVORd7Tfwj8UMRfBicEdDwA2AAEicMqQd3rCkib1jsVUXG27mjctr1pNyhAo7KYMliaicxyH4Kk8HltDevQ8n6mxA5Z87pObdnIC2EU/640?wx_fmt=png&from=appmsg)

这类能力尤其适合经常使用 AI 办公、AI 编程助手、在线工单、云文档和内部协作平台的用户。

---

# 场景二：授权测试中，梳理前端暴露面

在已获得授权的测试范围内，打开目标页面，点击「扫描当前页面敏感信息和 API」，Hx0 数据卫士会从当前页面出发，分析 DOM、注释、内联脚本、外链脚本、运行时请求和可疑路径。

它不会直接告诉你“这里一定存在漏洞”，而是把可能需要关注的线索结构化展示出来，让安全人员或开发人员进一步判断。

扫描过程中，工具会尽快返回页面快扫结果，并继续补充外链脚本和路径资产，最终合并到同一份报告里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWNfibQibRUwtRp5IcwAgROl1MYhhctMvZXU6kkOpO4Rex1CQjzrVgyU1n35XhEfrxdK9dk3m4cFhics45R1oiaDXwbHBmj3UQiaXWM/640?wx_fmt=png&from=appmsg)

常见命中包括：

* 明文密钥、Token、AccessKey；
* 手机号、身份证号、邮箱等个人信息样例；
* 内网地址、内部主机名、测试域名；
* 管理接口、调试接口、Webhook；
* SourceMap、路由片段、隐藏注释；
* 响应头中的服务端指纹或内部信息。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNXdBJiaIiaPu1nia4KnFYncliay0gc1xyuY8ZBvQRGdT6ZDqLY607vguTdnfJtmvI7AQpp9fsbGXib7V4Dhxj3xMyE7Y4jWPdQlhlq8/640?wx_fmt=png&from=appmsg)

需要强调的是：这些结果是线索系统，不是最终结论。真实安全判断仍需要结合上下文、授权边界和人工复核。

---

# 场景三：开发联调前，快速自查

很多敏感信息不是“被攻击出来的”，而是开发、联调、测试过程中无意留下的：

* 测试环境地址没有清理；
* 临时 Token 写进了前端；
* 调试接口忘记下线；
* 示例数据里混入真实号码；
* 外链脚本里留下了历史 API 路径。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUoeptFJCib2CIDh8p7JDDBL3KkIv7iayopZ0M0AzY31fXT8TCaMSPRXvgyP7VBLsglHetnK5ULAr93TzZ8O18Y2b4ViaNnhWM9wQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNWAKg9WcGRkXJLSs65KwicoqcqOSBP3clWnkxMpFK9MFkhZCNQiaZfjKaicMCEic61IjgmibdDThOaAFugia8WjicUnShFkaOBfJ56PHY/640?wx_fmt=png&from=appmsg)

上线前或联调阶段，对页面跑一遍扫描，可以更早发现这些问题。与其等上线后被别人扫到，不如在自己发布前先看一遍。

这一点对个人开发者、小团队、内部系统、CTF 靶场和临时项目都很实用。

---

# 场景四：安全报告留痕与整改闭环

安全发现不能只停留在“我看到了”。真正进入整改流程时，往往需要一份可以交付、可以复核、可以留痕的报告。

Hx0 数据卫士支持导出：

HTML：适合直接阅读和审计归档；

Markdown：适合工单、知识库、项目文档流转；

JSON：适合二次处理或接入其他内部流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWjicX4RRyUD1myQaP9uR9vreOmE5AeBrJTm2g5wTFguhLvcqfuhpruiahABfzTkS9rPLPQEyjZkVohKAjGmwK6OzxRxlmZu33bM/640?wx_fmt=png&from=appmsg)

报告中会尽量保留命中类型、风险等级、来源、上下文和扫描状态，方便后续形成「发现 → 研判 → 修复 → 留痕」的闭环。

> 导出的报告可能包含敏感上下文，请按照组织内部规范保存和流转。

---

# 页面扫描能力：先快出结果，再渐进补全

Hx0 数据卫士的页面检测采用「先快出结果，再渐进补全」的策略。

页面快扫会尽快返回，外链脚本和路径资产随后补入同一份合并报告。这样既不会让用户长时间等待，也能在预算允许的情况下尽量补齐更多线索。

主要扫描能力包括：

动态 DOM 扫描：采集页面文本、内联脚本、隐藏注释和后续插入节点；

脚本与路径资产分析：分析外链脚本、SourceMap 线索、路由片段和请求调用；

基础反混淆预处理：对常见 Base64 文本、简单字符串拼接和字典式隐藏内容进行轻量还原；

响应头指纹分析：被动识别Server、X-Powered-By、内部主机名等信息泄露线索；

运行时请求视角：结合动态探针，补全静态扫描盲区。

设置中提供四种扫描模式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNV3ose8hZaXWwJVZiaPCghyBGZD6HaI1XsCCByAbEynicrianCwsUTV5nKHyU21e2ePFjwZfc6O0cndY75Mgia80UY27R8swn83rNU/640?wx_fmt=png&from=appmsg)

| 模式 | 适用场景 |
| --- | --- |
| **快速** | 巨大页面或日常初筛，最小预算 |
| **性能** | 默认均衡，兼顾速度、覆盖和资源占用 |
| **兼容** | 慢站点、内网或不稳定网络，降低并发 |
| **全面** | 覆盖更多脚本和内容，耗时与资源占用更高 |

报告状态说明：

| 状态 | 含义 |
| --- | --- |
| **complete** | 预算内任务完成 |
| **partial** | 部分脚本因权限、CORS、证书、超时或体积限制被跳过，页面快扫结果仍有效 |
| **failed** | 核心流程未能完成 |

---

# 输入防泄漏：提醒、拦截和一键脱敏

输入防泄漏功能覆盖常见网页输入框，登录页和注册页默认排除，减少对正常账号密码输入流程的干扰。

主面板中有两个独立开关：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVgThPkGFZLqjx3QJ3uFHybibSlMs3RyW4yPMVApB8TicLtVayiayMgJJKk9X6pEAJ6eYHkuveDxib28gk1GUpo9MZicH2gkzwrtEPY/640?wx_fmt=png&from=appmsg)

| 开关 | 作用 |
| --- | --- |
| **输入与发送监测** | 监测输入框内已有文本；输入停顿约 1 秒后提醒；点击发送、按 Enter 或提交表单时，根据强度决定是否拦截 |
| **剪切板粘贴监测** | 在 `Ctrl+V` 写入输入框之前检查剪贴板；命中后一律弹出居中确认框 |

提醒与拦截力度可以在侧栏「设置」中选择：

| 强度 | 说明 |
| --- | --- |
| **轻提醒** | 主要检测高危规则，多为右上角提醒，一般不拦发送 |
| **标准（默认）** | 高危 + 中危规则；勾选「是否拦截」的规则会在发送时居中拦截 |
| **强拦截** | 高 / 中 / 低危规则；较严重命中常在发送时居中拦截 |

如果开启「剪切板粘贴监测」，粘贴命中后一律会出现居中确认框，支持：

* 一键脱敏
* 仍粘贴原文
* 取消粘贴

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVBOuOeygicFpwQD2hApOGicK6m6tG8ZOX9BtyibtFH7oiaJZMq97mrJlAibkfVD3pibZbxFr2ia3a4XicTKB1YPUObpDFNKpqPA6EUCLo/640?wx_fmt=png&from=appmsg)

用户确认后的动作，会记录在侧栏「输入防泄漏」日志中，便于本机复盘。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNXshe0k6HthWHFd0iaWDj1AYEGnzrVo6yaVoKBWrXULgXFN6AARgsNwLxabaANib4l36lSRmPLOldGLJsLFQtsBUnR7RGKVCibF1g/640?wx_fmt=png&from=appmsg)

如果某些内部站点你确定安全，也可以使用：

白名单：长期跳过某域名；

免打扰：当前站点 24 小时内不再提示。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVR5vxApEq1H2YzNAKWDxyibyd2oyNyPewIVx5icVQeCkb2d73pv9ib12QCJRp5yKaH0QhPgKUV6cko1GQ6x1ANF7dtUnMXc20E7c/640?wx_fmt=png&from=appmsg)

推荐配置：

> **输入与发送监测：开启****剪切板粘贴监测：开启****拦截力度：标准**

---

# 侧栏工作台：真正的研判主界面

弹窗适合快速开关和发起任务，侧栏更适合做完整研判。

| 模块 | 功能 |
| --- | --- |
| **总览** | 最近任务、风险统计、扫描阶段与实时耗时 |
| **页面敏感信息** | 按规则、风险和来源查看 DOM、注释、脚本片段中的命中 |
| **JS 泄漏与 API 检测** | 脚本提取路径、运行时请求和可选 HTTP 探测结果 |
| **规则中心** | 内置 + 自定义规则，支持搜索、分类开关、导入导出 |
| **输入防泄漏日志** | 复盘最近拦截、脱敏或放行动作，保存在本机 |
| **设置** | 扫描模式、拦截力度、白名单、用户 ID、报告清理等 |
| **报告** | 预览并导出 HTML、Markdown 或 JSON |

规则中心内置密钥、令牌、个人信息、网络资产、API/Webhook、AI Key 等类别规则，也支持自定义表达式、flags、分类、风险等级和替换展示文本。

报告层会对同一规则类型和同一原始命中值进行去重，减少 HTML 注释、动态节点和脚本片段多次触发导致的重复告警。

---

# API 与网络探测：只在授权范围内使用

除了本地扫描，Hx0 数据卫士也支持对提取到的 API 或可疑路径进行进一步探测。

使用流程大致是：

* 在 JS 泄漏或 API 检测视图中选择单条或批量 URL；
* 确认请求参数；
* 可选设置 GET / POST、自定义请求头、重定向、请求 Host / Origin 重写；
* 查看响应摘要，包括状态码、最终 URL、响应头、响应片段、耗时和包大小。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVVTIh2WOtelAM07YZwDJyWUukwIk47FwLPKNOuKDylzXxmP50kOApqjTAyHLvBibpHwPGUQLmaRzBjJFmialKLtAvxdByyESF34/640?wx_fmt=png&from=appmsg)

这类能力会产生真实网络请求，因此请务必只在自己拥有授权的系统、内部资产或靶场中使用。

---

# 为什么强调本地优先？

安全工具自己也应该尽量降低额外风险。

Hx0 数据卫士...