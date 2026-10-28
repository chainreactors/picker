---
title: 从 0 到\"神机\"：5 万条数据 + 模块化架构打造网络安全领域专属 LLM
url: https://mp.weixin.qq.com/s/HVl3ZASyQHmeNvCCyP8pYw
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:42:25.586157
---

# 从 0 到\"神机\"：5 万条数据 + 模块化架构打造网络安全领域专属 LLM

# 从 0 到"神机"：5 万条数据 + 模块化架构打造网络安全领域专属 LLM

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 专门针对网络安全领域的 AI 大模型训练系统 | 基于 Qwen2.5 LoRA 微调 | 6GB 显存即可运行

由 **云霖网络安全实验室** 开发，采用模块化架构设计，具备完整的身份认知和专业的网络安全知识体系。**内置 5 万+ 训练数据**，下载即可开始训练。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFWcPmUBv0sEI9IzLtsc6MugdnbsaEsK2s0Oc1Hs38DRmtK8rDAkG0mP9IeJ83qHkb2rl9pataiaejnHh79AGIq7iaicNLefrWhEs/640?wx_fmt=png&from=appmsg)

## 🚀 核心特性

### 功能亮点

| 特性 | 说明 |
| --- | --- |
| **神机身份认知** | 模型具备完整的"神机"身份认知，由云霖网络安全实验室训练 |
| **动态身份设置** | 推理时动态设置身份，无需修改模型文件 |
| **网络安全专精** | 针对渗透测试、代码审计、漏洞分析等场景优化 |
| **一键自动化** | 自动完成数据下载、环境配置、模型训练全流程 |
| **小显存优化** | 6GB 显存即可 LoRA 微调 |
| **中文增强** | 强化中文网络安全术语理解能力 |
| **实时监控** | 训练进度 + 系统状态可视化监控 |
| **模块化架构** | 分层设计，易于维护和扩展 |

### 技术栈

* **基础模型**: Qwen2.5-1.5B（默认），兼容 1.5B-72B 全系列
* **微调技术**: LoRA (Low-Rank Adaptation)
* **训练优化**: FP16 混合精度、梯度累积、检查点保存
* **模型下载**: ModelScope + HuggingFace 双源
* **身份系统**: Chat Template 动态注入

---

## 📋 系统要求

### 最低配置

| 组件 | 要求 |
| --- | --- |
| GPU | NVIDIA P106-100 6GB 或更高 |
| 内存 | 16GB+ |
| 存储 | 50GB+ 可用空间 |
| 网络 | 稳定网络（下载模型和数据） |

### 软件环境

* **OS**: Ubuntu 18.04+ / 其他 Linux 发行版
* **Python**: 3.8+
* **CUDA**: 11.0+
* **其他**: `screen`, `git`

---

## ⚡ 5 分钟快速开始

### 1. 环境准备

```
# 克隆项目
cd /qwen

# 赋予执行权限
chmod +x start_training.sh

# 安装系统依赖
sudo apt-get update
sudo apt-get install -y screen python3-venv python3-pip
```

2. 环境检查（推荐）

```
# 一键检查
python check_environment.py

# 或使用启动脚本
./start_training.sh --mode check
```

3. 一键启动训练

```
bash start_training.sh
```

### 📊 自定义训练数据（可选）

| 模式 | 路径 | 说明 |
| --- | --- | --- |
| 自动加载 | `/qwen/data/processed/*.json` / `*.jsonl` | 自动扫描并合并所有文件 |
| 指定文件 | `/qwen/data/processed/custom.json` | 训练时指定文件名 |

方式 1：对话格式（推荐）

```
[
  {
    "text": "<|im_start|>system\n你是神机，网络安全专家...<|im_end|>\n<|im_start|>user\n如何进行SQL注入测试？<|im_end|>\n<|im_start|>assistant\nSQL注入测试步骤包括...<|im_end|>"
  }
]
```

方式 2：指令格式

```
[
  {
    "instruction": "如何进行SQL注入测试？",
    "input": "",
    "output": "SQL注入测试步骤包括...",
    "category": "security"
  }
]
```

### 使用示例

```
# 创建目录
mkdir -p /qwen/data/processed

# 放置数据文件
cp security_data.json code_data.json /qwen/data/processed/

# 启动训练（自动加载所有文件）
./start_training.sh --mode train
```

### 🛠️ 详细使用指南

