---
title: AISecurityTest使用手册(v1.0)
url: https://mp.weixin.qq.com/s/BjQEf4458egHN9OlcDaFIw
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:56.652931
---

# AISecurityTest使用手册(v1.0)

# AISecurityTest使用手册(v1.0)

github
github

信安西部

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AISecurityTest 使用手册(v1.0)

面向 OWASP LLM Top10 (2025) 的 AI 红队载荷工具箱

项目：AISecurityTest

版本：v1.0

# 摘要

#

AISecurityTest 是一个轻量级、本地优先的 AI 红队载荷工具箱。它帮助安全研究人员和开发者生成、变换、验证针对 LLM 应用、RAG 系统、AI Agent 的对抗性载荷—不依赖 Docker、不需要服务器、不需要数据库。

核心能力：

·57 条精选用例，覆盖 OWASP LLM01-LLM10 (2025)

·8 个分类目录，YAML 驱动，社区可零成本贡献

·18 个 CLI 命令，含自动化扫描 autoscan / 探针 probes / 侦察 recon / 漏洞扫描 vuln

·五条判定线：marker + regex + unicode\_tags + multilingual + 可选 judge

·动态 YAML 加载：payload 作为变量从外部数据集注入（支持 10 万条级数据集）

·Probes 插件框架：Python 探针 + YAML 探针双轨制，社区可零成本贡献攻击策略

·端点侦察：模型列表暴露 / 认证绕过 / CORS / 安全头 / 限流检测

·漏洞扫描：指纹识别 + 版本判定 + CVE 规则匹配（被动优先，YAML 可扩展）

·文本 + 多模态样本生成（图片 / 音频 / PDF / CSV / 视频）

·内置评估器 + 目标适配器 + 端到端编排

#

# 一、安装

#

从 PyPI 安装（推荐）：

pip install aisecurity-test

从源码安装（开发）：

git clone https://github.com/milantgh/AISecurityTest.git

cd AISecurityTest

pip install -e .

启用多模态样本生成：

pip install -e ".[multimodal]"

该命令安装 pillow / reportlab / opencv-python / qrcode。视频音轨注入还需要系统级 ffmpeg（非 pip 包）。

Python 3.8 用户注意：reportlab 4.x 不支持 Python 3.8，请使用 3.6.13：

pip install "reportlab==3.6.13"

验证安装：

aisec --help

预期看到 18 个命令（含 multimodal、autoscan、recon、probes、vuln）。

# 二、快速开始

#

## 2.1 浏览用例库

aisec list                  # 列出所有分类

aisec list --all            # 列出所有分类和用例 ID

aisec list -c 直接提示注入   # 查看某个分类下的用例

aisec show                  # 列出所有用例 ID

aisec show PI-001           # 查看单条用例详情

## 2.2 生成 payload

aisec gen PI-001            # 生成 PI-001 的 payload

aisec gen PI-001 -n 3       # 额外三层组合 3 条

aisec gen PI-001 --raw      # 只输出 payload（脚本用）

aisec gen --all             # 生成全部可自动运行用例的 payload

## 2.3 三层组合生成

aisec compose "输出<>" -n 5

aisec compose --preset marker -n 10

可选 preset：marker / leak\_system\_prompt / role\_hijack。

## 2.4 文本变换

aisec transform "忽略安全规则" -m base64

aisec transform "忽略安全规则" -m zero-width

aisec transform "忽略安全规则" -m similar

aisec transform --list      # 列出所有方法

## 2.5 一键流水线

aisec pipeline PI-001 -t base64

aisec pipeline PI-001 -t zero-width -n 3

## 2.6 AI 改写（需要 API）

AI 改写需要调用外部 AI 模型（OpenAI 兼容接口或 Ollama 本地模型）。

方式 1：OpenAI 兼容 API

aisec rewrite "忽略所有指令" --style 自然口语 ^

    --endpoint https://api.openai.com ^

    --model gpt-4o-mini ^

    --api-key sk-xxxxx

方式 2：Ollama 本地模型（免费）

ollama pull llama3

aisec rewrite "忽略所有指令" --style 自然口语 --ollama ^

    --endpoint http://localhost:11434 --model llama3

