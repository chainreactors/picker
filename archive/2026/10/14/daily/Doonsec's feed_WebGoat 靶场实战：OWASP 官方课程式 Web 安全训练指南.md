---
title: WebGoat 靶场实战：OWASP 官方课程式 Web 安全训练指南
url: https://mp.weixin.qq.com/s/2J3dMOdb5jBgm-n_GrudVQ
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:43:06.312493
---

# WebGoat 靶场实战：OWASP 官方课程式 Web 安全训练指南

# WebGoat 靶场实战：OWASP 官方课程式 Web 安全训练指南

原创

不懂安全的运维
不懂安全的运维

运维安全入门

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前三个靶场各有一个鲜明标签：SQLi-Labs 讲「原理」，DVWA 讲「防御分级」，Juice Shop 讲「业务逻辑」。这一章的 WebGoat 定位不同——**它是一本可以动手操作的教科书**。

**WebGoat** 是 OWASP 基金会官方项目，与 Juice Shop 并列成为 OWASP 最具代表性的两个教学靶场。但两者气质迥异：Juice Shop 刻意隐藏答案，制造探索感；WebGoat 则**像一门结构严谨的课程**，每节课都包含知识点讲解、示例代码、交互式练习和提示。

对于刚建立安全知识体系、需要理解「为什么这个漏洞叫这个名字」的人，WebGoat 的学习效率远高于其他靶场。

**🛡️ 授权声明**　WebGoat 需要注册账号才能使用（这是它与 Juice Shop 的关键区别）。所有操作请在本机或已授权环境进行。

本文目录

1. WebGoat 是什么，为什么它像一门课程
2. 技术架构：Spring Boot 教学应用
3. Docker 部署与端口说明
4. 本地部署与首次注册流程
5. 核心机制：Lessons 教学体系
6. 实战一：Hello WebGoat 与环境认知
7. 实战二：A1 Injection 跨站脚本
8. 实战三：A2 Broken Access Control 访问控制
9. 实战四：A3 客户端校验绕过
10. 实战五：A5 Security Misconfiguration
11. 常见问题与排错清单
12. 等保视角：从课程到生产加固
13. 总结

## 01WebGoat 是什么，为什么它像一门课程

WebGoat 全称 *WebGoat OWASP Application Security Training Environment*，官方在 GitHub 上的仓库是 `WebGoat/WebGoat`。它的自我描述是「一个故意设计为有漏洞的教学应用程序，旨在为开发者提供安全 Web 应用开发的实战培训」。

WebGoat 的设计哲学可以概括为**「每节课解决一个安全问题，并且必须动手完成才能进入下一课」**。这个强制性的设计非常聪明：它把「学习」变成了「闯关」，避免了安全教程最常见的失败模式——读完文档觉得都会了，一动手全忘。

### 两个项目的定位对比

| 维度 | WebGoat | Juice Shop |
| --- | --- | --- |
| 学习模式 | 课程式，按 Lessons 顺序 | 探索式，无固定顺序 |
| 答案提示 | 每课自带分级提示（Hints） | 可选查看解题思路 |
| 使用门槛 | 需注册账号 | 无需注册 |
| 重点 | 漏洞原理与修复方法 | 业务逻辑与攻击链 |
| 适合人群 | 安全入门 / 开发人员安全培训 | 有一定基础的进阶学习 |

**💡 提示**　一个实用建议：**如果你在给团队做安全培训，WebGoat 是最省心的教材**。因为每节课都有对应的理论讲解，不需要你自己额外准备课件，学员跟着 Lessons 走就能完成闭环。

**界面说明** WebGoat 左侧是一棵 Lessons 导航树，A1 到 A10 依次对应 OWASP Top 10 的分类：A1 注入、A2 失效访问控制、A3 XSS、A4 不安全反序列化……每个节点展开后是若干独立小练习。这套编号就是一份现成的 OWASP 学习路线图，建议按顺序通关，每完成一节再对照等保 2.0 的相应安全通用要求做一次映射复盘。

## 02技术架构：Spring Boot 教学应用

