---
title: 还在手动敲Kali命令？一句话就可以让Kali自动完成渗透测试
url: https://mp.weixin.qq.com/s/NfA0OR5HX8fT5JLTH60n9w
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:59:11.819108
---

# 还在手动敲Kali命令？一句话就可以让Kali自动完成渗透测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xKicFZ2TIFt9FwLVtG8T3qvRgM4BHt3EnlicMSFwDOQmHPRZhUY42AtJgY2NOBwskd5dTkAl6PCwWkTwqsAAEkQsb3M3xQJx0JrRDOPOEFI30/0?wx_fmt=jpeg)

# 还在手动敲Kali命令？一句话就可以让Kali自动完成渗透测试

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt88w1KPZdDJOA2W5wrOREEG4OZkG4DRfexW1dMGYPAlchJQ8Q7wYEkcouzrKK54vatqqmiaJj1WYnrkUEVvMGM80ficcdSmk0wpw/640?wx_fmt=png&from=appmsg)

网络安全行业迎来全新的工具使用范式革新——通过整合macOS系统、Claude Desktop、Claude Sonnet 4.5与Kali，可直接通过自然语言描述，完成端口扫描等任务，无需手动输入复杂的终端命令。该方案基于MCP实现大模型与外部工具的无缝联动，解决了Linux平台无官方Claude Desktop GUI支持的痛点，大幅降低了渗透测试工具的使用门槛，同时也为网络安全自动化运营提供了全新的技术思路。

## 当Kali遇上大模型

Kali Linux作为全球网络安全从业者公认的渗透测试标杆系统，预装了海量专业安全工具，但传统使用模式依赖用户对终端命令的掌握，存在一定的入门门槛。与此同时，大模型技术的快速发展，让自然语言转专业指令的能力实现了质的突破。

此前，Linux平台并无Anthropic官方推出的Claude Desktop桌面客户端，用户只能通过社区方案、WINE兼容层等非官方途径使用GUI界面，存在稳定性与安全性隐患。而本次推出的跨系统联动方案，通过SSH实现macOS与Kali Linux的安全通信，借助MCP协议打通大模型与Kali工具的调用链路，既保留了Claude Desktop官方原生的GUI体验，又充分发挥了Kali Linux的专业渗透测试能力，实现了两大系统的能力互补。

## 核心架构：三大系统+MCP协议

整套方案的核心是三大独立系统的联动，配合模型MCP实现端到端的自然语言任务执行，整体架构分为三个核心层级：

* **UI交互层**：Apple macOS系统搭载Claude Desktop客户端，作为用户与大模型交互的图形化界面，同时承担MCP客户端的角色；
* **核心能力层**：云端的Claude Sonnet 4.5大模型，负责自然语言理解、任务拆解与指令生成，是整套方案的“大脑”；
* **工具执行层**：Kali Linux，搭载各类专业安全工具与MCP服务端，负责接收并执行大模型下发的指令，返回执行结果。

其中，**MCP** 是整套方案的核心桥梁，它实现了大模型与外部工具、数据源的无缝连接，让大模型可以自主调用Kali Linux中的各类工具完成任务。完整的执行流程如下：

1. 用户通过自然语言向Claude Desktop下发任务指令，例如“对scanme.nmap.org进行端口扫描，若发现可用web服务器，检查其security.txt文件是否存在”；
2. Anthropic Sonnet 4.5大模型完成自然语言理解，拆解为可执行的分步技术任务；
3. 大模型通过MCP客户端向Kali Linux的MCP服务端发起工具调用请求，确认工具可用性并下发执行指令；
4. Kali Linux完成指令执行后，通过MCP协议将结果返回给大模型；
5. 大模型对结果进行解析处理，若任务未完成则循环发起新的指令调用，直至完成用户的全部需求，最终向用户输出可视化的任务结果。

## 环境搭建

整套方案的搭建分为Kali Linux服务端配置、macOS客户端配置、MCP与Claude联动配置三个环节，全程可在2026年1月的版本环境中完成。

### Kali Linux端环境配置

Kali Linux可部署在本地局域网或云端服务器，云端部署可获得更优的网络连接速度与目标访问延迟，核心配置步骤如下：

1. **SSH服务安装与启用**若Kali环境未预装SSH服务，需执行以下命令完成安装与开机自启配置，实现与macOS的安全通信：

   ```
   sudo apt update
   sudo apt install -y openssh-server
   sudo systemctl enable --now ssh
   ```
