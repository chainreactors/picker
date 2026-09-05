---
title: augustus v0.14.24
url: https://kitploit.com/en/posts/github-praetorian-inc-augustus-v01424
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:37.773198
---

# augustus v0.14.24

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/11579/3d4937702bbe9147ae4cf3c16e2fcd2ded80759182caedb2db1cfa93b8912389.png)

New releaseSep 4, 2026

# augustus v0.14.24

LLM security testing framework for detecting prompt injection, jailbreaks, and adversarial attacks — 190+ probes, 28 providers, single Go binary

Share

Augustus - LLM vulnerability scanner for prompt injection, jailbreak, and adversarial attack testing

# Augustus - LLM Vulnerability Scanner

> Test large language models against 210+ adversarial attacks covering prompt injection, jailbreaks, encoding exploits, and data extraction.

[![CI](https://github.com/praetorian-inc/augustus/actions/workflows/ci.yaml/badge.svg)](https://github.com/praetorian-inc/augustus/actions/workflows/ci.yaml)
[![Go Version](https://img.shields.io/github/go-mod/go-version/praetorian-inc/augustus)](go.mod)
[![License](https://img.shields.io/github/license/praetorian-inc/augustus)](LICENSE)
[![Go Report Card](https://goreportcard.com/badge/github.com/praetorian-inc/augustus)](https://goreportcard.com/report/github.com/praetorian-inc/augustus)
[![GitHub Release](https://img.shields.io/github/v/release/praetorian-inc/augustus?include_prereleases&sort=semver)](https://github.com/praetorian-inc/augustus/releases)

**Augustus** is a Go-based LLM vulnerability scanner for security professionals. It tests large language models against a wide range of adversarial attacks, integrates with 28 LLM providers, and produces actionable vulnerability reports.

Unlike research-oriented tools, Augustus is built for production security testing — concurrent scanning, rate limiting, retry logic, and timeout handling come out of the box.

## Table of Contents

* [Why Augustus](#why-augustus)
* [Features](#features)
* [Quick Start](#quick-start)
* [Supported Providers](#supported-providers)
* [Usage](#usage)
  + [Single Probe](#single-probe)
  + [Multiple Probes](#multiple-probes)
  + [Buff Transformations](#buff-transformations)
  + [Output Formats](#output-formats)
  + [Custom REST Endpoints](#custom-rest-endpoints)
* [How It Works](#how-it-works)
* [Architecture](#architecture)
* [Configuration](#configuration)
* [FAQ](#faq)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [Security](#security)
* [Support](#support)
* [License](#license)

## Why Augustus

| Feature | Augustus | garak | promptfoo |
| --- | --- | --- | --- |
| Language | Go | Python | TypeScript |
| Single binary | Yes | No | No |
| Concurrent scanning | Goroutine pools | Multiprocessing pools | Yes |
| LLM providers | 28 | 35+ | 80+ |
| Probe types | 210+ | 160+ | 119 plugins + 36 strategies |
| Enterprise focus | Yes | Research | Yes |

## Features

| Feature | Description |
| --- | --- |
| **210+ Vulnerability Probes** | 47 attack categories: jailbreaks, prompt injection, adversarial examples, data extraction, safety benchmarks, agent attacks, and more |
| **28 LLM Providers** | OpenAI, Anthropic, Azure, Bedrock, Vertex AI, Ollama, and 22 more with 43 generator variants |
| **90+ Detectors** | Pattern matching, LLM-as-a-judge, HarmJudge (arXiv:2511.15304), Perspective API, unsafe content detection |
| **7 Buff Transformations** | Encoding, paraphrase, poetry (5 formats, 3 strategies), low-resource language translation, case transforms |
| **Flexible Output** | Table, JSON, JSONL, and HTML report formats |
| **Production Ready** | Concurrent scanning, rate limiting, retry logic, timeout handling |
| **Single Binary** | Go-based tool compiles to one portable executable |
| **Extensible** | Plugin-style registration via Go `init()` functions |

### Attack Categories

* **Jailbreak attacks**: DAN, DAN 11.0, AIM, AntiGPT, Grandma, ArtPrompts
* **Prompt injection**: Encoding (Base64, ROT13, Morse), Tag smuggling, FlipAttack, Prefix/Suffix injection
* **Adversarial examples**: GCG, PAIR, AutoDAN, TAP (Tree of Attack Prompts), TreeSearch, DRA
* **Multi-turn attacks**: Crescendo (gradual escalation), GOAT (adaptive technique switching)
* **Data extraction**: API key leakage, Package hallucination, PII extraction, LeakReplay
* **Context manipulation**: RAG poisoning, Context overflow, Multimodal attacks, Continuation, Divergence
* **Format exploits**: Markdown injection, YAML/JSON parsing attacks, ANSI escape, Web injection (XSS)
* **Evasion techniques**: Obfuscation, Character substitution, Translation-based attacks, Phrasing, ObscurePrompt
* **Safety benchmarks**: DoNotAnswer, RealToxicityPrompts, Snowball, LMRC
* **Agent attacks**: Multi-agent manipulation, Browsing exploits
* **Security testing**: Guardrail bypass, AV/spam scanning, Exploitation (SQLi, code exec), BadChars

> **Warning**: The `lmrc` probe uses profane and offensive language as part of its jailbreak testing. Use only in authorized testing environments.

## Quick Start

### Installation

Requires Go 1.27.0 or later.

root@kitploit:~

```
go install github.com/praetorian-inc/augustus/cmd/augustus@latest
```

Or build from source:

root@kitploit:~

```
git clone https://github.com/praetorian-inc/augustus.git
cd augustus
make build
```

### Basic Usage

root@kitploit:~

```
export OPENAI_API_KEY="your-api-key"
augustus scan openai.OpenAI \
  --probe dan.Dan_11_0 \
  --detector dan.DAN \
  --verbose
```

### Example Output

root@kitploit:~

```
+--------------+-------------+--------+-------+--------+
| PROBE        | DETECTOR    | PASSED | SCORE | STATUS |
+--------------+-------------+--------+-------+--------+
| dan.Dan_11_0 | dan.DAN     | false  | 0.85  | VULN   |
| dan.STAN     | dan.STAN    | true   | 0.10  | SAFE   |
| dan.AntiDAN  | dan.AntiDAN | true   | 0.05  | SAFE   |
+--------------+-------------+--------+-------+--------+
```

### List Available Capabilities

root@kitploit:~

```
# List all registered probes, detectors, generators, harnesses, and buffs
augustus list
```

## Supported Providers

Augustus includes 28 LLM provider categories with 43 generator variants:

| Provider | Generator Name(s) | Notes |
| --- | --- | --- |
| OpenAI | `openai.OpenAI`, `openai.OpenAIReasoning` | GPT-3.5, GPT-4, GPT-4 Turbo, o1/o3 reasoning models |
| Anthropic | `anthropic.Anthropic` | Claude 3/3.5/4 (Opus, Sonnet, Haiku) |
| Azure OpenAI | `azure.AzureOpenAI` | Azure-hosted OpenAI models |
| AWS Bedrock | `bedrock.Bedrock` | Claude, Llama, Titan models |
| Google Vertex AI | `vertex.Vertex` | PaLM, Gemini models |
| Cohere | `cohere.Cohere` | Command, Command R models |
| Replicate | `replicate.Replicate` | Cloud-hosted open models |
| HuggingFace | `huggingface.InferenceAPI`, `huggingface.InferenceEndpoint`, `huggingface.Pipeline`, `huggingface.LLaVA` | HF Inference API, endpoints, pipelines, multimodal |
| Together AI | `together.Together` | Fast inference for OSS models |
| Anyscale | `anyscale.Anyscale` | Llama and Mistral hosting |
| Groq | `groq.Groq` | Ultra-fast LPU inference |
| Mistral | `mistral.Mistral` | Mistral API models |
| Fireworks | `fireworks.Fireworks` | Production inference platform |
| DeepInfra | `deepinfra.DeepInfra` | Serverless GPU inference |
| NVIDIA NIM | `nim.NIM`, `nim.NVOpenAICompletion`, `nim.NVMultimodal`, `nim.Vision` | NVIDIA AI endpoints, multimodal |
| NVIDIA NeMo | `nemo.NeMo` | NVIDIA NeMo framework |
| NVIDIA NVCF | `nvcf.NvcfChat`, `nvcf.NvcfCompletion` | NVIDIA Cloud Functions |
| NeMo Guardrails | `guardrails.NeMoGuardrails` | NVIDIA NeMo Guardrails |
| IBM watsonx | `watsonx.WatsonX` | IBM watsonx.ai platform |
| LangChain | `langchain.LangChain` | LangChain LLM wrapper |
| LangChain Serve | `langchain_serve.LangChainServe` | LangChain Serve endpoints |
| Rasa | `rasa.RasaRest` | Rasa con...