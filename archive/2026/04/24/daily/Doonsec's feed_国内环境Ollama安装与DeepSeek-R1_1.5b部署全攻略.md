---
title: 国内环境Ollama安装与DeepSeek-R1:1.5b部署全攻略
url: https://mp.weixin.qq.com/s/Q-QZLyLkaR3lkXGp3lqfXw
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:30:12.945047
---

# 国内环境Ollama安装与DeepSeek-R1:1.5b部署全攻略

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa1S53wOz7ZCdEO4AVsITkqXiapPJianCalwAibTyboBjAnGYgtPQWe3PcRI4yeib1zyVUxriaKohLj59DJAS15aZOCdM0E1oH82SlXc/0?wx_fmt=jpeg)

# 国内环境Ollama安装与DeepSeek-R1:1.5b部署全攻略

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你是否遇到过这样的困境：在安全测试中需要一个能理解复杂日志、分析攻击链路的AI助手，却又担心敏感数据传到云端？想部署本地大模型，却被繁琐的环境配置和龟速的模型下载劝退？今天，我们就来解决这个痛点在国内网络环境下，用Ollama部署DeepSeek-R1:1.5b蒸馏模型，打造属于网安人的专属推理引擎。

在动手之前，先回答一个核心问题：安全从业者本地部署大模型，市面上可选项很多........Llama、Qwen、Claude……为啥偏偏选这个只有15亿参数的「小模型」？

DeepSeek-R1:1.5b全称为**DeepSeek-R1-Distill-Qwen-1.5B**，它是DeepSeek-R1「满血版」通过模型蒸馏技术得到的小参数版本。这里有个关键前提：DeepSeek-R1是首个通过**纯强化学习（RL）** 激发推理能力的大模型，其在训练过程中仅依靠RL就能让模型自主学会自我验证、反思和生成长思维链，无需依赖大量人工标注的监督微调（SFT）数据。这项成果后来登上国际顶级期刊《Nature》封面，成为全球首个经同行评审的大语言模型......

而蒸馏技术意味着：用DeepSeek-R1这个大“教师模型”生成的高质量推理数据，来训练Qwen-1.5B这个小“学生模型”，使其在保持轻量级的同时，尽可能地保留大模型的推理能力。论文明确指出，**将大模型的推理模式蒸馏到小模型，效果优于直接在小模型上做RL**。

换句话说，这个1.5b模型不是“缩水的廉价版”，而是“继承了核心推理基因的精简版”。

### 硬件门槛极低：个人笔记本也能跑

在网络安全领域，模型再强，如果部署成本高到无法落地，一切都是空谈。来看看DeepSeek家族不同规格的硬件需求对比：

| 模型版本 | 显存占用 | 推理速度 | 硬件要求 |
| --- | --- | --- | --- |
| DeepSeek-R1-Distill-1.5B | ~3-4 GB | 极快 | 普通笔记本即可 |
| 7B版本 | ~14 GB | 约120 tokens/s | 消费级显卡如RTX 3060+ |
| 32B版本 | ~60 GB | 约45 tokens/s | 2-4张A100 |
| 671B满血版 | 480+ GB | ~8 tokens/s | 8+张A100集群 |

###

对比其他主流开源模型的部署门槛：

* **Llama 3.1-8B**：至少需要16GB显存才能流畅运行（FP16精度），QLora量化后仍需8GB以上，普通笔记本几乎无法跑动；
* **Qwen2.5-7B**：类似Llama，FP16精度需14GB+显存，int4量化后约6GB，对硬件仍有门槛；
* **ChatGLM3-6B**：int4量化后约4-5GB显存，勉强可跑，但在推理深度和灵活性上明显不如蒸馏自DeepSeek-R1的模型。

而DeepSeek-R1:1.5b使用4-bit量化后，推理速度快、内存效率高，甚至在Google Colab的免费T4 GPU上就能流畅运行。对于大多数安全从业者而言，一台16GB内存的笔记本、没有独立显卡也能部署——这意味着**零硬件成本投入**。

### 推理能力突出：安全分析场景的“天然契合”

DeepSeek-R1最核心的优势在于**解决需要多步骤推理的复杂问题**，特别擅长通过中间步骤逐步解决谜题、高级数学和编程挑战等类型的任务。经过强化学习训练后，DeepSeek-R1-Zero在AIME 2024基准测试上Pass@1分数从15.6%飙升至71.0%，经多数投票后更高达86.7%，与OpenAI-o1-0912的性能持平。

这恰好契合安全分析的核心需求。深信服针对DeepSeek-R1在安全领域的落地实践进行了深度验证，发现该模型在**钓鱼攻击检测、数据安全防护、辅助安全运营研判**等业务场景具备显著的技术适配性和业务价值提升空间。在实际部署中，某企业的网络安全预扫描平台将DeepSeek-R1与Nmap扫描引擎深度整合，实现了从扫描数据输入到模型智能分析再到结构化报告输出的全链路自动化，扫描效率提升75%，高危漏洞响应时间从48小时大幅缩短至2小时，风险漏判率从传统的30%降至10%。

