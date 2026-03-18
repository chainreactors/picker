---
title: 开始执行编码任务，按照tasks.md文档逐步实现代码！
url: https://mp.weixin.qq.com/s/T2GmBpjV98c-B2jEk31wcA
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:16:43.602159
---

# 开始执行编码任务，按照tasks.md文档逐步实现代码！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVs6icGLVtEvpSKg3msQgTKggJumib7rA7FdP3icpic4uWoCuiaictNlewqlrMeBHcmxYykf2ePOPxXl3w5AwezrbPWocpDjANWt3a9hY/0?wx_fmt=jpeg)

# 开始执行编码任务，按照tasks.md文档逐步实现代码！

原创

SzHackingClub
SzHackingClub

灰帽安全

![]()

在小说阅读器中沉浸阅读

OpenClaw 如何切换到本地模型？如果希望在执行自动化任务时保持流畅、不出现卡顿，同时避免频繁触发上下文长度限制，那么选择一个合适的开源模型就非常关键。

对于 OpenClaw 来说，模型不仅需要具备良好的推理能力和语言理解能力，还需要拥有稳定的 工具调用（Tool Calling）能力。因为在自动化任务中，模型需要频繁调用各种工具完成操作，因此工具调用能力往往是选择模型时最重要的指标之一。、

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVuYuZKV1lfXOPFk7ARlia0TDNmGTK8vdniaKSkTGVZb3peLGvj4fXILqLia4Un6PObR3rCia7nGnAP7BTE9q0yJhq6Cz2Ad6FibiczHw/640?wx_fmt=webp&from=appmsg)

很多人在第一次尝试本地部署模型时，往往会选择 Ollama。它的优点确实很明显：安装简单、配置方便，几乎可以做到“傻瓜式”部署。

但在 OpenClaw 这种自动化任务场景下，Ollama 的调用方式和推理速度并不理想。实际使用中往往会遇到两个问题：

推理速度较慢上下文长度很容易被耗尽在连续运行多个任务后，经常会出现上下文不够用的情况。

因此，如果你希望获得更稳定、更高效的本地部署体验，就需要选择更合适的推理框架。

一般来说：远程集群 / 多 Agent 场景：推荐使用 SGLang软件

单卡本地部署：强烈推荐 vLLM

目前来看，vLLM 可以说是单机部署 OpenClaw 的最佳解决方案之一。

接下来我就给大家详细介绍vLLM 部署本地模型并对接到OpenClaw 的整个过程：

前期准备：在开始之前，建议大家安装下 Windows Terminal，它是一款新式、快速、高效、强大且高效的Windows 的终端程序，适用于命令行工具和命令提示符，PowerShell和 WSL 等 Shell 用户。可以方便我们切换不同的系统！

```
下载：https://apps.microsoft.com/detail/9n0dx20hk701?hl=zh-CN
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVvsVt07RUkaOop22IicUlo516MkpCicJzGXXnUMtprTkeciaMP6pKwwXV5tPTWahl9KvkAlYlWZ61t0Mp3nUZOibt0uJ8DfXPhCwvU/640?wx_fmt=webp&from=appmsg)

一、安装 WSL2

在 PowerShell（管理员）执行：

```
wsl --install
```

安装完成后重启电脑，然后安装Ubuntu，

```
wsl --install -d Ubuntu
```

检查版本：

```
wsl --version
```

确保输出结果是：WSL2

二、WSL 安装 CUDA 驱动支持

先确认 Windows 已安装 NVIDIA 驱动。

检查：

```
nvidia-smi
```

然后在 WSL Ubuntu 里运行：如果出现显卡信息说明 GPU直通成功。例如：

```
RTX 4090 # 根据你自己的显卡而定
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaK3IA1hoFVskyPiazp7FhIjxHEmAsC6OWPk6KGCh03QFKnqhkpRuJKkNVamd61lHbEUQLJWMoW6gtQHSIx4aTr9s7rpaGGZlhrokhGHicc4og/640?wx_fmt=png&from=appmsg)

三、安装 Python 环境

更新系统：

```
sudo apt updatesudo apt upgrade -y
```

安装 Python：

```
sudo apt install python3-pip python3-venv -y
```

创建虚拟环境：

```
cd ~python3 -m venv vllm-env
```

进入环境：

```
source vllm-env/bin/activate
```

四、安装 vLLM

安装命令：

```
pip install --upgrade pippip install vllm
```

安装完成后测试：

```
python -c "import vllm; print('vLLM installed')"
```

五、下载模型

推荐模型：

