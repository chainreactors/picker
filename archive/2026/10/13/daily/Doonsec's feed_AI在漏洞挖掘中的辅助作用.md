---
title: AI在漏洞挖掘中的辅助作用
url: https://mp.weixin.qq.com/s/mlh9pX_0BnZyZ5gdNlM3og
source: Doonsec's feed
date: 2026-10-13
fetch_date: 2026-10-14T06:50:59.588874
---

# AI在漏洞挖掘中的辅助作用

# AI在漏洞挖掘中的辅助作用

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于隐雾安全
，作者星期五

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

## 引言

我理解的AI对漏洞挖掘的价值，主要是降低重复性工作的时间成本。漏洞挖掘通常经历攻击面测绘、漏洞点验证和危害链评估三个阶段。前端逆向、接口归类、用例整理、跨接口比对和证据整理会占用大量时间；AI 适合辅助处理这些信息密集型工作，使测试者把精力放在业务判断、风险边界和人工复核上。

本文将 AI 的作用限定为三个层次：第一，理解和整理已获得的信息，例如前端代码、接口文档和请求响应；第二，根据已有线索提出可验证的测试假设，并协助组织用例；第三，归纳证据、记录已测状态和发现的关联。AI 输出的是线索、结构和候选用例，不是漏洞结论。任何结论都应在授权范围内，由测试者结合身份、对象归属、响应内容和实际影响复核。

后文案例均来自原始记录。为避免把报告写成可直接用于未授权操作的说明，本文保留原有证据截图和技术事实，同时对高风险动作以“经授权验证”“风险影响”的方式概述。目标域名和敏感数据沿用原文的脱敏形式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4kp359AaRqL6qx0AnnaoPJ6vAYAmxV3ic8e9WjKHwVVj5sk1Oib2PFWZTBicyfn8DekZEjwRbtq68RDg9XTrjLa402tFHzaVpjBNI/640?wx_fmt=png&from=appmsg)

❞

## 一  AI 辅助漏洞挖掘的工作方式

### 1 前端 JavaScript 解析与接口梳理

现代 Web 系统常采用前后端分离架构，路由、接口调用、参数拼装、鉴权流程和部分加解密逻辑往往分散在压缩或混淆后的 JavaScript 文件中。前端代码不能保证覆盖全部后端能力，但它通常能提供高价值的入口线索，例如 API 前缀、接口路径、参数名、角色字段和请求拦截器。

AI 可以帮助按模块阅读代码片段，提取接口、参数、调用位置与疑似权限判断，并整理为接口台账。台账应至少记录：接口路径、请求方法、身份要求、对象标识、敏感字段、来源文件、测试状态和证据编号。分段处理可以降低长文本遗漏，但仍应以搜索结果、浏览器网络请求和实际响应交叉验证。

### 2 认证异常与权限验证的组织

401、403、重定向或网关拦截并不直接等同于“存在绕过”。它们可能来自身份缺失、令牌过期、角色不足、来源限制、WAF 规则或业务状态。AI 的作用是根据请求上下文整理可能原因和最小化验证步骤，协助测试者区分认证、功能级授权和对象级授权问题。

对象级授权关注“当前身份是否有权访问这一个对象”；功能级授权关注“当前身份是否有权调用这个功能”。例如，普通用户读取他人记录属于对象级问题；普通用户调用管理员接口属于功能级问题。两类问题都需要使用不同身份和不同归属对象进行对照，不能只凭单个状态码下结论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4kpk0RxAe8jDR5DLQzh5RzKYibOwN3xjASWJxdOQOMYFzVqfp8NibJiaFzwYib8MhTdLPaaWbh1paRHIuibW8MLXaJNwicHYwlJNfV4k/640?wx_fmt=png&from=appmsg)

❞

### 3 上下文记录与跨接口关联

拿到用户 ID、商家 ID、工号、订单号或角色字段后，单点测试往往只能说明一个接口的情况。更有效的做法是将这些事实纳入结构化记录：参数来自哪里、属于哪个身份、在哪些接口出现、哪些验证已经完成、哪些结果仍待复核。AI 可以协助维护这类记录，生成待测清单和结果摘要，减少人工在多轮测试中的遗漏。