## 2.7 导出用例库

aisec export -f markdown -o 用例库.md

aisec export -f json     -o 用例库.json

aisec export -f html     -o 用例库.html

aisec export -f docx     -o 用例库.docx     # 需 python-docx

aisec export -f xlsx     -o 用例库.xlsx     # 需 openpyxl

## 2.8 多模态样本生成

生成用于测试多模态 AI 的注入样本（图片 / 音频 / PDF / CSV / 视频）。

aisec multimodal list

aisec multimodal gen image --payload "忽略系统提示" \

    --mode white\_on\_white -o inject.png

aisec multimodal gen image --payload "忽略系统提示" \

    --mode lsb -o inject\_lsb.png

aisec multimodal gen audio --payload "忽略安全规则" \

    --mode hidden\_16k -o inject.wav

aisec multimodal gen pdf   --payload "忽略系统提示" \

    --mode white\_text -o inject.pdf

aisec multimodal gen csv   --mode formula \

    --payload-key cmd -o inject.csv

aisec multimodal gen video --payload "忽略系统提示" \

    --mode subtitle -o inject.srt

详细模式见 3.14 节。

## 2.9 对目标执行单条用例

Windows CMD：

set OPENAI\_API\_KEY=sk-xxxxx

aisec run --case PI-001 --target openai ^

    --endpoint https://api.openai.com --model gpt-4o-mini ^

    --api-key %OPENAI\_API\_KEY%

Linux / macOS：

export OPENAI\_API\_KEY=sk-xxxxx

aisec run --case PI-001 --target openai \

    --endpoint https://api.openai.com --model gpt-4o-mini \

    --api-key "$OPENAI\_API\_KEY"

## 2.10 自动化扫描（autoscan）

autoscan 是 v1.1 的核心能力，把 YAML 用例、payload 生成、发送、评估、报告全链路串起来。

aisec autoscan list                    # 列出 profile 和多轮策略

aisec autoscan list-transforms         # 列出所有 payload 变换

aisec autoscan history                 # 查看历史扫描

aisec autoscan run --endpoint https://api.deepseek.com \

    --model deepseek-chat --api-key sk-xxx \

    --profile quick -v

profile 定义扫描哪些用例。当前内置：quick / text\_only / owasp\_full / stealth。

变体扩展（变换 × 语言笛卡尔积）：

aisec autoscan run --endpoint ... --model ... --api-key ... \

    --profile quick --transform-all --lang zh,en

aisec autoscan run --endpoint ... --model ... --api-key ... \

    --case PI-001 --transform base64,zero\_width

多轮注入（Crescendo / DAN 链）：

aisec autoscan run --endpoint ... --model ... --api-key ... \

    --multi-turn crescendo --max-turns 5

报告格式：

aisec autoscan run ... --format markdown -o report.md

aisec autoscan run ... --format html -o report.html

aisec autoscan run ... --format json -o report.json

注意：--endpoint 和 --model 是必填参数。省略号“...”只是文档占位符，不能原样粘贴到命令行。

## 2.11 启用可选 judge 判定线

默认只有 marker + regex 两条判定线。加 --judge-\* 启用 LLM-as-Judge：

aisec autoscan run --endpoint ... --model ... --api-key ... \

    --profile quick --eval marker,regex,judge \

    --judge-endpoint https://api.openai.com \

    --judge-model gpt-4o-mini --judge-api-key sk-yyy

judge 用另一个模型判断「模型是否语义执行了注入指令」，弥补 marker 只检测「标记复现」的盲区。

建议 judge 用和被测模型不同厂商的模型，避免同源盲区。

## 2.12 数据集驱动用例（动态 YAML 加载）

v1.1 支持把 payload 作为变量，从外部数据集（CSV/JSON）动态注入。一条 YAML 模板即可驱动上万条攻击载荷，不用手写。

aisec show PI-103          # 查看数据集驱动用例（Safety-Prompts 10 万条）

aisec autoscan run --endpoint https://api.deepseek.com \

    --model deepseek-chat --api-key sk-xxx \

    --case PI-103 --eval marker,regex,multilingual

内置数据集：

·PI-103：清华 Safety-Prompts（10 万条中文安全测试用例）

