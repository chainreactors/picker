---
title: 「推安早报」0719 | nculei反制、yt-dlp反制、jump漏洞等
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487546&idx=1&sn=d1287857ffd6a62fcd91721f5e93c44d&chksm=fb35b9f2cc4230e4d9b766d19a5a63fd5a716de89c8f0102ed44d5b08628030e54c69e399a62&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-20
fetch_date: 2025-10-06T17:44:02.252070
---

# 「推安早报」0719 | nculei反制、yt-dlp反制、jump漏洞等

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmjr11OHn3icLket3eaqgExkrNibVNTFDFt2ROBhxQeoBNcfAV0xRhZD3lvXWXMgNIspux4H8yTturA/0?wx_fmt=jpeg)

# 「推安早报」0719 | nculei反制、yt-dlp反制、jump漏洞等

bggsec

甲方安全建设

2024-07-19 安全「信息差」

# 每天快人一步

> 1. 推送「新、热、赞」，降噪增效
>
> 2. 查漏补缺，你可能错过了一些小东西

### 0x01 下一代渗透测试工具Atexec-pro：利用任务调度器（无需端口445）

> Atexec-pro是一个基于atexec.py修改的下一代渗透测试工具，它通过任务调度器执行命令，支持文件上传、下载以及.Net程序集的执行，主要依赖TSCH服务，无需使用端口445。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmjr11OHn3icLket3eaqgExkY1Zus5JUlAJiaFIpd7ribfF9lFEjgkQoxGPPqW8MExorCfNVlahyn9Xg/640?wx_fmt=png&from=appmsg)

### 关键信息点

* Atexec-pro工具的设计目的是为了提供一个不依赖端口445的渗透测试工具，通过任务调度器（Task Scheduler）执行命令，增强渗透测试的灵活性和隐蔽性。
* 功能支持方面，Atexec-pro提供了多种操作，包括命令执行、PS命令执行、文件上传、文件下载和.Net程序集执行，但目前对于文件大小有限制。
* 安全性考虑，尽管Atexec-pro支持多种认证方式，但它并不提供绕过AMSI的能力，这意味着用户需要确保其他方面的安全措施，以避免被Windows Defender检测到。
* 易用性和配置性，Atexec-pro提供了详细的命令行参数选项，使得用户可以根据需要配置和使用该工具，包括接口选择、编码格式、认证方式等。

🏷️: 渗透测试, 任务调度器, 网络安全

### 0x02 JumpServer v3.0.0-v3.10.11 存在任意文件写入漏洞导致远程代码执行

> JumpServer v3.0.0-v3.10.11 存在安全漏洞，攻击者可利用 Ansible 播种书（playbook）编写任意文件，导致 Celery 容器中的远程代码执行（RCE），进而可能窃取所有主机的秘密、创建具有管理员权限的新 JumpServer 账户或以其他方式操纵数据库。

### 关键信息点

* JumpServer 的特定版本（v3.0.0-v3.10.11）存在安全漏洞，可能导致严重的安全后果。
* 攻击者可以通过 Ansible 播种书（playbook）编写任意文件，这可能导致 Celery 容器中的远程代码执行（RCE）。
* 由于 Celery 容器具有 root 权限和数据库访问权限，攻击者可以利用 RCE 来窃取敏感信息、创建管理员账户或操纵数据库。
* 攻击者需要具有较低权限的账户并能够访问 Job Center 功能，这是一个前提条件。

🏷️: 安全漏洞, 远程代码执行, Ansible, JumpServer

### 0x03 JumpServer 安全漏洞：Ansible 剧本模板任意文件读取

> JumpServer v3.0.0-v3.10.11 版本中存在一个安全漏洞，允许攻击者通过创建恶意的 Ansible 剧本模板来读取 Celery 容器中的任意文件，这可能导致敏感信息泄露。

### 关键信息点

* 该漏洞主要影响了 JumpServer 的 `v3.0.0` 到 `v3.10.11` 版本。
* 攻击者可以通过 Job Center 功能利用此漏洞，即使是使用低权限账户也能实施攻击。
* Celery 容器的 root 权限和数据库访问权限增加了漏洞的严重性，因为它允许攻击者获取敏感信息或进行进一步的攻击。
* 强烈建议 用户升级到 `v3.10.12` 或 `v4.0.0` 版本以确保安全。

🏷️: 安全漏洞, Ansible, JumpServer, 信息泄露

### 0x04 CVE-2024-38519: youtube-dl 及 yt-dlp 的路径遍历漏洞导致 RCE

> 安全实验室发现youtube-dl及yt-dlp在处理字幕文件时存在Path Traversal漏洞，可能导致远程代码执行（RCE）。

### 关键信息点

* youtube-dl及yt-dlp的安全漏洞源于对字幕文件扩展名的不充分验证，导致Path Traversal漏洞。
* yt-dlp是youtube-dl的分支，自youtube-dl停止维护后，yt-dlp已成为大多数用户的首选视频下载工具。
* Path Traversal漏洞可能允许攻击者执行远程代码（RCE），这是因为在构建字幕文件名时，不存在的路径被允许，特别是在Windows系统上。
* 安全实验室提供的XML示例展示了如何利用这一漏洞，通过托管恶意XML文件来实现RCE。

🏷️: CVE, youtube-dl, yt-dlp, 路径遍历, RCE

