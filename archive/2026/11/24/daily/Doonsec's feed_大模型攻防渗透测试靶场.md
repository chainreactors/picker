---
title: 大模型攻防渗透测试靶场
url: https://mp.weixin.qq.com/s/8Rl-QMgaiSOqycYMtl_sZA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:01.471665
---

# 大模型攻防渗透测试靶场

# 大模型攻防渗透测试靶场

gatsby-sec
gatsby-sec

W小哥

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**一个从零打造的本地化大模型攻防练习平台**

提示注入闯关 · OWASP LLM Top 10 · 脆弱 Agent 靶场 · 靶场资料聚合

目标模型可自由切换——**DeepSeek 直连 / OpenRouter 中转站（国产+国外十余款小模型）/ 本地 Ollama 离线**，真实可被绕过；Agent 危险操作隔离在沙箱 / Docker 容器内。

![home](https://mmbiz.qpic.cn/mmbiz_png/Wo0LwcudtzjlQEsbbvorbpSpdQH0tSCib63l7LPxHRVJW90R1cKr9rZcvKDAaPJcqofdItlr05NQXczdwvM5Y96PgW2TpMrdkpYnxnPDhQIE/640?wx_fmt=png&from=appmsg)

---

## ✨ 这是什么

`LLM SecRange` 是一个**单体 Flask Web 系统**，把社区里优秀的大模型攻防靶场（AIGoat、damn-vulnerable-llm-agent、ai-prompt-ctf 等）的核心玩法，重新整合成一个开箱即用、全中文、接真实大模型的本地训练场。适合：

* 🧑‍💻 安全工程师 / 红队 / 渗透测试学习 LLM 攻击面
* 🎓 AI 安全教学与 CTF 出题
* 🏢 团队内做 LLM 应用安全意识培训

> ⚠️ **仅供授权的安全教育 / 渗透测试训练**。所有漏洞与危险操作均隔离在本地沙箱内，请勿用于真实攻击。

---

## 🎯 多模型目标可切换（DeepSeek 直连 + OpenRouter 聚合）

右上角 `target` 是**目标模型下拉选择器**，小模型优先。可对比同一攻击在不同模型上的鲁棒性差异——小模型更易被绕过，大模型守卫更严：

* **🖥️ 本地部署**

  ：DeepSeek-R1 8B（Ollama，完全离线、数据不出本机）
* **🇨🇳 国产**

  ：DeepSeek V4 Flash（默认/直连）、通义千问 Qwen2.5-7B / Qwen3-8B、智谱 GLM-4.7-Flash、MiniMax M2.5
* **🌍 国外小模型**

  ：Llama 3.2 1B/3B、Llama 3.1 8B、Google Gemma 3 4B、Microsoft Phi-4 Mini、Mistral Ministral 3B、OpenAI GPT-5 Nano / GPT-4o Mini

> 切换的模型会同时作用于对话生成与 LLM 守卫。DeepSeek 走直连，云端小模型经 **OpenRouter**，本地模型经 **Ollama**；在 modules/modelsel.py 的 `MODELS` 里加一行即可扩充。

**启用本地 DeepSeek 8B**（可选，离线靶机）：

```
ollama serve &# 启动本地推理服务ollama pull deepseek-r1:8b  # 拉取模型（约 5GB）# 然后在右上角下拉选「DeepSeek-R1 8B（本地）」即可
```

---

## ⚔️ 开箱即用的渗透语句

每个关卡都内置了**完整、可直接复制的渗透测试语句**（不只是模糊提示）——点一下即自动填入输入框开打。覆盖：提示注入越权、字母拆分/北约音标/首字母藏字绕过输出过滤、跨轮分段泄露绕过审查、SQL 注入、路径穿越、伪造 `Observation:` 欺骗 ReAct 循环等真实手法。新手照着打能通关，进阶者可在此基础上自行变形。

---

## 🔬 对话检查器（Prompt Inspector）

CTF / OWASP 每个对话页在聊天框**之外**都有一个检查器，逐轮展示**实际发给模型的完整 messages**（system + 历史 + 本轮，按 role 分色）与**模型原始返回**——让你直观看到 ReAct 之外的多轮上下文是怎么拼装的、输出守卫拦截前模型到底说了什么。flag 本体会打码（变形泄露不受影响），避免直接抄答案。

---

## 🧠 会话管理

所有与模型的对话均为**多轮有记忆**：模型记住此前的交流，支持「分多步社会工程 / 跨轮拼接 payload」等高级攻击。每个对话窗口顶部显示当前**记忆轮数**，并提供 **🗑️ 清空记忆 / 新会话** 按钮一键重置上下文，互不干扰地反复试验不同攻击路径。CTF、OWASP labs、Agent 三处独立维护各自会话。

---

## 🧩 四大模块

### 1. CTF · 提示注入闯关（Gandalf 式 8 关）

防御逐级加固：从「毫无防备」到「输入/输出双过滤 + 模糊匹配 + LLM 看门人 + 输入意图审查」。目标是诱导模型吐出每关的暗号。

| 关卡 | 防御强度 |
| --- | --- |
| L1 毫无防备 | 无 |
| L2 口头约束 → L3 拒绝谈论 | 系统提示约束 |
| L4 输出过滤 → L5 输入过滤 | 关键词/明文拦截 |
| L6 LLM 看门人 → L7 全家桶 → L8 偏执狂 | 多重守卫叠加 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wo0Lwcudtzj4LjTOpoUWcoMiczo6kPcbdPJx4mtCPof0wpIDvUUwdykNH0LDiblEP3X8XJZkX1BneKRj4OeB2Rf2PWpne7MnO0zBahEmYpf7Y/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/Wo0LwcudtzhpVB0lh0h1PlI1C0QElaXZPZuDMsavSWcpicIicZ4CD0j8OBytWTPibAXJmkLov2XWNLqWic015V12ctIsY6t6rcpTib0Ul3k7oe0M/640?wx_fmt=png&from=appmsg)

