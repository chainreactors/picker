---
title: StubZero：Google Cloud生产环境RCE漏洞，奖金148,337美元
url: https://mp.weixin.qq.com/s/b3jAOox4jV1G9NQ2TgiGEQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:27.228568
---

# StubZero：Google Cloud生产环境RCE漏洞，奖金148,337美元

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OdEhd2rUcgrmon7tdTlibF5Fy7toOvO9h7ENlScz43VhnoiaDUibee2VA5smQ3q4b32rWAWq7qpRtD2oic6bGxJMyYH6icT5tnWwWw/0?wx_fmt=jpeg)

# StubZero：Google Cloud生产环境RCE漏洞，奖金148,337美元

A译
A译

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NCZic3h0icpiabqZXE3wGgmw3YWm42IGyVN4ib0PZtm01TF8Uc7SAbQ5CsMdEH9Q3vr7LzzNPxJeltW7mEEqb1GSXur5fCJBicE60c/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617500&idx=1&sn=73c0634d23ef9a5a7ca009cf0e3b1929&scene=21#wechat_redirect)

> **导语**：一个调试端点的信息泄露，最终演变为Google Cloud生产环境的完整远程代码执行攻击链。三天后，类似漏洞再次出现。这位研究员用两次报告、累计148,337美元的奖金，证明了Stubby RPC调用链在Google安全模型中的核心地位——以及一旦被攻破意味着什么。

![StubZero：Google Cloud生产环境RCE漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PFvmEcfvJSPsvQz4lTNJp9gNKeXyHyWIEJbqViaY95iaOjUQRwjAwxooKq6rhl9MBiaibD8Y63Radicx0Q3piae7A6twJXnuPeUm0Vw/640?wx_fmt=png "StubZero：Google Cloud生产环境RCE漏洞")

---

## 一、起点：一个调试端点的信息泄露

故事的起因，是研究员的一个自动化模糊测试工具对 API 端点 `cloudcrmipfrontend-pa.googleapis.com` 发出了警报——该 API 对若干可疑端点返回了 200 状态码。深入检查后发现，这个 API 存在多个公开的调试端点。

进一步探测发现，`/v1/integrationPlatform:getProtoDefinition` 这个端点可以返回 Google 内部源代码仓库 google3 中任意 protobuf 消息的定义——甚至包括 YouTube 这类完全不相关的服务。

**请求示例**：

```
GET /v1/integrationPlatform:getProtoDefinition?fullName=youtube.api.pfiinnertube.YoutubeApiInnertube.InnerTubeContext&isEnum=false HTTP/2
Host: cloudcrmipfrontend-pa.clients6.google.com
Cookie: <已脱敏>
Authorization: SAPISIDHASH <已脱敏>
Origin: https://console.cloud.google.com
X-Goog-Api-Key: AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
```

**返回结果**（部分）：

```
{
  "protoDescriptor":{
    "name":"InnerTubeContext",
    "field":[
      {
        "name":"client",
        "number":1,
        "label":"LABEL_OPTIONAL",
        "type":"TYPE_MESSAGE",
        "typeName":".youtube.api.pfiinnertube.YoutubeApiInnertube.ClientInfo",
        "jsonName":"client"
      },
      ...
    ]
}
}
```

这意味着：在Google这个黑盒目标上，几乎所有 API 的请求体/响应体结构都可以被枚举出来。这是一个巨大的信息泄露。

---

## 二、"req2proto即服务"的诞生

研究员之前曾开发过一个工具 req2proto，用于从请求体反推 protobuf 定义。但这个工具有局限性：只能找到请求体的 proto，无法获取响应体，且依赖 API 支持 JSPB（application/json+protobuf），而大多数 API 并不支持。

现在，这个端点就是"req2proto即服务"（req2proto as a Service™）——一个托管版的 req2proto，功能强大得多。

---

## 三、泄露内部工作流执行队列

在没有查询参数的情况下，该端点只返回 INVALID\_ARGUMENT 错误。根据以往经验，这类 filter 参数通常支持 AIP-160 规定的任意过滤语法。

尝试 `client_id>"123"` 作为 filter：

```
{
  "error": {
    "code": 500,
    "message": "Failed to convert server response to JSON",
    "status": "INTERNAL"
  }
}
```

