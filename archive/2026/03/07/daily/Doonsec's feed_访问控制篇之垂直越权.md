---
title: 访问控制篇之垂直越权
url: https://mp.weixin.qq.com/s/jt-yLojrjeWvWjpINLsWkw
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:20.959705
---

# 访问控制篇之垂直越权

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qkajCoyKpkCQ0PGw9hfl3aXQD5KeDW6CxKzVOkA4c3b1xwJ5pOYgnfeCfTQDNyzhplb59Bh1JVBlgEbShJKoskic29o0AExtyGDGJyiccST4g/0?wx_fmt=jpeg)

# 访问控制篇之垂直越权

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

## 定义

* 垂直越权，也称为权限提升，是指低权限用户（如普通用户）能够执行高权限用户（如管理员）的功能，或访问高权限用户才能访问的数据
* 还有一种叫降权，高权限用户到低权限用户，一般只有非常特殊的情况才会用到
* 核心点： 未校验**角色 / 权限**（你有没有资格用）

## 为什么会出现垂直越权

* 垂直越权的核心问题：应用程序在服务端未能对用户的操作权限进行有效的、一致的校验，仅依赖客户端（如前端页面、按钮隐藏）来控制功能访问
* 具体来说，通常有以下几点原因：

+ 仅依赖前端进行权限控制：

- 这是最常见的原因。开发者将权限判断放在前端，比如根据用户角色显示或隐藏某些按钮、菜单。然而，攻击者可以直接通过抓包、构造请求等方式，绕过前端限制，直接向后端发送高权限操作的请求。如果后端没有再次验证权限，就会导致越权。

+ 缺乏统一的权限校验框架：

- 每个API端点各自实现权限检查，有的端点可能忘记了添加校验，或者校验逻辑存在缺陷。特别是对于新增的功能或快速迭代的代码，开发者可能只关注业务逻辑，而忽略了权限控制

+ 错误地信任用户输入的角色信息：

- 服务器从客户端提交的数据（如Cookie中的role=user、JWT中的角色字段）中读取用户角色，而没有在服务端进行二次验证或签名验证。如果这些信息可以被篡改，攻击者就可以将自己伪装成管理员

+ 不安全的默认配置或管理接口暴露：

- 一些默认的管理员接口（如/admin、/console）在部署后没有移除或未做严格的访问控制，导致普通用户也能访问。

+ IDOR（不安全的直接对象引用）的变体：

- 当高权限操作所操作的资源ID可以被枚举，且未校验用户权限时，也属于垂直越权。例如，管理员删除用户的接口是/deleteUser?userId=123，普通用户可能无权调用这个接口（接口本身可能对所有人开放），但如果服务端没有检查调用者是否为管理员，那么普通用户就能删除任意用户，这既是水平越权（删除其他用户）也是垂直越权（执行了管理员操作）

## 常见的攻击场景

### 未授权访问（最严重、最基础的垂直越权）

* 核心原理：服务端既没校验登录状态，也没校验权限，任何人（无需登录）都能直接调用管理员 / 敏感接口
* 技术实现：

+ 攻击者直接在浏览器 / 抓包工具请求敏感接口
+ 无需 Token、Cookie、登录状态
+ 接口直接返回数据 / 执行操作

* 漏洞根源：

+ 接口未加登录拦截
+ 未做任何权限控制

### 接口路径直接访问 / 枚举越权

* 核心原理：后端只在前端菜单隐藏管理功能，但接口未做权限校验（不校验是否是管理员），低权限用户登录后，直接通过「已知 / 猜解」的管理员接口路径访问
* 技术实现：

+ 普通用户正常登录系统
+ 知道 / 枚举管理员接口地址
+ 直接请求该接口，绕过前端权限控制

* 常见枚举路径：

+ /admin/user/list
+ /admin/user/delete
+ /admin/config/update
+ /admin/log/clear
+ /admin/reset/password

### 权限参数篡改越权（高频漏洞）

* 核心原理：后端信任前端传入的「角色、权限等级、身份标识」，攻击者通过修改 Cookie、请求头、POST 参数中的权限字段实现提权
* 技术实现：

+ Cookie篡改

```
# 原 Cookierole=user; user_id=1001
# 篡改为管理员role=admin; user_id=1001
```

+ 请求体篡改

```
# 原请求头X-User-Level: 1X-User-Role: normal
# 篡改后X-User-Level: 99X-User-Role: admin
```

+ POST参数篡改

```
// 个人信息修改接口{  "user_id": 1001,  "role": "user" // 篡改为 "admin"}
```

### 前端权限控制绕过（只藏不锁）

* 核心原理：权限只在前端控制

+ 通过 JS 隐藏管理员菜单
+ 通过路由守卫限制页面访问，但后端接口完全不校验权限

* 技术实现：

+ 前端禁用 / 隐藏管理员按钮、菜单
+ 攻击者：

- 浏览器控制台修改 DOM 显示菜单
- 直接构造请求调用管理员接口

+ 后端不做任何权限判断 → 越权

* 漏洞根源：**前端只能做展示，不能做鉴权**，所有鉴权必须在服务端完成

### 身份标识越权（用户 ID/Token 提权）

* 核心原理：

+ 通过篡改user\_id、uid、token中的身份信息，直接变成管理员用户

* 技术实现：

