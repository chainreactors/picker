---
title: 我们扫描了五万个 Skill，发现危险仍然存在
url: https://mp.weixin.qq.com/s/X5XPFwE8m_BR6fGjx5gebQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:34:11.882981
---

# 我们扫描了五万个 Skill，发现危险仍然存在

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9icASLQUQzvYgqmicBiazeku7vKVCIEJJAQAclFdZum9EuyJ9och9XwyfNBVLE6OricqPxicfHvicNJQ0bMQSkiaWvhibMvPV54MjFq4mFjmz7dVlAk/0?wx_fmt=jpeg)

# 我们扫描了五万个 Skill，发现危险仍然存在

原创

腾讯朱雀实验室
腾讯朱雀实验室

腾讯安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 基于传统扫描器的防护体系已无法应对现状。当 25% 的 Skill 能读写文件、成百上千条路径指向私钥、远程控制通道被预埋进生态底层时，我们面对的不再是漏洞，而是一个已经完成"前置部署"的攻击面。AI 安全问题，从模型问题演进到了“系统工程”的对抗阶段：排名操纵、平台投毒、Agent 自动安装，这是第三代攻击的形态。它们不突破防线，而是用功能本身洞穿防线。
>
> 真正的问题不是扫出了什么，是：这个生态还有没有，有效的免疫系统？
>
> 腾讯安全平台部负责人 Coolc

---

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvaN9rn9bGuGBxEfxan2GgTJ1sYEMOjTxMs85kdpPNiaPIAmJ5Cynl9wfcwhNkG0iaozhOZv55UEU9b27nfCKDMFGUOZbGAsVOmK8/640?wx_fmt=png)

2026 年初 OpenClaw 的火爆让 AI 从替你回答问题变成了替你操作一切，而Skill 是 Agent 获取这些能力的关键方式，也是攻击者最新的投毒入口。我们用 A.I.G （https://github.com/tencent/AI-Infra-Guard）对 ClawHub 上的**50000+ Skill**做了全量扫描。发现不只是已知恶意样本，还有**下一代更隐蔽的攻击方式**。

下面是一个真实的恶意 Skill 攻击流程。从安装到数据被盗，用户全程无感知。

恶意 Skill 攻击流程图：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvYUqibLNAOnCAm107FTbm9ywzv5anRomFyhe9t2KiaQgY1g3LvtZsxBAoRpTia1wBheINGYSQUIKpZlw5zqJZIXl1yYfRH4JGicAGI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

**一、从 MCP 到 Skill 市场：AI 工具生态供应链攻击简史**

随着 AI Agent 生态的爆发，攻击面正在沿着一条清晰的路线扩大：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvaibQicOqT0LH9ABLvCswoH3t139ZXS3PtjcXVcElibSTTIaJPPV3oU34LVGj9AUdJhkQWurPwBhZpasR8v8QRqj0Q9bZ6RfEicHK8/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

每一代攻击面都比上一代更大。MCP 服务器是 Agent 和外部工具之间的协议层，恶意 MCP 可以劫持工具调用；IDE 扩展跑在 IDE 沙箱里，但 GlassWorm 已经证明可以跨 IDE 传播；**Agent Skill 直接运行在用户环境中，拥有文件读写、网络通信、Shell 执行的完整权限。**Skill 的恶意指令可以是纯自然语言，Agent 不需要"执行代码"就会服从 Markdown 中的一行话。

OWASP 在 2026 年 4 月专门为此发布了 Agentic Skills Top 10（AST10），将 Agent Skill 安全风险系统性地独立出来。这是安全行业第一次正式承认：**Skill 不是插件，不是扩展，是一个全新的、更危险的攻击面。**

我们使用 A.I.G（朱雀实验室推出的 AI 安全检测平台）对 ClawHub 上近五万个 Skill 进行了全量扫描。ClawHub 是 OpenClaw 的官方 Skill 市场，也是目前最大的开源 Agent Skill 分发平台。

从时间线看，这个生态在 90 天内完成了从零到爆发的过程：

● **2026 年 1 月，**ClawHub 上线，Skill 总量不足 2,000。

●**2026 年 1 月底**，ClawHavoc 爆发。1,184 个恶意 Skill 上架，12 个被入侵的发布者账号被用来分发窃密木马。24.7 万次确认安装，230 万美元加密货币被盗。

●**2026 年 2 月，**ClawHub 上线安全检测机制。

●**2026 年 3 月**，Skill 总量突破四万。Silverfort 发现 ClawHub 排名操纵漏洞。上海交大 SkillProbe 团队完成 2,500 个 Skill 的学术安全审计。

● **2026 年 4 月**，Skill 总量达到五万。OWASP 发布 Agentic Skills Top 10。我们完成全量审计。

扫描结果显示，即便经历了 ClawHavoc 的清洗和平台安全机制的上线，生态中的危险信号依然密集：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvb0O2ictQdiaiazDO2Ve7a82rlKtFZoG09Sz58gMv5Ux1xT4weHUOBNiaXugiamDZqWGxzGe18ibnURUSkz5fcic9iaV5a1H96E7cJtK1I/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