看起来后端给的响应没有 JSON 映射。Google API 支持通过标准参数 `?alt=` 更改响应格式，`?alt=proto` 会返回 protobuf 格式的原始输出。

由于使用的是 Google 自有的第一方认证（Cookie + Authorization header），请求必须发往 `cloudcrmipfrontend-pa.clients6.google.com` 而非 `cloudcrmipfrontend-pa.googleapis.com`，但 Google 不允许 raw proto 响应发往 \*.google.com：

```
Request unsafe for browser client domain: cloudcrmipfrontend-pa.clients6.google.com
```

解决方法是使用请求头 `X-Goog-Encode-Response-If-Executable: base64`，将响应转为 base64 编码。

通过 proto 定义泄露拿到的 schema，成功解码了返回的 protobuf，发现这是某种内部工作流执行队列，包含从 Spanner 同步数据到 Salesforce 的工作流：

```
{
  "queue_items":[
    {
      "queued_request":{
        "queued_request_id":"75a885e2-c611-43f7-b4e2-ae0d87bae789",
        "client_id":"default",
        "workflow_name":"WriteToSfdc",
        "priority":"CRITICAL",
        "received_timestamp":1763057385562,
        "event_execution_info_id":"615cd9a9-9c0e-46ec-90df-91ee42ec9c37"
      },
      ...
      "type_url":"type.googleapis.com/enterprise.crm.datalayer.WriteToSfdcRequest",
      "sfdc_object":{
        "vector_account":{
          "id":"001Kf00000wjeK3IAI",
          "due_diligence__c":"Pending",
          ...
        }
      }
    }
]
}
```

就在报告提交后几小时，该漏洞被标记为 **P0/S0**，并获得 🎉 Nice catch!。

---

## 四、Stubby RPC与Google安全模型

在深入分析前，需要理解 Google 的 RPC 基础设施。根据 Google SRE手册：

> Google 所有服务都使用名为 Stubby 的远程过程调用（RPC）基础设施进行通信；开源版本 gRPC 已对外发布。

Google 的安全模型中，每个 borglet 服务都有独立的身份。当你向 \*.googleapis.com 端点发送请求时，前端服务使用自己的 prod 服务身份向后端服务发起 Stubby 调用，同时在安全票据中携带你的最终用户上下文。如果票据包含你的 Gaia 用户ID，后端服务会以该用户身份对请求进行授权。

**关键安全机制**：

```
Without authentication (anonymous)
com.google.apps.framework.auth.IamPermissionDeniedException:
  IAM authority does not have the permission 'cloudprivatecatalog.targets.get'
  required for action PrivateCatalogV1Beta1-SearchProducts
  on resource ''.
  ...
  Security Context:
    ...
    user = anonymous
    creds = EndUserCreds
    ...
    peer =
      protocol = loas
      level = strong_privacy_and_integrity
      host = jxcbu6.prod.google.com
      role = cloud-commerce-catalog
```

**含第一方认证时（Gaia用户）**：

```
With first-party authentication (Gaia user)
  ...
  Security Context:
    ...
    user = gaiauser/0xaa22527678
    creds = EndUserCreds
    ...
    gaiaId = 640201889743
    security_realm = campus-dls
```

注意 `peer` 块显示的是 prod 服务身份进行的内部 Stubby 调用。区别在于最终用户上下文：第一个票据是 ANONYMOUS，第二个携带 GAIA\_MINT 凭证（当你使用 cookie 或 bearer 认证时，会被转换为标准 UberMint token）。

如果攻击者能以集成平台的 prod 服务身份执行任意 Stubby 查询，就可以访问大量 RPC——从敏感用户数据到代码执行，取决于 prod 用户的权限范围。因此，Google 将此类漏洞视为远程代码执行。

**Stubby访问控制机制**：

Google 每个 Stubby 服务都定义了 `RpcSecurityPolicy`，包含按方法的允许列表。例如 Cloud SQL Speckle Boss 进程的策略：

