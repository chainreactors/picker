---
title: 从黑盒到白盒：一次 .NET 后台渗透实录
url: https://mp.weixin.qq.com/s/6C9D9_uJZlwn96QDZh65SA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:05:03.404924
---

# 从黑盒到白盒：一次 .NET 后台渗透实录

# 从黑盒到白盒：一次 .NET 后台渗透实录

轩公子
轩公子

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：轩公子

文章来源：https://forum.butian.net/share/5116

01

0x1 从黑盒到白盒：一次 .NET 后台渗透实录

## 一、登录框常规测试

目标是一个常见的后台登录页面。先用插件扫了一遍接口，不出所料，全部返回 403。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWmRJ2uNXAAZuoO9dibB5m9cI9gO4u62RibZX8dTDSibSgG3UL7xvmgSJRicjEK0u0qIWsd47dp9Hia4mHMzWoBC0LLwlYX8HGbGibwU/640?wx_fmt=png&from=appmsg)

image.png

抓登录包看数据格式，发现是 JSON 提交。本来想试试 Fastjson 反序列化，但响应头暴露了服务器信息：**IIS 7.5 + ASP.NET 8**，Java 那一套漏洞直接排除。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QV24YrhKgWG2JJQcyXEFNbt09oia0fc9SrFmKm3xwVxNyOwm47zDGob3JhmLjNPAia68mveJ3nUlpB2IVHCt86ePqdNDsC3ygpz4/640?wx_fmt=png&from=appmsg)

image.png

转向爆破弱口令，却发现验证码无法绕过——删除验证码字段返回"不能为空"。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QU8gJF8O11OAHQXdxw54Z1K5O77nDVa7036ekoKVz8zU8JxzAZFJcEP6S9vS9ZkjK8Xs7FCoyMA71lOv6cgDibPuJTiaYqEawkV4/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUk2F5O5Rgf5rnF233bicxBR8OqyVhIaaf2WbgsibIvMVwp5lhTjkfggepYCicciazHjlsKkorerGBlJ8ZkmnRZ4Vcu4toT5ufGicek/640?wx_fmt=png&from=appmsg)

image.png

有人可能会说用 OCR 识别，但这里的验证码是 Base64 内嵌的，现有爆破工具都不支持，需要写中转脚本配合，较麻烦，先放一放。

于是我又想到了，修改返回包，看看能否中个奖，绕过登录。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXo3XVoRNkzHjEWFgaiaduSTN4lEOUXwmGx9LA5GlsxW1BNF3mTCHSb55DhqR1qv3eaLL0KZd9cea9XwNA2rPYaiap0OGbuJfFK0/640?wx_fmt=png&from=appmsg)

image.png

返回了，jwt 认证格式，我寻思，jwt 不都是 java 里面的，net 竟然也会有

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVENYLGjQ6mjBnicytroHcw4OCmaV1OOIuBYwticnG66NMYglrAbJFC1C3AYibF6NrJNWDIq8VUyvefRKiab2ExfQFiag4RyWYXPIFE/640?wx_fmt=png&from=appmsg)

image.png

于是f12，全局搜索关键字，翻找半天，并未发现相关的参数，点燃的希望又破灭了

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWq83SNibj5uAdMqONXvE6WDEoBKUPiaw9Z2gwN0gnZUR8BzunqtnmE7oljAMf9HEtSkvicqib7rtiawACBWKOEUxBIxgpVz5rsAthA/640?wx_fmt=png&from=appmsg)

image.png

常规思路走完一遍，还是没有突破，剩下最后一招：**扫目录**。

## 二、Swagger 未授权访问

目录扫描命中了 Swagger 接口文档。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVs9TzUMkW6vSHAtwTXNUELmRvia70SZ3nZ0yNxLwXLicPzHDiaqtzHz2Ruugl7lNOpVr0eWlckesSZegHV4lGNsp19p0MdoaDT2o/640?wx_fmt=png&from=appmsg)

image.png

文档里列出了大量后台接口，但绝大多数都需要鉴权，只有两三个字典类接口能匿名访问，且不含敏感信息。

