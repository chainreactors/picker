---
title: 给编码 Agent 装一张嘴：DSH 语音 AI 女友完整搭建教程
url: https://blog.upx8.com/Agent-DSH-AI
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-02
fetch_date: 2026-11-03T08:50:30.920519
---

# 给编码 Agent 装一张嘴：DSH 语音 AI 女友完整搭建教程

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

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
给编码 Agent 装一张嘴：DSH 语音 AI 女友完整搭建教程

# 给编码 Agent 装一张嘴：DSH 语音 AI 女友完整搭建教程

[资源](https://blog.upx8.com/Free)
11-02
更新于 11-03 14:56
·
约 36 分钟
·
黑海洋
·

5,119

![给编码 Agent 装一张嘴：DSH 语音 AI 女友完整搭建教程](https://i0.wp.com/cdn.skyimg.net/up/2026/11/2/28c6a01c254a650a69d8212cec96e78a.webp)

> 开源项目：[`beiyege-01/dsh-voice-ai-girlfriend`](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2JlaXllZ2UtMDEvZHNoLXZvaWNlLWFpLWdpcmxmcmllbmQ)
>
> 技术栈：React 插件 / AudioWorklet / FastAPI / FunASR / OmniVoice / silero-VAD / DUIX / NapCat
>
> 目标平台：Windows 11 + NVIDIA GPU（16GB 显存推荐）+ WSL2
>
> 读完这篇你能做到：从一台干净电脑开始，装出一个能听、能说、能被打断、还能对口型说话的 AI 助手

---

## 先说清楚：这是什么（这篇文章是给纯小白人看的，ai老鸟绕过）

你在电脑上用 AI 写代码，通常是打字提问、看字回答。这个项目给那个对话框加了两样东西：

**一双耳朵**——点一下麦克风，你说话，它听。停顿一下自动断句，不用按键发送。

**一张嘴**——它的回答会被念出来。不是机器合成的塑料音，而是克隆自你提供的 10 秒录音，可以是任何人的声音。

再加三个不那么常见的东西：

* **你插嘴它会闭嘴**。它正说着，你开口，它立刻停，听你说完。想让它把话说完，点一下开关切回"排队"模式。
* **回答会变成视频**。旁边有个小窗口，姑娘闲着会发呆、说话时会开口，口型对得上（这叫数字人，可选）。
* **出门也能聊**。回复自动推到你手机 QQ，文本 + 语音都有（可选）。

### 能力清单

| 能力 | 实测表现 |
| --- | --- |
| 语音识别 | 5 秒音频 151ms，14 秒音频 155ms |
| 开口延迟 | 说完停顿 1.8 秒后，约 0.5 秒内开口（不含大模型思考时间） |
| 音色克隆 | 首轮 1.6 秒出音，之后每句约 1.3 秒 |
| 抗噪 | -35dB 噪声门，能挡住桌面风扇 |
| 打断 | 说话即打断，服务端同时停止合成（不空烧显卡） |
| 数字人 | 7.3 秒音频 14 秒出片，长回复切段连续播放 |
| 显存占用 | 全链路峰值约 15GB |

### 先判断：这台机器能装吗

**能装的**：NVIDIA 独立显卡、显存 16GB 以上、Windows 11、硬盘剩 40GB。

**装不了的**：AMD/Intel 核显、Mac、没有独立显卡的轻薄本。所有模型推理都依赖 CUDA，这个绕不过去。

**会很痛苦的**：8GB 显存。能跑，但语音和数字人不能同时开，得来回切。

如果你只是想看看这东西长什么样，不用装——项目 README 里有抖音演示链接。**装它是为了自己用，不是为了围观。**

---

## 第一部分：它怎么跑起来的（5 分钟看懂）

看一张图就够了：

```
┌────────────────────────────────────────────┐
│  浏览器（就是那个聊天界面）                  │
│                                            │
│   [对话面板]          [女友窗]              │
│   麦克风 ──▶ 文字 ──▶ 回答 ──▶ 声音 ──▶ 播放  │
│                                    ▲        │
└────────────────────────────────────┼────────┘
                                     │
┌────────────────────────────────────┴────────┐
│  语音桥接服务（本地 8765 端口）              │
│  负责：听写、合成语音、生成视频、收发 QQ      │
└──────┬──────────────┬───────────────────────┘
       │              │
┌──────▼──────┐  ┌────▼──────────────────┐
│ TTS 引擎     │  │ 数字人引擎             │
│ 9877 端口    │  │ 9000 端口              │
│ （跑在 WSL） │  │ （跑在 Docker）        │
└─────────────┘  └───────────────────────┘
```

**三层，各管一件事：**

**第一层，浏览器里的插件。** 它只是一堆界面代码——麦克风按钮、开关、那个小窗口。**它自己不会说话**，所有声音都要找第二层要。

**第二层，语音桥接服务。** 一个跑在本地的 Python 程序，监听 8765 端口。它像一个转接台：收到浏览器发来的录音，转给识别模型；收到文字，转给合成模型。所有 API 都从这里出入。

**第三层，真正的模型。** 识别、合成、生成视频这些重活，各自由专门的程序干。它们吃显存，所以单独拆出来，出问题好换、好重启。

### 为什么非要拆成三层

因为**这三层坏一个，不影响其他两个**。识别坏了你还能打字提问听语音；合成坏了你还能说话看文字。如果全塞在一个程序里，一个模型加载失败，整个系统就死了。

而且换引擎不用改界面。识别模型从 whisper 换成 FunASR，只改一行配置，浏览器那边完全不知道。

### 两个反直觉的设计

**声音合成不在 Windows 上跑。** 中间那个 9877 端口，实际跑在 Windows 里的 Linux 子系统（WSL2）中。听起来很折腾，但收益巨大：

|  | Windows 原生（Qwen3-TTS） | WSL 里跑（OmniVoice） |
| --- | --- | --- |
| 首轮出音 | 18.3 秒 | **1.6 秒** |
| 平时出音 | 2.2 秒 | **1.3 秒** |
| 占显存 | 7GB 常驻 | **5.3GB** |

差了 11 倍的启动速度，值得折腾一次。

**插件装了也可能没声音。** 插件只有界面，语音能力全在第二、三层。这就是为什么必须先装主仓库的桥接，再装插件——很多人反过来做，装完发现"按钮能点但没反应"，就是这个原因。

---

## 第二部分：装之前先对照

### 硬件

| 项目 | 要求 | 怎么查 |
| --- | --- | --- |
| 系统 | Win10/11 64 位 | `winver` |
| 显卡 | NVIDIA，显存 ≥16GB | `nvidia-smi` |
| 硬盘 | 剩余 ≥40GB | 资源管理器 |
| 内存 | ≥16GB | 任务管理器 |

`nvidia-smi` 报"不是内部或外部命令"，说明没有 N 卡或驱动没装。

显存怎么被吃掉的：

| 组件 | 占用 |
| --- | --- |
| 语音合成 | 5.3GB 空闲 ~ 11GB 峰值 |
| 语音识别 | ~1GB |
| 数字人 | 4~6GB |
| **同时工作** | **~15GB** |

### 软件（五个，缺一不可）

```
git --version
python --version        # 3.10 以上
node --version          # LTS 版
npm install -g pnpm
pnpm --version
```

下载地址：

* Git：https://git-scm.com/download/win
* Python：https://www.python.org/downloads/windows/ ← **安装时务必勾 "Add Python to PATH"**
* Node.js：https://nodejs.org/
* 显卡驱动：https://www.nvidia.cn/drivers/

不需要单独装 CUDA Toolkit，装依赖时会自带。

> 装完 Python 一定要**开个新终端**再验证，否则 PATH 没生效，会误判成没装。

### 要花多久

| 阶段 | 内容 | 时间 |
| --- | --- | --- |
| 一 | 环境体检 | 5 分钟 |
| 二 | 代码 + Python 环境 | 20 分钟 |
| 三 | 识别模型 | 15 分钟 |
| 四 | 语音合成引擎 | 30~90 分钟 |
| 五 | 声音素材 + 配置 | 10 分钟 |
| 六 | 服务验收 | 10 分钟 |
| 七 | 装插件 + 首次对话 | 25 分钟 |
| 八 | 数字人（可选） | 40 分钟 |
| 九 | QQ（可选） | 20 分钟 |

**最小可用只要一到七**，走完就能语音对话。

### 端口表（排障全靠它）

| 端口 | 谁在用 |
| --- | --- |
| 8765 | 语音桥接服务（核心） |
| 9877 | 语音合成引擎 |
| 3092 | 聊天界面（DSH 0.2.1） |
| 9000 | 数字人引擎 |
| 3000 | QQ 机器人接口 |
| 6099 | QQ 机器人管理页 |

六个端口，装完记不住没关系，出问题时回来看这张表。

---

## 第三部分：动手装

### 第一步：环境体检

跑一遍第二部分的检查命令，五个都有版本号、`nvidia-smi` 能看到显卡，就往下走。

---

### 第二步：拿代码和 Python 环境

```
cd D:\
git clone https://github.com/beiyege-01/dsh-voice-ai-girlfriend.git
cd dsh-voice-ai-girlfriend
```

**后面所有命令都在这个文件夹里执行。**

建虚拟环境（相当于给这个项目单独开一个干净的 Python 房间，不影响系统里其他 Python 程序）：

```
python -m venv venv-speech
venv-speech\Scripts\activate
```

激活成功时，终端行首会出现 `(venv-speech)`。

> **文件夹名必须是 `venv-speech`。** 后面的一键启动脚本里写死了这个路径，改成别的名字脚本就找不到 Python 了。

装依赖：

```
pip install -r bridge\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

会下载 PyTorch 一整套，**5~8GB，几分钟到半小时**。国内不走清华镜像基本装不完。

**你会看到**：最后一行出现 `Successfully installed ...` 一长串包名。

**怎么验证装对了**：

```
venv-speech\Scripts\python.exe -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

输出末尾必须是 **`True`**。如果是 `False`，说明装成了 CPU 版或者显卡驱动太旧，**这时候不要往下走**——后面所有模型都会跑在 CPU 上，慢到不可用。

---

### 第三步：下载识别模型

语音识别用阿里 FunASR 的中文模型，约 850MB。它识别中文比 whisper 准得多：

| 模型 | 同音字错误（测三句古诗） | 准确率 |
| --- | --- | --- |
| whisper-turbo | 尽→静、目→木、楼→牛、庵→安、钱→前 | 86% |
| **FunASR** | 五处全部纠正，只剩 2 处音近错 | **93%** |

下载：

```
pip install modelscope -i https://pypi.tuna.tsinghua.edu.cn/simple

# 先下到缓存
python -c "from modelscope import snapshot_download; snapshot_download('iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch')"

# 再拷进项目的 models 目录
mkdir models\funasr
xcopy /E /I "%USERPROFILE%\.cache\modelscope\models\iic--speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch\snapshots\master" "models\funasr\speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
```

还要一个小的：**silero VAD**（2MB，用来判断"你什么时候在说话"，打断功能靠它）。从 [silero-vad v4.0](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NuYWtlcnM0L3NpbGVyby12YWQvdHJlZS92NC4w) 拿 `files/silero_vad.jit`，放到：

```
models/silero-vad/silero_vad_v4.jit
```

> **一定要 v4 版本。** v5 带了额外组件，在新版 PyTorch 下会随机报错（这个项目实测过：同一个文件下午正常、晚上报错），排查起来很折磨。

**你会看到**：`models/` 下出现两个文件夹。

```
models/
├── funasr/
│   └── speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/
└── silero-vad/
    └── silero_vad_v4.jit          ← 约 1.4MB
```

---

### 第四步：语音合成引擎（二选一）

**这是全程唯一有难度的环节。** 两条路，先看区别再选：

|  | 路线 A：OmniVoice | 路线 B：Qwen3-TTS |
| --- | --- | --- |
| 首轮出音 | 1.6 秒 | 18.3 秒 |
| 平时出音 | 1.3 秒 | 2.2 秒 |
| 占显存 | 5.3GB | 7GB |
| 音色 | 克隆 + 参数设计 | 只能克隆 |
| 难度 | 高（要配 WSL + CUDA） | **低（一条命令）** |

**建议先走 B。** 20 分钟跑通，验证整条链路能出声，再升级到 A。这样卡住时你清楚问题在哪一层。直接上 A 卡住的话，你分不清是界面问题、桥接问题还是模型问题。

---

#### 路线 B：Qwen3-TTS（先跑这个）

```
pip install modelscope -i https://pypi.tuna.tsinghua.edu.cn/simple
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-Base --local_dir D:\models\Qwen3-TTS-12Hz-1.7B-Base
```

> **必须是 `-Base` 版本。** 名字带 `VoiceDesign` 的那个不支持参考音频克隆，装了也克隆不出你的声音。

记下 `D:\models\Qwen3-TTS-12Hz-1.7B-Base` 这个路径，第五步要填进配置。

---

#### 路线 A：OmniVoice（进阶）

先在 Windows 里装 Linux 子系统：

```
wsl --install -d Ubuntu-22.04
```

装完重启，设好 Linux 用户名密码。验证 WSL 里能看见显卡：

```
wsl -d Ubuntu-22.04 -- nvidia-smi
```

然后进 WSL 里干活：

```
wsl -d Ubuntu-22.04
```

```
mkdir -p ~/omnivoice-wsl && cd ~/omnivoice-wsl

...