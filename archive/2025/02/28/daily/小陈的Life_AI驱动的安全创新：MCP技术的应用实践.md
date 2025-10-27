---
title: AI驱动的安全创新：MCP技术的应用实践
url: https://mp.weixin.qq.com/s?__biz=MzAxNDk0MDU2MA==&mid=2247484563&idx=1&sn=40a58bb09da26af940bf1958aa28c471&chksm=9b8ae46cacfd6d7ae69627646a9ce89cbe1a440def99da1f715d4a44224ab6d5eb93b201f742&scene=58&subscene=0#rd
source: 小陈的Life
date: 2025-02-28
fetch_date: 2025-10-06T20:47:38.394847
---

# AI驱动的安全创新：MCP技术的应用实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78kuQ0djBFl8iaYoqbfMribhGwwV4ibQRpeQmuONAthO6LCLict1QYDHha4A/0?wx_fmt=jpeg)

# AI驱动的安全创新：MCP技术的应用实践

原创

Leiothrix

小陈的Life

## 前言

在2024年11月25日，由知名大模型Claude的母公司Anthropic发布模型上下文协议（MCP, Model Context Protocol），旨在解决AI模型因信息孤岛而无法高效访问外部数据的难题。它通过提供一个通用的标准接口，让AI应用能轻松连接到各种数据源，如数据库、API和企业工具。

我真正注意到这个概念是在2025年1月，当时正值DeepSeek爆红以及Cline开发插件的流行时期。Cline作为首批支持MCP的应用插件之一，让我对这个概念产生了浓厚的兴趣，但因为春节期间只想着好好享受假期，也就草草的上网搜了一下简介了解了个大概。

如果想寻求安全中如何利用大模型来为自己的基础设施服务提高效率，如何将LLM真正融入到企业级的CI/CD中，以及针对大规模多事件的运维处理事项上。开发一个定制化的MCP一定是众多解决方案中效果最好，扩展性最高的。

## MCP介绍

正如前言中所述，MCP通过一个通用的标准接口，可以让AI应用能轻松连接到各种数据源，因此也被人们称之为针对LLM的USB-C接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78Vmj5RPR02vv1ibYicsicweQiaynRwbJPwiaEfeCrHnmhJ8eicS5pORdWrtzQ/640?wx_fmt=png&from=appmsg)

如上图MCP的架构图所示，大致由五个部分组成：

* MCP Host：可以理解为你所需要通过MCP调用数据源的程序和工具。
* MCP Client：负责将工具的请求转换为MCP可识别的调用。
* MCP Server：轻量化的程序，如文件系统、Web搜索、数据库等服务。
* Local Data Sources：本地需要访问的数据资源。
* Remote Service：公开可调用的MCP接口等远程数据资源。 目前所支持的服务系统可以在GitHub仓库上找到：https://github.com/modelcontextprotocol/servers

而这里的MCP，指的就是一种开放协议，标准化了AI应用与外部数据源和工具的集成方式。其核心架构就为上图所示的客户端-服务器模型。根据MCP的介绍，MCP提供以下关键功能：

* 一系列预构建的集成，方便LLM直接使用。
* 灵活性，支持在不同LLM提供商和供应商间切换。
* 安全最佳实践，确保数据在基础设施内的安全性。

而在我写这篇文章的时候，翻阅了不少关于MCP的介绍文章，其中大部分的判断是MCP的出现不亚于Web动态语言的这一重大改革，还有一部分是说MCP是朝着LLM界的LSP（Language Server Protocol）标准对齐。而不管怎么说，这的确能让中小推理模型可以更好的结合上下文和获取到的基础数据，更好的提高模型能力，以用于解决复杂场景下机械性、重复性的工作。

其中，还有提到一个llms.txt的标准，将其类比Web2.0时期的robots.txt，用于帮助推理模型发现暴露的MCP、Agent等接口服务，让模型在访问到项目中的llms.txt就可以直接安装、使用对应的服务。

## MCP应用场景

因MCP适用于多种需要AI访问外部数据的情况下，所以应用场景多数为：