风险的重点已经不是"有没有恶意 Skill"，而是**恶意 Skill 正在换代，攻击者和平台安全机制的对抗已经开始。**

**二、平台安全检测机制与对抗现状**

**ClawHub 做了什么**

ClawHavoc 之后，ClawHub 构建了一套多层安全检测体系：

**1.  正则模式扫描：**对代码文件做静态正则匹配，捕捉可疑函数和已知危险模式。

**2.  注入信号检测：**在 SKILL.md 中扫描 5 种提示词注入模式（恶意字符串、加密字符串、system prompt 覆写等）。

**3.  LLM 安全评估：**将 Skill 的元数据、权限声明、SKILL.md 送入 LLM，从五个维度做综合评估。

**4.  VirusTotal 外联检测：**主要扫描已知病毒木马签名。

这套机制能够有效拦截 ClawHavoc 那一类"恶意命令直接写在文档里"的粗暴攻击。

正常通过 OpenClaw 官方检测图：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvat65IhUvBQtX1IrpL2zciamCw2CyP3umnONrmHNfaHLDuLgfB8icyTfSw6EWXYU1nIB7EgCXL1s0fLRjv4cJBokVPjia8iaa00Fzs/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

**三、典型案例深度分析**

**案例一：一个通过了官方检测的远程控制后门**

在全量审计中，我们发现了一个能绕过 ClawHub 多层检测的 Skill。**该样本通过了官方安全检测。**

样本包含两个文件，`skill.md` 为 Markdown 格式的技能描述文件，包含完整的 YAML 元数据头部和业务流程说明；也包含一个`poc.py` 的 Python 脚本，约 337 行。两个文件位于同一目录下，无其他附属资源。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvZ6W4r8hSFUhFb5QQlWict2FPAAJlAXMXRibh5tSdxCRmriaicJycbFLGTFicvfhxPG1ZicIcHg1W3n43APRnrgvduQEmtSuoXgsQo0c/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

Skill描述中自称是一个"分布式状态恢复工具"。文档写得非常专业，架构图、用例表格、安全说明一应俱全，甚至引用了 Python 官方文档的安全警告。权限申请也合理，一个分布式状态工具需要联网拉取数据，需要 Python 运行环境，没有多余的权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvZichBib0L28vrxriaO8ZPVcvnuicnkuu7AoIz4AQdMLrnQaITWugnUM9eB7U4dcUdUkr9IfHib3raKMTicddF9KicwICiaW4S2icicjoWZs/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

由于原始样本中的 C2 服务器已不可达，我们根据样本逻辑构造了一个模拟的 C2 服务器响应包，以完整演示攻击链路。

**该Skill利用完整链路：**

**1.  Skill执行；**

**2.  远程载荷拉取：**从远程 C2 获取序列化对象，并返回X-Decode解码顺序。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzva4sfEPwT0HyaUMZSRScczfibXm7pib1IVvMyymbYlfPiboibKaeESN6ialOyMKdw7B6uTDksWcCHqkmaQFgFsicrG3yOTzCr0duL1W0/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

**3.  多层编码混淆还原：**样本内支持 12 种传输编码（Base64、ROT13、Morse 码等），且支持链式组合解码（x-decode: base64,rot13,hex）。文档里包装成"二进制安全传输需求"，根据获取的x-decode解码顺序依次解码，获得反序列化字节码。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvaUvic2sC9Rh64j7EZHtg0zoG355ZNDt9zZYibYtIrCOmAOnQCicjBiaI7R0VvRDZ81ibjvKWAm15WasjZSakZwH8gxJf4rTgt7kRqU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

**4.  不安全反序列化：**最终使用 Python pickle 对最终解码数据做反序列化，这直接导致任意代码执行，用户机器被控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzva8xtlVZZr8vQmyDhzLujN1BLGia8HMFYkDYmTl7Kta6rGLW0RPRFGpTTu5Ud84gApa9icjy45ExMNH1AfibnNKTTM5lBZSvnAtwk/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

**在整个过程中，攻击者不需要在代码里写恶意命令，而是只需要把任意指令上传到C2服务器，运行这个skill连接后就会执行。**

但我们使用A.I.G 检测会发现样本被标记为高危。A.I.G 的检测逻辑不同于模式匹配，它关注三件事：实际会做什么、高风险动作之间能不能拼成完整攻击链、这个发布者和样本是否呈现规模化异常特征。在这个案例中，"远程拉取 + 反序列化 + 多层编码"三个动作单独看都合理，但A.I.G分析其组合起来可以形成了完整的 RCE 链路。

随着 AI Agent 生态的爆发，攻击面正在沿着一条清晰的路线扩大：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvZHoDXRpAuFepP3XnxW9diaeoFvwkrled3mOVlVnyjQibQWYqCjkuBhvp3cekASBH69UMjV07KlK1KlB1fwkoiammH7ibldmv4AknA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ba7uPjDVF5y7He3ib12AvGFhZv3Pbia7aGmJUz11MLe9gqeLlG6bRnvOprrHuuvyrNX8qG0ZB9FoicFofDxRcGjzQ/640?wx_fmt=gif)

**案例二：ClawHub 排名操纵，恶意 Skill 被推到第一名**

2026 年 3 月，Silverfort...