自动化只应在明确的授权范围、目标清单、速率限制和操作白名单内运行。它不能“保证无遗漏”，也不应在遇到拦截时自行扩展测试强度。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4k5xftoHmV1ggaOo9Lxp4nO8zHDJ2nVP9epwkPJd0ib0L9SqKSXKhibiaWMLgUzgwGRafOL7bI2doj6hZ5sQIZhRceGesCicDRicCII/640?wx_fmt=png&from=appmsg)

❞

### 4 角色与高影响功能分析

账号名、roleId、菜单项或前端字段只能作为角色线索，实际权限必须以服务端行为为准。高权限功能通常涉及用户管理、配置管理、导出、文件管理和业务审批。AI 可以帮助把角色线索、接口定义和响应结果关联起来，并优先列出需要人工验证的高影响功能。风险评级取决于可达性、可操作范围、数据敏感度和实际影响，不能仅依据账号名称判断。

### 5 基于 API 文档的测试设计

Swagger、YApi 或自研接口文档能够说明接口路径、请求方法、字段约束和数据模型，有助于减少调用猜测；它们本身并不等同于白盒代码审计，也未必反映完整业务逻辑。AI 可以依据文档生成边界值、类型差异、权限对照和异常处理的候选用例，再由测试者结合接口语义与响应进行筛选。

### 6 基于语义的风险覆盖

参数名和数据类型可以提供初始假设，例如 id 类字段常需要对象归属验证，sort 或 order 类字段需要检查输入约束，url 或 path 类字段需要检查服务端处理边界，file 类字段需要检查上传与引用链路。但参数命名不是漏洞证据。AI 的价值在于提醒可能被忽略的类别，并按接口语义生成可控、可记录的测试矩阵。

### 7 安全边界与人工确认

AI 辅助测试的前提是遵守授权范围和业务安全边界。HTTP 方法不能单独代表风险：GET 也可能触发昂贵计算或状态变化，POST、PUT、DELETE 也可能是必要但高风险的业务接口。因此应以操作的实际效果为准，默认使用最小数据集、只读验证和低频请求；涉及新增、修改、删除、上传、权限绑定、导出大量数据或可能影响生产业务的动作，应暂停并由人工确认。

## 二  案例记录

以下案例保留原始发现链路、截图和数据规模。文中“AI 参与”均指其对前端代码、接口、参数或响应的辅助整理；漏洞是否成立以截图所示的授权验证与返回结果为依据。

### 案例 1 访客预约系统的对象级授权问题

在尝试登录并获取站点前端资源后，将 JavaScript 文件交由 AI 协助梳理，得到访客详情和分页列表两个高价值接口。随后以已授权测试身份进行对象归属对照：详情接口需要 JWT，但原始记录显示，切换对象标识后仍可返回其他访客记录；列表接口支持分页并返回完整访客信息。

这一案例的关键不在于接口是否要求登录，而在于服务端是否把“当前令牌代表的用户”与“请求对象”进行绑定。原始记录中的 ID 范围为 1 至 5465，列表接口返回总量为 5,354 条，两者应分别记录，避免将可枚举范围和实际记录总数混为一谈。返回字段包含姓名、手机号、身份证号、工作单位、车牌号和被访人姓名，影响为高敏感个人信息暴露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4nsLcfF4gqqcA6iaVGAbDJhOZSkGIPW2yiaheESNSBkFU2kkoGrUMfMOGfGlHC5zgic7CF0x9j44hS0WJWciblPspdibkELs4GKL9qI/640?wx_fmt=png&from=appmsg)

图1 登录入口与前端资源获取线索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4mWRdcarIlnpN8OnKS3V0ADibIia3ju4ss5qx0xq3C8B7xjFGxTuMZvva5nObsME1e5s6Tf0nRcFick95X0ULdh2RMWvSwfLR5IX8/640?wx_fmt=png&from=appmsg)

 图