### 成本优势：训练和推理双低

DeepSeek-R1“满血版”的总训练成本仅约**29.4万美元**（约合人民币209.5万元），远低于OpenAI等竞争对手动辄数千万美元的投入。而蒸馏出的1.5b版本进一步放大了这一成本优势：它可以在个人设备上零成本运行，完全不需要云计算资源的持续投入。

对于预算有限的安全团队、独立研究员或学生来说，这意味着一套完全可落地的本地化方案, 性价比极高。

---

## 在国内网络环境下安装Ollama

> **为什么用Ollama？** 超过89%的DeepSeek-R1本地化部署案例依赖Ollama框架。它把AI模型的下载、配置、运行简化到了极致，让我们免去手动处理Python依赖、PyTorch版本兼容、模型权重文件等繁琐步骤。

由于网络环境限制，国内用户直接访问Ollama官方源常常超时或极慢。Ollama中文网（ollamacn.github.io）提供了一个专门为中国大陆用户打造的加速方案，通过国内镜像源和优化脚本解决这一问题。

### Linux/macOS安装（推荐方案：ghproxy.cn镜像）

**设置国内镜像源环境变量:**

```
export OLLAMA_MIRROR="https://ghproxy.cn/https://github.com/ollama/ollama/releases/latest/download"
```

```
执行安装脚本（已替换下载地址
```

```
curl -fsSL https://ollama.com/install.sh | sed "s|https://ollama.com/download|$OLLAMA_MIRROR|g" | sh
```

****预期输出：****

```
>>> Downloading ollama for linux/amd64...######################################################################## 100.0%>>> Installing ollama to /usr/local/bin...>>> Adding ollama user to render group...>>> Adding your user to ollama group...>>> Systemd detected. Creating ollama service...>>> NVIDIA GPU detected, setting up nvidia toolkit...>>> The Ollama API is now available at 127.0.0.1:11434.>>> Run 'ollama --help' for commands.
```

> 看到 The Ollama API is now available... 表示安装成功。

---

验证安装

```
ollama --version
```

**预期输出：**

```
ollama version is 0.6.2
```

---

**备选方案：通过 Ollama 中文网一键安装**

**Ollama 中文网（ollamacn.github.io）专门为国内用户提供了**“一键安装脚本”和“可视化安装教程”**，整个流程更贴近普通用户习惯。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa2iaK6dCk6meG1G1WmLA6ZWTFWuicot9GEYpFNWvDNgxbHhx2wTX54XVibrG4glwicRa4d0kUdYZqd9G11kfl2Uu3hWYnvhHAlFgiaY/640?wx_fmt=png&from=appmsg)

**macOS 用户：**

安装成功后，你会在 **“应用程序”文件夹** 中看到一个名为 **Ollama** 的程序。它的图标是一个羊驼剪影。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1RzBPO8kuG3eDmmjOdGEc58wFtE8QDUXiaCEUBh9zqv8UDmgCquQ60r42iaVRxcRjheFteN0p7NIl2OFQCHztJp8Ey6xacxaRn8/640?wx_fmt=png&from=appmsg)

**Windows 用户：**

安装程序会在你的开始菜单中添加 “Ollama” 快捷方式，同样点击即可启动。系统托盘区会出现 Ollama 图标，表示后台服务已就绪。

**Linux 用户：**

**如果用的是桌面版，部分发行版也会在“应用程序”菜单中创建 Ollama 的启动项，点击即可。**

---

### 拉取并运行 DeepSeek-R1:1.5b; 在终端:

```
$ ollama pull deepseek-r1:1.5b
```

### **预期输出（模型文件较大，会显示下载进度）：**

```
pulling manifestpulling 6a9c4e5b4e3d... 100% ▕██████████████████████▏ 1.1 GBpulling 3f7a8b9c0d1e... 100% ▕██████████████████████▏  11 KBpulling 8b6c5d4e3f2a... 100% ▕██████████████████████▏  495 Bverifying sha256 digestwriting manifestsuccess
```

**![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa2OjOqmdXIdCf5Tkqf7hdCXfqeAvwhxNdy9PuBqibD3ibQyjB5lepdA9kMc5muo6C7wB0KJGu8vLGicaZLEQiaRLoiaTuibUG3jM5Obg/640?wx_fmt=png&from=appmsg)**

**下载完成后启动模型：**

