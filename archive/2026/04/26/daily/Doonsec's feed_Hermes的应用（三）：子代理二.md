---
title: Hermes的应用（三）：子代理二
url: https://mp.weixin.qq.com/s/IQ8jacoqA6Pm3A8X1jvjPw
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:03:00.860908
---

# Hermes的应用（三）：子代理二

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2PhZXrB0gN7KuDKuIVbpLlRuFEr8a4g6KnsJrhwKCEOJcHSbOQlUmRVTJMic2thO7CpNYakXzqViaFC6FB0ReXDMPWz84ESt1FRg5Cn9xZcG0/0?wx_fmt=jpeg)

# Hermes的应用（三）：子代理二

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

上篇，调动了三个子代理开展工作，但被评判为三个独立无关联的子代理，虽同步但无联动。今天，我们来试个有联动的子代理。

一、设计题目

**任务：构建一个“AI大模型性能实时对比仪表板”系统，要求三个子代理按顺序协作完成，最终交付一个可通过 Docker 一键启动的完整项目。**

**具体子任务分工如下：**

**Agent A（数据分析师）**

* 从网上采集 2025 年最新的主流大模型基准测试数据（至少包含 Llama 3.3、Qwen2.5、Claude 3.5 家族中的代表模型）。
* 评测维度至少包含：GSM8K、MATH、MMLU、HumanEval、GPQA。
* 将数据清洗并整理成统一的 JSON 文件，保存到共享目录 `./shared/model_data.json`。
* 数据就绪后，在 `./shared/` 下创建一个 `data_ready.signal` 信号文件。

**Agent B（后端开发者）**

* 监听 `data_ready.signal` 文件，一旦存在即开始工作。
* 使用 Python FastAPI 读取 `model_data.json`，构建 RESTful API。
* API 必须支持：获取所有模型列表、按模型名模糊搜索、一次请求返回多个模型的对比数据。
* API 应自动生成 Swagger 文档（`/docs`），方便前端查阅。
* 完成后端后，在 `./shared/` 下创建 `backend_ready.signal` 信号文件。

**Agent C（前端开发者）**

* 监听 `backend_ready.signal` 文件，一旦存在即开始工作。
* 使用 React + 可视化库（如 Recharts 或 D3）构建仪表板界面。
* 界面应包含：模型多选器、多指标柱状图或雷达图对比、数据来源说明。
* 通过调用 Agent B 的后端 API 获取数据。
* 为整个项目编写 README 和 API 使用文档。
* 提供 `docker-compose.yml`，确保最终可通过 `docker-compose up` 一键启动。

**协作要求：**

* Agent A 和 Agent B 必须协调好 JSON 字段结构；如果格式有分歧，允许 Agent B 在等待期间向 Agent A 提出修改要求。
* Agent B 和 Agent C 通过自动生成的 API 文档对齐接口格式。
* 所有代理的日志或代码注释中应体现出对前一阶段输出的依赖（例如引用共享文件路径或 API endpoint）。
* 整个流程要保证解耦：任一环节失败可以单独重跑，不影响已完成的部分。

**最终交付标准：**

* 在项目根目录执行 `docker-compose up` 后，浏览器打开能正确展示包含真实数据的对比图表。
* 共享目录中保留完整的信号文件和中间产物，以证明协作链条。
* 生成一份协作过程摘要，说明各代理之间的数据传递与触发顺序。

二、运行过程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN51q0ItYjUTfN6xianlJCR1Rtic3BgSOj1rA1sENmWAo2dSIpvEuvZfWTRXNtSPw2Ocib7t4EcIQRrWib2HSqicOxU6lyylQtM8M2KQ/640?wx_fmt=png&from=appmsg)

### 图1：任务解析与全局规划

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN6mU03wMHsF3FwHE7WBBCaSmOT7sl7NichZksdlotgTXgZ1RicsNiaiaTwpAFchnwKb2ExKDwuRfE7zSkgNyQQkT8HRSCBySGc0jaY/640?wx_fmt=png&from=appmsg)

