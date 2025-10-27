---
title: CosMiss：Azure Cosmos DB Notebooks远程代码执行漏洞详解
url: https://www.4hou.com/posts/r7GB
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-09
fetch_date: 2025-10-03T22:01:39.389498
---

# CosMiss：Azure Cosmos DB Notebooks远程代码执行漏洞详解

CosMiss：Azure Cosmos DB Notebooks远程代码执行漏洞详解 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# CosMiss：Azure Cosmos DB Notebooks远程代码执行漏洞详解

布加迪
[技术](https://www.4hou.com/category/technology)
2022-11-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)152265

收藏

导语：Azure Cosmos DB近日曝出一个很严重的漏洞：Cosmos DB Notebooks缺少身份验证检查。

我们最近在Azure Cosmos DB中发现了一个很严重的漏洞，即Cosmos DB Notebooks缺少身份验证检查。我们将该漏洞命名为“CosMiss”。简而言之，如果攻击者知道Notebook的“forwardingId”（即Notebook Workspace的UUID），他们就拥有Notebook的全部权限，包括读写访问权，以及修改运行Notebook的容器的文件系统的能力。只要修改容器文件系统（即用于临时Notebook托管的专用工作区），我们就能够在Notebook容器中实现远程代码执行（RCE）。

发现该漏洞后，Orca Research Pod立即将其报告给微软安全响应中心（MSRC），后者在两天内修复了这个严重问题，这比我们在Azure Synapse中发现的Synapse漏洞的响应速度要快得多。我们验证了修正版，可以确认现在所有的Cosmos DB Notebook用户在访问Notebook之前都需要在请求头中有Authorization（授权）令牌。我们要感谢微软的合作和快速行动，以堵住该漏洞。

**CosMiss漏洞简介**

该漏洞存在于Azure Cosmos DB Jupyter Notebooks，这是微软的快速NoSQL数据库，广泛用于微软自己的电子商务平台和零售行业，用于存储目录数据和订单处理管道中的事件来源。

Jupyter Notebooks内置于Azure Cosmos DB中，被开发人员用来执行常见任务，比如数据清理、数据探索、数据转换和机器学习。我们在研究中发现，Cosmos DB Jupyter Notebooks缺少身份验证检查。

这是特别危险的，因为开发人员使用Cosmos DB Notebooks来创建代码，经常含有高度敏感的信息，比如嵌入在代码中的机密信息（secrets）和私钥。

“CosMiss”漏洞允许未经身份验证的用户获得对Azure Cosmos DB Notebooks的读写访问权、注入代码并覆盖代码，从而实施远程代码执行（RCE）。

然而，攻击者只有在知道Notebook Workspace的UUID（又叫forwardingId）的情况下才能够利用该漏洞。据我们所知，获得forwardingId的唯一方法是，以经过验证的用户的身份打开Notebook。但是forwardingId并未被记录为是机密信息，所以我们没有任何理由相信用户会把它当成机密信息。

2022年10月3日，Orca Security向微软报告了该漏洞，微软在两天内修复了该漏洞，现在要求每个Notebook会话的请求头中有授权令牌。

**Cosmos DB Notebooks简介**

CosMiss漏洞存在于Cosmos DB Jupyter Notebooks中。Azure Cosmos DB是一个快速NoSQL数据库。Azure Cosmos DB包含Jupyter Notebooks，这是一种开源交互开发环境（IDE），以便开发人员创建、执行和共享含有实时代码、方程、可视化和叙事文本的文档。由于开发人员使用Cosmos DB Notebooks来创建代码，因此可能含有高度敏感的信息，比如嵌入在代码中的机密信息和私钥。

**利用CosMiss的概念证明**

为了演示该漏洞，我们使用Azure Table API和Serverless Capacity模式创建了Cosmos DB。该漏洞还在Core SQL api（推荐）和吞吐量配置的部署环境上进行了验证。

Cosmos DB Data Explorer blade中的Notebooks功能让客户可以使用Jupyter功能（在Python、C#或其他运行时环境中）访问和可视化其数据。此外，客户使用该功能检查来自Cosmos DB的数据，并检查可以使用API进行集成的其他数据源。

**1. 不需要授权头**

当用户创建新的Notebook后，phoenixServiceUrl创建下列端点，它将生成以下项目：

POST

/api/controlplane/toolscontainer/cosmosaccounts/subscriptions/[tenant-id]/resourceGroups/Orca-

Research/providers/Microsoft.DocumentDB/databaseAccounts/orca-cosmos-

dev/containerconnections/multicontainer HTTP/2

Host: tools.cosmos.azure.com

Content-Length: 88

Sec-Ch-Ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"

Authorization: Bearer