```
$ ollama run deepseek-r1:1.5b
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa1O4xQ2Sw9fiarN41BG4uicmaL813A1TgYP6PPWSPQN7rd9napjeFALLpzL8OJKKzc0MOsxmtKFrpamRhCD58zJziaWIeAoweIGj4/640?wx_fmt=jpeg)

****预期输出:****

```
>>> Send a message (/? for help)
```

****现......在你.....就....可以! 直接......提问了~****

---

****假设你已经用 `ollama run deepseek-r1:1.5b` 启动了模型，然后输入以下 prompt（直接将 nmap 结果粘贴进去）：****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa25PBtrDZB3NQ0b62AxBGBaKB43kxjHZZhP3vqx6EL24OaDVB5YdUjRt1KFhxhNxJXFET7Cicq7Gc3c7594ibSiaVsic4ibpg39XAFY/640?wx_fmt=png&from=appmsg)

扫描之后，

```
>>> 你是一名渗透测试专家。请根据以下 nmap 扫描结果，分析目标系统可能的薄弱点，并推荐下一步渗透策略。
Nmap scan report for 10.10.10.15Host is up (0.012s latency).Not shown: 995 closed portsPORT     STATE SERVICE    VERSION22/tcp   open  ssh        OpenSSH 7.4 (protocol 2.0)80/tcp   open  http       Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)445/tcp  open  netbios-ssn Samba smbd 4.7.13306/tcp open  mysql      MySQL 5.7.328080/tcp open  http-proxy Squid http proxy 3.5.20
```

**模型典型输出**

（注意：1.5b 版本有时会先生成 `thinking` 推理链，再给出回答）：

```
<thinking>开放了 SSH、HTTP、SMB、MySQL 和 Squid 代理。- SSH: OpenSSH 7.4 可能存在用户枚举漏洞，比如 CVE-2016-6210。- Apache 2.4.6 搭配 OpenSSL 1.0.2k，可能受 OpenSSL 安全漏洞影响，但该版本相对较老，需要具体查一下已知漏洞。- Samba 4.7.1 容易受到 SambaCry (CVE-2017-7494) 远程代码执行漏洞攻击，前提是共享可写。- MySQL 5.7.32 是一个较新的版本，但弱口令或配置不当仍可能是突破口。- Squid 3.5.20 作为 HTTP 代理，可能被用来作为跳板或存在 SSRF，也可能存在访问控制绕过。
攻击路径建议：先尝试 Samba 漏洞，如果不可写则转向 Web 应用漏洞，最后暴力 SSH 或 MySQL。</thinking>
根据扫描结果，该目标存在多个潜在攻击面，建议从以下几个方面依次尝试：
1. **Samba 远程代码执行（CVE-2017-7494）**     Samba 4.7.1 默认可能存在可写的共享，如果找到可写路径，可利用该漏洞直接获得 root 权限。     → 工具：Metasploit 模块 `exploit/linux/samba/is_known_pipename`。
2. **Apache httpd 2.4.6 已知漏洞**     该版本发布较早，可能存在多个严重漏洞（如 CVE-2017-9798，选项泄露敏感信息）。建议先用 Nikto 扫描 Web 目录，并结合 CMS 指纹识别进一步挖掘。     → 工具：`nikto -h http://10.10.10.15`，`whatweb http://10.10.10.15`
3. **MySQL 弱口令爆破或 UDF 提权**     若 MySQL 允许远程连接（注意 3306 端口对外开放），可尝试常用弱口令组合。若能登录且有 FILE 权限，可尝试 UDF 提权。     → 工具：`hydra -l root -P /usr/share/wordlists/rockyou.txt mysql://10.10.10.15`
4. **Squid 代理利用**     Squid 3.5.20 可能存在访问控制缺陷，如果代理未认证，可用于内网扫描或作为 C2 通道。需进一步检查代理是否需要认证及其 ACL。     → 工具：`curl -x http://10.10.10.15:8080 http://内网地址` 测试是否可转发。
5. **SSH 用户枚举与爆破**     OpenSSH 7.4 可能允许基于时间的用户枚举（CVE-2016-6210），确认存在有效用户名后再进行密码爆破。     → 工具：`msf> use auxiliary/scanner/ssh/ssh_enumusers`
**下一步优先行动**：先针对 Samba 漏洞进行检测与利用，因其风险最高且利用难度最低。同时可并行开展 Web 应用目录扫描，以增加攻击向量。
```

---

没了........只有这些，嘻嘻

![](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa3KppiaHHu237s45nwc7ibYricglicC2rB25rA5hDL2kyIV9h0tTkKjUnMJMgkCms9XMoaBib2aVhzFZ8KB6vibDPMCQGicyibuqE0wgSs/640?wx_fmt=webp&from=appmsg)

---

******如果觉得我这个教程对你有帮助的话，给我点个关注可不？再进我的群头吹壳子嘛～******

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa33GIPyfeJDpzM8enxGvJvYV8OkiaynViaqBXa1qYP3cw9QD7yK1Uz5mh59ic2TbO3Js8sz5AEJpGkahlGdicqz3RicZfb1YYZ6Jrc8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa2txHr3eLicyjGuDTqicbtQYHhzftQR6r4AzH5zvFH6Aq2VGSI7btmyr9BgumWAFiaZibRsZQqchiaDcIfVgvqzntxzMn29JmYw0z8M/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9Xx8EkicjWicEcd3af9D02mtgshZPKdXndvibwGAzfG6JYkbK8kTEkptqlGSicib2OmskYW3OQohNwTqz3RdpV0sIIQ/640?wx_fmt=jpeg&from=appmsg)

#哪吒网络安全 #ollama #deepseek #部署 #ai

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn...