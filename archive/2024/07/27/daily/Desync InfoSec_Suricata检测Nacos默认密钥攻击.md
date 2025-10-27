---
title: Suricata检测Nacos默认密钥攻击
url: https://mp.weixin.qq.com/s?__biz=MzkzMDE3ODc1Mw==&mid=2247488248&idx=1&sn=aee2887be20161353a88c0a3e5e1ca7f&chksm=c27f6156f508e84011d819a84052918570ca3650131ec4d0a106602c70487859f062f5b8ab33&scene=58&subscene=0#rd
source: Desync InfoSec
date: 2024-07-27
fetch_date: 2025-10-06T17:44:29.091746
---

# Suricata检测Nacos默认密钥攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9DhkvTR0FkeMRFh2BtqxBYK4eS0DM05d5q81KuHRJfjbicSM9esicWLKtxokLkQqKCpND5eic7VuicBX9DYS9DNG5Q/0?wx_fmt=jpeg)

# Suricata检测Nacos默认密钥攻击

原创

safest\_place

Desync InfoSec

# Nacos简介

Nacos `/nɑ:kəʊs/` 是 Dynamic Naming and Configuration Service的首字母简称，一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。越来越多的微服务使用Nacos作为集中化的配置管理组件，因此在内网Nacos也成为攻击者的重点攻击目标之一。按Nacos官方文档记载，2.2.0.1版本前Nacos使用的jwt密钥默认值为：SecretKey012345678901234567890123456789012345678901234567890123456789。因此攻击者可以利用这一点生成jwt token，绕过身份认证，获取Nacos中的数据。本文的重点是检测该攻击行为，因此关于漏洞复现部分请读者自行上网查阅资料，也可参考文末的参考链接。

# 检测思路

首先我们拿到该漏洞利用时的HTTP请求如下：

```
GET /nacos/v1/cs/configs?dataId=&group=&appName=&config_tags=&pageNo=1&pageSize=10&tenant=&search=accurate&accessToken=eyJhbGciOiJIUzM4NCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTcxNzU5MzI0Nn0.314fYDxL_T3W319DiIye2dw0h-M0T9s3myGLwGBSHyuGeoImQE81HyX175p7VzzU HTTP/1.1
Host: 10.167.71.91:8848
User-Agent: curl/8.4.0
Accept: */*
```

可以发现HTTP请求中参数accessToken携带了jwt令牌。因此我们需要用Nacos默认jwt密钥校验这个token，如果校验通过，说明发起HTTP请求方意图通过默认jwt密钥获取Nacos中的数据，这有可能是攻击，也有可能是正常业务，但是这个业务系统存在Nacos默认jwt密钥的漏洞。

那么，使用suricata如何对这种流量进行检测呢？很遗憾，Suricata没有提供jwt校验的相关函数（显然这个行为无法通过静态规则进行检测）。在尝试使用lua脚本加载C语言编写的动态链接库这个方法失败后，我最终只能修改Suricata源码，在Suricata中内置一个jwt校验函数供lua脚本调用。

这里使用libjwt-dev这个C函数库实现jwt校验功能，首先我们需要安装这个库

```
apt install -y libjwt-dev
```

然后编辑detect-lua-extensions.c文件，在该文件中增加如下内容：

```
#include "util-base64.h"
#include "rust.h"
#include <jwt.h>

/**
 * \internal
 * \brief base64 decode from char* to char*
 * \retval base64decoded char*
 */
unsigned char *base64_decode(const char *base64)
{
    uint32_t input_len = strlen(base64);
    uint32_t output_len = strlen(base64);

    uint8_t* output_buffer = (uint8_t*)malloc(output_len);
    if (output_buffer == NULL) {
        SCLogError("Failed to allocate thread data");
        return NULL;
    }

    uint32_t consumed_bytes = 0;
    uint32_t decoded_bytes = 0;
    Base64Ecode ret = DecodeBase64(output_buffer, output_len, (const uint8_t*)base64,
                                   input_len, &consumed_bytes, &decoded_bytes, Base64ModeRFC2045);

    if (ret != BASE64_ECODE_OK) {
        SCLogError("Failed to decode base64 input");
        free(output_buffer);
        return NULL;
    }

    char* decoded_str = (char*)malloc(decoded_bytes + 1);
    if (decoded_str == NULL) {
        SCLogError("Failed to allocate memory");
        free(output_buffer);
        return NULL;
    }
    memcpy(decoded_str, output_buffer, decoded_bytes);
    decoded_str[decoded_bytes] = '\0';

    free(output_buffer);

    return decoded_str;
}

/**
 * \internal
 * \brief jwt token verify by libjwt
 * \retval verify result by int
 */
int LuaCallbackJwtVerifyImpl(const char *token, const char *base64_key)
{
    unsigned char *key = base64_decode(base64_key);
    SCLogNotice("base64decoded key: %s", key);
    SCLogNotice("token: %s", token);

    if (token == NULL || key == NULL)
    {
        SCLogNotice("token or key is null");
        return 0;
    }

    jwt_t *jwt = NULL;

    int ret = jwt_decode(&jwt, token, key, strlen(key));
    if (ret != 0 || jwt == NULL)
    {
        SCLogNotice("Failed to decode JWT");
        return 0;
    }

    jwt_free(jwt);
    free(key);
    if (ret == 0)
    {
        // verify success
        return 1;
    }
    else
    {
        // verify failed
        return 0;
    }
}

/**
 *  \brief Register Suricata Lua functions
 */
int LuaRegisterExtensions(lua_State *lua_state)
{
    //省略原有代码部分

    lua_pushcfunction(lua_state, LuaCallbackJwtVerify);
    lua_setglobal(lua_state, "SCJwtVerify");

    //省略原有代码部分
    return 0;
}
```

修改完成后，重新编译suricata 接着，我们完成lua脚本的编写，在lua脚本中提取URI中的token，调用SCJwtVerify函数进行校验。

```
local nacos_default_secret="SecretKey012345678901234567890123456789012345678901234567890123456789"

local function extract_access_token(url)
    local token = url:match("accessToken=([^&]+)")
    return token
end

function init (args)
    local needs = {}
    needs["http.uri"] = tostring(true)
    return needs
end

function match(args)
    local http_uri = tostring(args["http.uri"])
    if not http_uri then
        return 0
    end
    local token = extract_access_token(http_uri)
    if not token then
        return 0
    end
    SCLogInfo("extract jwt token success: " .. token)
    local result = SCJwtVerify(token, nacos_default_secret)
    SCLogInfo("result: " .. tostring(result))
    if result == true then
        return 1
    end
    return 0
end

return 0
```

最后，我们完成suricata静态规则的编写，并在规则中调用lua脚本，例如：

```
alert http any any -> any any (msg:"nacos"; flow: established, to_server; http.uri; content:"/nacos/v1/cs/configs"; lua:./lua/nacos_default_jwt.lua; classtype:bad-unknown; sid: 1000001; rev: 1;)
```

最终回放攻击流量测试，可成功触发告警。

# 参考链接

https://www.cnblogs.com/spmonkey/p/17505431.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过