---
title: 一份“指纹探测清单”深度解读
url: https://mp.weixin.qq.com/s/VW_41Jtr6ku23yKgmCQIJg
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:06.802760
---

# 一份“指纹探测清单”深度解读

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibPC5NLUVVrqj3j9EcDY2ibhH5rvpFbjLGjV0kPibu1op1zK312wtP6rhr0zXKI79NLflrdYibhUdgE99kZ8YfaOGTb1k8SsCWK9hkicPDL6jE/0?wx_fmt=jpeg)

# 一份“指纹探测清单”深度解读

原创

小话安全
小话安全

小话安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 1. `/ReportServer`

**系统/中间件**：帆软报表（FineReport / FineBI）
**说明**：帆软报表的核心服务入口。未授权访问可能导致报表数据泄露、模板被篡改，甚至利用后台功能执行系统命令（如插件上传、数据集写文件等）。

### 2. `/api/x`

**系统/中间件**：泛指自定义API端点（`x` 通常是具体的模块名，如 `user`、`system`）
**说明**：常见于前后端分离项目，如若依（RuoYi）、JEECG-Boot等框架生成的API。暴露后可能绕过前端权限校验，直接调用内部接口造成数据泄漏或越权操作。

### 3. `/api/v2/api-docs`

**系统/中间件**：Swagger / OpenAPI（常与Springfox、Springdoc集成）
**说明**：Swagger 2 的API文档JSON文件。攻击者可从中获取所有接口路径、参数类型、鉴权方式，从而精准构造攻击请求。

### 4. `/apps/x`

**系统/中间件**：可能指Cloud Foundry平台的应用列表，或某些PaaS平台的管理端点
**说明**：`x` 一般为应用名或ID。若未授权访问，可列出部署的应用信息、健康状态、路由等，为后续攻击提供内部拓扑。

### 5. `/druid/login.html`

**系统/中间件**：阿里巴巴Druid连接池监控台
**说明**：Druid Monitor提供SQL审计、URL监控、Session监控等。若未开启认证或使用弱口令，可直接查看数据库SQL语句（含敏感数据）、连接地址及账号信息。

### 6. `/geoserver/web/`

**系统/中间件**：GeoServer开源地理数据服务器
**说明**：暴露GIS数据和WMS/WFS服务。历史版本存在远程代码执行（如CVE-2024-36401）或路径遍历漏洞，可读取服务器文件或执行命令。

### 7. `/chat/x`

**系统/中间件**：即时通讯模块（如Openfire、Rocket.Chat、融云、环信接入端）
**说明**：`x` 可能是房间ID或用户标识。未授权访问可读取聊天记录、伪造消息，或利用WebSocket接口进行跨域攻击。

### 8. `/v2/api-docs`

**系统/中间件**：与 `/api/v2/api-docs` 相同，Swagger 2 API文档
**说明**：同上，直接暴露后端接口定义。

### 9. `/console/notinrealm/rest/commons/location`

**系统/中间件**：用友NC（UAP平台）或私有云管理控制台
**说明**：这是一个已知的未授权访问路径（常见于用友NC 6.5等版本），可获取系统部署路径、中间件版本、服务器环境信息，配合其他漏洞可实现远程命令执行。

### 10. `/WebReport/ReportServer`

**系统/中间件**：帆软报表（FineReport）的另一种部署上下文
**说明**：与 `/ReportServer` 功能一致，可能是同一应用的不同映射路径，同样存在报表越权、模板注入等风险。

### 11. `/env`

**系统/中间件**：Spring Boot Actuator 端点
**说明**：暴露全部环境变量、应用配置、数据库密码、内网地址、API密钥等。是**高危敏感信息泄露**终点。

### 12. `/api/jeecg-boot/`

**系统/中间件**：JEECG-Boot 快速开发平台
**说明**：该平台部分版本存在权限绕过（如Swagger接口未授权）、SQL注入、任意文件下载等漏洞。暴露该前缀意味着大量业务接口可被直接调用。

### 13. `/prod-api/`

**系统/中间件**：若依（RuoYi）框架的生产API前缀
**说明**：若依框架默认将后端API统一放在 `/prod-api` 下。若未正确配置网关鉴权，攻击者可直接访问所有业务接口，导致越权、数据泄漏。

### 14. `/api/swagger-ui.html`

**系统/中间件**：Swagger UI 的可视化界面
**说明**：提供API文档的交互式页面，攻击者可直接在此处尝试调用所有接口，比纯JSON文档更易利用。

