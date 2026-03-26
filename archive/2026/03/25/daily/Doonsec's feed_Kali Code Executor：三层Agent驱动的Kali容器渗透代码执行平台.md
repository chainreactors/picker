---
title: Kali Code Executor：三层Agent驱动的Kali容器渗透代码执行平台
url: https://mp.weixin.qq.com/s/9-dEbCf-fPa8FxjknE9svg
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:25:23.145692
---

# Kali Code Executor：三层Agent驱动的Kali容器渗透代码执行平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODw5VicyDkPZTbxxZkmibaqFibibRFlabrWYjqib1u48kqm56ZY9wBpgQqRIo9kdxpjuSicH79VK0nuoNEoSD6xOO9SIjMkK02LkrL7icg/0?wx_fmt=jpeg)

# Kali Code Executor：三层Agent驱动的Kali容器渗透代码执行平台

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# Kali Code Executor：三层Agent驱动的Kali容器渗透代码执行平台

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  Kali Code Executor是一款基于**三层Agent架构**的容器化代码执行系统，专为渗透测试人员设计，可在Kali Linux Docker容器中自动调度并安全执行50+渗透测试工具。

## 🚀 一句话优势

  通过三层Agent智能路由，一句话就能让系统自动完成从任务分类到工具执行的全流程，省去手动选工具和写命令的麻烦。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 三层Agent架构 | 任务分类器+领域专家+工具执行器自动路由 |
| 渗透工具执行 | 支持nmap、sqlmap、metasploit等50+主流工具 |
| 容器化安全运行 | 在隔离的Kali Linux Docker中执行所有操作 |
| 实时流式输出 | Web界面实时显示执行过程与结果 |
| 自定义代码执行 | 直接编写并运行Python代码，支持对话记忆 |

## ✨ 核心亮点

### 1. 三层Agent智能路由系统

  系统将用户指令先交给**Level 1 Agent**进行任务分类，再由**Level 2 Agent**选择对应安全测试领域，最后由**Level 3 Agent**在Docker中具体执行工具。这种分层设计让复杂渗透任务实现自动化链路，减少人为决策错误。*即使你只说“扫描目标80端口的Web漏洞”，系统也能一步步完成工具选择与执行*。

### 2. 容器化安全执行环境

  所有渗透工具和自定义代码都在独立的Kali Linux Docker容器中运行，天然隔离主机环境，避免工具冲突或意外破坏。支持nmap、sqlmap、metasploit等50+工具开箱即用，同时新增自定义Python代码执行能力。*这让你在做高风险测试时更加安心*。

### 3. Web界面与对话记忆

  通过WebSocket实现实时流式输出，无需刷新即可看到执行进度；支持完整对话历史记忆，可连续追问“基于刚才的扫描结果继续深入”。你还能一键导出JSON格式的历史记录，方便后续整理报告或团队协作。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| 三层Agent架构 | Level1分类 + Level2领域专家 + Level3工具执行器 | 任务路由清晰，易于扩展新领域和新工具 |
| Docker容器执行 | 使用docker\_executor在Kali环境中运行命令 | 环境隔离、安全可控、工具版本一致 |
| LangChain风格Agent | 结合OpenAI模型实现智能决策 | 自然语言输入即可驱动工具链 |
| WebSocket实时通信 | 前端自动推送执行流式输出 | 用户体验接近本地终端，操作直观 |
| 模块化工具定义 | tools.py与tools\_manuals.py分离 | 方便维护工具手册与新增工具 |

## 📖 使用指南

① **准备工作：** 确保Kali Linux Docker容器正在运行，克隆项目后执行 **pip install -r requirements.txt**，并在项目根目录创建 **.env** 文件，填入 `DOCKER_NAME`、`OPENAI_API_KEY`、`OPENAI_BASE_URL` 和 `MODEL_NAME`。

② **核心操作：** 运行 **python main.py** 启动服务，浏览器访问 *http://localhost:8000*，在对话框中直接输入渗透任务，如“扫描192.168.1.1的开放端口”或“对http://example.com进行SQL注入测试”，系统会自动路由并执行。

③ **结果查看：** 实时查看流式输出结果，支持输入“history”或“历史”查看完整对话记录，点击导出按钮可生成 **JSON** 文件，或使用“clear”清空历史。

## 📖 项目地址

```
https://github.com/ALKAERR/Kali_Hack_Agent
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwPr8UpJD9OuY73Pzy9eXu2BVToMrV0kP6GrqGroWjhE0k5TXvDx2MGoXjHrcOU9FeF8wia7NhFXXv1iaTz0MnQ4pJguN7DwiaeV4/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODzCtog7ElLXnrLg7t9j99DftdLLjjVKFwP6unsUPX1EquflicE51wMFjB3zIBWLf6W3qFHA5modicNn3XbwJE8roDq7njXZRfjuo/640?wx_fmt=jpeg&from=appmsg) |

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