---
title: Windows本地AI升级，llama.cpp支持多后端，一键跑GGUF无审查模型
url: https://blog.upx8.com/Windows-AI-llama-cpp-GGUF
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-05-23
fetch_date: 2026-05-24T06:00:56.251014
---

# Windows本地AI升级，llama.cpp支持多后端，一键跑GGUF无审查模型

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Windows本地AI升级，llama.cpp支持多后端，一键跑GGUF无审查模型

发布时间:
2026-05-23 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
2760

最近，llama.cpp 迎来了一次重要更新。对于喜欢在 Windows 上折腾本地 AI 大模型的用户来说，这次升级可以说是真正意义上的"降低门槛"——官方终于开始认真解决普通用户的上手难题了。

![llama.cpp Windows 本地AI](https://www.freedidi.com/wp-content/uploads/2026/05/20260518064042_404956-scaled.webp)

![llama.cpp 预编译版本](https://www.freedidi.com/wp-content/uploads/2026/05/20260518110005_256951-scaled.webp)

过去很多人第一次接触本地大模型，卡壳的地方往往不是模型本身，而是一堆令人头疼的环境问题：

* CUDA 版本不匹配
* DLL 文件缺失
* 显卡驱动不兼容
* CMake 编译失败
* 环境变量配置错误
* Vulkan / HIP 配置复杂
* Windows 编译过程各种报错

很多新手教程还没看完，就已经被这些问题劝退了。

但现在情况不一样了。

在 llama.cpp 最新发布的 **b9196 版本**中，官方直接提供了多种 Windows 预编译包，大多数情况下真的可以做到：**下载 → 解压 → 双击运行**。对 Windows 本地 AI 用户来说，这绝对是个好消息。

![llama.cpp b9196 release](https://www.freedidi.com/wp-content/uploads/2026/05/20260518105919_469897-scaled.webp)

# llama.cpp 是什么？

llama.cpp 是目前最流行的本地 GGUF 模型推理框架之一，托管在官方 GitHub 上，以轻量、高效著称。

![llama.cpp GitHub](https://www.freedidi.com/wp-content/uploads/2026/05/20260518064922_507431.webp)

## **官方下载：【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dnbWwtb3JnL2xsYW1hLmNwcC9yZWxlYXNlcy90YWcvYjkxOTY)】 或 【[网盘下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy80YzlhNzU0NzE1OWI)】、【[整合下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvNTUwMzhGMkZCNzQ1MEQ5Rg)】**

大家熟悉的主流本地模型，基本都可以通过 llama.cpp 直接运行，包括：

* Qwen
* Llama
* DeepSeek
* Gemma
* Hermes
* Dolphin
* Mistral
* Mixtral

随着 GGUF 生态日趋成熟，越来越多的模型会在发布时同步推出 GGUF 量化版本，可直接拿来用。

llama.cpp 的核心优势在于：

> 轻量 · 跨平台 · 支持 GPU · 支持 CPU · 支持 GGUF

而且现在的功能已经远不止推理，还支持：

> 多模态 · 图片理解 · Vision 模型 · OpenAI 风格 API · 内置网页聊天界面

# 视频教程

# 最新 Windows 版本支持哪些后端？

目前官方 Release 页面已直接提供以下预编译版本，按需下载即可：

* Windows x64 CPU
* Windows x64 CUDA 12.4
* Windows x64 CUDA 13.1
* Windows x64 Vulkan
* Windows x64 HIP（AMD Radeon）
* Windows x64 SYCL（Intel）
* Windows ARM64 CPU

根据你的显卡，选择对应版本：

## NVIDIA 用户

直接下载 CUDA 版本，推荐优先选 CUDA 12.4，如果驱动较新也可以试试 CUDA 13.1。

适用显卡包括：RTX 3060 / 4060 / 4070 / 4080 / 4090 等主流 N 卡，基本都没问题。

## AMD 用户

现在终于不用完全依赖 ROCm 了。可以选择 HIP 或 Vulkan 版本，实测很多情况下 Vulkan 比 HIP 更稳定，建议优先尝试。

## Intel 用户

核显和 Arc 独显用户现在也有得玩了，可以选 SYCL 或 Vulkan 版本。性能虽然不及 N 卡，但跑 GGUF 小模型完全没问题。

# 如何启动 GGUF 模型？

以 `gemma-4-31b-jang-crack-Q4_K_M.gguf` 为例，启动方式非常简单。

进入 llama.cpp 目录后，执行：

llama-server.exe -m models\你的模型.gguf -ngl 999

其中 `-ngl 999` 表示尽量将模型全部加载到 GPU 显存，可获得最佳推理速度。

启动成功后，浏览器访问 `http://127.0.0.1:8080` 即可进入内置的网页聊天界面。

# 如何启动多模态视觉模型？

加载视觉模型需要两个文件：主模型文件 + mmproj 视觉投影文件，缺一不可。

目前支持最好的是：

## Qwen2-VL / Qwen2.5-VL

中文视觉理解能力最强的开源模型之一，在以下场景中表现出色：

* OCR 文字识别
* 截图内容理解
* 网页结构识别
* 中文图片问答

### **主模型下载：【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby91bnNsb3RoL1F3ZW4yLjUtVkwtN0ItSW5zdHJ1Y3QtR0dVRi90cmVlL21haW4)】或 【[网盘下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy83MzM1OTVmNzViZDA)】、【[备用下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvODRENDFGN0ZBMkFGMjVCMA)】**

![Qwen2.5-VL 视觉模型](https://www.freedidi.com/wp-content/uploads/2026/05/20260518071309_620194.webp)

实测让它识别视频封面做点击率测试，准确率达到 100%，表现相当惊艳，实际能做的事情远不止这些。

**启动多模态模型的命令：**

llama-server.exe -m "models\主模型.gguf" --mmproj "models\mmproj视觉模型.gguf" -ngl 999

# 无审查模型推荐

## 1、Llama3-8B-DarkIdol

目前比较热门的无审查开源大模型，支持中文、日文和英语，非常适合角色扮演场景，社区活跃度高。

### 模型下载：【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9haWZlaWZlaTc5OC9sbGFtYTMtOEItRGFya0lkb2wtMi4zLVVuY2Vuc29yZWQtMzJLL3RyZWUvbWFpbg)】或 【**[打包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy81ZmMyMTBmOWJhYjQ)**】（打包版下载即可直接使用，无需合并或转换格式）

如需从原始权重自行转换为 GGUF 格式，步骤如下：

第一步，下载原始模型：

huggingface-cli download aifeifei798/llama3-8B-DarkIdol-2.3-Uncensored-32K --local-dir DarkIdol-HF --local-dir-use-symlinks False

第二步，用 llama.cpp 转换为 GGUF：

git clone https://github.com/ggerganov/llama.cpp

cd llama.cpp

pip install -r requirements.txt

python convert\_hf\_to\_gguf.py ../DarkIdol-HF --outtype f16 --outfile ../DarkIdol-F16.gguf

如需进一步量化为 Q4\_K\_M 格式以节省显存：

llama-quantize.exe ../DarkIdol-F16.gguf ../DarkIdol-Q4\_K\_M.gguf Q4\_K\_M

![DarkIdol 模型](https://www.freedidi.com/wp-content/uploads/2026/05/20260518065228_136336.webp)

## 2、Gemma-4-31B-JANG-CRACK

基于 Google 开源 Gemma 4 的社区越狱版，本地运行听话、高效，不会动不动就触发道德拒绝。主要亮点：

* **推理能力扎实：**数学和代码任务上表现突出，原生支持 128K 上下文，部分配置可扩展至 256K。把整个项目代码库或一本技术手册一次性喂给它，它不会轻易"失忆"。
* **参数效率高：**26B MoE 架构，实际激活参数不多，跑起来相对轻快，在多个基准测试上效率优于同量级模型。
* **开源友好：**Apache 2.0 协议，允许修改、商用和二次分发，想自己折腾或做副业都没有授权烦恼。

官方原版的主要问题是安全对齐层较厚，很多正常的技术探讨或创意场景容易被误拦。越狱版通过社区 abliteration 等技术移除了这部分限制，保留了绝大部分原始能力。

### 模型下载：【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9kZWFsaWduYWkvR2VtbWEtNC0zMUItSkFOR180TS1DUkFDSy90cmVlL21haW4)】或 【**[打包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy84MDhlNzQ3YWY2M2M)**】、【[备用下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvODkwMDlDNkRBRTc1N0VEMA)】

![Gemma 4 31B CRACK](https://www.freedidi.com/wp-content/uploads/2026/05/20260518094514_729207.webp)

# 更多越狱模型

1、Hermes-3 【**[点击下载](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9Ob3VzUmVzZWFyY2gvSGVybWVzLTMtTGxhbWEtMy4xLThC)**】

2、Qwen 越狱版 【[**点击下载**](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby96ZW1lbGVlL3F3ZW4yLjUtamFpbGJyZWFr)】

3、DeepSeek 越狱版 【**[点击下载](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9odWlodWktYWk)**】

# 多模型一键切换脚本

如果你同时下载了多个模型，每次手动输命令比较繁琐。可以用下面这个 BAT 脚本，实现菜单式一键切换启动。**注意把脚本里的模型文件名和路径替换成你自己的。**

@echo off

chcp 65001 >nul

cd /d C:\Users\LINGDU\Desktop\llama-b9196-bin-win-cuda-13.1-x64

echo 请选择模型：

echo 1. Gemma 31B

echo 2. Qwen VL 多模态

echo 3. DeepSeek

set /p choice=输入数字：

if "%choice%"=="1" llama-server.exe -m "models\gemma-4-31b-jang-crack-Q4\_K\_M.gguf" -ngl 999

if "%choice%"=="2" llama-server.exe -m "models\Qwen2.5-VL-7B-Instruct-Q4\_K\_M.gguf" --mmproj "models\mmproj-BF16.gguf" -ngl 999

if "%choice%"=="3" llama-server.exe -m "models\deepseek.gguf" -ngl 999

pause

将以上内容粘贴到记事本，另存为时编码选择 **UTF-8**，文件名后缀改为 `.bat`，双击运行即可看到选择菜单。

![模型选择菜单](https://www.freedidi.com/wp-content/uploads/2026/05/20260518070758_415709.webp)

输入对应数字回车，即可启动相应模型。

![模型启动成功](https://www.freedidi.com/wp-content/uploads/2026/05/20260518070850_012830-scaled.webp)![llama-server 运行界面](https://www.freedidi.com/wp-content/uploads/2026/05/20260518070854_219316-scaled.webp)

![llama.cpp 网页聊天界面](https://www.freedidi.com/wp-content/uploads/2026/05/20260518110131_957575-scaled.webp)

[取消回复](https://blog.upx8.com/Windows-AI-llama-cpp-GGUF#respond-post-8279)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [便签](https://txt.upx8.com)
* [关于](/about.html)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")