eyJ0eXAiOiJKV1QiLdaaaxxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQddaaam5ldC8yMjdkY2ExZC1iMWE1LTQ0MDEtYTVmZi05N2Q5OTMxZWE4YmUvIiwiaWF0IjoxNjY0NzE4NTI3LCJuYmYiOjE2NjQ3MTg1MjcsImV4cCI6MTY2NDcyMzIxOSwiYWNyIjoiMSIsndkbkZ3d1lKQUNNNjJjdmkrbERTVnRpQWIvdEpDOW9HV2VFd2pwWGhsL2x3aStzVzZWWHB5UmV5ZFpwMVgiLCJhdI0N2QtOTc0ZTUzY2JkZjNjIiwiYXBwaWRhY3Icadasdddddab3NtbyIsIm9pZCI6IjNhMzJkNmU1LWEyYzMtNGM5MS1iOTA5LTc0N2YxNjQ2NDg3MSIsInB1aWQiOiIxMDAzMjAwMjM2RUJBODZEIiwicmgiOiIwLkFZSUFIY3A5SXFXeEFVU2xfNWZaa3g2b3ZrWklmM2tBdXRkUHVrUGF3ZmoyTUJPQ0FHay4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJZTElsRzB1anZDaktlSWo5OHozRk94R3ZvTjl2Umx3UFRtczlOa1dfQng0IiwidGlkIjoiMjI3ZGNhMWQtYjFhNS00NDAxLWE1ZmYtOTdkOTkzMWVhOGJlIiwidW5pcXVlX25hbWUiOiJjb3Ntb0BvcmNhc2VjdXJpdHlyZXNlYXJjaC5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJjb3Ntb0BvcmNhc2VjdXJpdHlyZXNlYXJjaC5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiJuZ3VDVm1qZFhrS3RUSW5BaG9GbEFBIiwidmVyIjoiMS4wIiwieG1zX3RjZHQiOjE2MTg4MTYwODl9.Gyd3LXwzBG1yj-JfO0PCXOyD0exC7U-MCXwJBdsadcadad3xLIRZ7NqBq5BhE0WXLV2cgziYf-CAT9QT6oy1yIn58RaRdMojlVbhCpxlfFTdnsOXiorzNwTHzcwwvWsM4fbl2vV-RKMO

Content-Type: application/json

Sec-Ch-Ua-Mobile: ?0

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36

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

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396003160315.png "1667396003160315.png")

图1

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396020205963.png "1667396020205963.png")

图2

响应如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396033198359.png "1667396033198359.png")

图3

我们可以看到以下项目被创建：

1. 一个https://seasia.tools.cosmos.azure.com端点。

2. 唯一端口（端口范围是10000-10009，后面有详细介绍）。

3. 充当会话/Notebook ID的唯一值（UUIDv4），又叫forwardingId（上面例子中的ab83e033-1670-4bac-a186-32a1c0dddfbc）。

我们可以看到服务器在后台发送的以下端点：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396045193814.png "1667396045193814.png")

图4

我们目前的forwardingId似乎是27f180bc-cf93-4c42-b23e-f27a5085da57。

如果检查我们的Notebook服务器（即https://seasia.tools.cosmos.azure.com:10007/）发送的各种请求，似乎所有发送到服务器的请求都含有授权头，如下面截图所示：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396059100056.png "1667396059100056.png")

图5

当我们试图删除授权头并发送相同的请求时，我们看到无需授权头即可列出同一台服务器的不同Notebook。

https://seasia.tools.cosmos.azure.com:10007/api/containergateway/27f180bc-cf93-4c42-b23e-f27a5085da57/api/contents/notebooks

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396075878218.png "1667396075878218.png")

图6

由于Cosmos DB Table和Python Query基于Jupyter（+Tornado服务器），我们可以查看作为平台一部分的各种端点：

< https://github.com/jupyter-

server/kernel\_gateway/blob/master/kernel\_gateway/jupyter\_websocket/swagger.json >]

 (< https://github.com/jupyter-

server/kernel\_gateway/blob/master/kernel\_gateway/jupyter\_websocket/swagger.json >) # 36

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396088506248.png "1667396088506248.png")

图7

在检查各种Security Definitions（安全定义）时，我们可以假设默认情况下当前Security Configurations（安全配置）并没有正确设置，因为需要授权方法用授权头或查询字符串来设置。

考虑到这一点，我们现在可以尝试滥用这种错误配置来操纵各种Notebook和模板。

**2. 覆盖、删除和注入代码**

现在不妨尝试覆盖当前的Notebook数据。首先，我们在Notebook中编写一些示例代码。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396107105000.png "1667396107105000.png")

图8

然后我们保存它：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396118454792.png "1667396118454792.png")

图9

我们还可以通过Burp来检查Notebook（Untitled.ipynb）：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396128170122.png "1667396128170122.png")

图10

此外，我们可以从以下端点获取kernel\_id：

<https://seasia.tools.cosmos.azure.com:10002/api/containergateway/ab83e033-1670-4bac-a186-

32a1c0dddfbc/api/kernels/>

发送上述请求，我们将获得以下id：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667396138153224.png "1667396138153...