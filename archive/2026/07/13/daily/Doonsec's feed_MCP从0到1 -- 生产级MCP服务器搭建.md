---
title: MCP从0到1 -- 生产级MCP服务器搭建
url: https://mp.weixin.qq.com/s/7-iiRk-6jnc-0Q00NOcm9A
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:42:41.208416
---

# MCP从0到1 -- 生产级MCP服务器搭建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/y3xArqr5PZmC2a75d0doo2CGJAs6HnaHJHbNrw4hib3aFiaFayJic5usv6Q7kOUcxLU31MQGkH6ic9Ieoz5wROsLxAFiaZTgKbWZWnfcuibibTUFEU/0?wx_fmt=jpeg)

# MCP从0到1 -- 生产级MCP服务器搭建

原创

黄鹂儿
黄鹂儿

一路狂飚的蜗牛

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

从Hello World到Kubernetes部署，一步步构建可落地的MCP服务

一、什么是MCP？

MCP（Model Context Protocol，模型上下文协议）是由Anthropic提出的一种开放协议，旨在让大语言模型（LLM）能够以标准化的方式连接外部工具和数据源。

简单来说，MCP就是AI应用的"USB-C接口"——统一标准，即插即用。过去，每个AI应用如果要调用外部工具，都需要单独开发集成代码；有了MCP后，只需按协议实现一个Server，所有兼容MCP的客户端都能直接使用。

核心角色

| 角色 | 说明 | 类比 |
| --- | --- | --- |
| MCP Host | 运行LLM的应用（如Claude Desktop、CodeBuddy/TRAE IDE） | 电脑主机 |
| MCP Client | Host内部的协议解析器，与Server建立1:1连接 | USB控制器 |
| MCP Server | 暴露工具/资源的后端服务 | USB设备 |
| Tools | Server提供的可调用函数 | 设备功能 |
| Resources | Server暴露的只读数据 | 设备存储 |
| Prompts | Server预定义的提示模板 | 设备预设 |

三种传输方式一览

| 方式 | 适用场景 | 复杂度 |
| --- | --- | --- |
| Stdio（标准输入输出） | 本地开发、IDE集成 | ⭐ |
| SSE（Server-Sent Events） | 远程服务、需长连接推送 | ⭐⭐ |
| Streamable HTTP（推荐） | 生产部署、负载均衡 | ⭐⭐ |

接下来，我们将从最简单的Hello World开始，一步步深入这三种传输方式，最终构建一个可在Kubernetes上弹性伸缩的生产级MCP Server。

二、5分钟入门：Hello World

先从最简单的Stdio模式开始。只需十几行代码，就能写一个可用的MCP Server。

项目文件结构

