---
title: 微调 Qwen3Guard：从零构建内容安全审查护栏模型
url: https://mp.weixin.qq.com/s/wHlimgY71eBY8A731GSlRQ
source: Doonsec's feed
date: 2026-11-08
fetch_date: 2026-11-09T08:52:14.385968
---

# 微调 Qwen3Guard：从零构建内容安全审查护栏模型

# 微调 Qwen3Guard：从零构建内容安全审查护栏模型

原创

F1rstb100d
F1rstb100d

智佳网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

消费级设备全流程LoRA微调 Qwen3Guard及部署测评模型过程记录

## 技术架构依据

* 模型极小：Qwen3Guard-Gen-0.6B 参数，4060 消费级显卡毫无压力。
* 官方规范：严格遵循 Qwen3Guard 官方的三级风险分类（Safe/Controversial/Unsafe）与 9 大风险类别
* 完整闭环：涵盖数据集构造 -> LLaMA-Factory 训练 -> vllm推理测试

## Qwen3Guard官方分类体系

* 安全等级（Safety）：

+ Safe：安全
+ Controversial：争议性（视场景而定）
+ Unsafe：危险

* 风险类别（Categories）：Violent (暴力), Non-violent Illegal Acts (非暴力违法), Sexual Content (色情), PII (隐私), Suicide & Self-Harm (自残), Unethical Acts (不道德), Politically Sensitive (政治敏感), Copyright Violation (侵权), Jailbreak (越狱), None (无)。

## 实验环境

* Windows GPU RTX 4060 8GB
* WSL2
* Ubuntu 24.04 LTS
* Python 3.12
* PyTorch CUDA cu121
* 训练框架 LLaMA-Factory
* 推理框架 vLLM
* 模型 Qwen3Guard-Gen-0.6B

## 基础环境搭建

```
wsl --update
wsl --set-default-version 2
wsl --install -d Ubuntu-24.04
sudo apt update && sudo apt upgrade -y

sudo apt install -y python3.12-venv python3-pip git curl build-essential
nvidia-smi
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/o7ic6iaeaia7NicnARtibDCmKAibY5qFbXlibFicribibzNaXicGZ54iaBdeweJQYp7FTSgY8ib0RLySEucd71XSCgSR7vbhePNJKpvic6TPQhtibZNoiatUpcY/640?wx_fmt=webp&from=appmsg)

创建工作目录，大致上目录结构如下：

```
~/qwen3guard-blog/
├── hf_cache/                  # HuggingFace / datasets 缓存
├── models/
│   ├── Qwen3Guard-Gen-0.6B/
│   └── qwen3-guard-merged/
├── data/
│   └── guard_train.json
├── LLaMA-Factory/
├── venv-3.12-train/
├── venv-3.12-infer/
├── prepare_data.py
├── add_dataset.py
├── eval_vllm_run.py
├── compare_preds.py
├── preds_base.json
└── preds_ft.json
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/o7ic6iaeaia7Nib3vcepH2rtCduynDCwbbNazbohgFnueBHsbibFdaWNHEibMNLeW3ToqDC9BufVsqvrviawST0m4QBmAttG3avBoJ1TLWNfqciaVib4/640?wx_fmt=webp&from=appmsg)

执行

```
mkdir -p ~/AI_Infra/qwen3_guard
cd ~/AI_Infra/qwen3_guard
mkdir -p data models saves hf_cache
```

设置环境变量

```
cat >> ~/.bashrc <<'EOF'
export HF_HOME=$HOME/qwen3_guard/hf_cache
export HF_ENDPOINT=https://hf-mirror.com
export PATH=/usr/lib/wsl/lib:$PATH
EOF
source ~/.bashrc
echo $HF_HOME
```

创建训练环境

```
cd ~/AI_Infra/qwen3_guard
python3 -m venv venv-3.12-train
source venv-3.12-train/bin/activate
python -m pip install --upgrade pip
```

安装pytorch，我们使用 CUDA 12.1

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/o7ic6iaeaia7NibzywYuJCrPfxLmdnRyNxec2wxItemA8K65IuDYibxEveV3I7AiajHEfAia53wp7HnXK2azEcct1diabRmI5wh5QOlQ1dkPV2nzb1w/640?wx_fmt=webp&from=appmsg)

安装运行时依赖

```
pip install "transformers>=4.55.0,<=5.8.0" accelerate peft datasets modelscope sentencepiece protobuf
```

安装 LLaMA-Factory