不过有一个有价值的收获：响应中暴露了后端框架信息——**Vol.Core**（一个开源的 .NET 后台框架）。

## 三、源码审计：定位加密逻辑

既然知道了框架，直接下载源码审计。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWrJAtGXoEWuJR7havw68VYK7SsViavM5X0ATkaEXkic5w686rl0K7T5eyh9KNXdtzm9VNYdHVpKnR9NWPftCcIj6rQRV36gEBDU/640?wx_fmt=png&from=appmsg)

image.png

翻到 SQL 初始化文件，里面存了默认管理员密码，但是 Base64 解不开，说明是加密存储，需要找密钥。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVoEibc2CiaX2En7ja58hysHfhyDaNGy9H7c3Cpg023Kh9kIg1uDumiaq8mPqgvE6qW5hECAUBQO1bOhKrzP57FZGkqVTzcwZzkc0/640?wx_fmt=png&from=appmsg)

image.png

接着翻配置文件，找到了 Key。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVUJiavdVcicbGo6IGP7dBZSwGibPytdl23auPlFnRLcpzpJDQ43UlNP2cKHMibFNrxqA0Z5xZ9MgCnAFibIv6t5BbOuqdT4xDr0T5o/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWVR4hGHXPlA4TGgLyg96pwUcgblI9ZSREnlMnibFJvlxfhKOUKMtANKoO5eibQIwsocTQH8Icu46HSA9ZSnzfv3c8CvqciajwwsA/640?wx_fmt=png&from=appmsg)

image.png

但直接拿这个 Key 还是解不出来，说明加密逻辑不是简单的 AES/DES。全局搜索 `decrypt` 定位解密函数。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUcJeWk3DRE2DjnEqYWyI70RW6N5rJCtV3YpgPegMjOHEu8jQ3tkVA1hXe7XyfwCzayZRv6koRl41lE936afof46yxJ0onia9ks/640?wx_fmt=png&from=appmsg)

image.png

发现一个有意思的地方：函数命名是 `Des`，但内部实际调用的是 **AES**。密钥取配置值的前 16 位。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVS6QtgoB3Bvfkbu8FKn79kuwOic1oVuhUnTXqYvN0ZUiaZddbn2VyJeAjLOK5t7bwIEfRHGxW6J2v2YER8tUs5sJCEg0JXh5ka8/640?wx_fmt=png&from=appmsg)

image.png

解密成功，拿到默认 admin 密码，登录——失败。说明默认密码已被修改。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVQjgDk9Ab88op2v5oFtMgxA3hBCWHj7CVvicnIjBrUicP8zfEwQcvUTLCMnMgIVpH2qyjaze8bee8n236Ursj2JKosj5Jh2NviaU/640?wx_fmt=png&from=appmsg)

image.png

## 四、JWT 伪造：第一次尝试

思考片刻：配置文件里同时存在 JWT 密钥，如果默认密钥没改，直接伪造 Token 就能进后台。

伪造 Token 需要知道参数结构，前端没有，但这是后端，继续全局搜索 `jwt`，定位到核心生成逻辑。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUiaGnb6iaGNZy9DEDPr0Bfbl8qSLcvNukC0JBO2RMBbEgm9BoQUVzutIPicR4E3uiaHFhk6EUwPca4IadQLSQNRPrrVURWF0y312g/640?wx_fmt=png&from=appmsg)

image.png

需要六个字段：

| 字段 | 含义 |
| --- | --- |
| jti | 用户 ID |
| iat | 当前时间戳 |
| nbf | 当前时间戳 |
| exp | 过期时间戳 |
| iss | 配置中的 Issuer |
| aud | 配置中的 Audience |

构造 Payload：

```
{
  "jti": "1",
  "iat": "1788013440",
  "nbf": "1788013440",
  "exp": "1788020640",
  "iss": "vol.core.owner",
  "aud": "vol.core"
}
```

用 配置文件里的密钥签名后请求——**401**。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUVKejBTJzXadicOQGWZEht2ySPQpWScCeqgvW0B0t4ibffiakoy9lfccy7yskwkT4QrycJSn5WhfxfvZJZCxafW7O6kyeGALV1dY/640?wx_fmt=png&from=appmsg)