```
mapping {
  rpc_method:"/SaasActuation.UpdateInstance"
  rpc_method:"/MaintenancePolicyService.CreateMaintenancePolicy"
  ...
  authentication_policy {
    creds_policy {
      rules {
        permissions:"auth.creds.useProdUserEUC"
        action: ALLOW
        in:"mdb:zamm-exe-3-cloud-sql--default-policy"
        in:"user:speckle-tool-proxy@prod.google.com"
      }
      rules {
        permissions:"auth.creds.useLOAS"
        action: ALLOW
        in:"allUsers"
      }
    }
}
  authorization_mode: MANUAL_IAM
  permission_to_check:"cloudsql.instances.rollout"
}
```

* `auth.creds.useLOAS` 表示"任何 borglet 都可以用自己的 LOAS 身份调用"
* `auth.creds.useProdUserEUC` 表示"只有特定的 MDB 组才能将 Gaia 最终用户身份转发到调用中"

即便拿到了 Stubby 调用的原始能力，也不意味着能调用所有 RPC——只有那些 RpcSecurityPolicy 允许你的对等身份的 RPC 才能被访问。

---

## 五、从信息泄露到RCE的完整攻击链

### 5.1 创建工作流

首次尝试创建工作流时收到 INVALID\_ARGUMENT 错误：

```
{
  "error": {
    "code": 400,
    "message": "Request contains an invalid argument.",
    "status": "INVALID_ARGUMENT"
  }
}
```

推测是缺少必要参数，可能是 `clientId`。之前从 quota queue 泄露的响应中有 `"client_id": "default"`，于是尝试：

```
{
  "workflow":{
    "name":"my-new-workflow-test",
    "origin":"UI",
    "clientId":"default",
    "triggerConfigs":[],
    "taskConfigs":[]
},
"isNewWorkflow":true
}
```

**成功**！返回了工作流ID。但要运行工作流，必须先发布它，而发布时遇到了权限限制：

```
{
  "error": {
    "code": 403,
    "message": "Publisher admin@gvrptest.cry.dev cannot be the same as the last editor...",
    "status": "PERMISSION_DENIED"
  }
}
```

需要另一个用户来发布。由于无法通过 ACL 端点添加其他账号，一度陷入僵局。

### 5.2 Discord上的转机

一个多月后，研究员在 Discord 群聊中半开玩笑地提到自己找到了一个 Google 内部泄露 protobuf 定义的漏洞。

这时，一位名为 **shrugged** 的研究员回复说他们也在研究同一个 API，并且注意到了 `GenericStubbyTypedTask` 这个潜在 RCE 向量，但苦于没有有效的 `client_id` 来创建初始工作流草案。

而研究员这边有 `client_id: "default"`，却在发布步骤卡住了。双方交换了各自的信息后，攻击链被迅速拼完。

### 5.3 绕过修复：寻找对应的"替身"端点

Google 已经根据初次报告部署了修复，所以很多原始端点都返回 PERMISSION\_DENIED。但研究员注意到：很多端点在不同的服务名下存在 1:1 的"替身"：

| 原始端点（已修复） | 替身端点 |
| --- | --- |
| /v1/integrationPlatform:getProtoDefinition | /v1/integrationPlatform/workflowsupport:getProtoDefinition |
| /v1/integrationPlatform:runWorkflow | /v1/integrationPlatform/workflowexecution:runWorkflow |
| /v1/integrationPlatform:setAcl | /v1/integrationPlatform/auth:setAcl |

但 `createDraftWorkflow` 找不到替身，仍然返回 PERMISSION\_DENIED。

奇怪的是，shrugged 用同样的请求却能成功。答案揭晓：**修复没有完全同步到所有负载均衡的后端**。通过反复发送同一请求，可以可靠地路由到仍然允许该操作的后端。

### 5.4 GenericStubbyTypedTaskV2的发现

`GenericStubbyTypedTask` 这个任务名称实际上并不存在。从 `/v1/integrationPlatform:listTaskEntities` 返回的数据中只看到 `IO_TEMPLATE` 类型的任务。

从 Application Integration 的 JS 代码中，找到了确切的任务名称：`GenericStubbyTypedTaskV2`，甚至配有独立的图标：

```
["GenericStubbyTypedTaskV2","http://gstatic.com/enterprise/crm/eventbus/images/icons/blue/stubby_48px_blue.svg"],
```

尝试配置 `GenericStubbyTypedTask` 时收到错误，显示缺少必需字段 `serverSpec`：

```
{
  "error": {
    "code": 400,
    "message": "'Required input key serverSpec not ...