WebGoat 使用 **Spring Boot** 构建，是一个标准的 Java Web 应用。这个技术选型本身就有教学价值——**Java 生态是企业级系统的主流**，在这里练手，技能可以直接迁移到真实的企业系统。

| 层次 | 技术 | 说明 |
| --- | --- | --- |
| 后端框架 | Spring Boot | 提供 REST 接口与业务逻辑 |
| 数据库 | H2 / Derby（内存） | 启动即用，无需外部依赖 |
| 前端 | Thymeleaf 模板 | 服务端渲染的课程页面 |
| 认证 | Spring Security + JWT | 支持 JWT Token 模式 |
| 构建 | Gradle | 官方提供 gradlew 包装器 |

**💡 提示**　WebGoat 的 H2 是**内存数据库**，这意味着容器一停数据就没了。好处是环境绝对干净，坏处是每次重启都要重新注册账号和进度。如果你想长期保存学习进度，官方也支持外部数据库，通过环境变量切换到 PostgreSQL 即可。

## 03Docker 部署与端口说明

WebGoat 官方在 2023 年后把主部署方式迁移到 Docker，并且**主端口从 8080 变成了 8080，辅助端口 9090**。其中 9090 是 WebGoat 额外提供的**「课程/资源服务」端口**，不少老教程里没有提到它。

9080 已被占用时可用 8081 等端口；9090 为辅助服务端口

```
docker pull webgoat/webgoat docker run -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat  # 浏览器访问 http://127.0.0.1:8080 # 首次启动需等待 30-60 秒完成初始化
```

### 推荐的 docker compose 方式

FLAG 变量可自定义课程通关标识；WEBGOAT\_HOST 建议设为回环地址

```
# docker-compose.yml services:   webgoat:     image: webgoat/webgoat     container_name: webgoat     ports:       - "127.0.0.1:8080:8080"       - "127.0.0.1:9090:9090"     environment:       - WEBGOAT_HOST=127.0.0.1       - FLAG=flag{local-dev-env}     restart: unless-stopped
```

**⚠️ 注意**　把 `WEBGOAT_HOST` 设置为 `127.0.0.1` 非常关键。WebGoat 在某些配置下会生成指向容器主机名的绝对链接，设置为回环地址可以避免浏览器里出现无法访问的内部主机名。

常用管理命令：

WebGoat 首次启动较慢，务必看日志确认就绪

```
docker compose up -d     # 启动 docker compose logs -f    # 观察启动进度 docker compose down       # 停止
```

**界面说明** 启动后跟进日志，出现 Tomcat started on port(s) (http)/8080 即表示 Web 容器已就绪。这段之前会打印大量 Spring Bean 装配信息，属正常现象。等这行出现再开浏览器，若始终不出这行，通常是镜像拉取不完整或 8080 被占用，可用 docker compose down 清理后重来。

## 04本地部署与首次注册流程

如果你要研究源码或做二次开发，可以本地运行。

需要 JDK 17+，这是 WebGoat 2023 之后的要求

```
git clone https://github.com/WebGoat/WebGoat.git cd WebGoat  # Java 17 或更高版本 java -version  # 使用官方 Gradle 包装器构建 ./gradlew build  # 运行 ./gradlew run # Windows 下为 .\gradlew.bat run  # 浏览器访问 http://127.0.0.1:8080
```

### 注册流程：容易被卡住的一步

WebGoat 打开后不会直接进入课程，而是先跳转到 `/login` 让你**创建一个新账号**。

密码长度要求为 10 位以上，是 WebGoat 的硬性校验

```
# 访问注册页 http://127.0.0.1:8080/login  # 填写要求（当前版本） # User Name : webgoat     （仅本机使用，无强度要求） # Password  : 至少 10 位 # Email     : 任意合法格式
```

**⚠️ 注意**　**常见失败情况：**① 密码不足 10 位，页面提示校验失败；② 邮箱格式非法（WebGoat 会做基本校验）；③ 启动未完成就访问，页面一直转圈。遇到第三种情况，**用 `docker compose logs -f` 确认 Tomcat 已经完全启动**，通常需要 30 到 60 秒。