* **图2**：**为 Agent A 设计具体指令**，包括数据采集、格式、文件路径和信号创建

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6ibG7YgGia3yEelRoPZFt3H1icbj58G5AFwyP1NlCicQicAoVcpf0z9WN7hwHqSNzNbFFicdVdtCf6WkiaxWO2Z71f560ic0l53kwmS80/640?wx_fmt=png&from=appmsg)

* **图3**：信号驱动的 Agent B 顺利执行

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN6FnrQrT9GfYSYegQclTXLSZxCZHULYuPuZew24OfLqojibNicV9rWYfibn9W3duIjEic7jQwxple00icibvciasZkSPEtwFiaajRynLtc/640?wx_fmt=png&from=appmsg)

* **图4**：启动最终环节 Agent C

Deepseek V4评判如下：

这四张图完整记录了 Hermes 主代理从接收任务到逐步调度子代理 A、B、C 的全过程，清晰展现了**多代理协作中的任务拆分、依赖传递与逐级启动机制**。以下是逐图分析。

### 🏞️ 图1：任务解析与全局规划

**解决的问题**

* 主代理接收到复杂任务后，**解析任务要求**，明确三个子代理的角色、依赖顺序（A→B→C）和最终交付标准。
* **建立协作基础**：决定使用信号文件、共享目录 `./shared/`、Docker Compose 一键启动等核心机制。
* **创建项目骨架**：通过 `todo` 规划 8 个步骤，并实际创建了目录结构 `shared/`，为后续执行铺路。

**关键产出**

* 确认了“数据→后端→前端”的线性依赖链。
* 生成了可追踪的任务计划，避免遗漏环节。

### 🏞️ 图2：准备启动 Agent A，但陷入混乱

**解决的问题**

* 试图**为 Agent A 设计具体指令**，包括数据采集、格式、文件路径和信号创建。
* 暴露出两个问题：

1. **干扰性代码块**：反复插入无关的 Python 脚本（`transformers` 加载、伪数据循环），与 Agent A 任务毫无关系，可能是主代理上下文污染或错误输出。
2. **指令冗余**：多次重复“设计 prompt”的意图，却未给出最终可用的明确文本，说明主代理在提炼子代理 prompt 时遇到了表达困难。

**实际进展**

* 虽然混乱，但确认了 **Agent A 需要 `web` 和 `terminal` 工具**，并最终会用 `delegate_task` 启动。
* 为主代理后续修正提供了教训：子代理 prompt 必须简洁、无歧义，避免混杂无关内容。

### 🏞️ 图3：信号驱动的 Agent B 顺利执行

**解决的问题**

* **确认前置条件**：检查 `data_ready_signal` 文件，证明 Agent A 已成功完成（尽管中间过程被省略）。
* **为 Agent B 制定精确、可执行的 prompt**：

+ 要求读取 `/home/kali/shared/model_data.json`。
+ 明确三个 API 端点（`GET /models`、`GET /models/search`、`POST /models/compare`）。
+ 包含 Swagger、CORS、日志记录等工程规范。
+ 指定输出文件结构和信号文件名。

* **验证完成**：Agent B 执行后，主代理立即检查 `backend_ready_signal` 并更新任务状态，体现了**严格的依赖校验**。

**关键作用**

* 展示了**信号文件机制的实际运作**：B 只有在 A 的信号出现后才启动，解决了上一轮并行任务中“无依赖传递”的问题。
* 给出了一个成功的子代理 prompt 模板（目标明确、路径绝对、输出可验证）。

### 🏞️ 图4：启动最终环节 Agent C，但陷入重复设计

**解决的问题**

* **检查前置信号**：确认 `backend_ready_signal` 存在，满足 Agent C 的启动条件。
* **为 Agent C 设计任务大纲**：包括 React 前端、图表库、调用后端 API、编写 docker‑compose.yml 和 README。
* **探索前端与后端的通信方式**：反复权衡使用服务名 `backend` 还是 `localhost`，体现对 Docker 网络环境的适配思考。

