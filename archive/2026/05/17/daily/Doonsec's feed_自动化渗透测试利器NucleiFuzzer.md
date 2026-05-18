---
title: 自动化渗透测试利器NucleiFuzzer
url: https://mp.weixin.qq.com/s/5NlCon9G6u3Y-S7QuRiInA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:08:37.502329
---

# 自动化渗透测试利器NucleiFuzzer

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dMqqFicgqDGB7UIeCRldr8fBr8GdfTd6wfCgw2egZlE6xVoUTgcSCjdQiaGzBUaQHEUAzEpibvG5Ro58khGCqXAGJ2FmoUboAKotIrJVO5RqXs/0?wx_fmt=jpeg)

# 自动化渗透测试利器NucleiFuzzer

原创

simeon的文章
simeon的文章

小兵搞安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

NucleiFuzzer 是一款由安全研究者 0xKayala 开发的自动化渗透测试框架，当前版本为 **v4.0 (Python Core Engine)**。它巧妙地将多个业界知名的安全工具整合成一条高效的漏洞发现流水线，让安全测试人员能够从繁琐的重复工作中解放出来，专注于更有价值的漏洞验证与利用环节。

![](https://mmbiz.qpic.cn/mmbiz_png/dMqqFicgqDGAvcXagFrZE3KqOdOMYyteJcINgSzkHevfMsbiaVythQJv8kmMC2lbrl5V4cy7mOCLcibhjkmCIQclafEGxBkQchnfgZgicZZBicMo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dMqqFicgqDGAzBsWXPDJpvUnPvdxSWtr24mr5hVPPQc8QH01hLjyhCMvGPiby2iaE1rgTz9gV3choeu8ictMer0IpeWXreqxQtpX5kpCgSTg0go/640?wx_fmt=png&from=appmsg)

## 1. 工具定位与核心价值

在渗透测试的日常工作中，我们经常需要面对这样的场景：对某个目标域名进行全面的漏洞扫描，从 URL 收集、去重、存活探测，到最后的漏洞扫描，每一步都需要调用不同的工具、编写复杂的脚本串联。NucleiFuzzer 正是为解决这一痛点而生。

### 1.1 核心理念

NucleiFuzzer 的设计哲学可以概括为一个公式：

Nuclei + ParamSpider + waybackurls + gauplus + hakrawler + katana + Fuzzing Templates = NucleiFuzzer

这意味着你不需要手动管理多个工具的调用和数据流转，NucleiFuzzer 会自动完成从信息收集到漏洞扫描的全流程，并以直观的 HTML 报告呈现结果。

### 1.2 适用场景

NucleiFuzzer 特别适合以下场景：

* **授权的渗透测试项目**：需要对多个目标域名进行快速的安全评估
* **Bug Bounty 挖洞**：对目标资产进行系统性的漏洞发现
* **红蓝对抗前的目标侦察**：快速摸清目标的潜在攻击面
* **SRC 漏洞挖掘**：在海量资产中高效筛选可测试的目标

### 1.3 核心优势

相比传统的单工具扫描，NucleiFuzzer 具备以下优势：

|  |  |
| --- | --- |
| **特性** | **说明** |
| **自动化流水线** | 从 URL 收集到报告生成全自动执行，无需人工干预 |
| **多源数据融合** | 同时调用 5 个工具并行收集 URL，覆盖率更高 |
| **智能去重** | 使用 uro 专业去重工具，过滤无效和重复 URL |
| **可选验证闭环** | 支持 SQLMap 和 Dalfox 自动验证发现的漏洞 |
| **AI 辅助分析** | 集成 Gemini AI，可深度分析漏洞报告和 JS 文件 |
| **可视化报告** | 生成暗色主题的 HTML 报告，便于团队共享 |

## 2. 工作原理详解

理解 NucleiFuzzer 的工作流程，对于高效使用该工具至关重要。整个工具的执行分为 **6 个主要阶段**，外加 2 个可选的增强模块。

### 2.1 完整工作流程图

![](https://mmbiz.qpic.cn/mmbiz_png/dMqqFicgqDGBiaOkxHiamEtnRLsicVk4Cc1LuVWsZKfPdavcZV7VJzRVcwSG0peunZ6kxvibywBgf63wf9iclKMKxnCzk2obryibtwy9SgmsmkbGaE/640?wx_fmt=png&from=appmsg)

### 2.2 各阶段详细说明

#### PHASE 1 - Recon：并行 URL 收集

这是整个流水线的入口阶段，NucleiFuzzer 会同时启动 5 个工具来最大化 URL 收集效率：

|  |  |  |
| --- | --- | --- |
| **工具** | **命令示例** | **特点** |
| **ParamSpider** | `python3 ~/ParamSpider/paramspider.py -d {domain} --level high` | 专为参数发现设计，支持排除特定扩展名 |
| **Waybackurls** | `echo {domain} \| waybackurls` | 从 Wayback Machine 获取历史 URL |
| **Gauplus** | `echo {domain} \| gauplus -subs -b {exts}` | Gau 的增强版，支持过滤和子域名 |
| **Hakrawler** | `echo {url} \| hakrawler -d 3 -subs` | 轻量级快速爬虫，支持子域名发现 |
| **Katana** | `echo {url} \| katana -d 3 -silent` | Go 编写的现代爬虫，性能优异 |

这 5 个工具通过 Python 的 `ThreadPoolExecutor` 并行执行（max\_workers=5），显著缩短收集时间。

收集完成后，所有 URL 会合并到 `raw.txt`，同时 JavaScript 文件中发现的端点会单独提取到 `js_endpoints.txt`。

**默认排除的扩展名**：png, jpg, gif, jpeg, swf, woff, svg, pdf, json, css, js, webp, woff2, eot, ttf, otf, mp4, txt

#### PHASE 2 - Dedup：智能去重

收集到的 URL 往往包含大量重复和无价值的内容。此阶段使用以下命令进行去重：

sort -u raw.txt | uro > validated.txt

* `sort -u`：按字母序排序并去除完全重复的 URL
* `uro`：专业的 URL 去重工具，能够识别参数顺序不同但指向相同资源的 URL

💡**提示**：如果 `raw.txt` 为空（未收集到任何 URL），工具会直接终止并提示检查目标域名是否正确。

#### PHASE 3 - DNS Intel（可选）：DNS 情报收集

此阶段需要额外配置：

* **环境变量**：`SUBPIPE_API_KEY`
* **工具**：subpipe

执行命令：

cat validated.txt | subpipe > dns\_intel.txt

subpipe 会分析 URL 中的域名，返回 DNS 相关的情报数据，如 IP 地址、CDN 信息、Whois 数据等。

#### PHASE 4 - Probe Live：存活主机探测

使用 httpx 探测 URL 的存活状态：

httpx -silent -mc 200,204,301,302,401,403,405,500,502,503,504 -l validated.txt -o live.txt

* `-mc`：指定接受的 HTTP 状态码
* `-silent`：静默模式，减少输出噪音
* `-l`：输入文件列表
* `-o`：输出到指定文件

⚠️**重要**：如果 `live.txt` 为空（0 个存活主机），工具会终止执行。这是保护措施，避免 Nuclei 扫描空列表导致 IP 被封禁。

#### PHASE 5 - Nuclei Scan：DAST 漏洞扫描

核心扫描阶段，使用 Nuclei 进行动态应用安全测试：

nuclei -l live.txt -t ~/nuclei-templates -dast -rl {rate\_limit} -jsonl -o results.json

关键参数：

* `-l`：输入的存活 URL 列表
* `-t`：Nuclei 模板目录（默认 `~/nuclei-templates`）
* `-dast`：启用 DAST 模式（动态应用安全测试）
* `-rl`：速率限制，fast 模式为 200，普通模式为 50
* `-jsonl`：输出 JSON Lines 格式
* `-o`：输出文件

扫描结果会实时输出到终端，方便实时观察进度。

#### 报告生成

从 `results.json` 读取 JSONL 格式的扫描结果，生成暗色主题的 HTML 报告：

* 按严重程度排序：**critical > high > medium > low > info**
* 包含统计卡片和漏洞详情表格
* 支持一键分享和存档

## 3. 环境准备

### 3.1 系统要求

NucleiFuzzer 需要运行在 Linux 或 macOS 环境，Windows 用户建议使用 WSL2。基础要求如下：

|  |  |  |
| --- | --- | --- |
| **项目** | **最低要求** | **推荐配置** |
| 操作系统 | Ubuntu 18.04+ / Debian / macOS | Ubuntu 22.04 LTS |
| 内存 | 4 GB | 8 GB+ |
| 磁盘 | 10 GB 可用空间 | 20 GB+（存储模板和输出） |
| 网络 | 稳定的互联网连接 | 高带宽低延迟 |

### 3.2 依赖工具一览

NucleiFuzzer 依赖以下工具，按用途分类：

**核心依赖（必需）**

|  |  |  |
| --- | --- | --- |
| **工具** | **用途** | **安装方式** |
| Nuclei | DAST 漏洞扫描 | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| httpx | HTTP 存活探测 | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| katana | 网页爬虫 | `go install github.com/projectdiscovery/katana/cmd/katana@latest` |
| waybackurls | Wayback URL 收集 | `go install github.com/tomnomnom/waybackurls@latest` |
| gauplus | URL 收集增强 | `go install github.com/bp0lr/gauplus@latest` |
| hakrawler | 轻量爬虫 | `go install github.com/hakluke/hakrawler@latest` |
| uro | URL 去重 | `pip install uro` |
| ParamSpider | 参数发现 | `git clone https://github.com/0xKayala/ParamSpider` |
| nuclei-templates | Nuclei 模板库 | `git clone https://github.com/projectdiscovery/nuclei-templates` |

**可选依赖**

|  |  |  |
| --- | --- | --- |
| **工具** | **用途** | **启用条件** |
| sqlmap | SQL 注入验证 | `--validate`   参数 |
| dalfox | XSS 验证 | `--validate`   参数 |
| subpipe | DNS 情报 | `SUBPIPE_API_KEY`   环境变量 |
| Gemini | AI 分析 | `GEMINI_API_KEY`   环境变量 |

### 3.3 安装 Go 环境

由于大部分工具使用 Go 编写，需要先安装 Go 1.21+：

```
# 下载并安装 Go 1.26.1
wget https://go.dev/dl/go1.26.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.26.1.linux-amd64.tar.gz
rm go1.26.1.linux-amd64.tar.gz

# 配置环境变量
echo 'export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc

# 验证安装
go version
```

---

## 4. 安装步骤

### 4.1 一键安装（推荐）

最简单的方式是使用官方提供的安装脚本：

```
# 克隆仓库
git clone https://github.com/0xKayala/NucleiFuzzer.git
cd NucleiFuzzer

# 赋予执行权限并运行安装脚本
sudo chmod +x install.sh
./install.sh
```

安装脚本会执行以下操作：

1. 将文件复制到 `/opt/nucleifuzzer/`
2. 安装 Python 依赖：`colorama`, `requests`, `uro`
3. 创建全局命令 `nf`（软链接 `/usr/bin/nf` → `/opt/nucleifuzzer/nucleifuzzer.py`）

⚠️**注意**：安装脚本不会自动安装依赖工具，你需要先运行 `setup.sh` 或手动安装所有依赖。

### 4.2 完整依赖安装（setup.sh）

在克隆仓库后，运行 setup.sh 安装所有依赖工具：

```
cd NucleiFuzzer
chmod +x setup.sh
./setup.sh
```

setup.sh 会依次安装：

1. **系统依赖**：python3, pip3, jq, git, curl, wget, npm
2. **Go 语言环境**：go1.26.1
3. **Go 工具集合**：nuclei, httpx, katana, waybackurls, gauplus, hakrawler, dalfox, subpipe
4. **ParamSpider**：克隆到 `~/ParamSpider`
5. **Nuclei 模板库**：克隆到 `~/nuclei-templates`
6. **uro**：Python URL 去重工具

### 4.3 手动安装（自定义场景）

如果你是高级用户，需要定制化安装，可以按以下顺序手动安装：

```
# 1. 安装 Go（如果没有）
wget https://go.dev/dl/go1.26.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.26.1.linux-amd64.tar.gz

# 2. 配置 PATH
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin

# 3. 安装 Go 工具
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/tomnomnom/waybackurls@latest
go install github.com/bp0lr/gauplus@latest
go install github.com/hakluke/hakrawler@latest
go install github.com/hahwul/dalfox/v2@latest

# 4. 安装 Python 依赖
pip install colorama requests uro

# 5. 克隆项目
git clone https://github.com/0xKayala/ParamSpider ~/ParamSpider
git clone https://github.com/projectdiscovery/nuclei-templates ~/nuclei-templates

# 6. 配置全局命令
sudo ln -s /opt/nucleifuzzer/nucleifuzzer.py /usr/bin/nf
```

### 4.4 验证安装

安装完成后，运行诊断命令验证环境：

nf --doctor

正常情况下，你会看到类似输出（以下为源码实际输出格式）：

```
======================================
🩺 NucleiFuzzer Diagnostics (Doctor Mode)
======================================

[OK] python3 is installed.
[OK] pip3 is installed.
[OK] go is installed.
[OK] nuclei is installed.
[OK] httpx is installed.
[OK] katana is installed.
[OK] waybackurls is installed.
[OK] gauplus is installed.
[OK] hakrawler is installed.
[OK] uro is installed.
[FAIL] sqlmap is missing.
[...