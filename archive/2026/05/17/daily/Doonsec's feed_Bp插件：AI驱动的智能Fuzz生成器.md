---
title: Bp插件：AI驱动的智能Fuzz生成器
url: https://mp.weixin.qq.com/s/5-fe8mwvj524OSYUpMAIIA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:06:44.530178
---

# Bp插件：AI驱动的智能Fuzz生成器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwaJy7Fd116wnZl7QGdb01m3HiactJrGxUHb1bO6COjf9Ljw0KnX1Ka18mYaicqMewpo49GUCOqfpdVg5gMT6sLDnEJJDClQCSao/0?wx_fmt=jpeg)

# Bp插件：AI驱动的智能Fuzz生成器

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Bp插件：AI驱动的智能Fuzz生成器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  Burp AI Fuzzer 是一款基于大语言模型驱动的 Burp Suite 插件，能自动解析 HTTP 请求上下文，为指定参数**智能生成针对性 Fuzz 字典**。

## 🚀 一句话优势

  让大模型理解请求上下文，**自动生成高质量 Fuzz 字典**，告别手动构建 Payload 列表。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 智能字典生成 | 解析请求上下文，AI 自动生成针对性的 Fuzz Payload |
| 多模板管理 | 内置通用/SQL注入/XSS模板，支持自定义编辑和持久化 |
| 一键标记工具 | 请求编辑器中右键快速为参数添加 § 定界符 |
| Intruder 深度集成 | 支持将生成字典一键发送至 Intruder 作为 Payload 数据源 |
| 配置持久化 | API 配置自动保存至 Burp 全局设置，模板数据独立存储 |

## 📸 运行截图

| 模块 | 说明 | 建议文件名 |
| --- | --- | --- |
| 主界面 | AI Fuzzer 标签页配置区域与生成按钮 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzo1njJUeE6qRnnj4LUx3IoyKZjMHH6skB6V9otIdPSmLsSklec9ia6pbnZBAg6DR5BBCgsIX7QgjEB4ohb8UGybvicQ01aicQsh4/640?wx_fmt=png&from=appmsg) |
|  |  |  |
| Intruder集成 | Payload 类型选择 Extension-generated 并选中 AI Fuzzer | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzMjZsuWNhb7sib9o02f2VR5sDDc6EUqAPoOial9ja5RRsbaXZanUibALHreYibwr9ZAJ7pFaDgEyBlEBQiaYTe8yTU5s7N5eEZU22A/640?wx_fmt=png&from=appmsg) |
| 发送操作 | 右键菜单中 Send to AI Fuzzer 选项 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODw2XGWBPI4pqTIicSYpLjUGv4FlMiavtJCVJOnuuIZyZcuvqe8N9zNXib7WeaDaSCA6WssicQucBcibDTsRLfk8viaibrCl8BibWTnhKAg/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 上下文感知的智能字典生成

  传统 Fuzzer 依赖预设规则或静态字典，而 Burp AI Fuzzer 会将完整的 HTTP 请求发送给大模型，让 LLM 理解参数的**上下文含义**（例如判断参数是用户 ID、搜索关键词还是文件路径），然后生成针对性的 Payload。内置底层提示词约束，确保 AI 仅输出纯净的 Payload 列表，不会混入解释性文字或格式干扰。支持 OpenAI 和 Claude 等主流模型，你只需配置好 API 地址和密钥即可使用。

### 2. 多模板管理与灵活扩展

  插件预置了 **通用、SQL 注入、XSS** 三类提示词模板，覆盖最常用场景。同时支持用户**新增、编辑和删除自定义模板**，所有模板数据持久化在本地 JSON 文件中，方便迁移和备份。这意味着你可以针对特定业务场景（如 JWT 参数、文件上传接口）编写专属 Fuzz 策略，并在团队中共享。

### 3. 与 Burp Intruder 的无缝集成

  在请求编辑区使用 `§` 标记要测试的位置后，点击“生成 AI 字典”即可自动填充 Payload 列表。再点击“发送至 Intruder”，插件会*同步请求与 Payload* 到 Intruder 模块。在 Intruder 的 Payloads 选项卡中，只需将 Payload 类型设置为 *Extension-generated*，即可将 AI 生成的数据直接应用于爆破任务，无需手动复制粘贴。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Maven 项目结构 | 使用 Maven 管理 Java 依赖 | 编译打包简单，依赖清晰 |
| 提示词模板机制 | 模板数据存储在独立 JSON 文件 | 支持自定义模板，方便迁移和备份 |
| Burp 全局设置持久化 | API 配置自动保存至 Burp 设置 | 重启 Burp 后无需重新配置 |
| Extender API 集成 | 作为 Intruder 自定义 Payload 数据源 | 原生集成，操作流畅 |
| 右键菜单集成 | 通过右键 Send to AI Fuzzer 快速发送请求 | 操作路径短，符合 Burp 用户习惯 |

## 📖 使用指南

① **准备工作** 执行 `mvn clean package` 编译项目，在 `target/` 目录下找到 `ai-fuzzer-1.0-SNAPSHOT-jar-with-dependencies.jar`。打开 Burp Suite，进入 **Extensions → Installed → Add**，选择 Java 类型并加载该 JAR 文件。切换到 AI Fuzzer 标签页，填写你的 API Key、Base URL 和模型名称，点击 **保存配置** 并 **测试连接**。

② **核心操作** 在 Burp 的 Proxy、Repeater 或其他模块中，右键点击请求，选择 *Send to AI Fuzzer*。在插件编辑框中，使用 `§` 包裹你想测试的参数值，例如 `id=§1001§`。选择合适的提示词模板（通用/SQL注入/XSS），点击 **生成 AI 字典**，Payload 列表将自动填充。然后点击 **发送至 Intruder**，插件会自动同步请求和 Payload。

③ **结果查看** 切换到 Intruder 模块，在 Payloads 选项卡中确认 Payload type 为 **Extension-generated**，并选中 *AI Fuzzer Generated*。启动攻击后，Intruder 会使用 AI 生成的字典对标记位置进行自动化 Fuzz 测试。所有攻击结果将按 Burp 原生方式展示，你可以通过长度、状态码等字段快速筛选出异常响应。

## 📖 项目地址

```
https://github.com/238469/burp-ai-fuzzer
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |
| --- | --- |

### 推荐阅读

✦ ✦ ✦

| [渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485592&idx=1&sn=818004a6d625c4c4112ce73b83433854&scene=21#wechat_redirect) |
| --- |
| [AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485309&idx=1&sn=292afbe37fb95c64f33470f915b0c54e&scene=21#wechat_redirect) |
| [JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247486181&idx=1&sn=3ace47da643c72cec0d615aeccb955ac&scene=21#wechat_redirect) |
| [上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485488&idx=1&sn=a37acb031febe69db608de53ddee5732&scene=21#wechat_redirect) |
| [AI 原生安全测试平台(CyberStrikeAI)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485208&idx=1&sn=b5181181c1e0800124e3e099706ef2ef&scene=21#wechat_redirect) |
| [多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485805&idx=1&sn=8f374a239135f6a753d5cce887f8318b&scene=21#wechat_redirect) |
| [基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485314&idx=1&sn=56082cd314311ffc15cc0bcf03a395e2&scene=21#wechat_redirect) |
| [基于AI的自主渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485127&idx=1&sn=b5eb3fdc1cc23976011e2bca396c1bc7&scene=21#wechat_redirect) |

✦ ✦ ✦

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

0x八月

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

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