* AI驱动的IDE，连接代码仓库和开发工具。
* 增强聊天界面，整合知识库和客户数据。
* 定制AI工作流，访问数据库和企业系统。

为了能够更直观的理解MCP带来的LLM效能提升，我这里再引入一个使用案例辅助读者更好的理解这一概念。

首先我们可以在本地安装一个调试工具，这个工具在之后不论是测试还是开发都可以用到

```
npx @modelcontextprotocol/inspector
```

以官方的文件系统工具为例：https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem 该MCP服务可以通过调用对应的工具访问到本地的文件和目录，将其clone到本地

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78LRhCItxxeibRF1HukmXjgUgGd3vvMv92KOGtrMlx9ShzoSlI8WcjZcw/640?wx_fmt=png&from=appmsg)

之后在MCP Inspector链接该工具，方法很简单，直接在Command和参数中运行这个文件即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78n1279F0YRYMqcbVMohNJYbajh2dRspOMMc5UHAs0y3wMkXrvMKXDFQ/640?wx_fmt=png&from=appmsg)

这里链接成功后选择了list\_directory工具，输入需要读取的对应path即可访问到。看起来很简单是不是，就只要能让LLM能够正确选择对应工具名称和填对参数就行，其实本质上就类似于提供了一个Function Calling。但MCP的好处不同在于，协议提供了一种标准统一管理和发现、以及多种资源采集的访问能力。同时也有着低耦合，可以满足快速迭代的属性。

有了MCP的标准协议后，程序员在开发基础设施架构时，也可以利用常规的开发语言，将LLM的灵活性与中间件的强大功能巧妙融合，从而更高效、便捷地实现目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78UaMKsTPdQAbbf48WPEl9P96KVDHQtn0VBiaiahLg2JE802Pt0kiaEjNhw/640?wx_fmt=png&from=appmsg)

上图就是Java开发框架Spring AI对MCP的支持架构图

其MCP有两种部署方式，一种是本地，采用标准的输入/输出来进行通信；另一种则是远程，采用SSE (Server-Sent Events)的通信方式，而所有传输都使用 JSON-RPC 2.0 来交换消息。

## 开发一个自动研判恶意操作的MCP

因为目的是想着随便开发一个做个教学过程，正好最近在看类似的书，就一起做一个Demo来学习巩固下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78RelpXWbgzWeXdltM0wjC28e6Xu54VP6k2Lcj0WbJE1r8M0tgq41RWw/640?wx_fmt=png&from=appmsg)

程序大致逻辑就是通过ebpf写一个Agent安装在主机上来监听内核的执行命令，执行过的所有命令都保存在远端的Mongodb数据库中，而后续LLM（比如xxx时间段有恶意流量，需要上主机进一步排查取证）直接调用MCP查询某个时间段执行过的所有命令并研判是否属于恶意操作。

### 开发环境部署调试

开发MCP的框架很多，可以在这里找到你所熟知语言的框架：https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-zh.md#%E6%A1%86%E6%9E%B6

我这里就选Python的FastMCP来实现：https://github.com/jlowin/fastmcp

在开发之前，我先通过搭建一个Hello World例子，来完善开发所需要的一些前置条件：

```
uv init ebpfExecDB #创建一个用uv来管理虚拟python环境的项目
```

用uv的工具创建一个虚拟环境 通过uv的pip来安装框架依赖

```
uv pip install fastmcp
```

按照官网的例子，我直接用下面的代码来测试一下

```
# server.py
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a Static Resource
@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return"App configuration here"

# Add a dynamic resource
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    returnf"Profile data for user {user_id}"

# Add a prompt template
@mcp.prompt()
def review_code(code: str) -> str:
    returnf"Please review this code:\n\n{code}"
```

可以看到在代码中除了Tool的工具之外，还有Resource、Prompt等类型

* Resource：分为静态和动态两种资源类型，可以看作web2中的GET请求，用于请求某些特定的资源。如文本、PDF、图片、音视频等。
* Tool：这个可以执行代码，类似web2中的REST API请求端点。
* Prompt：有时候需要让工具接着调用其他的MCP或者处理定向的内容，可以用这个返回对应prompt，让模型更侧重自己的方向理解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj78Vfa7FqKcQsBJnGtz6vkn4TZSkaNpJ8hc3wh85IueFsvV1edVDh3jfw/640?wx_fmt=png&from=appmsg)