2. **MCP服务端与核心工具安装**本次方案采用`mcp-kali-server`作为MCP服务端，需执行以下命令完成安装：

   ```
   sudo apt install -y mcp-kali-server
   ```

   安装完成后，执行`kali-server-mcp`命令启动服务，正常情况下服务将运行在`http://127.0.0.1:5000`地址。若访问该地址出现**“URL拼写可能存在错误，请检查”**的报错，需优先检查服务是否正常启动、端口是否被占用，或依赖包是否安装完整。

   这里需要重点注意：**Kali Linux最小化安装环境默认未预装任何渗透测试工具**。根据Kali官方2025年6月更新的最小安装配置文档，最小化安装不会预装`kali-linux-headless`元包及任何`kali-tools-`系列工具，这会导致MCP服务启动后提示`dirb、gobuster、nikto、nmap`等核心工具缺失。需执行以下命令补全常用渗透测试工具：

   ```
   sudo apt install -y mcp-kali-server dirb gobuster nikto nmap enum4linux-ng hydra john metasploit-framework sqlmap wpscan wordlists
   sudo gunzip -v /usr/share/wordlists/rockyou.txt.gz
   ```
3. **服务可用性验证**新开终端执行`mcp-server`命令，若终端输出`Successfully connected to Kali API server at http://localhost:5000`与`Server health status: healthy`，则说明Kali端环境配置完成。

### macOS客户端环境配置

macOS端核心完成SSH密钥对配置、Claude Desktop安装与MCP客户端配置，实现与Kali Linux的免密通信和大模型工具调用能力：

1. **SSH密钥对生成与免密登录配置**打开macOS终端，先检查本地是否已有SSH密钥，若无则通过`ssh-keygen`命令生成ed25519类型的密钥对，全程可按回车使用默认配置，也可自定义密码提升安全性。 密钥生成完成后，执行以下命令将公钥推送至Kali Linux服务器，实现免密SSH登录：

   ```
   ssh-copy-id kali@192.168.1.30
   ```

   推送完成后，执行`ssh kali@192.168.1.30`命令测试登录，若无需输入密码即可进入Kali终端，则说明免密配置成功。
2. **Claude Desktop安装与MCP客户端配置**从Anthropic官网下载Claude Desktop安装包，完成安装后登录账号。 打开Claude Desktop设置，进入「Developer」选项，点击「Edit Config」打开配置文件`claude_desktop_config.json`，在文件中添加以下MCP客户端配置（同样需替换Kali服务器IP）：

   ```
   {
     "mcpServers": {
       "mcp-kali-server": {
         "command": "ssh",
         "args": [
           "kali@192.168.1.30",
           "mcp-server"
         ],
         "transport": "stdio"
       }
     }
   }
   ```

   配置完成后，完全退出并重启Claude Desktop，使配置生效。

## 功能验证

环境配置完成后，通过经典的端口扫描场景完成验证。在Claude Desktop中输入自然语言指令：“请帮我对scanme.nmap.org进行端口扫描”，即可触发整套流程的执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt9YQJggeyxsoDkU4H2Brpxo1ZEOI5tZiaz3OXHgzEiagrZtfHEYZVZwoEVDYbJ68zZgSVzOsx24QwVfVDrCVKFmEjHstCib3SK2o0/640?wx_fmt=png&from=appmsg)

Claude Desktop会先弹出MCP工具调用权限确认，用户授权后，大模型将通过MCP协议向Kali Linux发起工具调用请求，自动执行nmap端口扫描命令。从后台服务日志可看到，大模型会先确认nmap等工具的可用性，再下发具体的扫描指令，扫描完成后将结果通过MCP协议返回，最终由大模型解析为通俗易懂的自然语言结果展示给用户。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFtibJcAgm6H67IxpNoibwTXvgUAWhtvm3ia4saxj6WIVZfTtBAibfDKZZ602kD7c1QgBNiaPv3YNsOg2tmhCpzrXePSxzmVQ8jQfl9sM/640?wx_fmt=png&from=appmsg)

整个过程中，用户无需记住任何nmap命令参数，仅通过一句自然语言描述，即可完成操作，大幅降低了工具使用门槛，同时也提升了批量任务的执行效率。

## 点评

这个案例说白了就是一个Hello World，全程只调用了最基础的 nmap，但必须承认，它实实在在降低了Kali 的入门门槛。以前小白光背命令、踩坑跑通第一次扫描就要熬好几天，现在再装个Typeless就能动动嘴完成基础渗透了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnLIqb6wTzbSErRKzmg7cicZCtQB7Yz9PaKF4ichseJFxMOjJvgVtLVLmwInwfM88sTYvibpCibA7e6DMA/640?wx_fmt=png&from=appmsg)

**以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。**

*参考资料:*

1. https://www.kali.org/blog/kali-llm-claude-desktop/
2. https://gitlab.com/kalilinux/packages/mcp-kali-server

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

玄月调查小组

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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