**存在的问题**

* **严重的重复与冗余**：多次复制粘贴相同的决策点（如“后端地址是 localhost:8000”），陷入了一种“循环设计”状态，反映出主代理在高复杂度任务下容易出现**输出崩溃**。
* **指令未最终固化**：直到最后也没有给出 Agent C 的可直接执行 prompt，而是停留在“让我设计一个清晰的 prompt”的意图阶段。

**实际意义**

* 虽然执行受阻，但问题思考是到位的：明确了需要 Docker 多阶段构建、服务网络、文档路径等。
* 为人工介入或后续优化指出了方向：当主代理无法收敛时，应由用户给出更简洁的决策，或直接提供固化后的 prompt。

---

### 🔗 四张图之间的联系与作用

**1. 依赖传导链**
图1（总体规划）→ 图2（启动 A 的尝试）→ 图3（B 的成功执行，依赖 A 的信号）→ 图4（准备 C，依赖 B 的信号）。
整个过程严格遵循 `A.signal → B → B.signal → C` 的**线性依赖链**，体现了多代理协作的顺序性。

**2. 信号机制作为协作的“神经传递”**
图3和图4中，主代理两次主动检查信号文件（`data_ready_signal`、`backend_ready_signal`），这是这次多代理协作与之前“独立并行”的最大区别——**有了可见的数据传递和状态同步**。

**3. 主代理的“协调者”角色与局限性**

* 图1展现了协调者进行任务分解和路线规划的能力。
* 图2和图4暴露了协调者在生成子代理 prompt 时容易**引入噪声或陷入死循环**，说明当前版本的主代理在处理长链条、高细节任务时，需要更清晰的结构化提示或人机协作（例如用户提供固化指令）才能稳定前进。

**4. 整体任务推进的“螺旋上升”**
虽然图2和图4有波折，但最终依然实现了：目录创建 → Agent A 完成（信号可见） → Agent B 成功交付后端 → Agent C 的准备工作就绪。这种**螺旋式进展（尝试→混乱→纠正→前进）**正是多代理系统在现实任务中常见的执行特征。

**总结**：四张图连起来看，是一次**成功的多代理顺序协作**实验。它证明了信号文件驱动依赖的可行性（图3的顺畅执行），也如实反映了当前 Hermes 在自动生成复杂子代理 prompt 时容易出现冗余和循环的短板。对于使用者而言，最佳实践是**由人给出类似图3中那种精确、无歧义的子代理指令**，让主代理专注于调度和校验，从而兼顾灵活性与可靠性。

三、后面的事

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN7QPW3zFjn4hTpmjPztAuLpyBbgIkNxPgYUia0v6nyibicoFvcNOz2ygOeO1Nr970RrgVFpV1shheh0EUJktmFa70v1rvWxFuVJL0/640?wx_fmt=png&from=appmsg)

我对上面的表述是心存疑的，所以让它给出了代码，以及最后的截图，如上。

我将hermes所有的输出都存放在这里了，可以下载来看：

通过网盘分享的文件：467.txt

链接: https://pan.baidu.com/s/1Ho6R\_I6Ik\_kEsS5c4sJvkg 提取码: wjrz

四、怎么确定三个代理是同步开展的呢？

我的疑虑，可以看出三个代理有前后的联动，但怎么确定三个代理是同步开展的呢？让hermes自证。

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN5jZogKLc4vzgsvNYxXcBDn1CfZUrx4Qnxz8O6KLRbUdrHonsQmxJO4SZdu7djuVSaX5XPibnKzuMbgID1ib5wgPpiaicP9d6zR1AM/640?wx_fmt=png&from=appmsg)

给出了四种自证方法。

✅ 结论

    从信号文件时间戳、任务完成时间记录和主线程执行逻辑三方面证据来看，三个子代理确实是按顺序同步执行的，严格遵循 A → B → C 的依赖链。

    每个阶段完成后都会在共享目录留下信号文件，既是触发下一阶段的依据，也是协作完成的永久证明。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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