与此还有的是采样Sampling，可以将服务器需要补充或者修订的内容发送给客户端的LLM，让LLM和用户进行确认并采取下一步动作。比如MCP调用的时候会向用户发送可能输入的参数，当确定后将会进行调研，这个过程类比就是MCP采样能力。

接着将代码保存为server.py，并运行下面的命令启动调试，调试的方式就是直接运行fastmcp dev，其中内置了MCP Inspector的工具

```
uv run --with fastmcp fastmcp dev server.py
```

启动后会输出访问本地的5173端口，找到对应的工具直接调试使用即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zegbd9UNPM3icRABYORuThJ3Qzb5wsj782bvtfcibQn1CPFoiaZAqWP5Oe1ocBjxyS4msgyOTyme0ztseETCnBVkQ/640?wx_fmt=png&from=appmsg)

### LLM通过MCP取证程序开发

介绍完初步调试，在这里我就使用Cline来开发，先向它描述了我需要的开发需求

```
在ebpf2db.py文件中用ebpf编写一个监控本地Linux执行过的命令，并保存到日志文件中，同时写入到mongodb中
```

接着本地搭建一个mongodb

```
docker run -d -p 27017:27017 --name mongo-container mongo:7.0.16-rc1
```

AI给我生成的代码如下：

```
#!/usr/bin/env python3

from bcc import BPF
from pymongo import MongoClient
import time
import os
import logging

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "execMcpSecurity"
COLLECTION_NAME = "commands"

# Logging configuration
LOG_FILE = "/var/log/command.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# eBPF program
bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

struct data_t {
    char comm[TASK_COMM_LEN];
    char argv[256];
};

BPF_PERF_OUTPUT(events);

int syscall__execve(struct pt_regs *ctx, const char __user *filename,
                    const char __user *const __user *argv,
                    const char __user *const __user *envp) {
    struct data_t data = {};
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    bpf_probe_read_user_str(&data.argv, sizeof(data.argv), (void *)argv[0]);
    events.perf_submit(ctx, &data, sizeof(data));
    return 0;
}
"""

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def handle_event(cpu, data, size):
    event = b["events"].event(data)
    command = event.comm.decode('utf-8')
    args = event.argv.decode('utf-8')

    # Log to file
    log_message = f"Command: {command}, Args: {args}"
    logging.info(log_message)

    # Insert to MongoDB
    document = {
        "timestamp": time.time(),
        "command": command,
        "arguments": args
    }
    collection.insert_one(document)

# Load BPF program
b = BPF(text=bpf_text)
# 修改事件名为 __x64_sys_execve（x86_64 架构）
b.attach_kprobe(event="__x64_sys_execve", fn_name="syscall__execve")

print("Monitoring system commands... Press Ctrl+C to stop.")

# Process events
b["events"].open_perf_buffer(handle_event)
whileTrue:
    try:
        b.perf_buffer_poll()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        break
```

如果过程中有遇到如下错误，可能是使用了python 3.10+的版本

```
ImportError: cannot import name 'MutableMapping' from 'collections'
```

因为大多数apt install的方式下载的python3-bcc都比较老了，我这里用的是py 3.10+，最好的解决办法就是自己本地编译一个bcc

```
https://github.com/iovisor/bcc/blob/master/INSTALL.md#ubuntu---source
```

可以根据这个文档中介绍的安装依赖和编译bcc 完成编译之后如果没有在虚拟环境中安装成功bcc，还是提示找不到对应模块的话，可以在之前编译bcc的build/src/python目录下找到setup.py，手动安装一下即可。

```
(envname) root@chen-VMware-Virtual-Platform:~# python3 ebpfExec2DB.py
cannot attach kprobe, Invalid argument
Traceback (most recent call last):
File "/root/ebpfExec2DB.py", line 69, in
b.attach_kprobe(event="sys_execve", fn_name="syscall__execve")
File "/root/envname/lib/python3.12/site-packages/bcc-0.33.0+...