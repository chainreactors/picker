---
title: 8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）
url: https://blog.upx8.com/8G-RTX3070-Qwen3-6-35B-AI
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-05-23
fetch_date: 2026-05-24T06:00:58.432626
---

# 8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）

发布时间:
2026-05-23 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
3239

估计很多人不相信这是真的，一个非常大的误解，大多数人都会认为：35B 大模型 = 必须 24G 显存才能跑，但最近我实测发现，即使只有一张 RTX 3070 8G 显卡，只要搭配足够的内存，再通过 llama.cpp 的 CPU Offload 和 MoE 优化，居然真的可以跑起来 Qwen Qwen3.6-35B-A3B 模型。速度还非常快！

![20260522113534 921247](https://www.freedidi.com/wp-content/uploads/2026/05/20260522113534_921247.webp "8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）｜零度解说 1")

**甚至：**

* 支持长上下文
* 支持 Flash Attention
* 支持多模态（视觉）
* 支持本地网页 UI

这篇文章，就带大家完整实测与部署

# 一、我的硬件配置

本次测试平台：

CPU：i7-12700
GPU：RTX 3070 8GB
RAM：32G × 2
系统：Windows 11
推理框架：llama.cpp CUDA 12.4

![20260522113714 803209 scaled](https://www.freedidi.com/wp-content/uploads/2026/05/20260522113714_803209-scaled.webp "8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）｜零度解说 2")

#

# 二、为什么 8G 显存也能跑 35B？

这是这次测试最关键的地方。

Qwen3.6-35B-A3B：

> 35B 总参数
> 每次只激活约 3B

也就是说：并不是所有参数同时参与推理

因此：GPU 不需要一次性加载完整 35B ，再结合 llama.cpp 的：CPU Offload ；就能实现：GPU 跑注意力层、RAM 跑专家层。这也是：RTX3070 8G 成功运行 35B 的核心原因！

# 三、部署教程

### 1、下载 llama.cpp

推荐下载：【**[Github下载](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dnbWwtb3JnL2xsYW1hLmNwcA)**】、【**[网盘下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy80YzlhNzU0NzE1OWI)**】或 【**[整合包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvNTUwMzhGMkZCNzQ1MEQ5Rg)**】

#### llama.cpp 最新版支持 N卡、A卡、I卡 还有纯CPU运行，同时也可以在Mac、Linux系统上运行！所以几乎可以在任何电脑上进行运行。

![20260522112459 822918](https://www.freedidi.com/wp-content/uploads/2026/05/20260522112459_822918.webp "8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）｜零度解说 3")

2、安装显卡驱动，比如 N卡选择 CUDA 13.1，如果是  A卡请自行升级到最新版即可

【**[驱动下载](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXIubnZpZGlhLmNvbS9jdWRhLTEzLTEtMC1kb3dubG9hZC1hcmNoaXZl)**】或 【**[打包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy85ZTQ4ZGM5OWJlNTE)**】

## 四、下载模型

本次使用模型：Qwen3.6-35B-A3B-UD-Q4\_K\_M.gguf

量化格式：Q4\_K\_M

这是目前：

* 精度
* 显存
* 速度

综合平衡最好的格式之一。

### 模型下载：

### 【**[Huggingface下载](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby91bnNsb3RoL1F3ZW4zLjYtMzVCLUEzQi1HR1VGL3RyZWUvbWFpbg)**】或 【**[网盘下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy9hNzNlZGY4NThiYTQ)**】

# 五、多模态模型注意事项（非常重要）

这里很多人会踩坑。

Qwen3.6 多模态模型：必须搭配 mmproj

否则：

* 图片上传按钮灰色
* 无法识图
* Vision 不工作

例如：mmproj-BF16.gguf

# 六、最终启动命令（3070 8G 优化版）

下面是我最终稳定运行的配置：

@echo off

chcp 65001 >nul

cd /d C:\Users\LINGDU\Desktop\llama-b9196-bin-win-cuda-12.4-x64

llama-server.exe ^

-m "models\Qwen3.6-35B-A3B-UD-Q4\_K\_M.gguf" ^

--mmproj "models\mmproj-BF16.gguf" ^

-ngl 99 ^

--n-cpu-moe 999 ^

--flash-attn on ^

--jinja ^

-c 32768 ^

-t 12 ^

-b 512 ^

-ub 128 ^

--cache-type-k q4\_0 ^

--cache-type-v q4\_0 ^

--mlock ^

--host 127.0.0.1 ^

--port 8080

pause

注意将上面的llama.cpp的存放路径改成你自己的，因为我是放在桌面上的，所以路径是：C:\Users\LINGDU\Desktop\llama-b9196-bin-win-cuda-12.4-x64 务必改成你自己的路径！

将上面的启动命令另存为启动.bat 批处理脚本，打开运行即可！

![20260522113318 731775](https://www.freedidi.com/wp-content/uploads/2026/05/20260522113318_731775.webp "8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）｜零度解说 4")

成功运行后在浏览器上访问本地的地址：127.0.0.1:8080 就可以正式使用！

![20260522113416 200844 scaled](https://www.freedidi.com/wp-content/uploads/2026/05/20260522113416_200844-scaled.webp "8G 显存逆天了！RTX3070 成功跑 Qwen3.6-35B 多模态AI大模型！部署教程（优化脚本）｜零度解说 5")

[取消回复](https://blog.upx8.com/8G-RTX3070-Qwen3-6-35B-AI#respond-post-8278)

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