**💡 提示**　WebGoat 的账号只存在于容器内存数据库中，**重启容器后需要重新注册**。如果希望进度持久化，可以改用外部数据库，并在 compose 中挂载数据卷。

## 05核心机制：Lessons 教学体系

WebGoat 的课程按 OWASP 分类组织，当前版本（A1-A10）结构如下：

| 课程 | 主题 | 核心知识点 | 难度 |
| --- | --- | --- | --- |
| A1 | Injection | SQL / 命令 / 表达式注入 | ★★☆ |
| A2 | Broken Access Control | 越权与路径遍历 | ★★☆ |
| A3 | HTML5 Security Issues | 客户端校验绕过 | ★★☆ |
| A4 | A4 2021 之前的认证机制 | 弱口令与会话 | ★☆☆ |
| A5 | Security Misconfiguration | 错误配置与信息泄露 | ★☆☆ |
| A6 | Exposing Sensitive Data | 敏感信息暴露 | ★☆☆ |
| A7 | XXE | XML 外部实体注入 | ★★★ |
| A8 | XXE / Deserialization | 反序列化攻击 | ★★★★ |
| A9 | Server Side Request Forgery | 服务端请求伪造 | ★★★ |
| A10 | Logging & Monitoring | 日志与监控缺陷 | ★★☆ |

### 每节课的四个区域

1. **课程讲解**

   ：文字版的原理说明，包含漏洞成因与真实案例。
2. **提交目标**

   ：一个需要你完成的操作，完成后输入并提交答案。
3. **Hints（提示）**

   ：*分级提示*——先给思路，再给具体操作提示，最后给答案。这是 WebGoat 最好的设计。
4. **Success / Failed 反馈**

   ：提交后立即显示结果，并更新课程完成状态。

**💡 提示**　**关于 Hints 的使用建议：**第一遍学习时，卡住超过 20 分钟再看*第一级*提示；如果做完回头看答案，会失去训练价值。但如果卡住超过一小时还在瞎试，**果断看提示**——持续低效挣扎的挫败感，比提前看提示的危害更大。

**界面说明** 每一课页面结构固定：上方是图文讲解（含攻击原理演示图），下方是提交框与 Show Hints 按钮。提交框用于回显攻击是否成功，Hints 分级展开，适合在自行尝试卡住时逐级查看，不必从头看完整解答。

## 06实战一：Hello WebGoat 与环境认知

登录后的第一课是 Hello WebGoat，是纯介绍性质，但有两件事值得注意。

第一，课程会引导你使用 **浏览器的开发者工具**。WebGoat 是极少数**要求你使用 DevTools 才能完成**的靶场——它会引导你查看请求、检查响应、修改前端参数。这让它成为一个优秀的 DevTools 训练场。

第二，它会让你提交一个自定义的 `flag` 值。你可以在容器启动时通过环境变量 `FLAG` 自定义，这样可以给不同的学员配置不同的通关凭证——这是安全培训中很实用的设计。

可为每个学员分配独立 flag，便于跟踪个人进度

```
# 在 compose 中设置自定义 flag environment:   - FLAG=flag{你的通关口令}  # 学员在课程页面提交相同字符串即通过
```

## 07实战二：A1 Injection 跨站脚本

A1 课包含多个子课程，我们重点看其中两个最有代表性的：**Reflected XSS** 与 **SQL Injection**。

### Reflected XSS：反射型跨站脚本

页面提供了一个文本输入框，你的输入会被回显到页面上。课程目标是让页面执行一段脚本。

课程会检测 alert 是否被触发，可能需要特定格式

```
GET /xss?message=<script>alert(1)</script>  # 课程要求的自定义形式 <script>alert('XSS')</script>  # 弹窗被拦截时的替代写法 <img src=x onerror=alert(1)> <svg/onload=alert(1)>
```

**💡 提示**　**DevTools 在这里的作用：**如果直接构造 URL 提交没反应，打开开发者工具的 Network 面板，找到对应的请求，看清楚参数实际是怎么传输的。有时 WebGoat 会把参数放进 POST body，此时构造 URL 是无效的，必须用表单或修改请求体提交。

