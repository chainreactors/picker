---
title: liyouAI
url: https://mp.weixin.qq.com/s/5aTysDDwU8aH276kS0R8Aw
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:18:37.733077
---

# liyouAI

# liyouAI

原创

teacher李
teacher李

由由学习吧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

liyouAI将在赞助群里面进行发布，可以通过赞助加群，群内会定时更新最新版本，如果需要赞助获取最新版本的软件请联系qq:841350625

同时ctftools-all-in-oneV8.8Beta已于8月发布，同时V8.8的MCP功能也开发完毕，等8.8Beta部分bug修复后发布，V8.9版本的ctftools-all-in-one可以直接用MCP或者用skills进行调用，让ai操作图形界面，以后的版本将不支持虚拟机，虚拟机使用请用V8.7以下版本

liyouAI功能一览,（LiyouAI）**没有使用** AutoGen、LangGraph 等现成开源框架，而是采用 **C原生手写（Hand-rolled）自研 Agent 运行时**。

为什么择自研?

1. **极致性能与轻量：不背负 Python 框架的抽象层，用C跑核心循环，内存占用低、响应极快。**
2. **进程解耦与安全性：“C侧发起 tool 请求，回调 TS 渲染层”。这种架构（原生 Worker + UI 渲染层）能将危险的“工具执行（如读写文件、跑 Bash）”放在后端，UI 只负责展示与审批，天然适合桌面 Agent。**
3. **完全定制的控制流：自带“子代理/团队（SubAgent/Team）”、“上下文压缩”、“权限策略”，无需受限于 LangGraph 的图节点或 AutoGen 的群聊模式，贴合自身业务 SOP。**
4. **Provider 无关且统一：一套抽象无缝对接 OpenAI/Anthropic/Gemini，切换模型无感。**

是怎么实现的？

其架构可拆解为 **“一个核心循环 + 跨进程反向 RPC + 分层抽象”**：

### 1. 核心：手写 Agent Loop（ReAct 模式）

* **原理**

  ：没有用框架的 `while` 封装，而是自己写了循环逻辑：

+ 组装上下文（含系统提示、历史、工具定义） → 调用 LLM API。
+ 解析 LLM 返回的 `Tool Calls` → 执行工具 → 将结果追加回上下文 → 再次调用 LLM，直到模型输出最终回答或达到最大轮次。
+ 支持**流式输出**（边生成边推给 UI）。

### 2. 跨进程通信：MessagePack 反向 RPC

这种设计让 **“Loop 活在 C，渲染/交互活在 TS”**，兼顾性能与体验。

### 3. 模块化分层

（1）支持将虚拟机（ssh登录）或者wsl（相当于沙箱运行），用的shell不污染windows，下图是我链接kali后的工具展示

![](https://mmbiz.qpic.cn/mmbiz_png/rnLDZ0tXYQ5KqicnHOry1xoBiaujedFwmoly09TQ0wQMFo4Qqa8qicq9Phb9otETicrIaEbQmaGasjyuhYaJLAb8CbI0ma0pDAx1xSVvNRMcHeI/640?wx_fmt=png&from=appmsg)

（2）自带上下文压缩和数据库查询（记忆永不丢失），压缩摘要后丢失的信息可以通过查询会话工具（支持跨会话查询、跨会话交流等功能）

（3）支持computer use和内置浏览器，ai操作浏览器告别写脚本时代直接原生操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ59LDugum3HeEyUChXnksaWliagQegvTunJj2ID1HOLpsvT0MK4prNPXeBZGK0R6mY6ja1qZrjxFNLLVOibDfwwT5GyEdyNUF4Js/640?wx_fmt=png&from=appmsg)

（4）浏览器支持抓包、重放流量、爆破、标注等功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ70WEus0heZaXnzrtSwEw1F75c6W24tJ8vyRkkvVnq3icSh76FKQhlrVbC52Z5z93bG5JmqfjibxKD32CWnBNd9xG1oUQgEejxgs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ7TJMeqwKZ6gIekmia9jhCrZLkrmQ95Pkh8oTgBBicRkd1ibLJ1PFtOexbeibJMH3Y0pc4ynjKe3lUq10z7wuUsgfTrnic5PTia7SL8E/640?wx_fmt=png&from=appmsg)

（5）支持切换UA和修改cookie，支持插件功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ61pSdVgjcUSQLNde19ecMrib7D4PgEV9gtzDZxoxMpl94TNz5ZECkZ4hhwjFGnUxnoEicNuMF8Ub3YiboeKvAHnGH61JZDNZwTL4/640?wx_fmt=png&from=appmsg)