image.png

说明 JWT 密钥也被改了。继续硬刚的话，只能审未授权漏洞或前台 RCE

但审了半个多小时，确认 Swagger 里的接口和代码里的接口一一对应，**不存在未授权接口**。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUnTu5m1cibRBwKO4XoV2aycfUl4YbuVNGOU1kHE4MqjDzW3oGECPrQKwRmtMUuAqeM931V2Xa24nw26xf5o3KgD2eVfGfUTenA/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVsFgaOwnLtnglJfhnHo2jh0dKdtbKur2GIcjRFnN3GU6bWec4ULjr9pFkibhIbOYv8DlT1lzGJ112rKPxedDl1E6IbXCLSdMhA/640?wx_fmt=png&from=appmsg)

image.png

正当准备放弃时，重新仔细看了一遍接口文档，发现一个被忽略的接口：`string/{key}`。 而这个接口，findsomething 插件并未提取出来，所以在一开始接口 fuzz 的时候，并未注意。

起初不知道这个接口是干什么的，丢给 AI 生成了一批常见 key 值挨个试，还真发现了问题。

* `string/Path` → 返回系统环境变量
* `string/username` → 返回系统用户名
* `string/os` → 返回 `Windows`

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVMEcMq0ywGseBc17ISedm7Z1Xicpydv8bSYhzBhwS7XjQkdtOyfYzBlZQhyNDlXtKp1cXZj0V8HvP2ZZSn4ZdzvQn4OswoYvmM/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUMxyPibFhNlVVLXzpYWBVNnxr9CA5TE2JLYHbdoVXiaLPXMNUQYicQ5OCqFywYChDKbAMeJR0icTkEyMtscTXYiaIP1WIibF4eicAXyQ/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWnCJiaDPCHHzeSUedoAgAK6KcQMtuwllMePmeEMfG3Wck60ywiabF6GvibzoiaVYQ5MGyfcALTPQOqeMx1rnVSMMhia1k5mEznLqOw/640?wx_fmt=png&from=appmsg)

image.png

第一反应是命令注入或文件读取，但试了 `id`、`cmd:whoami` 都没反应

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QW9N2picsbTVsCoUorDYDZhWyahAL8d2rRVicytd8nvykLS4ccX9FI7hGIQeVfUVYRDYJ3XARiaNyrwibzoCgGbHcbzlyjF3ljBVMg/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QX3lOcB70JekP2aAoAA7VYP6o7r7DLhibbU3anvuvwicr1HGh0jXwGicp4slzH0G8WQxNBz3oJDIzDhWrJy8uHwHngOicQPqVvgHSM/640?wx_fmt=png&from=appmsg)

image.png

卡了一个小时无法深入利用。

回头看接口定义：

```
"/string/{key}": {
  "get": {
    "tags": ["ApiConfig"],
    "parameters": [
      {
        "name": "key",
        "in": "path",
        "required": true,
        "schema": { "type": "string" }
      }
    ],
    "responses": {
      "200": { "description": "Success" }
    }
  }
}
```

推测逻辑是：**根据 key 从 API 配置文件中返回对应的字符串值**。

关键来了——我手上有源码啊。匹配了三层参数后确认，这个接口就是从配置中按 key 取值。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWR0Dn6GWdJ32TJqxnLZEz40Lpq8h2NKtUJF8ZdgbxfvxbJjqmxnia2rpOLPhuD72dUVoB3VhoCFoo4ZKccW81GEopibLhH6Cyic0/640?wx_fmt=png&from=appmsg)

image.png

一一对应

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXvTVGpkPUibT3OwS5yrXHZrWPKltQ5dzN3ymTjSfbRBxdL9UQWeJugEickNyoJtic7u7XHsTPNW3lvAKQf2r1TRgnfqsRrSAXE1M/640?wx_fmt=png&from=appmsg)

image.png

既然前面 JWT 默认密钥伪造失败，那就用这个接口**把真实密钥读出来**。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWCNVhYkoJdf8ExBF17dqCB00xVo3S9A5JSZZENo0ibCOTlQPhSKU...