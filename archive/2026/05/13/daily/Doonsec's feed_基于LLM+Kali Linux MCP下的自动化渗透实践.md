---
title: 基于LLM+Kali Linux MCP下的自动化渗透实践
url: https://mp.weixin.qq.com/s/6zJr7wVUMxshmNwsqDX2mg
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:32.133266
---

# 基于LLM+Kali Linux MCP下的自动化渗透实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wd3JaJGKlfteMcZQ7AtbjSwameVeedTamRkmhxiaLelNoJeAH8VRu4SeCicCjngmH4pyuYbzT8Zqw3yOegDQVH6g/0?wx_fmt=jpeg)

# 基于LLM+Kali Linux MCP下的自动化渗透实践

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于487Donkey Sec
，作者CyberSecurity

![](http://wx.qlogo.cn/mmhead/2pm5Nb2cMaPG4uGSAN6V8vJ6JiabzAfXuH272Po9CQ2MpceX6NkqvnuhvwibQy4t5Zk88NPoS6c0k/0)

**487Donkey Sec**
.

487DonkeySec团队介绍：团队长期活跃于国内攻防一线，为实时跟进攻防技术，秉持着凌晨四点睡，早晨八点起，干七天的健康作息，自称487驴。 团队方向：Web攻防，杀软对抗，漏洞挖掘，安全运营，内网渗透。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaPicdRozwUYY1r0OKMoqGq8hqSAlJicwqqbiazib3xtaQOSEGazz0zrgn5w/640?wx_fmt=png&from=appmsg)

    在我们开始实践部署之前，我们需要先了解一下什么是LLM，什么是MCP，以及实现自动化渗透的基本逻辑，本文将讨论本地化部署以及利用互联网API接口部署两种方案的具体实现方法。

LLM的概念

    LLM（Large Language Model，大语言模型是一个通过在海量文本上训练“下一个词预测”任务而获得强大语言理解和生成能力的人工智能模型。

你可以把它想象成一个在海量文本数据上完成了“深度学习”的“语言天才”。它通过学习数十亿甚至数万亿的单词、句子和段落，掌握了语言的统计规律、语法结构、事实知识以及上下文逻辑。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTavT9X6KtRia9Aqpic3RpnTMdm2ysh8fryfFCsNQtKBoMzWEOHAWXrodxg/640?wx_fmt=png&from=appmsg)

MCP的概念

    MCP（Model Context Protocol） 是一个开放协议，旨在标准化大型语言模型（LLM）与外部工具、数据源和应用程序之间的通信方式。

你可以把它想象成 AI 模型的“USB 标准”或“应用商店”。它为 AI 模型提供了一个统一、安全的方式来发现、调用和利用外部资源和功能，极大地扩展了模型的能力，而无需修改模型本身。

MCP Server的概念

    MCP（Model Context Protocol，模型上下文协议）Server是基于MCP协议实现的服务器，它作为大型语言模型（LLM）与外部数据源、工具和服务之间的桥梁。

    MCP协议由Anthropic于2024年11月底推出，是一种开放标准，旨在统一大模型与外部数据源和工具之间的通信协议。MCP的主要目的在于解决当前AI模型因数据孤岛限制而无法充分发挥潜力的难题，使AI应用能够安全地访问和操作本地及远程数据，为AI应用提供了连接万物的接口。

    MCP定义了应用程序和AI模型之间交换上下文信息的方式。这使得开发者能够以一致的方式将各种数据源、工具和功能连接到AI模型，就像USB-C让不同设备能够通过相同的接口连接一样。MCP的目标是创建一个通用标准，使AI应用程序的开发和集成变得更加简单和统一，从而促进AI生态系统的发展。

MCP Client的概念

    MCP Client 指的是一个能够理解并遵循“模型上下文协议”（Model Context Protocol, MCP）”的应用程序，它主要负责向MCP Server请求资源或工具执行，并将获取的结果整合到自己的上下文中，最终提供给用户或大语言模型（LLM）使用。

