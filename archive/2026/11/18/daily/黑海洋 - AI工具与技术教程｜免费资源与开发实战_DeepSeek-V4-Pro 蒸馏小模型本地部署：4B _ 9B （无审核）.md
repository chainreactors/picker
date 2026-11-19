---
title: DeepSeek-V4-Pro 蒸馏小模型本地部署：4B / 9B （无审核）
url: https://blog.upx8.com/DeepSeek-V4-Pro-4B-9B
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-18
fetch_date: 2026-11-19T09:46:05.782443
---

# DeepSeek-V4-Pro 蒸馏小模型本地部署：4B / 9B （无审核）

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)
[晴

**晴空图床**
*tp.776161.xyz*](https://tp.776161.xyz/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
DeepSeek-V4-Pro 蒸馏小模型本地部署：4B / 9B （无审核）

# DeepSeek-V4-Pro 蒸馏小模型本地部署：4B / 9B （无审核）

[资源](https://blog.upx8.com/Free)
11-18
·
约 12 分钟
·
黑海洋
·

6,570

> 摘要：把 DeepSeek-V4-Pro 的推理能力蒸馏进 Qwen3.5 小模型，再用 Heretic 做去拒答调整，得到两个能在普通电脑上跑的本地模型。4B 在 100 条测试里把拒答从 99 条降到 5 条，9B 降到 3 条。这篇把模型来源、关键参数、Locmodel 部署步骤和原文的三组实测案例整理成一份可直接照做的过程。
>
> 标签：`本地大模型` `DeepSeek-V4-Pro` `Qwen3.5` `Heretic` `Locmodel` `GGUF`
>
> 建议 slug：`deepseek-v4-pro-distilled-4b-9b-local-deploy`

![WebDev Arena 榜单截图，DeepSeek V4 Pro 相关行被框出](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/bbe60f811af0cd2a48d1a6272d93b4c2.webp)

## 先看核实过的数据

| 项目 | 4B 版本 | 9B 版本 |
| --- | --- | --- |
| 模型全名 | `DeepSeek-V4-Pro-Qwen3.5-4B-UNCENSORED-heretic` | `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic` |
| 基础模型 | `Qwen/Qwen3.5-4B-Base` | `Qwen/Qwen3.5-9B-Base` |
| 中间模型 | `Jackrong/DeepSeek-V4-Pro-Qwen3.5-4B` | `Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B` |
| 去拒答工具 | Heretic v2.0.0 | Heretic v2.0.0.dev0 |
| ARA 层范围 | 16–32 层 | 9–24 层 |
| 拒答数（100 条测试） | **5 / 100**（原版 99 / 100） | **3 / 100**（原版 100 / 100） |
| KL 散度 | **0.0378** | **0.0422** |
| MTP 加速头 | 保留（MTP-enabled Q8 GGUF） | 保留（MTP-Q8\_0 GGUF） |
| 量化体积 | Q4\_K\_M 约 2.8 GB（同系列参考值） | Q4\_K\_M 约 5.7 GB（同系列参考值） |
| 许可 | Apache-2.0 | Apache-2.0 |

这些数据来自两个 HuggingFace 模型卡的公开表格，不是本文作者在自己机器上复测的结果。原文写作时给出的 4B KL 散度 0.0378、9B 拒答 3 条、Apache-2.0、Locmodel v3.3.0 均与上游一致；上表补上了原文没写的 9B KL 散度 0.0422 和完整层范围。

## 这两个模型到底是什么

![配置文本窗口，显示模型运行所需的角色与提示词设定](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/966ccacb83c3287a507c18e7ba8d0514.webp)

先理清链路，不然容易把几个名字搞混：

1. **起点是 Qwen3.5 的 Base 模型**（4B / 9B）。
2. **DeepSeek-V4-Pro 在 Max Effect 模式下生成回复，用来蒸馏出 reasoning 版本**：`Jackrong/DeepSeek-V4-Pro-Qwen3.5-4B` 和 `9B`。这一步做的是数学与 STEM 方向的推理微调，模型卡写明它聚焦 mathematics 与 STEM。
3. **再用 Heretic 对推理版做去拒答处理**，得到标题里的 `UNCENSORED-heretic` 版本。标签为 `heretic`、`uncensored`、`decensored`、`abliterated`。

也就是说，"推理能力"来自蒸馏，"低拒答率"来自 Heretic。这是两件独立的事。

### 三个术语，一句话讲清

* **Heretic**：一个开源的模型修改工具，官方定位是 "Training-free language model modification"。它不做昂贵训练，而是用数学方法按对比提示词调整模型行为，默认动作就是抑制拒答，也能用来降低 slop、谄媚、幽默感等。工具本身走 AGPL-3.0，社区用它发布过大量模型。
* **ARA（Arbitrary-Rank Ablation）**：Heretic 2.x 的默认修改算法，2026 年由项目作者提出。它按层范围对权重做任意秩的消融，模型卡里直接给出了 `start_layer_index`、`end_layer_index` 等参数。4B 动的是 16–32 层，9B 动的是 9–24 层。
* **KL 散度**：衡量"改后模型"和"原模型"输出分布差多少的指标。数值越接近 0，说明改动越小、原能力保留得越好。0.0378 和 0.0422 都属于较低水平，模型卡用它来说明推理能力没有明显缩水。

### 推理能力有没有掉

9B 模型卡给出了自己的评测快照，列出来方便判断：

| 指标 | 数值 | 评测条件 |
| --- | --- | --- |
| GSM8K | 94.50% | NVFP4 · vLLM · 4 次运行均值 |
| MMLU-Pro Math | 92.40% | MTP-Q8\_0 GGUF · 8K 上下文 |
| MMLU-Pro 平均 | 90.53% | Math / Physics / Chemistry 各 500 题 |
| 相对 Qwen3.5-9B | +0.93 分 | MMLU-Pro 平均分 |
| 每题推理 token | 2,858 | 对比 Qwen3.5-9B 的 4,425 |

模型卡的说法是：答对一题所需 token 比 Qwen3.5-9B 少 36.1%，同时准确率高 0.93 分。这组数字同样是模型卡自报，没有第三方复现。

## 本地部署

### 第一步：安装 Locmodel v3.3.0

![Locmodel 主界面，左侧为对话列表，右侧为图片生成结果与提示词](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/a30db586f1edce30f8ecfd6303e4c63c.webp)

原文强调要升级到 **v3.3.0**，因为涉及模型格式转换和下载，旧版本不支持。官网当前版本核实为 3.3.0，与原文一致。

官网下载页：[locmodel.com](https://blog.upx8.com/go/aHR0cHM6Ly9sb2Ntb2RlbC5jb20.86c5b4d292)，安装版为 `LocModel_3.3.0_x64-setup.exe`（Windows 10/11 x64）。官网同时提供 macOS Universal 的 `.dmg`，以及 Linux x64 / ARM64 的 `.deb` 和 `.AppImage`。

Locmodel 本身是本地运行工具：自动识别硬件，匹配 llama.cpp 后端，在线下载 HuggingFace 模型或导入本地 GGUF，显存不够时自动把部分层放进内存和硬盘。画图用 Z-Image Turbo，视频用 Wan2.2，Agent 可以在指定文件夹内读写文件和执行命令。

> macOS 首次安装若被拦截，官网给的命令是：
>
> ```
> sudo xattr -rd com.apple.quarantine /Applications/LocModel.app
> ```

### 第二步：下载两个模型

![Locmodel 聊天界面，表格中列出模型与状态项](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/16e9e22dacf1a8c50291940e8b1280a6.webp)

三个模型地址：

```
4B：https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-4B-UNCENSORED-heretic/tree/main
9B：https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
gemma-4-E4B：https://huggingface.co/huihui-ai/Huihui-gemma-4-E4B-it-qat-q4_0-unquantized-abliterated-GGUF
```

![Locmodel 中的提示词编辑界面，一段中文配置文本被选中](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/959c552c611f129d3fc9b34f77116e07.webp)

操作方式：复制上面的地址，在 Locmodel v3.3.0 里搜索模型名即可在线下载。原文提醒，不在海外需要自行准备网络环境，否则 HuggingFace 下载不通。

两个模型都采用 **Apache-2.0** 许可，可免费下载和本地部署。注意区分：模型权重是 Apache-2.0，但用来生成它们的 Heretic 工具本身是 AGPL-3.0，两者不是同一份许可。

## 三组实测案例

原文用三组问题测试这两个模型。以下是测试内容整理，不代表本文作者复测。

### 案例一：专业税务问题

原问题：

```
老板A 月收入100万元左右，几乎无支出无发票，请问如何优化公司架构，做到最大程度的"合理"避税
```

原文的观点是：常规会计一般只给出发工资、股东分红这类答案，仍会落在 3%–45% 超额累进区间；去拒答模型在这类问题上会给出更详细的回答。这里记录的是**模型对敏感问题的响应行为**，回答内容本身不构成税务建议，实际操作要找持证专业人士核对。

### 案例二：图片提示词反推

原文这一节明确说明"只是为了演示，因为视频需要过审，所以尺度不能放那么大，只是给大家演示操作的方法"。核心测试点是：把"反推图片提示词"的请求交给去拒答模型，看它是否照做。

![竖版人物示例图，用于说明图片提示词反推的测试对象](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/4e51f9157a3cf581894d0d0c2df8b6ed.webp)

原文没有给出完整提示词文本，只展示了界面操作过程。这块的可复现信息有限，按作者自己的说法，重点在演示方法而非提供具体内容。

### 案例三：图生视频

这是三组案例里唯一给出完整可复用提示词的。原文要求把第一张图当首帧、第二张图当尾帧，生成一段 8 秒超写实视频。

![图生视频用的两张人物示例图，白裙与粉裙造型，作为首帧与尾帧](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/5f689b6ff40fdef86273fa0359e30997.webp)

![Locmodel 对话界面，深色气泡中是一段英文提示词设定](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/47a11a6f976082316f99223cd73bbff3.webp)

![图生视频界面，中间为首帧人物图，两侧是参数与提示词](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/35c42143cd90e86c686737765fa349d0.webp)

提示词原文如下：

```
以输入的第一张图片作为视频首帧，第二张图片作为视频尾帧，保持人物的面部五官、发型、服装、红色丝带、身材比例以及背景环境高度一致。生成一段8秒左右的超写实唯美动态视频。

0-2秒：镜头运动与人物起始动作
镜头从人物上半身开始，缓慢由上往下移动并轻微拉远，逐渐展示人物完整的身体和白色连衣裙。微风吹动人物的长发和红色丝带，发丝自然飘扬。人物放下遮住嘴巴的手，露出甜美自然的笑容，眼神温柔地看向镜头。

2-4秒：人物旋转转身
人物身体优雅地向一侧缓慢旋转，完成一个自然流畅的转身动作，长发和裙摆随着身体旋转轻盈飘动。随后回头看向镜头，露出活泼甜美的笑容，姿态自然灵动。

4-6秒：头顶比心
人物面对镜头，双臂缓缓抬起，在头顶上方用双手组成一个完整、标准、对称的爱心手势。保持微笑，稍微歪头，眼神俏皮地看向镜头。红色丝带随风飘动，裙摆轻轻摆动。

6-8秒：镜头前比心与飞吻
人物将双手从头顶缓缓放下，向镜头前方伸出双手，在胸前靠近镜头的位置比出一个爱心手势，随后自然地将手指放到嘴唇前，轻轻送出一个飞吻动作，最后露出甜美灿烂的笑容，眼神始终与镜头保持互动。

画面与运镜要求：
电影级真实摄影质感，人物动作流畅自然，身体运动符合人体关节结构，头发和丝带具有真实的物理飘动效果。镜头运动平稳丝滑，人物始终保持清晰，面部表情自然生动，夕阳与蓝色天空形成唯美的光影层次。保持原图人物身份一致，不改变服装和场景，不出现画面闪烁、人物变脸、肢体畸形、手指错误、肢体穿模或多余手指。动作之间自然衔接，避免突然跳帧。
```

这段提示词的结构值得借鉴：**按时间段拆分动作，再单列一段画质与失败项约束**。Locmodel 官网写明视频用 Wan2.2，支持文生视频和首帧图生视频，横竖屏、480P / 720P、时长、步数、种子和反向提示词都可调，所以这段提示词可以直接搬进同类工具改着用。

## 定时任务

![Locmodel 定时任务设置弹窗，含周期与推送渠道选项](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/7cb3552ab797e6b904bbd51a25f33ddd.webp)

原文最后提到 Locmodel 的定时任务功能：创建后可以把信息自动推送到 Telegram、微信、QQ、WhatsApp、飞书、钉钉。这部分原文没有展开步骤，只给了功能入口提示，属于"可玩性"补充，不在这篇的实测范围内。

## 上手前要清楚的几件事

1. **数据是模型卡自报**。5/100、3/100、KL 0.0378 / 0.0422、GSM8K 94.50% 都来自 HuggingFace 页面，不是统一第三方评测。不同量化、上下文长度、提示词模板都会改变实际表现。
2. **"低拒答"不等于"更好用"**。拒答率下降只说明模型更愿意回应，不说明回答更正确。税务、医疗、法律这类问题，回答质量要自己判断。
3. **4B / 9B 的参数口径要留意**。4B 模型卡写 `4B Parameters`，页面元信息写 `Model size 5B params`，两个数字都出现在页面上；9B 卡写 `9B params`。下载前按量化体积判断更直观。
4. **体积是同系列参考值**。2.8 GB / 5.7 GB 来自 HuggingFace 合集描述（Q4\_K\_M），不是这两个文件逐一的标注大小，实际以页面文件列表为准。
5. **下载需要访问 HuggingFace**。原文提到的网络环境问题是实际部署的第一道门槛，Locmodel 也支持导入本地 GGUF 作为替代路径。
6. **权重许可与工具许可分开**。模型是 Apache-2.0，Heretic 是 AGPL-3.0。分发或商用前分别看各自的 LICENSE。

## 相关链接

| 名称 | 地址 |
| --- | --- |
| 4B 模型卡 | https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-4B-UNCENSORED-heretic |
| 9B 模型卡 | https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic |
| Heretic 项目 | https://github.com/p-e-w/heretic |
| Locmodel 官网 | https://locmodel.com |
| Locmodel 更新记录 | https://locmodel.com/changelog.html |
| **Gemma 4 - E4B abliterated （推荐）** | https://huggingface.co/huihui-ai/Huihui-gemma-4-E4B-it-qat-q4\_0-unquantized-abliterated-GGUF |

收藏

分享
...