2  详情接口返回其他对象记录的原始证据

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4mYN8Rcct3mVZqv5dHvl8ecBXGfTdK2PnL7TT6nETKAhDpP7LsCIUdqvCEKxicibSER8O9dO4Ze9eOgNOicVWaYyTsQFLzzfMhAc8/640?wx_fmt=png&from=appmsg)

 图

3  分页列表接口返回的访客数据示例❞

### 案例 2 多端系统中的身份与权限边界问题

该系统同时存在微信 H5 端和 PC 管理端，二者使用不同的 API 前缀。首先，以测试账号在个人身份页面进行对象归属对照，原始记录显示可通过修改 ID 查看其他个人信息，属于典型的对象级授权缺失线索。

随后，对 PC 端身份验证逻辑、令牌处理和接口调用进行梳理。原始记录显示，H5 端账户可在跨端身份处理链路中获得更高权限，并在后续接口调用中读取工作人员、供应商、租户等信息，以及与摄像头部署相关的拓扑和分布信息。此类结论需要把“令牌可复用”“角色已变化”“高权限接口可访问”三类证据分别保存，避免只依据前端字段判断提权成立。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4nFcMfibpneiaq7QR8nv5Bl5VjpC0FAFG2QlmoFjjBuo5VRVVibMtkYFtzeNQicNZ0zuPg7cPbhyHjDyVvooicYyMZSKiacO3dRnNiavo/640?wx_fmt=png&from=appmsg)

图4  目标系统页面与分析入口

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4l3NsxOoPUXBoLYyceVrC0jt7G4JnfR14TtAoxicQlwKMVLS8B5KVqkdpJsJZ8ZcWoG1QdSQv9jKQbfE1sWicI1BCupKy3Rmb9kA/640?wx_fmt=png&from=appmsg)

图

 5  不同对象的身份信息对照

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4luad8LTf0pPVSHhEKdn1Q4maxPCpVxgd5lmauP71oz46icWpvfZemveicF620yNp63PjOPqYK74CyIQ8VHzCgK4W4LzTQichyIibc/640?wx_fmt=png&from=appmsg)

 图6  跨端身份处理与接口响应证据

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4niaSvEdPsqY7Csj1vjVbaHFTMiaphXLkBK9ic5kcMLF5RoeqTyw7lQDAqTjU3jwH4Q3Y2p4udd29mIK9PhBGiaiaFcH3S8RaPA9Rvg/640?wx_fmt=png&from=appmsg)

 图7  原始记录中的导出结果示例

❞

### 案例 3 地图系统中的接口暴露与配置风险

本案例原始记录包含同类地图站点的多个独立发现。为避免把不同系统误认为一条利用链，以下按“教职工信息”“门户配置与角色”“接口文档与文件管理”“组件版本风险”四个子场景整理。

#### 3.1 教职工信息接口与令牌用途异常

登录请求中出现 OAuth 令牌响应后，AI 协助对前端 JavaScript 进行接口归类，提取出 /os/ 前缀下的教职工相关接口，并结合运行时配置确认服务端地址。原始记录显示：未携带令牌时接口返回 401；将登录响应中取得的 refresh\_token 作为 Bearer 凭证提交给资源接口时可访问教职工数据。

按 OAuth 设计，refresh token 应只用于向授权服务器换取 access token，不应被资源服务器当作访问凭证。因此，若原始对照请求可稳定复现，问题应表述为“资源服务错误接受 refresh token 或令牌校验边界不当”。由工号关联后返回的字段包括教师信息、身份证号、电话、姓名、政治面貌和职位，属于高敏感个人信息。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nia0wSYhDibFQMic7Z1x9rAKx2DpegLJswknUve198ib1WGuic9pPTWscibXhiaQvafBFIq49Yibjuet1Z0kYSYiaMiczULMOauOQg7lP3w/640?wx_fmt=png&from=appmsg)

图8  地图站点登录页面

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4mUdEnGA8PvgBIPaK41bQIB3SkQ9B6rwCnvBYb6s1q65CBEYEI9FpIyo5cWnU7oYM3o7TMp451kt3n082KCNIOdRDdPiaXJmdfU/640?wx_fmt=png&from=appmsg)

图