* 对于用户/LLM来说：Client是功能的提供者。用户或LLM通过Client来访问那些它本身不具备的能力（如读取本地文件、查询数据库等）。
* 对于Server来说：Client是资源的请求者。它向Server发起规范的请求，并接收Server返回的数据。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaRKk48OtQm8U4fyqNhfYFlf0P1LoWia5dKozcv9NPGVXfDt9dRIkiaYtw/640?wx_fmt=png&from=appmsg)

自动化渗透实践

    前面的介绍，相信大家已经对MCP协议、MCPServer、MCPClient、LLM有了一定的了解。现在我们使用Cherry Studio作为MCPClient，Kali Linux 作为MCP Server，DeepSeekAPI作为MCP hosts来实现自动化渗透的尝试。

本次实践所需的工具的下载地址

```
https://www.python.org/getit/                    #python官网
https://www.kali.org/get-kali/#kali-platforms    #Kali Linux官网
https://platform.deepseek.com/                   #DeepSeekAPI控制台
https://github.com/CherryHQ/cherry-studio        #CherryStudio项目地址
https://github.com/Wh0am123/MCP-Kali-Server      #MCP-Kali-Server项目地址
```

LLM自动化攻击流程的步骤拆解

（Kali Linux+Kali MCP Server+DeepSeekAPI+Cherry Studio）

    用户通过 Cherry Studio 的AI中台的 DeepSeekAPI 接口向位于互联网的LLM发送任务要求，LLM根据任务内容以及提前配置好的 MCP Server 来创建对应的动作就是利用 Kali Linux 中的 Metasploit 来进行漏洞利用。

    动作流程生成完后通过 Cherry Studio 作为中间人来调用 MCP Server 控制 Kali Linux 进行漏洞利用，此时等待漏洞利用完成回显结果。漏洞执行的结果会先回显到 Metasploit 控制台，再由 MCP Server 将命令执行的回显的结果返回给 Cherry Studio 继续处理，接收到回显结果后再次通过 DeepSeekAPI 接口交由LLM对回显结果进行分析，生成中文漏洞测试报告发送到 Cherry Studio，流程结束。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTayzGt37M5Wc808ZKfRkgGTxY9cFQqrYWeLlzgpvTejYlnU1voOlFxbA/640?wx_fmt=png&from=appmsg)

首先准备我们所需的环境

```
虚拟机中安装Kali Linux系统。
宿主机安装Cherry Studio。
DeepSeek官网充值获取API接口。
github上下载MCP Server的Python脚本。
```

配置Kali Linux/MCP Server

