---
title: 攻防场景Cursor实战化挖掘漏洞--从2天到20分钟
url: https://mp.weixin.qq.com/s/f5bLH6n9V_-oSedvH_QvSA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:55.647986
---

# 攻防场景Cursor实战化挖掘漏洞--从2天到20分钟

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbh2SjqVbWL0U7rypeEOenGKGgowVeVgQvzIsMBMb7usB68jI7xz8muYuwSLeET4hfC1uwwq59L2icg/0?wx_fmt=jpeg)

# 攻防场景Cursor实战化挖掘漏洞--从2天到20分钟

原创

Hyyrent

0xSecurity

![]()

在小说阅读器中沉浸阅读

## Cursor挖掘漏洞成果展示

先看看AI输出的漏洞审计报告，准确率基本达到80%，如果没有企业会员可以去闲鱼购买一个

![image-20260109150839854](https://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh2SjqVbWL0U7rypeEOenGKicEAwVF7qOms6ickoNKe1uTdW3JQx6qPoD06y2ZY17OrHAcpWBQGE0NA/640?wx_fmt=png&from=appmsg)

## 一、为什么选择 Cursor 做代码审计？

传统 Java 代码审计的痛点：

* 项目体量大，调用链复杂
* 手工追踪 Controller → Service → DAO 成本极高
* 容易漏掉“隐藏参数”“内部逻辑分支”
* 扫描器噪声大，人工二次确认成本高

**Cursor 的优势在于：**

* 能自动拉取上下文（跨文件 / 跨层级）
* 擅长“沿变量 / 参数”扩展分析
* 适合灰盒场景（已有接口 / 流量 / 入口）

> Cursor ≠ 自动扫描器 Cursor = **代码审计加速器**

---

## 二、整体审计思路（强烈推荐）

```
接口入口 → 配置映射 → 参数接收 → 调用链路 → 漏洞 Sink
```

Cursor 的正确用法是：**先缩小范围，再让 AI 深挖。**

---

## 三、阶段一：Web 配置与接口暴露面分析

### 3.1 web.xml / Spring 配置分析

重点关注以下配置点：

#### web.xml

* `<servlet>`
* `<servlet-mapping>`
* `<url-pattern>`

Cursor 提示词示例：

```
列出 web.xml 中所有可直接访问的 URL Pattern，
并指出对应的 Servlet 或处理类。
```

---

#### Spring MVC / Spring Boot

重点注解：

* `@Controller`
* `@RestController`
* `@RequestMapping`
* `@GetMapping` / `@PostMapping`

Cursor 使用技巧：

* 打开 Controller 文件
* 让 Cursor 自动汇总路径

示例提示词：

```
列出这个类中所有对外暴露的接口路径，
并标注是否存在访问控制。
```

---

### 3.2 鉴权绕过配置检查

重点关注：

* Filter
* Interceptor
* SecurityConfig
* WebSecurityConfigurerAdapter

Cursor 提示词：

```
分析认证和鉴权配置，
是否存在 permitAll、ignore、excludePathPatterns 等绕过点。
```

---

## 四、阶段二：classes / lib / jar 源码分析

### 4.1 WEB-INF/classes 分析

* 对比 `.class` 与反编译 `.java`
* 注意是否存在未部署源码

Cursor 辅助点：

* 帮你快速理解反编译代码
* 标记关键逻辑分支

---

### 4.2 lib 目录下 jar 包审计

重点关注：

* 是否包含业务逻辑
* 是否存在内部接口实现
* 是否存在调试 / 管理功能

Cursor 提示词：

```
这个 jar 是否包含业务处理逻辑？
是否存在对外暴露或可调用的接口？
```

---

## 五、阶段三：调用链路识别（Cursor 最强能力）

### 5.1 入口函数确认

常见入口：

* `request.getParameter()`
* `@RequestParam`
* `@RequestBody`
* `HttpServletRequest`

### 5.2 前置知识输入

不同的语言审计的方法和思路不一样，在让AI分析代码时候需要提供一些前置知识，这能让 AI 更精确地聚焦在“可能的风险点”，而不是泛泛地猜测

像SQL注入，不同语言的sink点也不完全相同

| 语言 | 方法 / 函数 | 示例代码 / SQL |
| --- | --- | --- |
| Golang | `(*gorm.io/gorm).Where` | `db.Where(StringData).First(&data)` |
| Golang | `(*github.com/jmoiron/sqlx.DB).Queryx` | `db.Queryx(query, params)` |
| Java | mybatis like | `select * from users where username like '%${name}%'` |
| Java | mybatis order by | `select * from users order by ${orderby}` |
| Java | mybatis-plus apply | `wrapper.eq("id", id).apply("username=" + name);` |
| Python | pymysql execute | `sql = "select * from users where username = '%s'" % (name)` |
| Node.js | mysql query | `sql = "select * from users where username = ${name}"` |

在Shiro和Spring Security中，可以配置哪些API不需要进行权限校验

* 在Shiro中，可以使用Shiro的过滤器链（Filter Chain）来配置不需要进行权限校验的API
* 在Spring Security中，可通过继承WebSecurityConfigurerAdapter类并重写其中的configure()方法，配置不需要进行权限校验的API

![image-20251230153740679](https://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh2SjqVbWL0U7rypeEOenGKvdu9gLNoDic312al6xzCDlbzVibSC2cGkjiak8Ws8DvPk4hESkXZMTHAA/640?wx_fmt=png&from=appmsg)

### 5.3 最终Cursor 提示词：

```
1.web.xml/Spring配置分析
找出其中配置的可直接前台访问的 .jsp、.do、.action、.html、.json、.servlet等接口路径。
指明配置项与访问路径的对应关系：
web.xml→<servlet-mapping>、<url-pattern>
@Controller、@RestController、@RequestMapping等注解标注的接口
检查是否存在匿名访问的接口（无登录/权限验证拦截）。
检查Filter、Interceptor、SecurityConfig、WebSecurityConfigurerAdapter等中是否存在鉴权绕过配置。

2.classes/lib/jar源码分析
对比WEB-INF/classes下的 .class文件与反编译后的 .java文件。
对lib下的 .jar文件进行反编译，检查是否包含业务逻辑代码。
逐一分析对应的Controller、Service、DAO、Repository层实现：
对应的请求路径（前台/后台）
涉及的外部依赖或第三方库（如HttpClient、JdbcTemplate、Hibernate等）
标注潜在的高危点：未校验的用户输入、外部命令调用、文件上传写入、动态SQL拼接等。

3.识别调用链路
标识所有暴露给前端或外部调用者的接口（如RESTAPI、RPCEndpoint、Controller方法、Servlet）。
确定入口函数是否为用户完全可控（如request.getParameter()、@RequestParam、@RequestBody）。
检查系统是否已接入统一认证（如SpringSecurity/JWT/OAuth2/Session）。
深入分析完整调用链：
Controller→Service→Repository→外部系统
判断入口是否存在强约束：
用户归属验证
签名、时间戳、防重放机制
输出是否可以绕过认证或越权。

4.重点模块审计（前台与后台分开）
重点排查以下常见的漏洞类型：
漏洞类型漏洞Sink点（常见函数/类）审计描述
SQL注入Statement.executeQuery(), Statement.executeUpdate(), JdbcTemplate.queryForList(), createNativeQuery(), EntityManager.createQuery()检查点：SQL是否通过字符串拼接、+、String.format、concat等方式插入用户输入（如Request参数）。优先关注MyBatis自定义SQL与原生JDBC使用场景。
命令执行（RCE）Runtime.getRuntime().exec(), ProcessBuilder.start(), ShellUtils.exec()检查点：是否拼接用户输入到命令中，或允许上传执行脚本。
文件上传/任意文件写入MultipartFile.transferTo(), FileOutputStream.write(), Files.write(), FileUtils.copyInputStreamToFile()检查点：是否校验扩展名、MIME、目录路径；是否防止 .jsp、.jspx、.java等脚本文件上传。
反序列化ObjectInputStream.readObject(), JSON.parseObject(), Yaml.load(), XStream.fromXML()检查点：是否对外部输入执行反序列化；是否使用存在漏洞的库（如fastjson<1.2.83, Jackson未加白名单）。
任意文件读取Files.readAllBytes(), FileInputStream, IOUtils.toString(), response.getOutputStream().write()检查点：是否直接读取用户指定路径；是否存在目录遍历绕过。
路径遍历newFile(), Paths.get(), ServletContext.getRealPath(), File.delete()检查点：是否存在 ../等拼接导致目录逃逸。
XXE（XML外部实体）DocumentBuilderFactory.newInstance(), SAXParserFactory.newInstance(), XmlMapper.readValue()检查点：是否关闭外部实体解析；是否解析来自不可信来源的XML。
SSRFHttpURLConnection, HttpClient.get(), RestTemplate.getForObject(), URL.openConnection()检查点：是否允许用户指定URL并由服务器发请求；是否存在内网访问风险。
XSSresponse.getWriter().write(), 模板引擎输出 (<%= ... %>, Thymeleaf, Freemarker)检查点：是否未进行HTML/JS输出转义。
认证绕过/越权缺少@PreAuthorize、@Secured、Session检查或过滤器逻辑错误检查点：检查接口访问控制逻辑，是否能直接调用他人资源。

5.输出结构（每个发现需包含以下部分）
每个发现必须包含以下字段：
风险点名称
漏洞类型+影响接口+文件路径
漏洞成因
简述代码逻辑错误或输入未过滤的原因。
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh3njCWzKrGE2uj3jicFkAqjVIHpJKhnC78W3CS7OGrfItJxbfRKCxwY4fNYP1j8ric9Gk8bAun4Cibw/0?wx_fmt=png)

0xSecurity

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh3njCWzKrGE2uj3jicFkAqjVIHpJKhnC78W3CS7OGrfItJxbfRKCxwY4fNYP1j8ric9Gk8bAun4Cibw/0?wx_fmt=png)

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