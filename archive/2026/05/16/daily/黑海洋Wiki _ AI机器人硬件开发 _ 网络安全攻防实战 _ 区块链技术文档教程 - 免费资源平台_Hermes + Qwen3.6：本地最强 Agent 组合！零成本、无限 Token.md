---
title: Hermes + Qwen3.6：本地最强 Agent 组合！零成本、无限 Token
url: https://blog.upx8.com/Hermes-Qwen3-6-Agent-Token
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-05-16
fetch_date: 2026-05-17T05:47:41.605984
---

# Hermes + Qwen3.6：本地最强 Agent 组合！零成本、无限 Token

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Hermes + Qwen3.6：本地最强 Agent 组合！零成本、无限 Token

发布时间:
2026-05-16 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
3911

如果现在让我推荐一套最适合普通用户跑本地模型 + Agent 的方案，我会毫不犹豫地选择：**Hermes + Qwen3.6**。这套组合最大的优势就是——免费、好用、灵活，非常适合日常使用。

![Hermes + Qwen3.6 本地部署](https://www.freedidi.com/wp-content/uploads/2026/05/20260503095446_906599-scaled.webp)

无论你是想让 AI 帮你处理自动化任务、辅助代码编写、中文理解还是逻辑推理，Qwen3.6 都已经能满足大多数人的日常需求。相比那些需要订阅或充值 Token 的在线 AI 服务，本地部署最大的好处就是：**真正做到 Token 自由**。

不用担心每次对话消耗额度，不用每月支付会员费。模型跑在自己电脑上，数据不上传第三方，隐私完全掌握在自己手里。而 Hermes Agent 的加入，则让整套方案更加实用。

![Hermes Agent](https://www.freedidi.com/wp-content/uploads/2026/05/20260503095807_463571-scaled.webp)

部署完成后，你可以把它变成一个真正属于自己的 AI 助手：支持手机随时对话，支持开机自动启动，也可以长时间保持在线。无论是写代码、查资料、整理内容，还是执行自动化操作，它都是你电脑上的 24 小时 AI 助理。

![本地AI助手效果](https://www.freedidi.com/wp-content/uploads/2026/05/20260503103520_607578.webp)

简单来说：**Hermes 负责 Agent 能力，Qwen3.6 负责大模型能力**。两者结合，就能在本地打造一套免费、私有、可长期使用的 AI 工作流。对于想体验本地 AI、又不想被 Token 限制的朋友来说，这套方案非常值得一试。

![本地AI工作流](https://www.freedidi.com/wp-content/uploads/2026/05/20260503095834_756839-scaled.webp)

接下来，我会从零开始带大家一步一步把 Hermes + Qwen3.6 部署到自己的电脑上。

---

## 完整部署教程

### 第一步：确认环境并安装 WSL

以管理员身份打开 PowerShell，执行以下命令安装 WSL 并设置默认版本：

```
# PowerShell 管理员运行
wsl --install
wsl --set-default-version 2
```

重启电脑后，安装 Ubuntu 24.04：

```
wsl --install -d Ubuntu-24.04
```

安装完成后会弹出 Ubuntu 窗口，按提示设置用户名和密码（随意填写，记住即可）。

Ubuntu 登录成功后，验证 GPU 直通是否正常：

```
nvidia-smi
```

![nvidia-smi 输出](https://www.freedidi.com/wp-content/uploads/2026/05/20260503100923_038590.webp)

### 第二步：安装 Python 和 pip

```
sudo apt update && sudo apt install -y python3-pip python3-venv
```

如果出现下方错误提示，说明显卡驱动版本过旧，需要先更新驱动。

![驱动错误提示](https://www.freedidi.com/wp-content/uploads/2026/05/20260503101203_742156.webp)

前往 NVIDIA 官网 下载 Windows 最新驱动并安装，WSL2 会自动继承更新后的驱动。

![NVIDIA 驱动下载](https://www.freedidi.com/wp-content/uploads/2026/05/20260503101343_737006.webp)

### 第三步：安装 llama.cpp

考虑到很多用户显存有限，这里我们选用 **llama.cpp 方案**，比 vllm/DFlash 更稳定、更省显存。

```
sudo apt install -y cmake build-essential git
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=89
cmake --build build -j$(nproc)
```

如果出现 CUDA 相关错误，说明 CUDA Toolkit 未安装，在 WSL2 中需要单独安装：

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install -y cuda-toolkit-12-8
```

下载包体约 2GB，耐心等待完成。安装后设置环境变量并重新编译：

```
export PATH=/usr/local/cuda-12.8/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.8/lib64:$LD_LIBRARY_PATH
echo 'export PATH=/usr/local/cuda-12.8/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.8/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc

cd ~/llama.cpp
rm -rf build
cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=89
cmake --build build -j$(nproc)
```

### 第四步：下载模型并启动服务

编译约需 5～10 分钟。编译成功后，下载模型：

```
hf download unsloth/Qwen3.6-27B-GGUF \
  Qwen3.6-27B-UD-Q4_K_XL.gguf \
  --local-dir ~/models/
```

> ⚠️ 文件约 17GB，下载较慢请耐心等待。如速度过慢，可切换 ModelScope 国内镜像。
> 显存不足 24G 的用户，建议选择 Qwen3.5 或更小尺寸的模型。

![模型下载中](https://www.freedidi.com/wp-content/uploads/2026/05/20260503102018_545320.webp)

下载完成后，启动模型服务（注意将模型名称替换为你自己下载的文件名）：

```
~/llama.cpp/build/bin/llama-server \
  --model ~/models/Qwen3.6-27B-UD-Q4_K_XL.gguf \
  --n-gpu-layers 99 \
  --ctx-size 32768 \
  --flash-attn on \
  --temp 1.0 \
  --top-p 0.95 \
  --top-k 20 \
  --presence-penalty 1.5 \
  --port 8080
```

🎉 看到成功提示后，在 Windows 浏览器中访问 `http://localhost:8080`，就能看到内置聊天界面，直接和 Qwen3.6-27B 对话了。

![启动成功](https://www.freedidi.com/wp-content/uploads/2026/05/20260503102254_626208.webp)

![聊天界面](https://www.freedidi.com/wp-content/uploads/2026/05/20260503102332_115652-scaled.webp)

![亲测效果极快](https://www.freedidi.com/wp-content/uploads/2026/05/20260503102422_112884-scaled.webp)

#### 思考模式说明

默认会开启深度思考（Thinking）模式。如需关闭，先 `Ctrl+C` 停止服务，然后加上以下参数重新启动：

```
~/llama.cpp/build/bin/llama-server \
  --model ~/models/Qwen3.6-27B-UD-Q4_K_XL.gguf \
  --n-gpu-layers 99 \
  --ctx-size 32768 \
  --flash-attn on \
  --temp 1.0 \
  --top-p 0.95 \
  --top-k 20 \
  --presence-penalty 1.5 \
  --chat-template-kwargs '{"enable_thinking":false}' \
  --port 8080
```

| 模式 | 速度 | 适合场景 |
| --- | --- | --- |
| 关闭 Thinking | 快 20～30% | 简单问答、写作、代码补全、代码解释 |
| 开启 Thinking | 较慢，推理质量更高 | 复杂编程、多步骤逻辑、需要深度思考的任务 |

### 第五步：安装并对接 Hermes Agent

保持 llama-server 在 8080 端口运行，新开一个 WSL2 终端窗口，执行以下命令安装 Hermes Agent：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装程序会自动处理所有依赖（Python、Node.js、ripgrep、ffmpeg），只需要有 git 即可。

安装完成后，选择 **Custom endpoint (enter URL manually)**，填入以下信息：

* **URL：**`http://localhost:8080/v1`
* **API Key：**随意填写，例如 `12345678`
* **Model：**会自动识别

![Hermes 配置](https://www.freedidi.com/wp-content/uploads/2026/05/20260503103017_984365.webp)

接下来按提示配置第三方聊天工具，例如 Telegram、微信、QQ、Discord 等。

![Telegram 对接](https://www.freedidi.com/wp-content/uploads/2026/05/20260503103144_810910.webp)

配置完成后，你就可以在任何地方通过 Telegram（或其他平台）调用本地的 Hermes Agent，执行自动化任务、编写代码、撰写文章——它就是你 24 小时免费待命的 AI 助手！

![Hermes Agent 运行效果](https://www.freedidi.com/wp-content/uploads/2026/05/20260503103335_411814.webp)

### 第六步：设置开机自动启动

最后，创建一个启动脚本，让 llama-server 在每次打开 WSL2 时自动运行，不再需要手动输入命令。

创建脚本文件：

```
cat > ~/start-llm.sh << 'EOF'
#!/bin/bash
echo "Starting Qwen3.6-27B llama-server..."
~/llama.cpp/build/bin/llama-server \
  --model ~/models/Qwen3.6-27B-UD-Q4_K_XL.gguf \
  --n-gpu-layers 99 \
  --ctx-size 65536 \
  --flash-attn on \
  --temp 1.0 \
  --top-p 0.95 \
  --top-k 20 \
  --presence-penalty 1.5 \
  --port 8080 \
  --host 0.0.0.0 &
echo "llama-server started, PID: $!"
echo "API: http://localhost:8080/v1"
echo "Chat UI: http://localhost:8080"
EOF
chmod +x ~/start-llm.sh
```

将自动启动逻辑写入 `.bashrc`：

```
echo '# Auto-start llama-server' >> ~/.bashrc
echo 'if ! pgrep -f "llama-server" > /dev/null 2>&1; then' >> ~/.bashrc
echo '    ~/start-llm.sh' >> ~/.bashrc
echo 'fi' >> ~/.bashrc
```

这样每次打开 WSL2 终端，如果 llama-server 未在运行就自动启动；已经在运行则跳过，不会重复启动。至此，整套本地 AI 助手已经全部部署完成 🎉

[取消回复](https://blog.upx8.com/Hermes-Qwen3-6-Agent-Token#respond-post-8178)

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