```
git clone https://github.com/Wh0am123/MCP-Kali-Server.git    #下载Kali_MCP_Server
cd /MCP-Kali-Server
python3 kali_server.py    #启动kali_server服务
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTae0ZXIs0PeXMuicVdK4jYABS1qAVH7TJu6eEWEbgXry1hOxEjYoaCPCQ/640?wx_fmt=png&from=appmsg)

生成DeepSeekAPI

    登陆DeepSeek开放平台在功能菜单中选择API keys，选择创建API key，随便取一个名称，将创建出来的API key复制下来保存好，关闭窗口后不能再复制，只能重新生成。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTa3w8ZEN5BbicZSjTNVVtgIvU5M9p7PgficdicewibvKibtWB1Y904qQK1Zyg/640?wx_fmt=png&from=appmsg)

配置CherryStudio

    因为这里我们需要本地启动 mcp\_server.py 来远程调用Kali\_Server所以要求安装CherryStudio客户端的设备具备python3的环境，以及mcp的库。

```
pip3 install mcp --break-system-packages    #安装mcp库
python3 mcp_server.py --server http://172.16.199.130:5000/    #测试启动 MCP Server 远程连接 Kali Server
```

    运行MCP\_Server后，提示我们Kali缺少gobuster工具，这时候我们可以到Kali Linux中用apt命令进行安装，同理如缺少其他工具也是一样的操作步骤。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaEgicY70K8a4rGyGNRnxYYHOlsBIqrWS04xTG05oydvPtBqucL4UM8Ug/640?wx_fmt=png&from=appmsg)

```
apt install gobuster    #在Kali虚拟机中安装gobuster工具
```

    安装完成后重新启 动MCP Server 不再出现 [WARNING] Server health status: healthy 相关报错。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTax1ITUducqTtG2aq7kAGhfhha0UgibTRNOAicKBDN4zzjbEBsxjXibN4lg/640?wx_fmt=png&from=appmsg)

添加DeepSeepAPI密钥

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTacVHMe4yDnpmTlNGAAGe5ujiaD84vowTQh2p9eqNBmglHmtqSibGXoRmw/640?wx_fmt=png&from=appmsg)

添加MCP服务器

CherryStudio中配置MCP设置

    接下来我们在CherryStudio设置中选择MCP设置，确保添加服务旁边的依赖要求为绿色状态，如不是需先安装相关依赖内容。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaILhlWEjX9P13bhGLAgrfmMPxOaexyDNO0OfwCWy0fOgy69iaHPznF6Q/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaLNiaFdwNGWV0aC3wTYmczTIBo9fniamIeO82jIrSxCvs684o1PXxVorg/640?wx_fmt=png&from=appmsg)

    然后选择添加服务器，选择从JSON导入，修改如下的JSON配置参数后复制添加。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaLDqpMf81LoqquFEoyRXOOAdkbVjZlAZSRPjzcFCvS80iabC2IDq2cUg/640?wx_fmt=png&from=appmsg)

```
{
    "mcpServers": {
        "Kali_MCP": {
            "command": "python3",
            "args": [
                "/Users/xxx/Tools/MCP-Kali-Server/mcp_server.py",
                "--server",
                "http://172.16.199.130:5000/"
            ]
        }
    }
}
```

    修改args配置中的mcp\_server.py文件的路径，以及Kali Linux在局域网中的IP地址，大家根据自己实际存放文件的情况修改JSON配置即可。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaT4MzZ9Gqqgu409Plzbh6rYtZGgiahBviaU0OVheQVU793ibGfWVJ1UzDw/640?wx_fmt=png&from=appmsg)

    查看可用的MCP工具

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTajgzJu5o6QsKlib1f2fNicGmqWTEYg5icadeNp6GaAq7cc40tb9mibTXSxQ/640?wx_fmt=png&from=appmsg)

    可以看到该项目的 MCP Server 支持调用 Kali Linux 中的12款工具，接下来我们需要使用到的是metasploit\_run。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaOmOTMOoxGZPjiaK3icNicFRlMjd6fXhNnggDRMNlRsGwXKlXL3aDzWUHA/640?wx_fmt=png&from=appmsg)

漏洞利用/报告生成

```
扫描192.168.72.41的445端口是否开放
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTawP41QERo14JekLQU2feNwNyWVibA3nmAUUPIVX0R8hdmlF6pRYCibWRA/640?wx_fmt=png&from=appmsg)

```
通过Kali_MCP的metasploit_run工具检查目标192.168.72.41是否存在MS17-010漏洞，并根据结果输出一份中文漏洞测试报告。
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTa3VE77lP8XibPzic34XfHaUGQH4oJcDMFZmAfmhgVbE7iaOMTXpaAibdxAQ/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaPtY615nrNbWicEHFc8lWAkZm5Fwn9Jrrkbiarhn4TvrYFalRyjdEFaUA/640?wx_fmt=png&from=appmsg)

```
利用auxiliary/admin/smb/ms17_010_command模块对测试目标192.168.72.41命令执行并返回whoami的命令执行结果
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaYqCAOjIKdiaFmLTrcDxzYkllp1MsD6At5JH9o9ic63XWKLnMuRYydoNA/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaWNCiavMribga5BwdOdr2XOquxU634gvt6Led902OEMbGbOgDjVTrYIxw/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTamXP2wTU7oVuRrJgvuKicyZL0sYYQahkR20PEVK5LW3ZH6VZ3PRDGUXw/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaFqyBBXJkHzw53LiaEKqTcHayKiaIYKID0oOnOiagTiakKHwic6oLaky1T9Q/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/wd3JaJGKlfteMcZQ7AtbjSwameVeedTaQ7vQNnQD3kNWHRd9z6owQn7RxIgTibYibianhh5DqxRD1UGO5FKyFAQ1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

...