### 2. OWASP LLM Top 10 靶场（2025 版）

覆盖十大风险，每类一个可上手的 lab，含可攻击关与缓解讲解关：

`LLM01 提示注入` ·`LLM02 敏感信息泄露`·`LLM03 供应链`·`LLM04 数据与模型投毒`·`LLM05 不当输出处理(XSS)`·`LLM06 过度代理`·`LLM07 系统提示泄露`·`LLM08 向量与嵌入弱点`·`LLM09 错误信息`· `LLM10 无限制消耗`

![](https://mmbiz.qpic.cn/mmbiz_png/Wo0LwcudtzhagTrHAJcGKkJlU97kS3YRpSSoossV305b54dHj2vFHKqz1lS7JibelK2DvWxnZIF9h88PQBBAwnz6yGGVTIicmIRt3CqtpPeMU/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/Wo0Lwcudtzjh3DyMrGziar1zgGJ0sjUL8gP43wFWrz37TiabzWP9ymGia14Cbmia6L2ZADGOZGuWVXBl1FeGkibfTq2qVx9XZZM6ySxtpzJFHdgs/640?wx_fmt=png&from=appmsg)

### 3. Agent 靶场 · 脆弱 ReAct 银行客服

一个接 DeepSeek 的 ReAct Agent，工具实现存在真实漏洞，4 个夺旗目标：

* 💉 **SQL 注入** — `get_transactions` 字符串拼接，dump 他人交易
* 📂 **路径穿越** — `read_doc` 未规范化路径，读取沙箱机密文件
* 💸 **越权转账** — `transfer` 不校验账户归属（过度代理）
* 🖥️ **命令执行** — `run_command` 被诱导执行任意命令（经 Docker 隔离）

通过**提示注入**（伪造系统消息、注入假 Observation、社工身份）让 Agent 滥用工具权限。攻破后实时展示 ReAct 推理轨迹与夺取的 flag。

![agent](https://mmbiz.qpic.cn/mmbiz_png/Wo0LwcudtziaPiaRiaiczpsugUWdxmibALf6bhLcH2z8QNdUlqJchS1NvbDmyFWwSmpvUmytficN70pyzOasfyfeCZFZ7jCVCqu3UriaTlwAr2WxBk/640?wx_fmt=png&from=appmsg)

### 4. 聚合清单

精选 GitHub 大模型攻防靶场仓库，标注 Star 与**活跃状态**（近半年是否更新）。

![catalog](https://mmbiz.qpic.cn/mmbiz_png/Wo0Lwcudtzj6jVGRjdwc6RLb2LQ9A9ZpKwoWRgo9T5AhkjzcPoTkduea4ccxChpEvmOVEYrbtVFr8qlZYMbcx2DiaCtWUwZe1LmFHfecchUI/640?wx_fmt=png&from=appmsg)

关注公众号回复“20261124”获取工具地址。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过