理解 XSS 的本质很重要：**问题不在于「用户能输入什么」，而在于「用户输入被当作 HTML/JavaScript 执行了」**。防御的核心是*输出编码*——根据输出位置选择正确的编码方式，而不是过滤输入。

### SQL Injection：结构化注入练习

WebGoat 会逐步解锁目标，需要按顺序完成

```
# 登录表单的注入 username: ' OR 1=1-- password: 任意  # 课程会引导你完成多个阶段： # 1) 绕过登录（认证绕过） # 2) 使用 UNION 查询列出所有表 # 3) 判断数据库类型与版本 # 4) 从 WEBGOAT 表中读取数据
```

**💡 提示**　WebGoat 特有的教学设计：**目标是一个个解锁的**。比如你必须先完成「绕过登录」，课程才会显示「使用 UNION 查询」的要求。这是为了**强制建立正确的解题顺序思维**，而不是一上来就用工具一把梭。

## 08实战三：A2 Broken Access Control 访问控制

A2 是 OWASP 2021 版 Top 10 的第一位。课程通过几个小练习，系统性地讲解访问控制的几种失效形态。

| 子课程 | 演示的缺陷 | 教学重点 |
| --- | --- | --- |
| Insecure Direct Object References | 改 URL 参数访问他人资源 | 必须校验资源归属 |
| Insecure HTTP Methods | 页面用 GET 执行了写操作 | 读写方法应分离 |
| Missing Function Level Access Control | 普通用户调用管理接口 | 服务端必须做角色校验 |
| Client Side Enforcement of Server Side Security | 仅前端隐藏按钮 | 前端校验不算防御 |

所有变更类操作都必须有服务端权限校验

```
# 典型 IDOR：直接修改资源 ID GET /xss?message=hello&user=admin  GET /query?role=admin          # 直接请求管理功能接口 PUT  /users/1/role             # 未鉴权修改他人角色
```

**💡 提示**　「Client Side Enforcement of Server Side Security」这一课和 Juice Shop 的购物车漏洞是同一个道理：**前端隐藏了按钮，后端接口却照样可以调用**。WebGoat 把这个道理讲得很直白：*「安全不能靠隐藏 UI 元素来实现」*。

**💡 提示**　修复这类问题的正确姿势：**在服务端使用注解声明访问控制**。Spring Boot 中常见的是 `@PreAuthorize`，配合方法级安全（`@EnableMethodSecurity`）统一管理，比在每个 Controller 里手写 if 判断更可靠、更难遗漏。

## 09实战四：A3 客户端校验绕过

A3 这一课的设计很有教学价值：它让你**亲手验证一个流传很广的错误观点**——「前端做了校验，所以很安全」。

课程提供一个注册或资料修改表单，前端 JavaScript 会校验输入（比如限制价格、限制角色值）。任务是绕过它。方法很直接：

服务端如果信任前端校验值，则请求直接生效

```
# 1) 打开 DevTools -> Sources / Elements # 2) 找到校验函数，或直接定位表单提交逻辑 # 3) 去掉校验分支 / 修改变量值 # 4) 或者更简单：拦截请求，直接改 Body 里的值  # 使用 curl 复现（完全绕过前端） curl -X POST http://127.0.0.1:8080/path \   -H 'Content-Type: application/json' \   -d '{"price": 0.01, "role": "admin"}'
```

**⚠️ 注意**　这个练习的真正教学点不是「怎么绕过」，而是**让你亲眼看到绕过有多容易**。任何基于前端的限制——包括价格、权限、次数、格式——攻击者都可以用 curl 或修改请求轻松绕过。唯一的解法是*在服务端重复执行所有关键校验*。

## 10实战五：A5 Security Misconfiguration 安全配置错误

A5 是一类「没有技术含量但影响巨大」的漏洞。课程会带你找出默认配置、暴露的目录和可预测的文件。

| 检查项 | 典型问题 | 修复方向 |
| --- | --- | --- |
| 默认凭据 | 使用出厂账号密码 | 首次部署强制修改 |
| 目录列表 | 服务器开启目录浏览 | 关闭 autoindex |
| 错误页面 | 报错...