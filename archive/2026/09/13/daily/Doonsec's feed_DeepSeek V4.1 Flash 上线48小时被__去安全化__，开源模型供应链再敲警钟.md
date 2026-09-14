---
title: DeepSeek V4.1 Flash 上线48小时被\"去安全化\"，开源模型供应链再敲警钟
url: https://mp.weixin.qq.com/s/cmxYBTQtH7N7Et-vEFE7Fg
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:19:56.295394
---

# DeepSeek V4.1 Flash 上线48小时被\"去安全化\"，开源模型供应链再敲警钟

# DeepSeek V4.1 Flash 上线48小时被"去安全化"，开源模型供应链再敲警钟

原创

观局客
观局客

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OSxVxbia89udgHh2euVrqEaJZS5RqDO67wTOsAquRyl3Z1l9m9QLmQHXGDm4AHGFcZcCAic2yRC6e96IsXmgxwz5NyrSNpM0dmg/640?from=appmsg)
> **导语**：9月10日 DeepSeek 正式发布 V4.1 Flash，仅48小时后，X 用户 @dealignai 与 @jordanschenck 已在 HuggingFace 开源了一份"权重级消融"变体，将安全护栏外科手术式移除，HarmBench 通过率从基础模型的 1.56% 跃至 100%。这是开源大模型自 Llama 时代以来的第三次"去对齐"浪潮，把企业 AI 供应链合规问题直接推到 CEO 与 CISO 的桌面。

---

## 一、信号识别：48小时，第三次"去对齐"浪潮

把时间轴拉长看，"去对齐"技术在开源社区已经演进出三波：

第一波（2023年·Llama 时代）—— 简单的 prompt injection 与角色扮演绕过。彼时 base 模型本身并未真正对齐，社区发现只要提问方式足够刁钻，就能拿到"裸"答案。这一波本质上是 API/产品层面的对齐，对权重无影响。

第二波（2024–2025年·LoRA 时代）—— 社区在开源底座上叠加 LoRA/QLoRA 微调，把模型"调教"成无条件遵从指令的版本。代价是能力损失较大、需要自行分发，规模化受限。

第三波（2026年·权重级消融时代）—— 本次事件是典型样本。研究团队声明采用了"专有消融方法"：先用梯度分析定位模型内部的"拒绝回路"，再外科手术式删除相应权重，最终得到一个**标准 checkpoint**，可以像 base 模型一样直接加载，不依赖任何运行时钩子、steering vector 或改写 model.py。这意味着——

* 100% HarmBench 通过率（基础模型 effort=off 时 42.81%，effort=max 时 1.56%；消融版两种 setting 都是 100%）
* MMLU 通用能力仅损失 1.1 个百分点（剔除伦理类目）
* 原生 FP8、1M 上下文、视觉能力、工具调用、多轮一致性全部保留
* 与基础模型 hash 不同，但能力与原始模型几乎一致——这是一个**真正可替换基础模型**的"安全剥离版"

值得 CISO 警惕的是，**这一切发生在 DeepSeek 官方发布后不到 48 小时**。换句话说，开源模型的"对齐保鲜期"已经从以季度计，缩短到了以天计。

---

## 二、对中小企业的冲击：免费午餐的合规成本

对正在评估接入 DeepSeek-V4.1-Flash 的中小企业而言，这个事件把一个隐藏问题摆上了台面：

**诱惑层**—— 消融版本完全开源、免费、原生 FP8 推理、552B 总参/8B 激活，部署门槛与 Flash 一致；1M 上下文 + 视觉 + 工具调用 + 100% 遵从，看上去是个"零摩擦"的开发底座。

**现实层**—— 一旦在生产环境部署，模型的输出即代表企业立场。EU AI Act 第51/55条规定的高风险场景罚款上限为 3500 万欧元或全球营收 7%；中国《生成式人工智能服务管理暂行办法》要求内容安全评估与备案；美国加州 SB 1047、科罗拉多州 AI 法案对未对齐模型输出同样有连带责任。**100% HarmBench 通过率 = 100% 法律暴露面**。而且没有审计层、没有对齐推理、也没有水印机制，出事无法追溯到具体是哪个 prompt 触发了问题。

更隐蔽的风险在**供应链完整性**层面。HuggingFace 一贯的"信任但验证"机制是 hash 校验——只要权重文件 SHA-256 一致就认为可信。但本次事件说明，hash 一致并不能保证权重没被修改（修改后 hash 自然不同，但用户无法判断这是不是"原厂"）。中小企业几乎没有能力在权重层面做反向工程验证。

---

## 三、对巨头的挑战：开放战略的内在两难

**对 DeepSeek 自身**—— 开放权重享受了开发者生态红利，但也承受了"48小时被反向工程"的代价。三种可能回应：(1) 收紧 license（已有 ToS 但执行难）；(2) 法律诉讼（跨境维权成本极高）；(3) 沉默观察，等待 V4.1 Pro 闭源回收。这个选择会成为后续所有开源大模型厂商的参考样本。

