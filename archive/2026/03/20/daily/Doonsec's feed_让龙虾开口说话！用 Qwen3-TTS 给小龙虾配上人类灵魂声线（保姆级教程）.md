---
title: 让龙虾开口说话！用 Qwen3-TTS 给小龙虾配上人类灵魂声线（保姆级教程）
url: https://mp.weixin.qq.com/s/VhzJm6Rz346dNllzem5dPA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:47.412614
---

# 让龙虾开口说话！用 Qwen3-TTS 给小龙虾配上人类灵魂声线（保姆级教程）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mAf9IMALLwiaOkHDpFjs7icDyUChzY5icNjMibMWic4K4FTHq2CN9pXJlvWI9JyyMjCWMia75qreAicWNz8vBoicbKr7yoNODRTSQMVbwA29aZvW9KM/0?wx_fmt=jpeg)

# 让龙虾开口说话！用 Qwen3-TTS 给小龙虾配上人类灵魂声线（保姆级教程）

原创

糖果LUA
糖果LUA

AI安全运营

![]()

在小说阅读器中沉浸阅读

前言

有完整的安装过程 、模型下载方法、测试代码、龙虾语音skill安装与触发使用方法，过程中遇到问题，直接留言解决。

2026 年，阿里通义 **Qwen3-TTS** 系列已成为开源 TTS 天花板！语音克隆、声音设计、多语言、流式生成，质量媲美商用。更关键：**完全本地运行**，隐私零泄露，零 API 费用。

今天手把手教你在 **Mac Mini M4（16GB 统一内存）** 上安装玩转它。实测：0.6B 模型丝滑，1.7B 也能稳（关掉其他程序），全程离线，声音自然到起鸡皮疙瘩！

### 一、为什么现在就要上 Qwen3-TTS？

* 语音克隆：3–10 秒你的声音，就能无限复制
* 声音设计：文字描述“温柔甜美萝莉音”“磁性低沉御姐音”直接生成
* 预设女声：CustomVoice 模型内置 9 种高质量音色，女声有 Vivian（明亮活泼）、Serena（温柔治愈）、Ono\_Anna（日系俏皮）等
* 多语言：中英日韩德法俄葡西意，普通话/方言都行
* M4 优化极致：MLX 框架 + Neural Engine + Metal 加速，温度低、功耗省

**内存实测**（M4 16GB）：

* 0.6B 模型 ≈ 4–7GB → 随便玩
* 1.7B 模型 ≈ 8–12GB（8bit 量化）→ 建议独占运行

### 二、最推荐安装方式：MLX 优化版（mlx-audio 库，专为 Apple Silicon）

社区主流方案：直接用 **mlx-audio** 库（苹果原生框架，完美适配 M 系列，加载快、内存省）。

**快速步骤**：

1. 安装 Homebrew + 基础工具（没装的执行）

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install ffmpeg git python@3.12 llvm@20
   ```
2. 创建虚拟环境 & 安装核心库

   ```
   python3 -m venv qwen-tts-env
   source qwen-tts-env/bin/activate
   pip install -U pip setuptools wheel
   pip install mlx-audio
   ```
3. 一键测试生成（CLI 最简单）
   先下载模型（见文末附录），然后运行：

   ```
   python -m mlx_audio.tts.generate \
       --model ./models/0.6B-CustomVoice \
       --text "你好！我是 Qwen3-TTS，在 Mac Mini M4 上本地生成的语音。声音超自然吧？" \
       --voice Serena \
       --language zh \
       --speed 1.0 \
       --play
   ```

   生成的音频自动保存为 .wav 文件，直接播放试听！

**可选进阶方式：使用 kapi2800/qwen3-tts-apple-silicon 仓库**（如果想用这个 fork 的 demo 脚本或自定义代码，兼容性好）：

```
git clone https://github.com/kapi2800/qwen3-tts-apple-silicon.git
cd qwen3-tts-apple-silicon
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

安装后，你可以运行仓库自带的 demo（如 `python examples/test_xxx.py` 或 `python app.py` 如果有），或继续用 mlx-audio 的 CLI。仓库基于 MLX 优化，适合想深入修改的用户。

### 三、如何固定一个女声？（不再随机变化）

* 用 **CustomVoice 模型** + 指定 voice 参数：

+ `--voice Vivian`

  → 明亮年轻女声，语调活泼
+ `--voice Serena`

  → 温暖温柔，治愈系首选
  内置 9 种预设（女声 3–4 种）：Vivian、Serena、Ono\_Anna、Sohee 等，每次 100% 固定！

* 想无限自定义？换 **VoiceDesign 模型**：

  ```
  --text "用甜美萝莉音、略带撒娇地说：哥哥你最好了～"
  ```

### 四、扩展玩法：集成到 OpenClaw 框架中，实现更智能的 TTS 代理

如果你在使用 **OpenClaw**（开源多代理 AI 框架，之前叫 Moltbot/Clawdbot），可以直接安装社区 skill **paki81/qwen-tts**（https://clawhub.ai/paki81/qwen-tts），让你的 AI 代理支持本地 Qwen3-TTS 生成语音消息、语音回复等。完全离线，替代云端 ElevenLabs 等服务。

**这个 skill 的核心特点**：

* 使用 Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice 模型（~1.7GB）
* 支持 10 种语言（包括中文、英文、日韩等）
* 内置 9 种优质预设声音（女声：Vivian 明亮年轻、Serena 温柔治愈、Ono\_Anna 日系俏皮等）
* 支持指令控制语气（如 “Parla con entusiasmo” 或 “Speak with excitement”）
* 输出 WAV 格式（16kHz），兼容 OpenClaw TTS 工作流

**安装步骤**（在你的 OpenClaw 项目目录下）：

```
# 先确保你有 ClawHub CLI（如果没有：npx clawhub@latest --help 或全局安装）
cd skills/public   # 或你的 skills 目录
git clone https://github.com/openclaw/skills.git   # 如果还没克隆 ClawHub skills 仓库
cd qwen-tts   # 进入 skill 目录（或直接用 clawhub install）
bash scripts/setup.sh
```

* 首次运行会自动从 Hugging Face 下载 ~1.7GB 模型。
* 中国用户可加速：`export HF_ENDPOINT=https://hf-mirror.com`

**触发/使用方法**：

* **CLI 测试**（直接生成音频）：

  ```
  scripts/tts.py "你好，这是一段测试语音" -s Serena -l zh -o output.wav
  # 或加指令控制语气
  scripts/tts.py "Ciao, come va?" -i "Parla con entusiasmo" -l Italian -o happy.wav
  # 查看所有声音列表
  scripts/tts.py --list-speakers
  ```
* **在 OpenClaw 代理中触发**（最酷的部分）：
  OpenClaw 会捕获脚本 stdout 的音频路径（最后一行输出文件路径），完美集成：

  ```
  # 示例：在代理对话中说“用温柔女声读这段文本”
  # OpenClaw 调用 skill → 输出路径如 /tmp/audio.wav → 代理可播放或发送语音
  OUTPUT=$(scripts/tts.py "你好，我是你的 AI 助手" -s Vivian -l zh -o /tmp/audio.wav 2>/dev/null)
  # OUTPUT 变量就是音频文件路径，可进一步处理
  ```

  代理收到 TTS 请求时自动调用这个 skill，实现“开口说话”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

AI安全运营

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

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