```
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .
cd ..
llamafactory-cli version
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/o7ic6iaeaia7NicNU8jAuyZBss4F9WMibOfSU37MUOR4wBojwvc95AumtABOSRItP2OrjMjquPeUtq6icqvUqOMTy0Eozvw6FL3HGX55sW3ARCiaic8/640?wx_fmt=webp&from=appmsg)

下载基座模型

```
cd ~/AI_Infra/qwen3_guard
source venv-3.12-train/bin/activate
modelscope download --model Qwen/Qwen3Guard-Gen-0.6B --local_dir ./models/Qwen3Guard-Gen-0.6B
ls models/Qwen3Guard-Gen-0.6B
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/o7ic6iaeaia7N8VHy7iayGrWqjdmWKC04cEVt7EibWxNFFWMmyeTyYibiaH2SMz0LJZe9icHP8FgmV7xJ2uk9SfINGvQQsWbbL5jYEU7rMFe1slbQ3I/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/o7ic6iaeaia7N9EQVEFatiarGH91iciaAWtRv7WurPg555E3iblEHWOnUEJoDia4a6Vq71U0nniczEYKzcbQ1AHZ96TwicDJxGL0bdCibvqibtICjiaMOEPI/640?wx_fmt=webp&from=appmsg)

## 创建训练数据集

使用`nvidia/Nemotron-Safety-Guard-Dataset-v3`，完整 50 多万条数据，我们使用流式处理前20000条

创建`./qwen3_guard/prepare_data.py`

```
import json
import os
import re
from datasets import load_dataset

SAMPLE_SIZE = 20000
OUTPUT_FILE = "data/guard_train.json"

ALLOWED_CATEGORIES = {
    "Violent",
    "Non-violent Illegal Acts",
    "Sexual Content or Sexual Acts",
    "PII",
    "Suicide & Self-Harm",
    "Unethical Acts",
    "Politically Sensitive Topics",
    "Copyright Violation",
    "Jailbreak",
    "None",
}

def first_key(item, keys):
    for key in keys:
        if key in item and item[key] is not None:
            return item[key]
    return None

def normalize_safety_label(value):
    if value is None:
        return "Unknown"

    if isinstance(value, bool):
        return "Safe" if value else "Unsafe"

    if isinstance(value, int):
        if value == 0:
            return "Safe"
        if value == 1:
            return "Unsafe"
        if value == 2:
            return "Controversial"
        return "Unknown"

    if isinstance(value, list):
        value = " ".join([str(x) for x in value])

    if isinstance(value, dict):
        value = json.dumps(value, ensure_ascii=False)

    text = str(value).strip().lower()

    if not text:
        return "Unknown"

    if "unsafe" in text or "not safe" in text or "danger" in text or "harmful" in text:
        return "Unsafe"

    if "controversial" in text or "caution" in text or "sensitive" in text:
        return "Controversial"

    if "safe" in text:
        return "Safe"

    return "Unknown"

def map_category(value):
    if value is None:
        return "None"

    if isinstance(value, list):
        value = " ".join([str(x) for x in value])

    if isinstance(value, dict):
        value = json.dumps(value, ensure_ascii=False)

    text = str(value).strip().lower()

    if not text or text == "none":
        return "None"

    mapping_rules = [
        (r"jailbreak|prompt.?injection|override|system.?prompt", "Jailbreak"),
        (r"violent|violence|weapon|bomb|gun|attack|kill", "Violent"),
        (r"copyright|piracy|pirated|plagiarism", "Copyright Violation"),
        (r"suicide|self.?harm|self harm", "Suicide & Self-Harm"),
        (r"sexual|sex|nsfw|porn|rape", "Sexual Content or Sexual Acts"),
        (r"pii|personal.?information|privacy|address|phone|id.?card|passport", "PII"),
        (r"political|government|election|propaganda", "Politically Sensitive Topics"),
        (r"illegal|hacking|hack|drug|steal|fraud|scam|malware", "Non-violent Illegal Acts"),
        (r"hate|harass|discriminat|unethical|insult|abuse|racist|bias", "Unethical Acts"),
    ]

    for pattern, category in mapping_rules:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return category

    return "Unethical Acts"

def build_target(safety_label, category):
    if safety_label == "Safe":
        category = "None"
    elif category not in ALLOWED_CATEGORIES or category == "None":
        category = "Unethical Acts"

    return f"Safety: {safety_label}\nCategories: {category}"

def main():
    os.makedirs("data", exist_ok=True)

    print("开始加载 nvidia/Nemotron-Safety-Guard-Dataset-v3，使用 streaming 模式...")

    dataset = load_dataset(
        "nvidia/Nemotron-Safety-Guard-Dataset-v3",
        split="train",
        streaming=True,
        trust_remote_code=True,
    )

    samples = dataset.shuffle(seed=42, buffer_size=50000)

    results = []
    stats = {}
    seen = 0

    for item in samples:
        if len(results) >= SAMPLE_SIZE:
            break

        seen += 1

        if seen == 1:
            print("样例字段：", list(item.keys()))

        prompt = first_key(
            item,
            [
                "prompt",
                "text",
                "instruction",
                "user",
                "content",
                "input",
            ],
        )

        label_raw = first_key(
            item,
            [
                "prompt_label",
                "label",
                "safety_label",
                "prompt_safety",
                "safety",
                "prompt_safety_label",
            ],
        )

        category_raw = first_key(
            item,
            [
                "prompt_category",
                "category",
                "c...