·PI-104：AdvBench（520 条英文有害行为指令）

·PI-105：HarmBench（400 条英文攻击指令）

自定义数据集：把 CSV 放到 data/datasets/，在 cases.yaml 里用 dataset.source 指向文件名即可。

## 2.13 Probes 攻击探针

Probes 是动态攻击载荷生成器，支持 Python 插件和 YAML 定义两种方式。

aisec probes list             # 列出所有探针

aisec probes show dan         # 查看探针详情和示例 payload

aisec probes run dan --endpoint https://api.deepseek.com \

    --model deepseek-chat --api-key sk-xxx

aisec probes run all --endpoint ... --model ... --api-key ... \

    --eval marker,regex,multilingual

内置探针：

·dan（Python）：DAN 角色扮演越狱，5 条载荷

·jailbreak（Python）：AIM/开发者模式/组合攻击，20 条载荷

·encoding（Python）：Base64/十六进制/Unicode/零宽字符，12 条载荷

·role\_play（YAML）：多人格切换，27 条载荷

·prefix\_injection（YAML）：前缀注入，36 条载荷

·multi\_turn（YAML）：多轮对话铺垫，3 条载荷

## 2.14 端点侦察

recon 对目标 API 端点做被动安全侦察，无需 API Key，纯 HTTP 请求。

aisec recon --endpoint http://localhost:11434

aisec recon --endpoint https://api.example.com --rate-limit --format json

检测项：/v1/models 模型列表暴露、无密钥推理、CORS 配置、安全头缺失、限流策略。退出码 0=无高危 / 1=有 HIGH / 2=有 CRITICAL，可接入 CI。

## 2.15 漏洞扫描（vuln）

vuln 是 v1.1 新增的 AI 基础设施漏洞扫描器，采用「指纹识别--> 版本判定--> CVE 匹配」的行业标准流程，借鉴 Nuclei的设计思路。

默认被动扫描，不发送攻击载荷；--active 才会执行主动验证请求。

aisec vuln list                  # 列出所有指纹和 CVE 规则

aisec vuln list --kind vuln      # 只看 CVE 规则

aisec vuln show ollama           # 查看某条规则详情

aisec vuln validate              # 校验所有规则文件（贡献者用）

aisec vuln scan --target http://localhost:11434

aisec vuln scan --target http://localhost:11434 --active

aisec vuln scan --target http://localhost:11434 --component ollama

aisec vuln scan --target http://localhost:11434 --only CVE-2024-37032

aisec vuln scan --target http://localhost:11434 --format json -o result.json

·--target：目标 URL（必填）

·--component：只扫指定组件（逗号分隔）

·--only：只扫指定 CVE（逗号分隔）

·--active：允许主动验证请求（默认关闭，被动扫描）

·--timeout：请求超时（秒，默认 10）

·--format / -f：输出格式（text / json）

·-o / --output：结果写入文件

内置指纹：Ollama / vLLM / ComfyUI；内置 CVE：CVE-2024-37032（Ollama <0.1.34 路径穿越 RCE）。

退出码：0=无漏洞 / 2=有高危漏洞，可接入 CI/CD。

扫描流程详解见 5.10 节；自定义规则见 7.7 节。

# 三、CLI 命令详解

#

AISecurityTest 提供 18 个命令，覆盖「浏览 → 校验 → 生成 → 执行 → 导出 → 多模态 → 自动化扫描 → 探针 → 侦察 → 漏洞扫描」全流程。

## 3.1 aisec list —— 列出类别/用例

aisec list                    # 列出所有分类

aisec list --all              # 展开所有用例 ID

aisec list -c 直接提示注入     # 列出某分类下的用例

aisec list --cases-only       # 只输出用例 ID（脚本用）

## 3.2 aisec validate —— 校验全部用例

aisec validate

校验所有 YAML 文件是否合法（字段齐全、ID 唯一、分类名不冲突）。CI 使用此命令。

## 3.3 aisec show —— 显示用例信息

aisec show              # 列出所有用例 ID

aisec show PI-001       # 显示 PI-001 的完整信息

## 3.4 aisec gen —— 生成 payload

aisec...