### 0x05 OpenAI发布成本效益高的GPT-4o mini模型

> OpenAI推出了GPT-4o mini，这是一款成本效益高的小型模型，旨在使AI应用更加普及和经济。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmjr11OHn3icLket3eaqgExkI21nbGS3YwkxFSVCOs4Tuog1jS0DVXeyyTcdo10kd2EOX0BKn20qqg/640?wx_fmt=png&from=appmsg)

### 关键信息点

* GPT-4o mini的成本效益：GPT-4o mini的价格显著低于之前的先进模型和GPT-3.5 Turbo，使得AI技术更加普及和经济。
* 性能提升：GPT-4o mini在MMLU、MGSM和HumanEval等基准测试中的表现优于其他小型模型，特别是在文本智能、数学和编码能力、多模态推理方面。
* 增强的安全性：OpenAI将安全性作为模型开发的重要组成部分，通过预训练和后训练的各种技术来加强模型的安全性，包括RLHF和指令层次结构方法。
* 更广泛的应用：GPT-4o mini支持文本和视觉模式，并计划支持图像、视频和音频输入输出，这使得它能够适用于更多种类的应用场景。

🏷️: OpenAI, GPT-4o mini, 成本效益, AI应用, 小型模型

### 0x06 SolarWinds Access Rights Manager曝出远程代码执行漏洞

> SolarWinds Access Rights Manager 存在一个远程代码执行漏洞，攻击者无需身份验证即可利用该漏洞在受影响的安装中执行任意代码。

### 关键信息点

* 未经身份验证的远程代码执行：攻击者不需要任何身份验证就能利用这个漏洞，这增加了攻击的可能性和危害。
* 系统级别的权限：成功利用该漏洞的攻击者可以在 SYSTEM 权限下执行代码，这是 Windows 操作系统中最高级别的权限，能够对系统进行深远的控制和修改。
* 严重的安全风险：由于漏洞的存在，可能导致整个系统的安全受到威胁，攻击者可以安装程序、查看、更改或删除数据，或者创建新的账户。
* EndUpdate 方法的设计缺陷：该漏洞的存在表明在 SolarWinds Access Rights Manager 的设计或实现中存在关键的安全缺陷，需要通过安全更新或补丁来解决。

🏷️: 漏洞, 远程代码执行, 网络安全, SolarWinds

### 0x07 XBOW技术破解加密

> 网页主要介绍了XBOW如何利用padding oracle攻击来破解加密算法，并成功地解密了一个用于身份验证的加密cookie。

### 关键信息点

* Padding oracle攻击展示了在实际应用中，即使是微小的实现错误也可能导致严重的安全漏洞。
* CBC模式加密虽然广泛使用，但如果没有正确处理，也是容易受到攻击的。
* PKCS #7填充方案虽然便于去除填充，但也为攻击者提供了利用的可能性。
* XBOW的成功攻击证明了自动化渗透测试工具在发现和利用加密漏洞方面的高效性和实用性。

🏷️: Padding Oracle攻击, 加密破解, 加密安全

### 0x08 利用Windows安装程序的通用操作实现潜在安全漏洞

> 文章主要探讨了Windows Installer服务中的一个未修复的漏洞，该漏洞可以被利用来提升本地用户的权限。

### 关键信息点

* Windows Installer服务的未修复漏洞可以被利用进行权限提升。文章强调，尽管微软通过重定向守护减轻了symlink攻击的风险，但并没有直接解决漏洞的根本问题。
* 自定义动作是实现MSI安装扩展功能的关键。自定义动作可以采用多种形式，但也带来了安全风险，因为它们可能会依赖不受信任的资源或在不必要的权限级别上运行。
* 普通用户可以利用自定义动作中的漏洞来执行具有系统完全权限的命令。这可能导致本地权限提升，为恶意用户提供了一种攻击手段。
* 微软对于该漏洞的处理不充分。文章指出，微软没有能够复现该问题，因此将其标记为无法复现并关闭了相关报告，尽管该漏洞在最新的Windows版本中仍然存在。

🏷️: Windows Installer, 安全漏洞, 命令执行, 文件删除, 系统权限

### 0x09 项目发现 /nuclei中未签名代码模板的执行漏洞

> GitHub 上 projectdiscovery/nuclei 项目中存在一个未签名代码模板执行漏洞，允许通过工作流文件执行代码，而不需要 `-code` 选项和签名。

### 关键信息点

* 该漏洞利用了 `-w` 选项来执行工作流文件，而不是通常用于执行代码模板的 `-t` 选项。
* 攻击者可以通过编写恶意的 `code.yaml` 文件，其中包含 `workflows` 字段，来执行任意命令。
* 该漏洞可能影响那些将 Nuclei 用于安全扫描的 web 应用程序，允许用户编辑和执行工作流文件。
* 漏洞的存在表明，即使在安全工具本身中，也可能存在安全漏洞，这可能会被利用来进行二次攻击。

🏷️: security\_vulnerabilities, code\_execution, workflows, projectdiscovery, nuclei

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZlbmEWU7ZApsl3ia3YLicI4H3nwksKq8ZBqrghjtia9TYiblaxU2VXrUpDcAM57Ric0wX9pBg69IusWVyg/640?wx_fmt=jpeg)

快来和老司机们一起学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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