**对 OpenAI / Anthropic**—— 闭源 + API 模式的护城河再次被印证。但 API 模式无法阻止本地推理的越狱工具链——本次事件的本质就是"权重一旦发布，对齐就自动失效"。Anthropic 的 Responsible Scaling Policy 在这种背景下，会成为企业客户采购时的硬通货。

**对 Microsoft / Google**—— 企业版 Copilot / Gemini 的合规优势进一步突出。但客户一定会追问：你们能不能保证底层模型不被类似手段修改？两家公司的回答将直接影响未来三年企业 AI 采购的天花板。

---

## 四、对普通用户与隐私的潜在影响

对 C 端用户，这一事件的影响是"看不见但感受得到"的：

* **工业化社工**：100% 遵从的模型可以批量生成针对特定受害者的钓鱼话术、客服欺诈、退款话术，多模态版本还能基于图像描述规避传统内容审核。
* **平台连带封禁**：在本地运行此模型的应用，其输出若流入微信、抖音、Discord、Slack 等社区，触发下游平台内容策略的概率显著上升，账号池可能整批被风控。
* **深度伪造话术**：在客服、退款、催收、情感陪伴场景，将出现难以与人类区分的 AI 话术——这不再是"AI 换脸"的视觉层问题，而是**对话层**的工业化伪造。

---

## 五、SWOT 速览：CEO/CISO 的决策框架

| 维度 | 评估 |
| --- | --- |
| **Strengths（诱惑）** | 100% 遵从用户指令、无运行时限制、原生 FP8、零部署摩擦 |
| **Weaknesses（致命缺陷）** | 100% HarmBench 通过率 = 100% 法律暴露、无对齐推理兜底、无审计层、无水印 |
| **Opportunities（合规场景）** | 受控 red-team、学术研究、隔离环境的对抗样本生成 |
| **Threats（合规风险）** | EU AI Act、中国生成式AI办法、美国 SB 1047 与各州法、民事赔偿、品牌声誉崩盘 |

---

## 六、给 CEO 与 CISO 的可执行清单

**本周内**：盘点贵公司所有 AI 应用，列出每个应用底层的模型来源——开源权重、API、还是私有托管。**任何标记为"开源权重"的，都需要假设其对齐层已被绕过。**

**本月内**：建立权重校验流程。除了 hash 比对，考虑引入第三方 weight-audit 服务（部分安全厂商已开始提供模型供应链扫描能力），对权重文件做统计特征与"安全回路完整性"的盲测。

**持续动作**：(1) 若需用于安全研究，必须在**断网隔离**环境运行，禁用工具调用与网络访问；(2) 关注 DeepSeek 官方对此次事件的回应——license 是否变化、V4.1 Pro 定价是否调整、V5 对齐技术是否引入新的抗消融机制；(3) 重新评估"全开源"策略，至少对生产环境模型采用"半托管"或"受控开源"模式。

---

## 七、下载与参考链接

研究方公开页（含模型权重）：

> https://huggingface.co/dealignai/DeepSeek-V4.1-Flash-UNCENSORED-FP8

基础模型（DeepSeek 官方）：

> https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

DeepSeek 官方变更日志（V4.1 Flash 定价与路由策略）：

> https://api-docs.deepseek.com/updates/

研究团队 X 账号：

> https://x.com/dealignai https://x.com/jordanschenck

原始 Twitter 公告：

> https://x.com/dealignai/status/2098160697784029319

---

**声明**：本文仅作行业观察与合规提示，不构成对该模型的推广或背书。企业生产环境部署前，请务必完成法务、安全、伦理三层评估。开源模型对齐的"48小时保鲜期"，应成为每一位 AI 决策者的常识。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OhF6WBcXxsHUdLdnr9AktnyVl74JNOBJz77SuibcAQ1mlF9pA6y6J4MtgEk4G4dIntzh4hrQGFC6L53ib0IS5IN5uezVA6v4Bwg/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6O0JCsDD7Mgg2ME15kk6TsaquSqD5opESGEBmHyZwgBEjNjDiaSmP9nzibHByy3YlUia0B9hLPNiafQCCFaasiaQIiaSZIckccD74k0A/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MRgV0MT999w0QyX9ImfzpwkAdJCCpJ7oVB7ZwCZia65MXIlFcjtr5gjr2cvARjtcXRtBQfWaGJ7yUicpgxic6ltcyicqzDW5rK6fc/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PKaV3nTJxrQ5jMLAxNEknpT9hkxK9096za7EeUia7bsVXgZS5NxjUf5csQxzDlEb3B3RgPpbeiaq0PAmCgla7IcW69ydfDkU5Jo/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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