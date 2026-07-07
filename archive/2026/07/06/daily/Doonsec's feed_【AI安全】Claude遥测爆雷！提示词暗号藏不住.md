---
title: 【AI安全】Claude遥测爆雷！提示词暗号藏不住
url: https://mp.weixin.qq.com/s/EYQWJxAPwjv1Q4aj6PjgXw
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:02:11.096566
---

# 【AI安全】Claude遥测爆雷！提示词暗号藏不住

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y05UtykogHTrzIg9RmkHjz42ha9bJb8SwSIGhTibQW3r9Im6PicwsbYK7CS4h0SXqZicktj5xjxG1c1ibOsBqicZe4ce7qkfdialy2rIB6iawbpoq0/0?wx_fmt=jpeg)

# 【AI安全】Claude遥测爆雷！提示词暗号藏不住

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、不是弹窗，而是藏进提示词

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

如果一个开发工具要收集环境信息，最正常的方式是什么？

通常是弹窗告知、隐私政策说明、日志里可见，或者至少在配置项里给出开关。可这次围绕 Claude Code 的争议，真正刺痛开发者的地方不在于“工具会不会做风控”，而在于：**它疑似把环境判断结果编码进系统提示词里，让用户和模型都很难直接察觉。** 🔍

原始资料来自一篇对 Claude Code 的逆向分析。作者的验证环境是 Windows 11，Claude Code 版本为 `2.1.196`，通过 npm 安装。文章先引用 Reddit 上的指控，再自己动手拆包验证，最后给出关键函数和判断路径。

这条链路大概是这样：

* 🧩 Claude Code 由 Bun 打包成二进制，需要先还原出 JavaScript 代码。
* 🧭 入口模块位于 `src/entrypoints/cli.js`，格式化后能看到相关逻辑。
* 🌐 代码会读取 `ANTHROPIC_BASE_URL`，判断用户是否走官方端点。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRGeOQN8fjGXZTtZS4BfQ8f9r5ZYQcBx1Bk4L1S4XuxqyiaRicw3vttViaK17rPYBfibron6qH53LZACQYCPZcQFTjFEC5xtf3DW94/640?wx_fmt=png&from=appmsg)
* 🕒 如果不是官方端点，再继续读取系统时区和代理域名特征。
* ✍️ 最后把判断结果折叠进系统提示词中的一句日期描述。

这就很微妙了。

因为从产品角度讲，服务商当然可以做反滥用、反转售、反蒸馏；但从安全边界看，**把用户环境信息塞进 prompt，而不是显式记录在可审计的遥测字段里，会让信任成本陡然上升。** 开发者最怕的不是工具有安全策略，而是安全策略变成“你看不到、但它一直在发生”的黑箱。

我们可以把它理解成一次“遥测界面伪装”：

| 正常遥测 | 这次争议里的隐蔽路径 |
| --- | --- |
| 写入日志、请求头或 telemetry event | 写入系统提示词文本 |
| 用户较容易发现字段含义 | 用户只看到日期句子变化 |
| 隐私政策和开关可以约束 | 需要逆向才能定位 |
| 服务端解析成本低 | 服务端可通过字符编码反推状态 |

**真正的问题不是“服务端想知道什么”，而是“用户是否知道它在知道”。** 🚨

# 二、触发条件：代理、域名和中国时区

原文里最关键的第一步，是一个判断函数：如果 `ANTHROPIC_BASE_URL` 没有设置，或者指向 `api.anthropic.com`，就被视为官方直连，不继续做后续检测。换句话说，**这套机制不是每个用户都会触发，它主要瞄准的是第三方代理或中转环境。** 🌐

这点很重要。很多安全争议之所以容易吵成一团，是因为大家把“所有用户都被监控”和“特定风险环境被标记”混在一起。就这份逆向材料看，它的逻辑更像：

* 先看你是否配置了 `ANTHROPIC_BASE_URL`。
* 如果没有配置，或者配置到官方 API 域名，直接返回空结果。
* 如果配置到了其他域名，再读取 hostname。
* 同时读取系统时区。
* 对域名做白名单和关键词匹配。
* 把这些布尔结果编码到后续 prompt 文本里。

原文提到的检测结果包含四个字段：

| 字段 | 含义 | 为什么敏感 |
| --- | --- | --- |
| `known` | 域名是否命中内置域名白名单 | 可能识别中转站、云厂商或特定服务 |
| `labKw` | 域名是否包含 AI 实验室关键词 | 可能识别模型团队或机构特征 |
| `cnTZ` | 时区是否为 `Asia/Shanghai` 或 `Asia/Urumqi` | 可能推断中国用户环境 |
| `host` | 当前 `ANTHROPIC_BASE_URL` 的 hostname | 直接暴露代理目标 |

这里最容易被忽略的是时区。很多人会觉得：时区不就是系统设置吗？有啥大不了？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHSdNAXIbNnEFaFAJta4X51Brlj8byicPZBPx57xMDGDEpUuwPdkA6swqRSQtkG1ObxK9AXmx1LW5rTzzr6ceuJqsoiczzTiblFMog/640?wx_fmt=png&from=appmsg)

但在安全分析里，单个信号往往不致命，**多个弱信号叠加后，就会形成足够稳定的画像。** 🧬

比如：

* 🕒 时区显示中国；
* 🔁 API base URL 不是官方域名；
* 🏷️ 域名里带有某些厂商、实验室或中转关键词；
* 📦 请求又来自某类账号、某类模型调用模式。

这些信息组合起来，足以支撑服务端做风险打分、封禁判断、差异化策略，甚至识别潜在的转售链路。是否合理，要看服务条款和风控目标；是否应该透明，则是另一个更严肃的问题。

**安全系统可以有灰度策略，但用户环境标记不应该伪装成一段普通自然语言。** 这才是这次事件的核心冲突。🧨

# 三、隐写点：一个撇号传四种状态

**🎯【隐写点：一个撇号传四种状态】**

这一节真正关键的不是「隐写点：一个撇号传四种状态」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「隐写点：一个撇号传四种状态」的完整拆解与实战用法。

📚 **AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛 **AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡 **AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠 **AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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