+ 低权限用户登录，拿到自己的 Token / 用户 ID
+ 篡改请求中的用户 ID 为**管理员 ID**（如 1、0、admin 等）
+ 后端以篡改后的 ID 执行操作

### 敏感操作接口未鉴权（高危）

* 核心原理：

+ 重置密码、删除数据、批量导出、系统配置等高风险操作，只做了登录校验，未做权限校验

* 技术实现：

+ 普通用户登录
+ 调用「重置任意用户密码」「清空日志」「批量删除」接口
+ 接口直接执行，无权限拦截 ，重置管理员 / 任意用户密码 → 直接接管账号

### 权限逻辑缺陷 / 配置错误越权

* 核心原理： RBAC 权限体系设计错误

+ 角色权限配置错误
+ 权限继承混乱
+ 接口权限码绑定错误 ， 导致低权限角色**天生拥有高权限**

* 技术实现：

+ 权限系统配置：普通用户角色被误配管理员权限
+ 接口权限码写错，普通权限可访问
+ 新上线接口**忘记绑定权限**，默认所有人可访问

* 漏洞根源：

+ 权限设计不规范
+ 上线未做权限回归测试

## 漏洞危害

垂直越权的危害通常比水平越权更为严重，因为它直接导致权限失控，使攻击者获得高权限

* 数据泄露：获取所有用户的数据、系统配置、数据库信息等。
* 数据篡改/破坏：修改或删除任何数据，包括用户信息、业务数据、系统设置等。
* 系统控制：如果获得管理员权限，攻击者可能进一步上传webshell、添加系统用户、控制整个服务器。
* 业务瘫痪：关闭服务、篡改关键业务逻辑，导致业务无法正常运行。
* 法律与合规风险：严重的数据泄露事件可能导致巨额罚款和声誉损失。

## 靶场

https://portswigger.net/web-security/all-labs#access-control-vulnerabilities

实验一：用户角色可在用户配置中进行修改

测试：直接修改邮箱，然后在请求正文中的JSON数据中增加角色ID

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBgmgzmH3xPWTPTIY8pyTanqmNKAncy1j4Y1D5GB3NHUjwuCKO2zpmtNyAYiaCO2mGrRyhDLwdYdrKUbhoIMIVh9e9naks3IZXs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDe8BtyTITkQNicfJibJtIKVibrZEx624cT9GeqPQzmjyFSTf0rgTkWtVznPicnvbOHia8gdVS5pJomz4VXdblKqqeHzwtEbIEuuiaug/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkB7UWiaK5WbFKReC3vXeQ6gC0XcA8fo0z5vo9xYR4FGtJUIudT22dMq9l52n4e1gosUZsVLy0hFH1gpaOZAUZaK1dUl2Ogwo5Mw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkA1Q1FPKIdlp8OVUvjia8ucVDPZN71KPYSueYicvV5hbsO8NSWBxokia9Xk9jD6sJnXxQkJfSsvoSrOHXcQXjibVlNzNGia9DibgAg6A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAtNRyu9p9o8Ae9y8ZXq6SWBA7dH5d5UYwGHiaNUYG77qoLXEL8r3ic5IdZxQQicVuQficZPFHatoMOHTkWOxRmX6p0TAk7PZzjpKY/640?wx_fmt=png&from=appmsg)

roleid：角色id，可尝试修改

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDbOmicLdWDAvoWRYp7avbjfKb2c0oxc2lYRAXjH7nSxtawbWq1ufcPkamajhXmT0e7h9kib6kiakiauSD1b7iaWYdquiaATdSplJHas/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAXXjqOyTSLa8RdRU5Mh4PWvNNasAIFSiaxleNcIYxwhc1pgRF6NKiaNurcD1K6uiaGVibPNE0s4PHouh8r37GEyTmF5ibNm5LSfORI/640?wx_fmt=png&from=appmsg)

成功垂直越权

实验二：用户ID通过请求参数进行密码泄露

测试：修改用户名，然后源代码中出现密码，导致密码泄露

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCPibYRNnqC7CoFicNyNBwcN6L3Y2wM2AwOWUpvr4knOLdI9v9lxcfaCTS4fjXsbdfr3qbKIsCSkzcOSQ89EVqfcGOyNIoNKkniaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkA3UkcWXzABd1IJwYibJiaUdSQgEL25vg3TNMXsHlPw2TfbicYj64VKTlgnNeras0qU5v457m1hg8xh2fMRg6iaiclJmc1pIUutBL00/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkB8JtIQsNsEc6QpxB9ibJAwCLGWWLpAIzDXYcH5VYsyC8ibNUlwQN4ibczibe5pZbeicic9GmVCs2cyCBqJSKIoSKY0omRNZpHibJSe3E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDpibat0udfwf1QX9icrNoibu0UGOxQMETDyfK2zUTqDduxoxO4kFibaL4FAHd4icicEj5yr5UXjeVCaQQv5Sgkc3OwH7phYGu2KiaiaqQ/640?wx_fmt=png&from=appmsg)

成功垂直越权

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RycyD0uC9K3FoibQ01tEZGuibOZ3V0n635gHObOkMwIDIPiapmdmhho8uib89ulc9aCVfqtP7A8GZmHEQ/0?wx_fmt=png)

一个努力的学渣

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RycyD0uC9K3FoibQ01tEZGuibOZ3V0n635gHObOkMwIDIPiapmdmhho8uib89ulc9aCVfqtP7A8GZmHEQ/0?wx_fmt=png)

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