### 15. `/httptrace`

**系统/中间件**：Spring Boot Actuator 端点
**说明**：记录最近100次HTTP请求的详细信息，包括请求头、Cookie、Session ID、授权Token等。可导致用户会话被劫持。

### 16. `/jeecg-boot/`

**系统/中间件**：JEECG-Boot 应用根路径
**说明**：可能是前端页面或后端根路径。若可直接访问，会暴露登录页、静态资源，甚至直接显示异常堆栈信息。

### 17. `/nacos/`

**系统/中间件**：Alibaba Nacos 配置中心/服务发现平台
**说明**：Nacos 默认控制台路径。若未启用鉴权或存在CVE-2021-29441（绕过鉴权），可读取所有配置（含数据库、中间件密码），甚至修改配置注入恶意脚本。

### 18. `/jeecgboot/`

**系统/中间件**：同 JEECG-Boot（无连字符的写法也是该平台常见上下文）
**说明**：同上，暴露平台敏感信息。

### 19. `/minio/`

**系统/中间件**：MinIO 对象存储管理控制台
**说明**：MinIO Console。若未配置访问密钥或存在CVE-2023-28432（信息泄露），可列出所有存储桶、下载/上传任意文件，严重时覆盖可执行文件导致远程代码执行。

### 20. `/signin/x`

**系统/中间件**：登录处理端点（`x` 可能是回调参数或认证方式）
**说明**：常见于自定义SSO、Keycloak或Spring Security的 `/signin` 路由。暴露后可能未对OAuth回调进行校验，引发开放重定向或CSRF攻击。

### 21. `/webroot/decision/login`

**系统/中间件**：帆软决策平台（FineDecision / FineReport决策系统）
**说明**：报表系统的管理后台登录页。许多旧版本存在默认口令（admin/123456）或权限绕过，可直接进入后台执行模板注入、SQL查询等。

### 22. `/api/nacos/`

**系统/中间件**：Nacos 的 REST API 接口
**说明**：用于服务注册、配置拉取的HTTP API。若未鉴权，外部可以直接获取配置中心的全部内容，或注册恶意服务进行内网探测。

### 23. `/trace`

**系统/中间件**：Spring Boot Actuator 端点（老版本）
**说明**：与 `/httptrace` 作用相同，记录HTTP跟踪信息。同样会泄露Cookie、Authorization头等敏感数据。

### 24. `/toLogin`

**系统/中间件**：通用登录跳转路径（Shiro、Spring Security、很多自研系统）
**说明**：通常用于将未认证用户重定向到登录页。但如果该路径本身未过滤，可能暴露登录前的referer信息或引起开放重定向漏洞。

### 25. `/xxl-job-admin/toLogin`

**系统/中间件**：XXL-JOB 任务调度中心
**说明**：XXL-JOB 的管理界面。历史版本存在默认口令（admin/123456）、未授权访问（CVE-2022-36157等），可导致恶意任务被调度，进而执行任意系统命令。

### 26. `/webroot/decision/system/info`

**系统/中间件**：帆软决策系统信息接口
**说明**：直接返回系统版本、License信息、服务器路径、部分环境变量等。攻击者可据此精准匹配已知漏洞（如特定版本的RCE漏洞）。

### 27. `/swagger-ui.html`

**系统/中间件**：Swagger UI 标准入口
**说明**：最经典的API文档页面。其暴露的危害与上述Swagger接口一致，甚至更加直观。

---

### 综合风险评级

以上绝大多数路径都属于**高危**或**严重**级别，因为它们要么直接泄露数据库密码、API密钥、Session令牌等关键凭证，要么暴露完整的接口定义，为后续精准攻击铺路。**最直接的修复措施**：禁止公网访问这些路径；若业务必需，则通过网关或防火墙做IP白名单，并对所有端点进行强身份认证与权限校验。同时，立即升级相关组件到已修复漏洞的最新版本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVXqKQxqxX38MdQFibYGUWYAyDKHfpibNl31oq1qWjy44stFJvficsdbWBv18AVhOO4ibY7UWIHXZToM0mt9LDdC0PgNpILnlIHE60s/0?wx_fmt=png)

小话安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVXqKQxqxX38MdQFibYGUWYAyDKHfpibNl31oq1qWjy44stFJvficsdbWBv18AVhOO4ibY7UWIHXZToM0mt9LDdC0PgNpILnlIHE60s/0?wx_fmt=png)

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