![](https://mmbiz.qpic.cn/mmbiz_png/y3xArqr5PZme1IyR5H5R5LEpt6IiaULFficic9VXKfqlia7tf83fWxNxVQ7QcmCxyelqNr8lzXibeCriav4vWCkJQP5ZVHTO6mmEWVqjZvdZicdiaYs/640?wx_fmt=png)

▲ 项目文件结构一览

Server端代码

# hello\_mcp\_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp-server")

@mcp.tool()
def hello(name: str) -> str:
    """向指定的人或内容打招呼"""
    return f"Hello, {name}!"

if \_\_name\_\_ == "\_\_main\_\_":
    mcp.run()

▲ 仅11行代码即可实现一个MCP Server

Client端代码

import asyncio
from mcp import stdio\_client, StdioServerParameters, ClientSession

async def main():
    server\_params = StdioServerParameters(
        command="python3", args=["hello\_mcp\_server.py"])
    async with stdio\_client(server\_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call\_tool("hello", {"name": "woniu"})
            print(result.content[0].text)  # 输出: Hello, woniu!

asyncio.run(main())

💡 Stdio模式通过标准输入输出来通信，Client启动Server子进程，通过管道读写JSON-RPC消息。这是最简单的方式，适合本地测试和IDE集成。

三、三种传输方式深度对比

理解了Hello World之后，我们来深入理解三种传输方式的差异。这是选择生产部署方案的关键知识。

3.1 Stdio模式

通过标准输入输出（stdin/stdout）通信。Client启动Server子进程，JSON-RPC消息在管道中传递。

✅ 优点：零网络配置，安全简单   ❌ 缺点：无法远程访问，不支持负载均衡

适用场景：IDE本地集成、开发调试。

3.2 SSE模式

通过HTTP SSE（Server-Sent Events）建立长连接，支持服务端主动推送。

mcp.settings.host = "0.0.0.0"
mcp.settings.port = 8080
# ... 工具定义 ...
mcp.run(transport="sse")

✅ 优点：支持远程访问和服务端推送   ❌ 缺点：需要会话亲和性（Sticky Session），扩展复杂

3.3 Streamable HTTP模式（生产推荐）

通过HTTP POST发送请求，响应可以是JSON或SSE流。支持无状态部署，是生产环境的首选方案。

mcp.settings.host = "0.0.0.0"
mcp.settings.port = 8081
mcp.settings.stateless\_http = True  # 关键：无状态模式
# ... 工具定义 ...
mcp.run(transport="streamable-http")

✅ 优点：无状态设计原生支持负载均衡和水平扩展   ❌ 缺点：不支持服务端主动推送

三种方式总结

| 特性 | Stdio | SSE | Streamable HTTP |
| --- | --- | --- | --- |
| 通信方式 | 进程stdin/stdout | HTTP SSE流 | HTTP POST + SSE |
| 适用场景 | 本地开发 | 远程+推送 | 生产部署 |
| 会话管理 | 进程生命周期 | 需会话亲和性 | 无状态 |
| 负载均衡 | 不支持 | 复杂 | 原生支持 |
| 推荐环境 | IDE调试 | 实时推送 | 企业生产 |

⚠️ 生产环境首选Streamable HTTP + stateless\_http=True，这是本文后续所有部署方案的基础。

四、调试方法：不用每次启动LLM

开发过程中如果每次都要通过LLM来测试MCP工具，效率太低。下面介绍三种高效的调试方法。

4.1 MCP Inspector（官方工具，最推荐）

一行命令启动，浏览器可视化调试：

npx @modelcontextprotocol/inspector

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y3xArqr5PZnzvHOtNQia3qCKtdsvIWkn2seqr9Vy3sibLSia4UPzlv9q3Dk7qUhe7cIflBGPY1DZpiarPVcFK95XoJYgXzm9gUOmrmYhzBt8uxk/640?wx_fmt=png)

▲ MCP Inspector连接成功，可查看工具列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y3xArqr5PZnW3pImDNeeFymQCxE6juL3p4MOZnLibFSBR7eZEpUAuktwPIXlU3EqA7YKAZa3Gg2NqGappHsUic5yIgWjuvzk2SHR6A0icNCptE/640?wx_fmt=png)

▲ 在Inspector中调用hello工具，查看输入和输出

Inspector能做什么：列出所有工具 → 手动输入参数 → 查看JSON-RPC原始消息 → 验证元数据。

4.2 curl命令行调试

# 初始化连接
curl -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize",...}'

# 调用工具
curl -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"callTool",
        "params":{"name":"hello","arguments":{"name":"woniu"}}}'

4.3 日志调试

在工具函数中添加日志，记录每次调用的参数、结果和耗时：

import logging, time, uuid
logger = logging.getLogger(\_\_name\_\_)

@mcp.tool()
def hello(name: str) -> str:
    request\_id = str(uuid.uuid4())[:8]
    start = time.time()
    result = f"Hello, {name}!"
    duration = (time.time() - start) \* 1000
    logger.info(f"[{request\_id}] hello({name}) -> {duration}ms")
    return result

五、企业级MCP Server开发

Hello World只是开始。生产环境的MCP Server需要考虑更多：无状态设计、健康检查、结构化日志、容器化支持等。

5.1 增强版Server核心代码

import logging, os, json, socket, time, uuid
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP("enterprise-mcp-server")
mcp.settings.host = "0.0.0.0"
mcp.settings.port = int(os.environ.get("PORT", 8000))
mcp.settings.stateless\_http = True# 无状态，负载均衡基础