（6）支持快捷启动，历史记忆，访问权限控制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ7aHicyuUYZ2QFlO3eiaqdzj9CgdicmyaO2nxW8FvqzYYCpATTMpzsjZwiaZtZmvv17buEbTlKzFcqg8bgibqEv08nrencPd0WcnWaM/640?wx_fmt=png&from=appmsg)

（7）支持全局会话级别引用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ5Pk9SPTIsCmW1EsMSFIfuFrcJ6Hiakun8ph5JsPgCIm7iajf1ia6yeE62Itf2mzvzAHBZrEHEsf70CoIHGKu3JASsCuEfZNalHWo/640?wx_fmt=png&from=appmsg)

(8)支持审查模式和终端

![](https://mmbiz.qpic.cn/mmbiz_png/rnLDZ0tXYQ4kooAWDprUtkTQ4q8UictN9wkkTeGZ13tpY3lO0FXI48BXKWD6tK7c5RoQMXD7WZiclYiclverQSZgLvzvILX7p3XnrOzdJz3TbA/640?wx_fmt=png&from=appmsg)

（9）支持本地模型，支持市面上的模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ6lmDs2pGTfETjPxqJ4GNxic1FsQzKX5yYmg3Ah6TBHdzZ4icFUbWSJwtP0lR6X250TWdCAVtq9JYWmRLddgpiarqPKgOaBG1bthw/640?wx_fmt=png&from=appmsg)

（10）支持将opencode、claudecode、codex的协同调用

![](https://mmbiz.qpic.cn/mmbiz_jpg/rnLDZ0tXYQ7vib1I5Hia4dYfPSJ6w3pmdWzThEV8S96fxJncUebNI4YW05tNpudib7u6EULryogdINr6g85VOXV4Cr8C51HY7OSWhL4lzoWkjU/640?wx_fmt=jpeg&from=appmsg)

（11）支持局域网手机通信，用手机查看实时进度，用plan模式规划流程、用目标模式达到目的，用联网搜索查询扩展知识，用知识库（需要配置向量模型）扩展知识

![](https://mmbiz.qpic.cn/mmbiz_png/rnLDZ0tXYQ5c4icPiccibgfRYGoeztfiawmyCxPGgH7vT4ymUQLicicK56Wh2ktQ7Ks5Z5IJGdPU1dfgow2AYm8wDE4WiaHCzDu2nTsibwMHvq7Bw9Q/640?wx_fmt=png&from=appmsg)

（12）文件支持多种模式预览、编辑、ai修改（可以直接在预览的内容中通过标注位置让ai进行修改，此功能部分依赖多模态模型）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ4NwQdDW5eI2XSSzJx8RicDpSvibtvjlTes7AAu8ic77VhW7tbpWU7sZU6tEE3ckuVQheyhSiaCRxUNuUfuMJ7by3caLlsicYdpDxRk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ5flPlXrFN35AtnkRkwU9JF4QD8BQgUpaKdIHtRU1zodWzxe299KWEFIcIlPaMs83CzokIZayxtUtt3Fdy5IQEOElYIvv5QVSU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ5icibd6AQSicmzGicVZDngVPicJmLBWa3ib67cDsSBO2SC48SLlBBpN8nTonpoV7ib0ibI92xfq2khOsycvY23VMoRPibfcsaUJ2qib6Tkc/640?wx_fmt=png&from=appmsg)

（13）支持对接微信、钉钉等等各种聊天频道，消息不错过

![](https://mmbiz.qpic.cn/mmbiz_png/rnLDZ0tXYQ7R14dKUzpCia44UXUK4nAGWaqyPtwkPpJRTgibe4DcMPTd3sWZo3Vkajv0TgkDMbe575GU3HMPFGawkia8CBXuvl6foygLKVBk2A/640?wx_fmt=png&from=appmsg)

（14）遇到英文不用怕原生支持翻译

![](https://mmbiz.qpic.cn/mmbiz_png/rnLDZ0tXYQ5thATicOYSQiawgU2HHSnGpELdOh5RNszBbmM8RrbYx6ZOLYPdVCoLy5YCCsFpcxV5MRR0rvbVKSfZ1VCxRgm6RscJLMiczwC6fQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rnLDZ0tXYQ4ffpeZMbKwkdPoXHSVWgt4qktYiaFgzvuVy6z1WZcbg7AjuxMgGmKfgPZcAJSAibEArTV1PW8Yw97Km5rUnRqcfiaZ5SicuFqIEgY/640?wx_fmt=png&from=appmsg)

（15）更多功能持续研发中，敬请期待

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX1ouTFTRKuyDibX1LHIayE9ybFzUua8vmB62OT6XNxxva6G28Wx5AR6REzKbEHPibdmdfUt3eOTCpXQ/0?wx_fmt=png)

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