```
Qwen2.5-14B-Instruct-AWQ
```

模型优点：

```
中文强
Agent能力好
支持更全面的工具调用能力
启动 vLLM 时会自动下载模型。
```

显存提示

本教程演示使用的是 24GB 显存显卡。如果你的显存更小，建议选择参数规模更小的模型，否则在加载模型时可能会出现：显存不足（Out of Memory）的问题。

如果显存不够大，那么可以选择：Qwen2.5-7B-Instruct-AWQ 或  Qwen2.5-4B 等更小的模型

六、启动 vLLM 服务

运行命令：

```
python -m vllm.entrypoints.openai.api_server \  --model Qwen/Qwen2.5-14B-Instruct-AWQ \  --quantization awq_marlin \  --gpu-memory-utilization 0.9 \  --max-model-len 16384 \  --enable-auto-tool-choice \  --tool-call-parser hermes
```

成功后会看到：

![](https://mmbiz.qpic.cn/mmbiz_png/iaK3IA1hoFVvXsecSuelUzknpujnlCqAwe4co9rtFmTErNJ7IqbpoOzw7rlXeFwtGJn08nc5xgxjM12jKxDq3hbXQXz6icgsNOJmcicAN9LZnw/640?wx_fmt=png&from=appmsg)

说明 API 已启动成功。

七、测试模型

在 Windows PowerShell 测试：

```
curl http://127.0.0.1:8000/v1/models
```

返回模型信息：

```
Qwen/Qwen2.5-14B-Instruct-AWQ
```

说明连接正常。

八、安装 OpenClaw

在 WSL 子系统里执行安装命令：

先安装Nodejs

```
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -<br />sudo apt install -y nodejs
```

再执行安装Openclaw

```
sudo npm install -g openclaw@latest
```

九、OpenClaw 配置本地模型

进入配置：

```
openclaw onboard
```

添加模型：

模型提供商必须选择自定义的：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVsluu9YY72gbAQ61ArH1XFlF0ibpiawQzyelX4A5qIeozqOdGkyMvG6tdzNricXVKiazUeDzjrib6sL5ppthCWicN1JBjkUnSianh5vXc/640?wx_fmt=webp&from=appmsg)

```
Base URL：http://127.0.0.1:8000/v1
API key：123456 (随便填写)
模型名称：Qwen2.5-14B-Instruct-AWQ
最后保存即可！
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVu7n3x6IebKicGnliaCsgmwhSDnt9ibK4Mq2yHbutz9IvQ97gAlwJZJoMAyzuxg7gRN1sbBChFU0cWrg9c7bVQZyLKH2zeqnQ3pYk/640?wx_fmt=webp&from=appmsg)

十、OpenClaw 推荐参数（优化）

为了避免卡顿：

```
Context length：6000–8000Temperature：0.7Max tokens：2048
```

十一、优化推理速度（强烈推荐）

vLLM启动参数建议：

```
python -m vllm.entrypoints.openai.api_server \  --model Qwen/Qwen2.5-14B-Instruct-AWQ \  --quantization awq_marlin \  --gpu-memory-utilization 0.9 \  --max-model-len 16384 \  --enable-auto-tool-choice \  --tool-call-parser hermes
```

效果：

```
prefix cache 加速 promptGPU利用率更高
```

十二、解决长对话卡顿

在 OpenClaw System Prompt 加：

```
When the conversation becomes long,summarize previous messages into a short memory.Keep the memory under 200 tokens.
这样：8000 token↓200 token memory
```

速度不会下降。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaK3IA1hoFVtEALwdUV8sQbZ4LedwEiaLap7DRGeEj3mevUAdibPXWOvy1EpXu4qLJMBDhltFIhRYYTdjBcmYCY1YCcokcLsiaaK1A4dqwUoEwo/640?wx_fmt=png&from=appmsg)

本地模型跑 Openclaw 就完全够用。

![](https://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4AoxN1uN9D9c1ibdnPviaOD2v7hKY8FBZBx4c0UcuOhGfEI5OibJwQtvSLxHsDWbTib5pSeic0hSOicJwYw/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4Du5uDacz69OWbdwAUlNfCrXUOicJH7wDmzV9CsHbsXjZ5lEDQcHMK6M33ZM0aApjXjcsBNjRqYx1g/0?wx_fmt=png)

灰帽安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4Du5uDacz69OWbdwAUlNfCrXUOicJH7wDmzV9CsHbsXjZ5lEDQcHMK6M33ZM0aApjXjcsBNjRqYx1g/0?wx_fmt=png)

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