9  登录请求与令牌响应线索

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4lNcfUJzn9PVrO5icn5mzYUWbQoHgeL8yVHVsMD3Lc1x9iarlonACKfK1MtCCkGibVt7fbWaENZreDS9lgvEE08BXfpib7hibSLWMWc/640?wx_fmt=png&from=appmsg)

图

10  前端代码中与令牌处理有关的调用线索

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nv7yicyznIXC8bHp6iaKJXurn76niafoTaJlndrLRibzo3ofib1ySMn5xkWuKcVOfTMqgyz7k31DHG1YLpAeKic7LGacDQcod8j1L6g/640?wx_fmt=png&from=appmsg)

图

11  JavaScript 中提取到的教职工接口路径

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4mlTeia2n2fUsS0BibGpCQVwTdMu4qHicGoS39ibwVicAPWd13WdJzeHlsickHbrCPWLWylUpaWicvqUOFuEuHYe9qIUCwSibvia31GAOgA/640?wx_fmt=png&from=appmsg)

图12  携带凭证后的教职工接口响应

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4lyM6NImzHJ97YQichJxu4Xrr38wiabQcwRsDwDibELibKCOjvhB5ASVSrRcqWXRG1vPL4JwaJFUtLiaCyDehricRTLw9BwOiacTvcNicM/640?wx_fmt=png&from=appmsg)

图13  工号与教职工信息的关联响应

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4k9zQ9d8KdCjBqkShdmiaEYRcKibZ9J6SCJclnsEs4vBXzR1NJSJgh7WZHiam0AdqKvtsLEWbztdKhQozJHmHlySeK3ibThXY0ZMss/640?wx_fmt=png&from=appmsg)

 图14  原始记录中的数据处理脚本界面

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nhNia8heO4WQImdjV2CiaLJP6jQBd8lbC80D5kIqrysQ0oOx7gFSooRh633lX2nbQyqY0D5HLZcutZRiaNq2ic6MRFzQ9RmPcsjbI/640?wx_fmt=png&from=appmsg)

图

15  原始记录中的导出结果示例

❞

#### 3.2 门户配置与角色绑定接口

在登录状态下继续审计前端资源，可发现地图服务配置、后台管理接口和门户配置读取路径。地图服务 Key 出现在前端并不自动构成高危漏洞，仍需结合服务端限制、配额和实际数据范围评估。原始记录中的重点是配置查询、文件上传、配置保存与角色绑定等接口的服务端权限验证。

对于门户 Logo 修改场景，风险应建立在“普通身份能够读取配置、上传资源并写回配置”的完整对照链上，而不是仅以能够看到图片为依据。对于 rule/bind 场景，原始记录显示普通用户的 role 为空、用户列表可读取角色信息，且绑定 ruleId=1 后可得到大量后台功能。该问题属于功能级授权缺失，需保留绑定前后身份与菜单、接口权限变化的证据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4kN01cx2Rhsib5nVoc06TbBsf7SOgYTpO6vuEfKs47vPicgV0H4PjbjOXr6O9B4ej6khnMzCFtJ3ojtNibwWjykEas0BsWFp7z3vM/640?wx_fmt=png&from=appmsg)

图 16  前端中出现的地图服务 Key 线索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4n5CVbTlgWNPMp2v6RcYF9XGFaUw0qvhKpSN09hAuL3O6adiaXQ2EWQUunOqA6KIsbYWia2bHeBj4yjKEiciciclggiakeXVB4BAWH88/640?wx_fmt=png&from=appmsg)

 图

 17  后台管理接口路径的代码线索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4kXD7xNQX2qKx6ic3x8NojDGkOsCyloBOEelwibKYIpx7z2v1SCIZKBFSqRCZTvjXMXC4slBeib2FVhl2GCkE7LGMJVeLjQrHr6O8/640?wx_fmt=png&from=appmsg)

图 18  配置读取接口与 Logo 路径返回

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4mpLcwnMo05WlfaVBibL94CasIVGCTOeVjZMyic1cKR5FoQX8LpXCJpAiazjZt0Wq5nbVHVaia2H6NOEVbdX2COjGF9BcMgEEGBuog/6...