```
./start_training.sh --help              # 显示帮助
./start_training.sh                     # 完整流程（默认）
./start_training.sh --mode full         # 同上
./start_training.sh --mode data         # 仅下载处理数据
./start_training.sh --mode data --force-download  # 强制重新下载
./start_training.sh --mode train        # 仅训练
./start_training.sh --mode test         # 仅测试
./start_training.sh --mode interactive  # 交互式对话
./start_training.sh --mode check        # 环境检查
```

### Python 直接运行

```
export PYTHONPATH="$PWD/src:$PYTHONPATH"

python main.py --mode full        # 完整流程
python main.py --mode data        # 仅数据处理
python main.py --mode train       # 仅训练
python main.py --mode test        # 仅测试
python main.py --mode interactive # 交互式对话
```

### 📁 项目结构

```
qwen/
├── requirements.txt              # Python 依赖
├── main.py                       # 主程序入口
├── start_training.sh             # 启动脚本
├── download_model.py             # 模型下载
├── check_environment.py          # 环境检查
├── src/                          # 源代码
│   ├── config/                   # 配置模块
│   │   ├── settings.py           # 基础配置
│   │   ├── training_config.py    # 训练配置
│   │   └── data_config.py        # 数据配置（含神机身份模板）
│   ├── data/                     # 数据处理
│   │   ├── downloader.py         # 数据下载
│   │   ├── processor.py          # 数据处理器
│   │   └── loader.py             # 数据加载
│   ├── model/                    # 模型管理
│   │   ├── downloader.py         # 模型下载
│   │   ├── trainer.py            # 模型训练
│   │   └── inference.py          # 模型推理（动态身份）
│   └── utils/                    # 工具模块
│       ├── logger.py             # 日志
│       ├── environment.py        # 环境检查
│       └── monitor.py            # 训练监控
├── tests/                        # 统一测试框架
├── data/processed/               # 训练数据（5万+ 内置）
├── models/                       # 基础模型
├── checkpoints/                  # LoRA 检查点
│   └── checkpoint-6/
│       ├── adapter_model.safetensors
│       └── chat_template.jinja   # 神机身份模板
├── logs/                         # 训练日志
└── venv/                         # Python 虚拟环境
```

### 🤖 模型管理 CLI

```
# 列出可用模型
python scripts/model_manager.py list

# 下载模型
python scripts/model_manager.py download qwen2.5-7b

# 切换当前模型
python scripts/model_manager.py switch qwen2.5-7b

# 查看当前模型
python scripts/model_manager.py current

# 测试推理
python scripts/model_manager.py test qwen2.5-1.5b

# 交互对话
python scripts/model_manager.py chat qwen2.5-1.5b

# 模型详情
python scripts/model_manager.py info chatglm3-6b
```

### 显示内容：

* 训练会话状态
* 当前训练进度
* GPU 使用情况
* 系统资源状态
* 最新训练日志

### 日志文件

| 文件 | 说明 |
| --- | --- |
| `logs/training_YYYYMMDD_HHMMSS.log` | 详细训练日志 |
| `training.log` | 主程序日志 |
| `training_report.txt` | 训练完成报告 |

### 🎭 神机身份系统

| 特性 | 说明 |
| --- | --- |
| 默认身份 | "你是神机，由云霖网络安全实验室训练的网络安全大模型" |
| 动态设置 | 推理时实时调整，无需改模型文件 |
| Chat Template | 标准化对话模板确保身份一致 |
| 多轮保持 | 完整对话周期内身份不丢失 |

### 🌐 支持的模型

| 系列 | 模型 | 适用场景 |
| --- | --- | --- |
| **Qwen2.5** | 1.5B / 7B / 14B / 32B / 72B | 全系列适配，1.5B 适合资源受限环境 |
| **ChatGLM3** | 6B | 中文多轮对话优化 |
| **Baichuan2** | 7B-Chat / 13B-Chat | 中文对话强化 |
| **Llama2** | 7B-Chat / 13B-Chat | 英文场景，已适配 |

### 🐳 Docker 部署（可选）

```
docker run -d \
  --gpus all \
  -v /path/to/data:/qwen/data \
  -v /path/to/models:/qwen/models \
  -p 8080:8080 \
  yunlin-security/shenji:latest
```

### 项目地址

```
https://github.com/jinghunsanzu/shenji
```

## 低价出售安全证书不限于cisp、pte等cnvd、请Vme～建了一个项目群，想进群的请回复进群即可

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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