# K8S/Docker 健康检查端点
@mcp.custom\_route("/health", methods=["GET"])
async def health\_check(request: Request) -> JSONResponse:
    return JSONResponse({"status":"healthy"})

# 工具：获取服务器信息（验证负载均衡用）
@mcp.tool()
def get\_server\_info() -> str:
    return json.dumps({
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
        "port": mcp.settings.port,
        "timestamp": datetime.now().isoformat()
    })

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if \_\_name\_\_ == "\_\_main\_\_":
    mcp.run(transport="streamable-http")

5.2 关键设计要点

| 特性 | 作用 |
| --- | --- |
| stateless\_http=True | 无状态模式，每个请求独立，是负载均衡的基础 |
| 环境变量PORT | 方便容器化和多实例部署 |
| /health自定义路由 | Docker/K8S健康检查所需，是生产部署必备 |
| UUID请求追踪 | 记录每次调用的request\_id，便于排查问题 |
| 结构化日志 | 记录工具名、参数、结果、耗时 |

5.3 配置到IDE

完成Server开发后，将其配置到CodeBuddy/TRAE IDE，让AI助手直接调用你的工具。

![](https://mmbiz.qpic.cn/mmbiz_png/y3xArqr5PZnykx7icr2Qgc2w5ynicvUJ7aN0enI4zIgBvxwNUImALUI2XcwdAOarVibr2icm0pqUG0u04ibmaJg7EsytbjkCI49Z6R3rRP00rBqg/640?wx_fmt=png)

▲ IDE中配置MCP Server的JSON

![](https://mmbiz.qpic.cn/mmbiz_png/y3xArqr5PZlfvNLqTNtm3gxrticf9zahcW8Iz2NcZA7eiavVPxQ3Klmt95Tyo5iadzbUvno4LZ6NetlxYfBfeuAghCwrGWLJicPb2fB0AYIRnic4/640?wx_fmt=png)

▲ AI助手调用MCP工具的实际效果

六、Docker化与Nginx负载均衡

容器化是生产部署的第一步。我们将用Docker Compose编排3个MCP Server实例 + 1个Nginx负载均衡器。

6.1 Dockerfile

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY mcp\_server\_pro.py .
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s \
    CMD python -c "import httpx; \
    r = httpx.get('http://localhost:8000/health'); \
    exit(0 if r.status\_code == 200 else 1)"
CMD ["python", "mcp\_server\_pro.py"]

6.2 docker-compose.yml

services:
  mcp-server-1:
    build: .
    ports: ["8001:8000"]
    networks: [mcp-network]
    healthcheck:
      test: ["CMD", "python", "-c",
        "import httpx; ...exit(0 if ok else 1)"]
mcp-server-2:# 同上，端口 8002
mcp-server-3:# 同上，端口 8003
nginx:
    image: nginx:1.25-alpine
    ports: ["80:80"]
    volumes: [./nginx.conf:/etc/nginx/nginx.conf]
    depends\_on: [mcp-server-1, mcp-server-2, mcp-server-3]

6.3 nginx.conf

upstream mcp\_servers {
    server mcp-server-1:8000;
    server mcp-server-2:8000;
    server mcp-server-3:8000;
}
server {
    listen 80;
    location /mcp {
        proxy\_pass http://mcp\_servers/mcp;
        proxy\_buffering off;       # SSE需要关闭缓冲
        proxy\_read\_timeout 300s;
    }
    location /health {
        proxy\_pass http://mcp\_servers/health;
    }
}

6.4 架构图

![](https://mmbiz.qpic.cn/mmbiz_png/y3xArqr5PZmJxVO9KRVMgLrqmd4uEsygR7YOF1KlFSPicOWwUjvhYDcH7ZYOmDtutg8BCiauEKBR6cSluxBiaiaIv8tyvwcCS0LhQZgfM9Yclwk/640?wx_fmt=png&from=appmsg)

6.5 启动与验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y3xArqr5PZltykDr1wzh13wTExica4Y09DmR6afd64jCtBjXDKFFZByCib7TffiaTibmHftdebjAwUzwqpic7TowI4Lia3xW5MlTD...